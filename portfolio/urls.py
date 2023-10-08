from django.urls import path
from .views import lista_projetos, ProjetoDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lista_projetos, name='lista_projetos'),
    path('projeto/<int:id>/', ProjetoDetail.as_view(), name='projeto_detail'),
    # ... outras URLs ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)