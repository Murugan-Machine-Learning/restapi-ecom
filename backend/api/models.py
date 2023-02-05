from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=100)

class Country(models.Model):
    name = models.CharField(max_length=100)

    def country_name(self):
        return self.country.name
    country_name.short_description = 'Country Name'

    class Meta:
        verbose_name_plural = "Countries"




class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='api_users')
    groups = models.ManyToManyField(Group, related_name='api_user_groups', through='ApiUserGroups')
    user_permissions = models.ManyToManyField(Permission, related_name='api_user_permissions', through='ApiUserPermissions')
    gender = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def user_type_name(self):
        return self.user_type.name

    user_type_name.short_description = 'User Type Name'

class ApiUserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class ApiUserPermissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)