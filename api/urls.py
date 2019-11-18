
from rest_framework import routers

from api.views import APIViewSet

router = routers.DefaultRouter()
url(r'api/label', APIViewSet.model_label, base_name='apiviewset')
url(r'api/language', APIViewSet.model_language, base_name='apiviewset')
url(r'api/repository', APIViewSet.model_repositories, base_name='apiviewset')
router.register(r'^api/repositories/(?P<lang>[\w.@+-]+)$', APIViewSet.model_language2, base_name='apiviewset')


