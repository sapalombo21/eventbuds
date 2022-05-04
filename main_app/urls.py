from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/', views.events_index, name='events'),
    path('events/<int:event_id>/<int:user_id>', views.event_detail, name='event_detail'),
    path('events/<str:event_id>/delete/<int:user_id>', views.ticketmaster_create, name='ticketmaster_create'),
    path('events/<int:event_id>/create_comment/<int:user_id>', views.create_comment, name="create_comment"),
    path('events/<int:event_id>/delete/<int:comment_id>/<int:user_id>', views.delete_comment, name="delete_comment"),
    path('events/search/', views.search, name="search"),
    path('user/<int:user_id>', views.user_detail, name='user_detail'),
    path('user/add_photo/<int:user_id>', views.add_photo, name='add_photo'),
    path('events/<int:event_id>/going_event/<int:user_id>', views.going_event, name='going_event'),
    path('user/create', views.create_user, name='create_user'),
    path('user/add_bio/<int:user_id>', views.add_bio, name='add_bio'),
    path('user/<int:user_id>/not_going/<int:event_id>', views.not_going, name='not_going'),
    path('events/<int:event_id>/update/<int:comment_id>/<int:user_id>', views.update_comment, name='update_comment'),
    path('events/<int:event_id>/update_content/<int:comment_id>/<int:user_id>', views.update_content, name='update_content'),
    path('events/<int:event_id>/update_event', views.update_event, name='update_event'),
    path('events/<int:event_id>/update_details/<int:user_id>', views.update_details, name='update_details'),
    path('events/create/', views.create_event, name='events_create'),
    path('events/new_events', views.new_event, name='new_event'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('user/<int:user_id>/add_comment', views.add_comment, name='add_comment'),
]