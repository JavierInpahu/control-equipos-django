from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('metricas/', include('metricas.urls')),
    path('ejemplos/', include('ejemplos.urls')),

    # FIX IMPORTANTE: NO duplicar prefijo
     path("", include("control_equipos.urls")),
]