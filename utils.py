#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import models

class BaseHandler(tornado.web.RequestHandler):
	user = models.User
	article = models.Article
	menu = models.Menu
	option = models.Option
	slider = models.Slider
	term = models.Term

	def get_current_user(self):
		user = self.get_secure_cookie("user")
		if not user:
			return None
		return user

	def prepare(self):
		models.db.connect()
		return super(BaseHandler, self).prepare()

	def on_finish(self):
		if not models.db.is_closed():
			models.db.close()
		return super(BaseHandler, self).on_finish()

class Route:
	handlers = []

	def __init__(self, pattern):
		self.pattern = pattern

	def __call__(self, handler):
		self.handlers.append((self.pattern, handler))
		return handler