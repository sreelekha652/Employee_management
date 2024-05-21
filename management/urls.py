from django.urls import path
from . import views

urlpatterns = [
    path('indexpage',views.indexpage,name="indexpage"),
    path('employee', views.employee_list, name='employee'),
    path('employee_add', views.employee_add, name='employee_add'),
     path('employee_edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee_delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('signup/', views.sign_up, name='signup'),
    path('', views.admin_login, name='adlogin'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_add', views.admin_add, name='admin_add'),
    path('admin_list', views.admin_list, name='admin_list'),
    path('admin_edit/<int:id>/', views.admin_edit, name='admin_edit'),
    path('admin_delete/<int:pk>/', views.admin_delete, name='admin_delete'),
    path('edit_profile', views.edit_profile, name='edit_profile'),


]