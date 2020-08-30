from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Role

ADDITIONAL_USER_FIELDS = (
    ('Profile', {'fields': ('avatar', 'roles')}),
)


class CustomUserAdmin(UserAdmin):
    """ Add extra user fields to default user admin """
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

    def save_related(self, request, form, formsets, change):
        super(CustomUserAdmin, self).save_related(
            request, form, formsets, change
        )

        if form.instance.roles.count() == 0:
            form.instance.roles.add(
                Role.objects.get_or_create(id=Role.STUDENT)[0]
            )


admin.site.register(Role)
admin.site.register(get_user_model(), CustomUserAdmin)
