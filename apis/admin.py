from django.contrib import admin
from apis.models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Tag)