from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.api_views.medico import MedicoViewSet
from api_app.api_views.paciente import PacienteViewSet
from api_app.api_views.cita_medica import CitaMedicaViewSet
from api_app.api_views.especialidad import EspecialidadViewSet

# Enrutador para manejar automáticamente las rutas de los ViewSets o Vistas de API

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet, basename='medico')
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'especialidades', EspecialidadViewSet, basename='especialidad')
router.register(r'citas', CitaMedicaViewSet, basename='cita_medica')

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas generadas por el router
]

