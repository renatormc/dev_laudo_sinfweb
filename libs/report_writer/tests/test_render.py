from report_writer import Renderer
from tests.models import example
from report_writer import html_render




def test_test():
    context = example.test_data.context
    r = Renderer(example)
    r.render(context, "test.docx")
   
    