from django.urls import path
from .views import lista_projetos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lista_projetos, name='lista_projetos'),
    # ... outras URLs ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)