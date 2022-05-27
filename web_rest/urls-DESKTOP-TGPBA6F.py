from rest_framework import routers
from .views import PersonaViewset
from django.urls import path,include

router = routers.DefaultRouter()
router.register('persona', PersonaViewset)

urlpatterns = [
    path('api/',include(router.urls)),
]
