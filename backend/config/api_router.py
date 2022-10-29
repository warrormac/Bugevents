from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sistema_gestor_de_zapatillas.management.api.views import (
    PointOfSaleViewSet,
    ProviderViewSet,
)
from sistema_gestor_de_zapatillas.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("providers", ProviderViewSet)
router.register("pointofsale", PointOfSaleViewSet)


app_name = "api"
urlpatterns = router.urls
