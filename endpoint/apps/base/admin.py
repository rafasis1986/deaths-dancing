from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    queryset = Client.objects.all()
    list_display = ('id', 'username', 'email', 'is_staff',)


admin.site.register(Client, ClientAdmin)
