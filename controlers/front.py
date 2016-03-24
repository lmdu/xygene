#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from shares.route import route

@route('r/', name="index")
class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hello,world')

