
from rest_framework import routers
from api.views import APIViewSet

router = routers.DefaultRouter()

router.register(r'label', APIViewSet, base_name='api-label')
router.register(r'language', APIViewSet, base_name='api-language')
router.register(r'repository', APIViewSet, base_name='api-repository')


