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
from shares.route import Route
from controlers import front

print Route.routes()

app = tornado.web.Application(Route.routes(), config.settings)

class NotFound(tornado.web.RequestHandler):
	def get(self):
		raise tornado.web.HTTPError(404)

define("port", default=8888, help="run on the given port", type=int)

if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
	tornado.options.parse_command_line()
	tornado.web.ErrorHandler = NotFound
	http_server.listen(options.port)
	loop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(loop)
	loop.start()