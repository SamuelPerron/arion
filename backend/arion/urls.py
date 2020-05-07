from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from arion.common.views import UserViewSet
from arion.partners.views import PartnerViewSet, ContactViewSet
from arion.products.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
