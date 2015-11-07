"""Templates module for Zinnia"""
from django.template.defaultfilters import slugify


def loop_template_list(loop_position, instance, default_template,
                       registery={}):
    """
    Build a list of templates from a position within a loop
    and a registery of templates.
    """
    templates = []
    instance_class = instance.__class__.__name__.lower()
    instance_string = slugify(str(instance))

    for key in ['%s-%s' % (instance_class, instance_string),
                instance_string,
                instance_class,
                'default']:
        try:
            templates.append(registery[key][loop_position])
        except KeyError:
            pass

    templates.append('%s_%s' % (default_template, loop_position))
    templates.append(default_template)

    return templates
