# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Developer(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rate = models.IntegerField(default=20)


class Task(models.Model):
    project = models.ForeignKey(Project)
    developer = models.ForeignKey(Developer)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    task = models.ForeignKey(Task)
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
