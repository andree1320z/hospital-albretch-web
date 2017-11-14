from django.conf.urls import url
from patient import views

urlpatterns = [
    url(r'^register$', views.register, name='patient_register'),
    url(r'^home$', views.home, name='patient_home'),
]
