from django.contrib import admin
from .models import Category, Customer, Product, Order ,Profile
from .models import driver
# Register your models here.

from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


#mix profile Infor and user infor

class ProfileInline(admin.StackedInline):

    model = Profile

#Extend User Model
    
class UserAdmin(admin.ModelAdmin):

    model = User
    
    field = ["username", "first_name", "last_name", "email"]

    inlines = [ProfileInline]

#unregister the old way
    
admin.site.unregister(User)

#Re-Register

admin.site.register(User, UserAdmin)

# Register your models here
admin.site.register(driver)