from django.contrib import admin, auth
from django.urls import path, include

from . import views
from .views import deleteView

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delete/<int:item_id>', views.deleteView, name='delete'),
]
