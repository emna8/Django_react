from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('person_list/', views.person_list, name='person'),
]
urlpatterns = format_suffix_patterns(urlpatterns)