import datetime
import logging
from urllib.parse import urlencode

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template.context_processors import csrf

from patient.models import Patient
from django.contrib.auth.models import User
from django.contrib import auth
from patient.models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from schedule.models import Schedule
from receptionist.models import Receptionist


def register(request):
    # try:
    #     if not (request.user.is_authenticated() and request.user.profile.user_type == 0):
    #         return HttpResponse("server_message: Access Denied")
    # except:
    #     return HttpResponse("server_message: Access Denied")
    if request.method == "POST":
        try:
            # birth = request.POST['birthday']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['ssn'],
                                            first_name=fname,
                                            last_name=lname,
                                            email=request.POST['email']
                                            )
            user.save()
            # rec = Receptionist.objects.get(user=request.user)
            patient = Patient(
                # parent_hospital=rec.hospital,
                user_type=2,
                user=user,
                firstname=fname,
                lastname=lname,
                Tel=request.POST['tel'],
                ssn=request.POST['ssn'],
                # birthday=birth,
                age=request.POST['age'],
                marital_status=request.POST['marital_status'],
                occupation=request.POST['occupation'],
                country=request.POST['country'],
                city=request.POST['city'],
                district=request.POST['district'],
                street=request.POST['street'],
                alley=request.POST['alley'],
                building_no=request.POST['building_no'],
                postal_code=request.POST['postal_code']
            )
            patient.save()
        except Exception as e:
            logging.exception("message")
            try:
                if user: user.delete()
                if patient: patient.delete()
            except:
                pass
            # return HttpResponse("An Error Has Occured During Registration, Since Required Fields Are Not  \
            #                   Entered Properly , Please Try Again")
            return render(request, 'physician/register.html', {'flag': False})

        # return HttpResponseRedirect(reverse('rec_app:patient-list'))
        return HttpResponseRedirect(reverse('login_all'))
    return render(request, 'register.html', {'flag': True})


def home(request):
    try:
        if not (request.user.is_authenticated() and request.user.profile.user_type == 2):
            d = {'server_message': "Not Logged In."}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' + query_str)
    except:
        d = {'server_message': "not logged in"}
        query_str = urlencode(d)
        return HttpResponseRedirect('/login_all/?' + query_str)
    try:
        patient = Patient.objects.get(user=request.user)
    except:
        patient = None
    try:
        sch = Schedule.objects.get(patient=patient)
    except:
        sch = None
    c = {'patient': patient, 'sch': sch, 'request': request}
    c.update(csrf(request))
    return render_to_response('patient_home.html', c, RequestContext(request))
