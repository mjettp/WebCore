# encoding: utf-8

"""Allow a single method to return different data formats.

Non-functional until the helpers get worked on a bit.
"""

from web.dialect.helper import render, require


class Root(object):
    @render('mako:./multihead.html')  # default if no extension
    @render('mako:./multihead.html', 'html')  # /details.html
    @render('mako:./multihead.xml', 'xml')  # /details.xml
    @render('json:')  # /details.json
    @render('bencode:')  # /details.bencode
    @render('yaml:')  # /details.yaml
    def details(self):
        return dict(name="Bob", age=27)
    
    @require(False)
    def foo(self):
        return "We matched the predicate."
    
    @foo.require(True)
    def foo(self):
        return "We matched a different predicate."
    
    @foo.otherwise
    def foo(self):
        return "uh, wut?"



if __name__ == '__main__':
    from web.core.application import Application
    from marrow.server.http import HTTPServer

    HTTPServer('127.0.0.1', 8080, application=Application(Root)).start()
