#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import peewee
import config

db = peewee.MySQLDatabase("xygene", 
	host = config.DB_HOST, 
	user = config.DB_USER, 
	passwd = config.DB_PASS,
	charset = 'utf8'
)

class BaseModel(peewee.Model):
	class Meta:
		database = db

class User(BaseModel):
	ID = peewee.PrimaryKeyField()
	name = peewee.CharField()
	password = peewee.CharField()
	email = peewee.CharField()
	avatar = peewee.CharField(null=True)
	group = peewee.IntegerField(default=1)
	registered = peewee.DateTimeField(default=datetime.datetime.now)

	class Meta:
		db_table = 'users'

class Menu(BaseModel):
	ID = peewee.PrimaryKeyField()
	name = peewee.CharField()
	order = peewee.IntegerField()
	description = peewee.TextField(null=True)
	link = peewee.CharField(null=True)

	class Meta:
		ordery_by = ('order',)
		db_table = 'menus'

class Slider(BaseModel):
	ID = peewee.PrimaryKeyField()
	title = peewee.CharField(null=True)
	description = peewee.TextField(null=True)
	link = peewee.CharField(null=True)
	picture = peewee.CharField()

	class Meta:
		db_table = 'sliders'

class Term(BaseModel):
	ID = peewee.PrimaryKeyField()
	name = peewee.CharField()
	slug = peewee.CharField()
	meta = peewee.CharField(null=True)

	class Meta:
		db_table = 'terms'

class Option(BaseModel):
	ID = peewee.PrimaryKeyField()
	name = peewee.CharField()
	value = peewee.TextField()

	class Meta:
		db_table = 'options'

class Article(BaseModel):
	ID = peewee.PrimaryKeyField()
	name = peewee.CharField()
	title = peewee.TextField()
	content = peewee.TextField()
	category = peewee.ForeignKeyField(Term)
	created = peewee.DateTimeField(default=datetime.datetime.now)

	class Meta:
		db_table = 'articles'