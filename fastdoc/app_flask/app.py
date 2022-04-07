from pathlib import Path
from flask import Flask, render_template, request, flash, abort, send_from_directory
from flask_bootstrap import Bootstrap5
from .helpers import get_web_form, random_id
from fastdoc import config
from fastdoc.helpers import get_models_list, get_model_meta, render_doc
from .ajax_helpers import ajax_helpers

app = Flask(__name__)
app.register_blueprint(ajax_helpers, url_prefix="/ajax-helpers")
app.config['SECRET_KEY'] = config.SECRET_KEY
bootstrap = Bootstrap5(app)


@app.route("/", methods=("GET", "POST"))
def index():
    models_list = get_models_list()
    models = [{'name': m, 'meta': get_model_meta(m)} for m in models_list]
    model = request.args.get("model")
    if not model in models_list:
        return render_template("base.html", models=models)
    form = get_web_form(model)
    if form.validate_on_submit():
        context = form.get_context()
        print(context)
        render_doc(model, context, form.dfile.data)
        flash(f"Documento renderizado com sucesso em \"{form.dfile.data}\"", "alert-success")
    if request.method == "GET":
        form.load_initial_data()
    model_meta = get_model_meta(model)
    return render_template("doc_form.html", form=form, models=models, model=model, model_meta=model_meta)


@app.route("/download-file")
def download_file():
    path_str = request.args.get("path", "")
    print(path_str)
    path = Path(path_str)
    if not path.exists():
        abort(404)
    return send_from_directory(path.parent, path.name)

@app.context_processor
def always_in_context():
    return dict(
      random_id = random_id
    )
