# from django import forms 
# from .models import IncidentModel


# class IncidentForm(forms.ModelForm):
# 	class Meta:
# 		model = IncidentModel
# 		fields = ('location', 'incident_des', 'incident_location', 'suspected_cause', 'actions_taken', 'reported_by', 'incident_date', 'initial_severity')

# 	widget = {
# 	'location': forms.ChoiceField(),
# 	'incident_des' : forms.Textarea(attrs={'id':'incident_des', 'class':'form-control'}),
# 	'incident_location' : forms.TextInput(attrs={'id':'incident_location', 'class':'form-control'}),
# 	'suspected_cause' : forms.Textarea(attrs={'id':'incident_cause', 'class':'form-control'}),
# 	'actions_taken' : forms.Textarea(attrs={'id':'actions_taken', 'class':'form-control'}),
# 	'reported_by' : forms.TextInput(attrs={'id':'reported_by', 'class':'form-control'}),
# 	'incident_date' : forms.DateInput(attrs={'id':'date-field', 'class':'form-control'}),
# 	'initial_severity' : forms.Textarea(attrs={'id':'initial_severity', 'class':'form-control'})
# 	}