__author__ = 'andree'

from django.conf.urls import url
from .views import patient_list_view, delete_guardian, set_schedule_view, update_schedule_view, delete_schedule, search_rec
from .views import patient_create_view, patient_update_view, detail, delete, allocate_ward_view, update_ward_view
from receptionist import views

urlpatterns = [
    url(r'^search/', search_rec, name='rec_search'),

    url(r'^$', patient_list_view, name='patient-list'),
    url(
        r'^create/$',
        patient_create_view,
        name='patient-create',
    ),
    # url(
    #     r'^delete/(?P<pk>[\w]+)/$',
    #     PatientDeleteView.as_view(),
    #     name='patient-delete',
    # ),
    # url(
    #     r'^update/(?P<pk>[\w]+)/$',
    #     patient_update_view,
    #     name='patient-update',
    # ),
    # url(
    #     r'^(?P<username>[\w]+)/$',
    #     PatientDetailView.as_view(),
    #     name='patient-detail',
    # ),
    url(
        r'^delete/(?P<username>[\w]+)/$',
        delete,
        name='patient-delete',
    ),
    url(
        r'^update/(?P<username>[\w]+)/$',
        patient_update_view,
        name='patient-update',
    ),
    url(
        r'^(?P<username>[\w]+)/$',
        detail,
        name='patient-detail',
    ),
    url(
        r'^allocate_ward/(?P<username>[\w]+)/$',
        allocate_ward_view,
        name='allocate-ward',
    ),
    url(
        r'^update_ward/(?P<username>[\w]+)/$',
        update_ward_view,
        name='update-ward',
    ),
    url(
        r'^delete_ward/(?P<username>[\w]+)/$',
        delete_guardian,
        name='delete-ward',
    ),

    url(
        r'^set_schedule/(?P<username>[\w]+)/$',
        set_schedule_view,
        name='set-schedule',
    ),
    url(
        r'^update_schedule/(?P<username>[\w]+)/$',
        update_schedule_view,
        name='update-schedule',
    ),
    url(
        r'^delete_schedule/(?P<username>[\w]+)/$',
        delete_schedule,
        name='delete-schedule',
    ),
]
