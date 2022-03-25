from .doc_handler import DocxHandler
# from app.report_writer.doc_handler import OdtHandler
from pathlib import Path
from importlib.machinery import SourceFileLoader
import models

class Renderer:
    def __init__(self, model, models_folder):
        self.model = model
        self.model_folder = Path(models_folder) / model
        if not self.model_folder.exists():
            raise Exception(f"Folder {self.model_folder} doesn't exist")
        

    def get_form(self):
        try:
            return getattr(md, self.model).form.Form()
        except AttributeError:
            return

    # def get_tipos_objetos(self):
    #     return getattr(md, self.model).tipos_objetos

    def pre(self, context):
        p = self.model_folder / "pre.py"
        if p.exists():
            mod = SourceFileLoader("module.name", str(p)).load_module()
            mod.pre(context)
       


    def render(self, type_, context, name_prefix="", only_laudo=False):
        self.pre(context)
        Filters = getattr(models, self.model).filters.Filters
        custom_filters = [getattr(Filters, func) for func in dir(Filters) if callable(getattr(Filters, func)) and not func.startswith("__")]
        Functions = getattr(models, self.model).functions.Functions
        custom_functions = [getattr(Functions, func) for func in dir(Functions) if callable(getattr(Functions, func)) and not func.startswith("__")]
        self.engine = DocxHandler(self.model_folder / "templates", custom_filters=custom_filters, custom_functions=custom_functions) # if type_ == "docx" else OdtHandler(self.model_folder)
        return self.engine.render(context, name_prefix=name_prefix, only_laudo=only_laudo)
       