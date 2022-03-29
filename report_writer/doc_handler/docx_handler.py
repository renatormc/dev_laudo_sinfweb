from pathlib import Path
from typing import  Union
from docxtpl import DocxTemplate, InlineImage
import jinja2
from .filters import filters
from .jinja_env_functions import global_functions
from docx.shared import Mm
from uuid import uuid4
from zipfile import ZipFile
import tempfile


class SubdocFunction:
    def __init__(self, tpl, templates_folder):
        self.tpl = tpl
        self.templates_folder = templates_folder

    def __call__(self, template, context):
        path = self.templates_folder / f"{template}.docx"
        if not path.exists():
            print(f"Não foi encontrado o arquivo {path}")
            return
        subtpl = DocxTemplate(str(path))
        subtpl.render(context)
        sd = self.tpl.new_subdoc()
        sd.subdocx = subtpl.docx
        return sd


class SInlineImage:
    def __init__(self, tpl):
        self.tpl = tpl

    def __call__(self, file, width):
        path = Path(file)
        if not path.exists():
            return
        return InlineImage(self.tpl, file, width=Mm(width))


class DocxHandler:
    def __init__(self, templates_folder, custom_filters=[], custom_functions=[]):
        self.templates_folder = Path(templates_folder)
        self.TEMPFOLDER =  Path(tempfile.gettempdir(), "edoc")
        if not self.TEMPFOLDER.exists():
            self.TEMPFOLDER.mkdir()
        self.custom_filters = custom_filters
        self.custom_functions = custom_functions

    def make_jinja_env(self, tpl):
        jinja_env = jinja2.Environment()
        for filter_ in filters:
            jinja_env.filters[filter_.__name__] = filter_
        for function_ in global_functions:
            jinja_env.globals[function_.__name__] = function_
        for filter_ in self.custom_filters:
            jinja_env.filters[filter_.__name__] = filter_
        for function_ in self.custom_functions:
            jinja_env.globals[function_.__name__] = function_
        jinja_env.globals['subdoc'] = SubdocFunction(
            tpl, self.templates_folder)
        jinja_env.globals['image'] = SInlineImage(tpl)
        return jinja_env

    def render_temp(self, template, context):
        path = self.templates_folder / template
        if path.exists():
            tpl = DocxTemplate(str(path))
            jinja_env = self.make_jinja_env(tpl)
            tpl.render(context, jinja_env)
            tempfile = self.TEMPFOLDER / f"{uuid4()}.docx"
            tpl.save(tempfile)
            return tempfile

    def render(self, context, name_prefix="", only_laudo=False):
        if only_laudo:
            tempfile = self.render_temp("Main.docx", context)
            return tempfile
        tempzip = self.TEMPFOLDER / f"{uuid4()}.zip"
        with ZipFile(tempzip, 'w') as zipf:
            tempfile = self.render_temp("Main.docx", context)
            if tempfile:
                zipf.write(tempfile, f"{name_prefix}laudo.docx")

            tempfile = self.render_temp("Main_capa.docx", context)
            if tempfile:
                zipf.write(tempfile, f"{name_prefix}capa.docx")

            tempfile = self.render_temp("Main_midia.docx", context)
            if tempfile:
                zipf.write(tempfile, f"{name_prefix}midia.docx")
            # shortcut = config.app_dir / "app/report_writer/shortcut.lnk"
            # if shortcut.exists():
            #     zipf.write(shortcut, "imprimir_laudo.lnk")
        return tempzip

    def render_other(self, context: dict, template: str, output: Union[Path, str]) -> bool:
        path = self.templates_folder / template
        output = Path(output)
        if not path.exists():
            return False
        tpl = DocxTemplate(str(path))
        jinja_env = self.make_jinja_env(tpl)
        tpl.render(context, jinja_env)
        tpl.save(output)
        return True
