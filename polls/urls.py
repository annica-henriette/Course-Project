from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/<int:item_id>/', views.deleteView, name='delete'), 
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('new_question_text/<int:question_id>/', views.questionText, name='question_text'),
]
