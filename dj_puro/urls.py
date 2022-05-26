from django.urls import path,include
from . import views


urlpatterns = [
    path('categorias/',views.categoria_list, name='categoria_list'),
    path('categoria/<int:pk>',views.categoria_detalle, name='categoria_detalle'),
]
