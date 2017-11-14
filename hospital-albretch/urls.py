from django.conf.urls import include, url

from django.contrib import admin

from . import views

import hello.views

admin.autodiscover()

# Examples:
# url(r'^$', 'hospital-albretch.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'hospital/', include('hospital.urls')),
    url(r'^patient/', include('patient.urls', namespace='patient_app')),
    url(r'^rec/', include('receptionist.urls', namespace='rec_app')),
    # url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.firstpage, name='firstpage'),
    url(r'^SystemHomePage/', views.systemhomepage, name='systemhomepage'),
    url(r'^PatientSearch/', views.patientsearch, name='patientsearch'),
    url(r'^login_all/', views.login, name='login_all'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^reports/', views.get_reports, name='reports'),
    url(r'^physician/', include('physician.urls', namespace='doc_app')),
    url(r'^messages/', include('django_messages.urls', namespace='django_messages')),
]
