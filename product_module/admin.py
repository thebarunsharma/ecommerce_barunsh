from importlib.resources import Package
from pyexpat import model
from django.contrib import admin
from .models import guide, package, booking, agency, customer

class packageAdmin(admin.ModelAdmin):
    list_display= ["package_id", "package_name", "price", "type", ]
    search_fields= ["package_id", "package_name", "price", "type", ]
    list_filter= ["package_name", "price", "type", ]
    class Meta:
        model= Package
admin.site.register(package, packageAdmin)

class guideAdmin(admin.ModelAdmin):
    list_display= ["guide_name", "experience", "type", "contact_no", "review",]
    search_fields= ["guide_id", "guide_name", "experience", "type", "contact_no", "review",]
    list_filter= ["guide_name", "experience", "type", "contact_no", "review", ]
    class Meta:
        model= guide
admin.site.register(guide, guideAdmin)

class customerAdmin(admin.ModelAdmin):
    list_display= ["fullname", "address", "phone", "email",]
    search_fields= ["customer_id", "fullname", "address", "phone", "email",]
    list_filter= ["customer_id", "fullname", "address", "phone", "email", ]
    class Meta:
        model= customer
admin.site.register(customer, customerAdmin)

class agencyAdmin(admin.ModelAdmin):
    list_display= ["agency_id", "agency_name", "location", "package_id",]
    search_fields= ["agency_id", "agency_name", "location", "package_id",]
    list_filter= ["agency_id", "agency_name", "location", "package_id",]
    class Meta:
        model= agency
admin.site.register(agency, agencyAdmin)

class bookingAdmin(admin.ModelAdmin):
    list_display= ["destination", "ticket_type", "customer", "guide", "package",]
    search_fields= ["booking_id", "destination", "ticket_type", "customer", "guide", "package",]
    list_filter= ["booking_id","destination", "ticket_type", "customer", "guide", "package",]
    class Meta:
        model= booking
admin.site.register(booking, bookingAdmin)


