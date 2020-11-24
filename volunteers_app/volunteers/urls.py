from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('volunteer_form', views.volunteer_form, name='volunteer_form'),
    path('<int:id>/volunteer_form', views.volunteer_form, name='volunteer_update'),
    path('volunteers_list', views.volunteers_list, name='volunteers_list'),
    path('volunteer_delete/<int:id>/', views.volunteer_delete, name='volunteer_delete'),
    path('branch_form', views.branch_form, name='branch_form'),
    path('<int:id>/branch_form', views.branch_form, name='branch_update'),
    path('branch_list', views.branch_list, name='branch_list'),
    path('branch_delete/<int:id>/', views.branch_delete, name='branch_delete'),
]
