from django.urls import path
from .views import process_letter_request

urlpatterns = [
    path('letter/',process_letter_request, name='letter'),
]