from __future__ import absolute_import, unicode_literals
from django.urls import path, re_path
from wagtailcomments_xtd import views


urlpatterns = [
    path('', views.pages, name='wagtailcomments_xtd_pages'),
    path('<int:pk>/', views.comments, name='wagtailcomments_xtd_comments'),
    path('<int:page_pk>/comment/<int:comment_pk>/thread/',
        views.comment_thread, name='wagtailcomments_xtd_comment_thread'),
    re_path(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/update/(?P<action>publish|unpublish|hide|show)/$',
        views.update, name='wagtailcomments_xtd_publication'),
]
