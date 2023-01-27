from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

# Configure Admin TItles
admin.site.site_header = "My Booking Administration Page"
admin.site.site_title = "Browser Title"
admin.site.index_title = ""