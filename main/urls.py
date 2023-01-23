
from main import views
from django.urls import path

urlpatterns = [
   
    path('',views.home, name='home'),
    path('admit-student/',views.admit, name='admit'),
    path('delete/<int:pk>/',views.delete_student, name='deleteStudent'),
    path('edit/<int:pk>/',views.edit, name='edit'),
]
