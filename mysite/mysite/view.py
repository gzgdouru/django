from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from datetime import datetime, timedelta

def hello(request):
    return HttpResponse("hello world!")

def current_datetime(request):
    current_date = datetime.now()
    return render_to_response("time_template.html", locals())

def hours_ahead(request, offset):
    try:
        hours_offset = int(offset)
    except:
        raise Http404()

    next_time = datetime.now() + timedelta(hours=hours_offset)
    return render_to_response("hours_ahead.html", locals())

def get_request(request):
    # values = request.META.items()
    # values.sort()
    # html = []
    # for k, v in values:
    #     html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    # return HttpResponse("<table>%s</table>" % "\n".join(html))
    request_head = request.META
    return render_to_response("request_head.html", locals())