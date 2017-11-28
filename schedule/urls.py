from django.conf.urls import url

from schedule import views

urlpatterns = [
    url(r'^calendario$', views.calendar, name='calendario'),
]
