from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^loan/$', views.loan, name='loan'),
    url(r'^user/$', views.user, name='user'),
    url(r'^show_data/$', views.show_data, name='show_data'),
    url(r'^clear/$', views.clear_session, name='clear_session'),
    url(r'^show_configs/$', views.show_configs, name='show_configs'),
    url(r'^loan_config_detail/(?P<id>[0-9]+)/$', views.loan_config_detail, name='loan_config_detail'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
]