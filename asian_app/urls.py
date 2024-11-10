from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'), 
    path('jobs/', views.jobs_page, name='jobs_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('likes/', views.likes_page, name='likes_page'),
    path('information/', views.information_page, name='information_page'),
    path('jobs/detail/<int:pk>/', views.job_infromations_page, name='job_infromations_page'),
    path('guide/detail/<int:pk>/', views.guide_job_page, name='guide_job_page'),
    path('category/jobs/<slug:slug>/', views.Joe_Biden_page, name='Joe_Baiden_page'),
    path('register/', views.sign_up_page, name='registration_page'),
    path('login/', views.log_in_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]