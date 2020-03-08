from django.contrib import admin
from Myapp.models import user
from Myapp.models import UserProfileInfo

# Register your models here.
admin.site.register(user)
admin.site.register(UserProfileInfo)
