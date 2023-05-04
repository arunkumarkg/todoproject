from . import views
from django.urls import path


urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbrhome/',views.Tasklistview.as_view(),name='cbrhome'),
    path('cbrdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbrdetail'),
    path('cbrupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbrupdate'),
    path('cbrdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbrdelete'),

]
