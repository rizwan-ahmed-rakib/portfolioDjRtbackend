from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutMeViewSet, SkillViewSet, ServiceViewSet,
    TagViewSet, PortfolioViewSet, MessageViewSet
)

router = DefaultRouter()
router.register(r'about-me', AboutMeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'tags', TagViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
