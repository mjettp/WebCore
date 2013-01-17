# encoding: utf-8

"""Basic class-based demonstration application.

Applications can be as simple or as complex and layered as your needs dictate.
"""


class Root(object):
    def __init__(self, context):
        self._ctx = context
    
    def __call__(self):
        """Handle "index" lookups."""
        return "Path: /"
    
    def index(self):
        """Handle calls to /index -- this is no longer the 'default' index lookup."""
        return "Path: /index"
    
    foo = "Static string!"
    bar = "mako:./template.html", dict()


if __name__ == '__main__':
    from web.core.application import Application
    from marrow.server.http import HTTPServer
    from web.ext.template import TemplateExtension
    
    app = Application(Root, extensions=[TemplateExtension()])
    
    HTTPServer('127.0.0.1', 8080, application=app).start()
