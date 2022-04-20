from flask import Blueprint, render_template, request
from rlibs.report_writer.types import ObjectType


ajax_helpers = Blueprint('ajax_helpers', __name__)


@ajax_helpers.route('/case-pics-object', methods=("POST",))
def case_pics_object():
    data = request.json
    data['pics'][0]
    obj = ObjectType(pics= data['pics'], name=data['name'])
    return render_template("ajax_helpers/case-pics-object.html", object=obj)


