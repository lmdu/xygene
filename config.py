#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#MySQL database information
DB_HOST = 'localhost'
DB_NAME = 'xygene'
DB_USER = 'root'
DB_PASS = ''

#templates path
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

#static file path
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

#upload directory
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'uploads')

#Debug mode true or false
DEBUG = True

#Gzip compress true or false
GZIP = True

#cookie secret
SECRET = 'DZeGSPAMSFucHmx3PxntevoZxQJvbUUmlJrUSmyhF3I='
