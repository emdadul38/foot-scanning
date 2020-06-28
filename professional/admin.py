from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from professional.models import (User, Organization, Address, Professional, Patient)


# Register your models here.

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'phone',  'organization', 'shipping_address', 'billing_address', 'is_admin', 'is_staff',)

class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    
    add_fieldsets = [
        ('Basic Info', {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)
        }),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'phone', 'organization',  'shipping_address', 'billing_address', )}),
        ('Permissions', {'fields': ('is_admin', 'is_staff',)}),
        ('Address', {'fields': ()}),
    ]
    
    list_display = ('email', 'username', 'first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'phone',  'organization', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# @admin.register(Organization)
class CustomOrganization(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    
    filter_horizontal = ()
    list_filter = ['name']
    fieldsets = ()

class CustomProfessional(admin.ModelAdmin):
    list_display = ['id', 'user', 'facility', 'unit_size', 'unit_weight', 'user_type']
    search_fields = ['user']
    
    filter_horizontal = ()
    list_filter = ['user', 'user_type']
    fieldsets = ()
    
class CustomAddress(admin.ModelAdmin):
    list_display = ['id', 'street_1', 'street_2', 'city', 'zipcode', 'country']
    list_filter = ['city', 'zipcode', 'country']

class CustomPatient(admin.ModelAdmin):
    list_display =['user', 'practitioner', 'height', 'weight']
    search_fields = ['height']
    
    filter_horizontal = ()
    list_filter = ['user', 'practitioner']
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(Organization, CustomOrganization)
admin.site.register(Address, CustomAddress)
admin.site.register(Professional, CustomProfessional)
admin.site.register(Patient, CustomPatient)