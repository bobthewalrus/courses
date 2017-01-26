from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^addcourse$', views.addcourse),
  url(r'^deletecourse/(?P<id>\d+)',views.deletecourse),
  url(r'^cancel$', views.cancel),
  url(r'^deleteconfirm/(?P<id>\d+)', views.deleteconfirm),
]
