from django.http import HttpResponse,Http404
from django.template import Template,Context
#from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello world")

#def current_time(request):
#	now = datetime.datetime.now()
#	html = '<html><body>It is %s.</body></html>' % now
#	return HttpResponse(html)


#def current_time(request):
#	now = datetime.datetime.now()
#	t = Template("<html><body>It is now {{current_date }}.</body></html>")
#	html = t.render(Context({'current_date': str(now)}))
#	return HttpResponse(html)


#def current_time(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_date': str(now)}))
#	return HttpResponse(html)


def current_time(request):
	current_date = str(datetime.datetime.now())
	return render_to_response('current_datetime.html',locals())

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset,dt)
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		hour_offset = int(offset)
	except ValueError:
		raise Http404()
	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	return render_to_response('hours_ahead.html',locals())