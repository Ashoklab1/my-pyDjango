"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from .views import (
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('my_posts/', include('my_posts.urls')),
    path('', ItemListView.as_view(), name='item_list'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('my_posts/', include('my_posts.urls')),
    path('my_comments/', include('my_comments.urls')),
    path('my_likes/', include('my_likes.urls')),
    path('my_users/', include('my_users.urls')),
    path('my_notifications/', include('my_notifications.urls')),
    path('my_messages/', include('my_messages.urls')),
    path('my_settings/', include('my_settings.urls')),
    path('my_tags/', include('my_tags.urls')),
    path('my_search/', include('my_search.urls')),
    path('my_analytics/', include('my_analytics.urls')),
    path('my_reports/', include('my_reports.urls')),
    path('my_subscriptions/', include('my_subscriptions.urls')),
    path('my_moderation/', include('my_moderation.urls')),
    path('my_admin/', include('my_admin.urls')),
    path('my_invitations/', include('my_invitations.urls')),
    path('my_bookmarks/', include('my_bookmarks.urls')),
    path('my_polls/', include('my_polls.urls')),
    path('my_events/', include('my_events.urls')),
    path('my_media/', include('my_media.urls')),
    path('my_authentication/', include('my_authentication.urls')),
    path('my_followers/', include('my_followers.urls')),
    path('my_api/', include('my_api.urls')),
       

]