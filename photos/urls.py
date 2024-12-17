from django.urls import path
from . import views
urlpatterns =[
  
    path('my-images/',views.all_photos_view,name='all_photos'),
   
]