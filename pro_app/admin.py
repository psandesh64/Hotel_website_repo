from django.contrib import admin
from pro_app.models import *
# Register your models here.
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)

admin.site.register(Category)
class list_view(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

admin.site.register(Food_Items,list_view)
admin.site.register(Customer)
admin.site.register(Business_staff)
admin.site.register(Team_staff)