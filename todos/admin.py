from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.views.generic import View

from .models import Todo


# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user', 'status', 'updated_at')


admin.site.register(Todo, TodoAdmin)
