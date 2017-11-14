from django.conf.urls import url

# import views
from hospital import views

urlpatterns = [
    url(r'^$', views.index, name='system_home'),
]
