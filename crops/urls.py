from django.urls import path
from .views import CropList, CropSingle


urlpatterns = [
    path('list/', CropList.as_view()),
    path('crop', CropSingle.as_view()),
]