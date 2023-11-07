from django.contrib import admin

from .models import Category, Product, ImageURL, Note


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ImageURL)

# test jwt authen-authorization
admin.site.register(Note)
