from django.contrib import admin
from .models import guide, package, booking, agency

admin.site.register(guide)
admin.site.register(package)
admin.site.register(booking)
admin.site.register(agency)
