from django.contrib import admin
from .models import UserCustom
from .models import Project, Todo


admin.site.register(UserCustom)
admin.site.register(Project)
admin.site.register(Todo)
