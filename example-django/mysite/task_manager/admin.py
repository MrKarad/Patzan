# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Project
from .models import Developer
from .models import Task
from .models import Comment

admin.site.register(Project)
admin.site.register(Developer)
admin.site.register(Task)
admin.site.register(Comment)