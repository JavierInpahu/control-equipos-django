from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('equipo_list')),

    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('metricas/', include('metricas.urls')),
    path('ejemplos/', include('ejemplos.urls')),
    path('', include('control_equipos.urls')),
]