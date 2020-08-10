from django.contrib import admin

from  users.models import*
from .models import Position


admin.site.register(User)
admin.site.register(Position)




