from django.contrib import admin

from models import Signup


class SignupAdmin(admin.ModelAdmin):
        list_display = ('email', 'added', 'invitation_sent', 'city')
        list_filter = ('invitation_sent', 'added', 'city')
        date_hierarchy = 'added'

admin.site.register(Signup, SignupAdmin)
