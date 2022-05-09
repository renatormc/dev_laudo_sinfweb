import copy

def pre(context):
    context['peritos'] = copy.deepcopy(context['relatores'])
    if context['revisor']:
        context['peritos'].append(context['revisor'])
    # context['objects'].find_objects_types_from_name()
    context['n_objetos'] = len(context['objects'].objects)