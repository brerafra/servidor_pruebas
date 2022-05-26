from django.contrib import admin
from .models import *

admin.site.site_header = 'Brent-soft-Admin'
admin.site.index_title = 'Panel de control y administración'
admin.site.site_title = 'Bren-soft'

admin.site.register(Categoria)