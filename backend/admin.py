from django.contrib import admin
from .models import User,Test,Disease
# Register your models here.
admin.site.register(User)
admin.site.register(Test)
admin.site.register(Disease)