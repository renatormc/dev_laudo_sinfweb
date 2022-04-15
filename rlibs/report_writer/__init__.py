from pathlib import Path
from typing import Any, Optional, Tuple, Union
from .doc_handler import DocxHandler
from .html_render import render_pre_html

class Renderer:
    def __init__(self, model):
        self.model = model
        self.model_folder = Path(model.__file__).parent
     

    def pre(self, context):
        self.model.pre.pre(context)
              

    def render(self, context, dest_file: Union[Path, str], type_="docx") -> Tuple[Any, Optional[Path]]:
        self.pre(context)
        render_pre_html(self.model, context)
        self.engine = DocxHandler(self.model)
        return context, self.engine.render("Main.docx", context, dest_file)
       