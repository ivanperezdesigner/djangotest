from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/<str:question_text>', views.results, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test', views.test)

]