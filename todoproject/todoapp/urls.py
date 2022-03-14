from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('details/',views.details,name= 'details'),
    path('delete/<int:todoid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('cbvlist/',views.TodoListView.as_view(),name='cbvlist'),
    path('cbvdetail/<int:pk>/',views.TodoDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TodoUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TodoDeleteView.as_view(),name='cbvdelete'),

]