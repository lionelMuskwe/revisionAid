from django.contrib import admin
from .models import Question, Subject, Topic

# Register your models here.
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Topic)