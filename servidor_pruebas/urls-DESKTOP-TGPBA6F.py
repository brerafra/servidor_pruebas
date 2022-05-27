
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador',include('administrador.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api_django/',include('dj_puro.urls')),
    path('',include('web_rest.urls'))
]
