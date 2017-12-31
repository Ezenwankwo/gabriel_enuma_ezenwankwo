from django.contrib import admin
from .models import Profile, Poll, Choice



# Register your models here.




admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(Poll, admin.ModelAdmin)
admin.site.register(Choice, admin.ModelAdmin)