from django.contrib import admin
from cars.models import Car
from cars.models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
  list_display = ('model', 'brand_id', 'factory_year', 'model_year', 'value')
  search_fields = ('model',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
