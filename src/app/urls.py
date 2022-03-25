from django.urls import path
# from api.views import mail_sender
from api.views import EmailerViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', EmailerViewSet, basename='email')

urlpatterns = router.urls
