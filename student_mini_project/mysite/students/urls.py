from django.urls import path

from . import views

urlpatterns = [
    path('', views.listStudent, name='list_student'),
    path('<int:studentId>/add_edit', views.addStudent, name='add_edit_student'),
    path('<int:studentId>/delete', views.deleteStudent, name='delete_student'),
]