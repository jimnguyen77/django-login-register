from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar_view', views.calendar_view, name='calendar_view'),
    path('calendar_view/<int:year>/<str:month>/', views.calendar_view, name='calendar_view'),
   
    path('list_venues', views.list_venues, name='venue-list'),
    path('show_venue/<venue_id>', views.show_venue, name='venue-show'),
    path('add_venue', views.add_venue, name='venue-add'),
    path('search_venues', views.search_venues, name='venue-search'),
    path('update_venue/<venue_id>', views.update_venue, name='venue-update'),
    path('delete_venue/<venue_id>', views.delete_venue, name='venue-delete'),
    path('venue_text', views.venue_text, name='venue_text'),
    path('venue_csv', views.venue_csv, name='venue_csv'),

    path('list_events', views.list_events, name='event-list'),
    path('add_event', views.add_event, name='event-add'),
    path('update_event/<event_id>', views.update_event, name='event-update'),
    path('delete_event/<event_id>', views.delete_event, name='event-delete'),
]
