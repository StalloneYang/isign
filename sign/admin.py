from django.contrib import admin
from sign.models import User, Site, Sign, Detail
# Register your models here.

admin.site.register(User)
admin.site.register(Site)
admin.site.register(Sign)
admin.site.register(Detail)