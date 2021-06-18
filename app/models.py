from django.db import models

# Create your models here.


list_for_dropdown = [
	('Coporate_Headoffice', 'Coporate Headoffice'),
    ('Operation_Deparment', 'Operation Deparment'),
    ('Work_Station', 'Work Station'),
    ('Marketing_Division', 'Marketing Division'),
]

class IncidentModel(models.Model):
	location = models.CharField(choices=list_for_dropdown, max_length=100, default='Coporate_Headoffice')
	incident_des = models.TextField(max_length=500)
	incident_date = models.DateField(max_length=100)
	incident_time=models.TimeField(max_length=100)
	incident_location = models.TextField(max_length=200)
	incident_severity = models.TextField(max_length=500)
	suspected_cause = models.TextField(max_length=500)
	action_taken = models.TextField(max_length=500)
	sub_type_incident = models.CharField(max_length=100)
	reported_by = models.TextField(max_length=100)

	def __str__(self):
		self.reported_by = reported_by



