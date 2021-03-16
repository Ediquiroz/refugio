from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, \
    SolcitudUpdate, SolcitudDelete

urlpatterns = [
    url(r'^$', index_adopcion),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', SolcitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolcitudDelete.as_view(), name='solicitud_eliminar'),
]