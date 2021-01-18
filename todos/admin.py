from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.views.generic import View

from .models import Todo


# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user', 'status', 'updated_at')

#     def get_urls(self):
#         urls = super().get_urls()

#         add_urls = [
#             path('add_page/', self.admin_site.admin_view(TodoAdminView.as_view()),
#                  name="add_page"),
#         ]

#         return add_urls + urls


# class TodoAdminView(View):

#     template_name = 'admin/todos/todo/add_page.html'

#     def get(self, request):
#         return render(request, self.template_name)


admin.site.register(Todo, TodoAdmin)
