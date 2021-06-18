from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse

from .models import IncidentModel
# from .forms import IncidentForm
# Create your views here.

def index(request):
	return render(request, 'index.html')

def incident(request):
	return render(request, 'incident.html')

def incidentprocess(request):
	if request.method == 'POST':
		location = request.POST['location']
		incident_des = request.POST['incident_des']
		incident_date = request.POST['incident_date']
		incident_time = request.POST['incident_time']
		incident_location = request.POST['incident_location']
		incident_severity = request.POST['incident_severity']
		suspected_cause = request.POST['suspected_cause']
		action_taken = request.POST['action_taken']
		sub_type_incident = request.POST['list_of_subtype']
		reported_by = request.POST['reported_by']
		list_data = [reported_by, sub_type_incident]
		incidentmodel = IncidentModel(location=location, incident_des=incident_des, incident_location=incident_location,
			incident_date=incident_date, incident_time=incident_time, incident_severity=incident_severity,
			suspected_cause=suspected_cause, action_taken=action_taken, sub_type_incident=sub_type_incident,
			reported_by=reported_by)
		incidentmodel.save()
		mes = "Reported Saved"
		return JsonResponse({'Save':1, 'message':mes})
	else:
		print('In else')
		mes = 'Report Not Saved. Please try again'
		return JsonResponse({'Save':0, 'message':mes})

def register(request):
	if request.method == 'POST':
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		email = request.POST['email']
		password1 = request.POST['password1']
		username = request.POST['username']

		if password1:

			if User.objects.filter(username=username).exists():
				mes = 'Username Already Exists'
				return JsonResponse({'status':0, 'messages':mes})

			elif User.objects.filter(email=email).exists():
				mes = 'Email Already Exists'
				return JsonResponse({'status':0, 'messages':mes})


			else:
				user = User.objects.create_user(username=username, password=password1, 
					email=email, first_name=first_name, last_name=last_name)
				user.save()
				# messages.info(request, 'User created')
				print('User created')
				return JsonResponse({'status':1})

		else:
			return JsonResponse({'status':0, 'messages':mes})

	else:
		return render(request, 'register.html')


def login(request):

	if request.method=='POST':
		print('Inside login if')
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return JsonResponse({"status":1})
		else:
			mes = 'Invaled Credentials'
			return JsonResponse({'status':0, 'messages':mes})
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect("app:index")