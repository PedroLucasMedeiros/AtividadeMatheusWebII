from rest_framework.routers import DefaultRouter
from .viewsets import ClientViewSet, OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
