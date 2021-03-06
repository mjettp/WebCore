# encoding: utf-8

"""A callable class example."""


class Root(object):
	def __init__(self, context):
		self._ctx = context
	
	def __call__(self, name):
		"""
		/ -- 500
		/?name=Bob
		/ POST name=bob
		/Bob
		"""
		return "Hello " + name


if __name__ == '__main__':
	from web.core import Application
	Application(Root).serve('wsgiref')

