from django.contrib import admin

# Register your models here.
from .models import Book, Publisher, Author, UserProfile, OrderItem, Order, Warehouse 

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(UserProfile)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Warehouse)