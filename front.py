#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from utils import Route

@Route(r'/')
class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hello,world')

