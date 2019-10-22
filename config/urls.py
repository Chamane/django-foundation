from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls')),
    #path('pages/', include('apps.pages.urls')),
    path('', include('apps.core.urls')),
]

handler404 = 'apps.pages.views.handler404'
handler500 = 'apps.pages.views.handler500'
