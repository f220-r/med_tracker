from django.contrib import admin
from .models import User
from .models import Equipment
from .models import Report

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Report)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def save_model(self, request, obj, form, change):
        if not change:  # If the user is being created
            obj.set_password(form.cleaned_data['password'])
        else:
            if 'password' in form.changed_data:  # If the password is being changed
                obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)