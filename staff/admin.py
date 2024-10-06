from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'phone_number', 'salary', 'date_joined', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role', 'is_active')
    ordering = ('-date_joined',)

admin.site.register(Staff, StaffAdmin)
