import copy

def pre(context):
    context['peritos'] = copy.deepcopy(context['relatores'])
    if context['revisor']:
        context['peritos'].append(context['revisor'])
    # context['n_objetos'] = len(context['objects']['objects'])