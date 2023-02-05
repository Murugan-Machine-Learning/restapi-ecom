from django.contrib import admin

# Register your models here.
from api.models import UserType, User, Country


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(UserType, UserTypeAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Country, CountryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type_name', 'gender', 'first_name', 'last_name', 'country_name', 'city')

    def country_name(self, obj):
        if obj.country is not None:
            return obj.country.name
        else:
            return "-"

    country_name.short_description = 'Country Name'

admin.site.register(User, UserAdmin)

