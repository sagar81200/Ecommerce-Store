from rest_framework.routers import DefaultRouter
from .views import ProductViewset, CategoryViewset

router = DefaultRouter()

router.register("products", ProductViewset, basename="products")
router.register("category", CategoryViewset, basename="category")

urlpatterns = router.urls
