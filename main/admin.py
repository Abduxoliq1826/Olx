from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_('Extra'), {'fields': ('type', 'image')}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Information)
admin.site.register(AdImage)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Subcategory)
admin.site.register(Ads)
admin.site.register(Message)
admin.site.register(Wishlist)
admin.site.register(Helps_q)
admin.site.register(Helps_a)
admin.site.register(Distirc)
