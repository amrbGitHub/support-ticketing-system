from rest_framework import routers
from emails.viewsets import EmailViewSet

router = routers.SimpleRouter()
router.register(r'emails', EmailViewSet, basename="emails")

urlpatterns = router.urls

