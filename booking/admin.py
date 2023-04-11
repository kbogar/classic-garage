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
        'updated_on', 'message', 'status')
    list_filter = ('admin_approved', 'created_on')
    search_fields = ['name']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        """
        Handels approval action
        """
        queryset.update(approved=True)
