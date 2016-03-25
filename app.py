#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import tornado.autoreload
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import options, define

import config
import admin
import front
from utils import Route
from models import *

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(
			debug = config.DEBUG,
			gzip = config.GZIP,
			template_path = config.TEMPLATE_PATH,
			static_path = config.STATIC_PATH,
			cookie_secret = config.SECRET,
			login_url = '/login'
		)
		handlers = Route.handlers
		handlers.append(tornado.web.url(
			r"/upload/(.+)",
			tornado.web.StaticFileHandler,
			{'path': config.UPLOAD_PATH}, 
			name='upload_path'
		))
		super(Application, self).__init__(handlers, **settings)

define("cmd", default="start", metavar="start|initial", type=str)
define("port", default=8888, help="run on the given port", type=int)

def run_server():
	http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
	http_server.listen(options.port)
	loop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(loop)
	loop.start()

def create_db():
	db.connect()
	db.create_tables([User, Menu, Slider, Term, Option, Article])
	db.close()


if __name__ == '__main__':
	tornado.options.parse_command_line()
	if options.cmd == 'initial':
		create_db()
	elif options.cmd == 'start':
		run_server()