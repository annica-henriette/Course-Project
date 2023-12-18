from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .views import deleteView

app_name = 'polls'
urlpatterns = [
    #path('', LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/<int:item_id>/', views.deleteView, name='delete'), 
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
