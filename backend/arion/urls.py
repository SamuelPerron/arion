from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from arion.common.views import UserViewSet
from arion.partners.views import PartnerViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'partners', PartnerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
