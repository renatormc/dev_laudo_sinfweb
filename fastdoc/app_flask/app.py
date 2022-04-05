from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap5
from .helpers import get_web_form
from fastdoc import config
from fastdoc.helpers import get_models_list, get_model_meta, render_doc

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
bootstrap = Bootstrap5(app)

@app.route("/", methods=("GET", "POST"))
def index():
    models_list = get_models_list()
    models = [{'name': m, 'meta': get_model_meta(m)} for m in  models_list]
    model = request.args.get("model")
    if not model in models_list:
        return render_template("base.html", models=models)
    form = get_web_form(model)
    if form.validate():
        context = form.get_context()
        if config.debug:
            print(context)
            render_doc(model, context, form.dfile.data)
            flash(f"Documento renderizado com sucesso em \"{form.dfile.data}\"", "alert-success")
        else:
            try:
                render_doc(model, context, form.dfile.data)
                flash(f"Documento renderizado com sucesso em \"{form.dfile.data}\"", "alert-success")
            except Exception as e:
                flash(str(e), "alert-danger")
    model_meta = get_model_meta(model)
    return render_template("doc_form.html", form=form, models=models, model=model, model_meta=model_meta)