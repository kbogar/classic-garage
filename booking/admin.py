from django.contrib import admin
from .models import BookingModel, CustomModel

admin.site.register(CustomModel)


@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    """
    It represents the Booking Model in the
    Admin page.
    """
    list_display = (
        'name', 'email', 'created_on',
        'updated_on', 'service_type', 'message', 'status')
    list_filter = ('admin_approved', 'created_on', 'service_type')
    search_fields = ['name']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        """
        Handels approval action
        """
        queryset.update(status=1)
