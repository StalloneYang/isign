from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    #登录页面

    url(r'^login/$', views.login, name='login'),
    url(r'^loginHandle/$', views.loginHandle, name='loginHandle'),
    # url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^isign/$', views.isign, name='isign'),
    url(r'^mysign/$', views.mysign, name='mysign'),
    url(r'^details/$', views.details, name='details'),
    url(r'^person-info/$', views.persionInfo, name='person-info'),
]