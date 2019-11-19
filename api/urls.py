
from rest_framework import routers
from api.views import LabelViewSet, LanguageViewSet, RepositoryViewSet

router = routers.DefaultRouter()

router.register(r'label', LabelViewSet, base_name='api-label')
router.register(r'language', LanguageViewSet, base_name='api-language')
router.register(r'repository?', RepositoryViewSet, base_name='api-repository')


