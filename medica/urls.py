from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('api_app.urls')),  # Rutas web
    path('api/', include('api_app.api_urls')),  # Rutas API (Asegúrate de que existe api_urls.py)
]
