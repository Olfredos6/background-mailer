from api.views import EmailerViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import index, error


router = DefaultRouter()
router.register(r'', EmailerViewSet, basename='email')

urlpatterns = [
    path('', include(router.urls)),
    path('/welcome', index)
]

handler404 = index
handler500 = error
