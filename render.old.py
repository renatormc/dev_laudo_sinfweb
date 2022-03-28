from pathlib import Path
from report_writer import Renderer
import os
import sys
import shutil
from helpers import get_test_context, choose_model

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
model = sys.argv[1] if len(sys.argv) > 1 else choose_model()

r = Renderer(model, app_dir / "models")
context = get_test_context(model)
path = r.render("", context, only_laudo=True)
shutil.move(path, app_dir / "compilado.docx")
print("Renderizado arquivo compilado.docx")