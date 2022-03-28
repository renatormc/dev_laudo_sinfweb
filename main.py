import argparse
import shutil
import config


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')
parser.add_argument("-m", "--model", default="choose", help="Model")

p_render = subparsers.add_parser("render")
p_start = subparsers.add_parser("start")


args = parser.parse_args()

if args.command == "start":
    shutil.copytree(config.app_dir / "models_example", config.app_dir / "models")
else:
    from helpers import choose_model, get_test_context
    from report_writer import Renderer
    if args.model == "choose":
        args.model = choose_model()
        config.model = args.model
    if args.command == "render":
        r = Renderer(config.model, config.app_dir / "models")
        context = get_test_context(config.model)
        path = r.render("", context, only_laudo=True)
        shutil.move(path, config.app_dir / "compilado.docx")
        print("Renderizado arquivo compilado.docx")