from django.contrib import admin
from .models import Expense, Category, Proxy
# Register your models here.

admin.site.register(Proxy)
admin.site.register(Expense)
admin.site.register(Category)