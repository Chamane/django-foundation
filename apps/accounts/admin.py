from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from . import models

class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields":(
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            }
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined")},
        )
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","password1", "password2"),
            },
        ),
    )
    list_display = (
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = ("fist_name", "last_name")
    ordering = ("email",)

admin.site.register(models.User, UserAdmin)
