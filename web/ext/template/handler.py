# encoding: utf-8

from marrow.util.compat import basestring


def template_handler(context, result):
    if 2 > len(result) > 3:
        return False
    
    if len(result) == 2:
        template, data, extras = result + (dict(),)
    elif len(result) == 3:
        template, data, extras = result
        
    if not isinstance(template, basestring) or not isinstance(extras, dict):
        return False
    
    response = context.response
    mime, response.body = context.render(template, data, **extras)
    
    if response.mime is None:
        response.mime = mime
    
    return True


def annotated_template_handler(context, result):
    """Allow you to declare the template to use within the declaration of the method itself.
    
    For example,
    
        class Controller(object):
            def hello(self) -> 'json':
                return dict(foo="bar")
    
    This is an alternate form of the (dynamic) 2-tuple or 3-tuple return type handler, and as such
    you can safely define a longer template string:
    
        class Controller(object):
            def hello(self) -> 'mako:myapp.templates.hello':
                return dict(foo="bar")
    
    """
    
    handler = context.path[-1][0]
    value = getattr(handler, 'func_annotation', {}).get('return', None)
    
    if not value:
        return False
    
    # Allow people to define just "json" as the return type.
    # Return value annotations like these are treated as serialization formats.
    if '.' not in value and value[-1] != ':':
        value = value + ':'
    
    return template_handler(context, (value, result))
