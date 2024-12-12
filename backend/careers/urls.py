from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CareersViewSet

router = DefaultRouter()
router.register(r"", CareersViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
