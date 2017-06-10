from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^salaCasd/$', views.salaCasd, name='salaCasd'),
    url(r'^salaCasdVest/$', views.salaCasdVest, name='salaCasdVest'),
    url(r'^salaCasdinho/$', views.salaCasdinho, name='salaCasdinho'),
    url(r'^salaDepCult/$', views.salaDepCult, name='salaDepCult'),
    url(r'^login/$', login, {'template_name': 'reservations/login.html'}),
    url(r'^logout/$', logout,{'next_page': '/index/'})
]