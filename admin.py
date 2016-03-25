#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from utils import BaseHandler, Route

class AdminHandler(BaseHandler):
	def get_login_url(self):
		return '/admin/login'

	def get_template_path(self):
		template_path = self.application.settings.get("template_path")
		return os.path.join(template_path, 'admin')


@Route(r'/admin')
class DashbordHandler(AdminHandler):
	def get(self):
		self.render('index.html')
