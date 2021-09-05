from django import forms
from django.forms import ModelForm, DateInput, TextInput, TimeInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from portals.models import Vet_Forms, Sick_Approach_Form, Death_Approach_Form, Surgical_Approach_Form, Deworming_Form, Vaccination_Form, Artificial_Insemination_Form, Calf_Registration_Form, Livestock_Inventory_Form, Pregnancy_Diagnosis_Form, Farm_Consultation

User = get_user_model()
	
class SickApproachForm(ModelForm):
	class Meta:
		model = Sick_Approach_Form
		exclude = ['vet_form', 'vet', 'report_created_on',]

		widgets = {
            'start_dose_date': DateInput(attrs={'type': 'date'}),
        }

	


class DeathApproachForm(ModelForm):
	class Meta:
		model = Death_Approach_Form
		exclude = ['vet_form', 'report_created_on',]

		widgets = {
            'death_date': DateInput(attrs={'type': 'date'}),
			'death_time': TimeInput(attrs={'type':'time'})
        }


class SurgicalApproachForm(ModelForm):
	class Meta:
		model = Surgical_Approach_Form
		exclude = ['vet_form', 'report_created_on',]

		widgets = {
            'operation_date': DateInput(attrs={'type': 'date'}),
        }

class DewormingForm(ModelForm):
	class Meta:
		model = Deworming_Form
		exclude = ['vet_form', 'report_created_on',]

		widgets = {
            'date_of_deworming': DateInput(attrs={'type': 'date'}),
			'next_date_deworming': DateInput(attrs={'type':'date'}),
        }


class VaccinationForm(ModelForm):
	class Meta:
		model = Vaccination_Form
		exclude = ['vet_form', 'report_created_on',]

		
		widgets = {
            'date_of_vaccination': DateInput(attrs={'type': 'date'}),
			'next_date_of_vaccination': DateInput(attrs={'type':'date'}),
        }


class ArtificialInseminationForm(ModelForm):
	class Meta:
		model = Artificial_Insemination_Form
		exclude = ['vet_form', 'report_created_on',]

		widgets = {
			'time_of_heat_sign':TimeInput(attrs={'type':'time'}),
			'time_of_insemination':TimeInput(attrs={'type':'time'}),
            'date_of_insemination': DateInput(attrs={'type': 'date'}),
			'date_of_birth':DateInput(attrs={'type':'date'}),
			'date_of_repeat_checked': DateInput(attrs={'type':'date'}),
			'date_of_pregnancy_diagnosis': DateInput(attrs={'type':'date'}),
			'expected_date_of_calving': DateInput(attrs={'type':'date'}),
        }


class CalfRegistrationForm(ModelForm):
	class Meta:
		model = Calf_Registration_Form
		exclude = ['vet_form', 'report_created_on', 'farmer_username',]

		widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
			'expected_date_of_weaning': DateInput(attrs={'type': 'date'}),
        }


class LivestockInventoryForm(ModelForm):
	class Meta:
		model = Livestock_Inventory_Form
		exclude = ['vet_form', 'report_created_on', 'Attach_photos_of_your_animal']

		widgets = {
            'date_of_culling': DateInput(attrs={'type': 'date'}),
        }


class PregnancyDiagnosisForm(ModelForm):
	class Meta:
		model = Pregnancy_Diagnosis_Form
		exclude = ['vet_form', 'report_created_on',]

		widgets = {
            'date_of_insemination': DateInput(attrs={'type': 'date'}),
			'date_of_pregnancy_diagnosis': DateInput(attrs={'type':'date'}),
			'next_date_of_pregnancy_diagnosis' : DateInput(attrs={'type': 'date'}),
			'expected_date_of_delivery' : DateInput(attrs={'type' : 'date'}),
        }		

class FarmConsultationForm(ModelForm):
	class Meta:
		model = Farm_Consultation
		exclude = ['vet_form', 'report_created_on',]	

