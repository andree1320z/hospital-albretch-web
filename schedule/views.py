from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def calendar(request):
    try:
        if not (request.user.is_authenticated() and request.user.profile.user_type == 6):
            d = {'server_message': "Not Logged In."}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' + query_str)
    except:
        d = {'server_message': "not logged in"}
        query_str = urlencode(d)
        return HttpResponseRedirect('/login_all/?' + query_str)
    return render(request, 'horario.html', )
