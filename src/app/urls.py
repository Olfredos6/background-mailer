from django.urls import path
from api.views import mail_sender

urlpatterns = [
    path('', mail_sender),
]
