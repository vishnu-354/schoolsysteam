from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('student/<str:username>/', views.student, name='student'),
    path('teacher/<str:username>/', views.teacher, name='teacher'),
    path('principal/<str:username>/', views.principal, name='principal'),
    path('institutionadmin/<str:username>/', views.institutionadmin, name="institutionadmin"),
    path('organisationadmin/<str:username>/', views.organisationadmin, name="organisationadmin")
]
