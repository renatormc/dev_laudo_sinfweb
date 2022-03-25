from .doc_handler import DocxHandler
# from app.report_writer.doc_handler import OdtHandler
from pathlib import Path
from importlib.machinery import SourceFileLoader

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
        self.engine = DocxHandler(self.model_folder / "templates") # if type_ == "docx" else OdtHandler(self.model_folder)
        return self.engine.render(context, name_prefix=name_prefix, only_laudo=only_laudo)
       