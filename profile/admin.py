from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Profile


# class InventoryFilter(admin.SimpleListFilter):
#     title = 'inventory'
#     parameter_name = 'inventory'

#     def lookups(self, request, model_admin):
#         return [
#             ('<10', 'Low')
#         ]

#     def queryset(self, request, queryset: QuerySet):
#         if self.value() == '<10':
#             return queryset.filter(inventory__lt=10)

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',  'membership']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__email']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username','membership','birth_date'),
        }),
    )