#!/usr/bin/env python
# -*- coding: utf8 -*-

class Route:

	handlers = []

	def __init__(self, pattern):
		self.pattern = pattern

	def __call__(self, handler):
		self.handlers.append((self.pattern, handler))
		return handler