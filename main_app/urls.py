from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/', views.events_index, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/create_comment', views.create_comment, name="create_comment"),
    path('events/<int:event_id>/delete/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('user/', views.user_detail, name='user_detail'),
    path('user/add_photo/<int:user_id>', views.add_photo, name='add_photo'),
]