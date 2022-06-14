from django.contrib import admin
from .models import guide, package, booking, agency, user

admin.site.register(guide)
admin.site.register(user)
admin.site.register(package)
admin.site.register(booking)
admin.site.register(agency)
