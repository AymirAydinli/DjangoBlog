from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Post




# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username','email', 'first_name', 'last_name', 'user_id']
#     class Meta:
#         model = User



admin.site.register(Post)
