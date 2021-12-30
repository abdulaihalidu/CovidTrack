from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Drug)
admin.site.register(Prescription)
admin.site.register(Covid)
admin.site.register(ChronicDisease)
admin.site.register(ContactedPersons)
