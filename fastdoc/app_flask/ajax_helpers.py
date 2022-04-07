from flask import Blueprint, render_template, request
from fastdoc.custom_types.objects_type import ObjectType

ajax_helpers = Blueprint('ajax_helpers', __name__)

@ajax_helpers.route('case-pics-object', methods=("POST",))
def case_pics_object():
    data = request.json
    obj = ObjectType(pics= data['pics'])
    return render_template("ajax_helpers/case-pics-objects.html", objects=obj)