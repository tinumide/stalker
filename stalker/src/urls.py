from django.urls import path

from .views import GetIdentifierView

urlpatterns = [
    path('/get/identifier', GetIdentifierView.as_view(), name='api-identifier')
]