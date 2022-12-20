from rest_framework import routers
from .api import AutoViewSet, MarcaViewSet
router = routers.DefaultRouter()

router.register('api/autos', AutoViewSet, 'autos')
router.register('api/marcas', MarcaViewSet, 'marcas')

urlpatterns = router.urls