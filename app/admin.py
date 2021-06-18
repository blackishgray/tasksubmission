from django.contrib import admin

from .models import IncidentModel

# Register your models here.

@admin.register(IncidentModel)
class IncidentModelAdmin(admin.ModelAdmin):
	list_display = ('location', 'incident_des', 'incident_date', 'incident_time', 'incident_location', 'incident_severity', 'suspected_cause', 'action_taken', 'sub_type_incident', 'reported_by')
