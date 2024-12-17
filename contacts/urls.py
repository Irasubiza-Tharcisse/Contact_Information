from django.urls import path
from . import views

urlpatterns =[
  
  path('all_contacts/',views.all_contacts_view,name="all_contacts"),
  path('edit_contact/<int:contact_id>/',views.contact_edit_view,name="edit_contact"),
  path('delete_contact/<int:contact_id>/',views.delete_contact_view,name="delete_contact"),
  path('new_contact/',views.new_contact_view,name="new_contact"),
]