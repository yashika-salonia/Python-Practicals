from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Admin Portal"
admin.site.index_title = "Welcome"
admin.site.site_title = "Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
]
