from rest_framework import routers
from emails.viewsets import EmailViewSet

router = routers.SimpleRouter()
router.register(r'email', EmailViewSet, basename="email")

urlpatterns = router.urls

