from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls')),
    #path('pages/', include('apps.pages.urls')),
    path('', include('apps.core.urls')),
]

handler404 = apps.pages.handler404
handler500 = apps.pages.handler500
