from django.shortcuts import render, redirect
from user.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.views import View
from .render import Render
from django.utils import timezone



def vet_check(request):
    return request.is_vet_officer

def farmer_check(request):
    return request.is_farmer

def student_check(request):
    return request.is_student    


@user_passes_test(vet_check, login_url='vet-login')
def portal_vet(request):
    vet_officers = Vet_Officer.objects.all()
    no_vet_forms =Vet_Forms.objects.filter(vet_username=request.user).count()
    context = {
        'all_vets': vet_officers,
        'count': no_vet_forms
    }
    return render(request, 'portals/dashboardVet.html', context)

@user_passes_test(farmer_check, login_url='vet-login')
def portal_farmer(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/dashboardFarmer.html', context)

@user_passes_test(student_check, login_url='vet-login')
def portal_student(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/dashboardStudent.html', context)  


@user_passes_test(vet_check, login_url='vet-login')
def sick_form_view(request):
    sick_approach_forms = Sick_Approach_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Clinical Approach Form',
        'forms': sick_approach_forms
    }    
    return render(request, 'portals/formview.html', context)
 
    
@user_passes_test(vet_check, login_url='vet-login')
def edit_sick_form(request, pk):
	try:
		sick_sel = Sick_Approach_Form.objects.get(pk = pk)
	except Sick_Approach_Form.DoesNotExist:
		return redirect('index')
	sick_form = SickApproachForm(request.POST or None, instance = sick_sel)
	if sick_form.is_valid():
		sick_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':sick_form, 'form_name':'Clinical'})


 
@user_passes_test(vet_check, login_url='vet-login')
def dead_form_view(request):
    dead_approach_forms = Death_Approach_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Post Mortem Approach Form',
        'forms': dead_approach_forms
    }    
    return render(request, 'portals/deadformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_dead_form(request, pk):
	try:
		dead_sel = Death_Approach_Form.objects.get(pk = pk)
	except Death_Approach_Form.DoesNotExist:
		return redirect('index')
	dead_form = DeathApproachForm(request.POST or None, instance = dead_sel)
	if dead_form.is_valid():
		dead_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':dead_form, 'form_name':'Post Mortem'})

 
@user_passes_test(vet_check, login_url='vet-login')
def surgical_form_view(request):
    surgical_approach_forms = Surgical_Approach_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'surgical Approach Form',
        'forms': surgical_approach_forms
    }    
    return render(request, 'portals/surgicalformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_surgical_form(request, pk):
	try:
		surgical_sel = Surgical_Approach_Form.objects.get(pk = pk)
	except Surgical_Approach_Form.DoesNotExist:
		return redirect('index')
	surgical_form = SurgicalApproachForm(request.POST or None, instance = surgical_sel)
	if surgical_form.is_valid():
		surgical_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':surgical_form, 'form_name':'Surgical'})

@user_passes_test(vet_check, login_url='vet-login')
def deworming_form_view(request):
    deworming_approach_forms = Deworming_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Deworming Approach Form',
        'forms': deworming_approach_forms
    }    
    return render(request, 'portals/dewormingformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_deworming_form(request, pk):
	try:
		surgical_sel = Deworming_Form.objects.get(pk = pk)
	except Deworming_Form.DoesNotExist:
		return redirect('index')
	deworming_form = DewormingForm(request.POST or None, instance = surgical_sel)
	if deworming_form.is_valid():
		deworming_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':deworming_form, 'form_name':'Deworming'})


@user_passes_test(vet_check, login_url='vet-login')
def vaccination_form_view(request):
    vaccination_approach_forms = Vaccination_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Vaccination Form',
        'forms': vaccination_approach_forms
    }    
    return render(request, 'portals/vaccinationformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_vaccination_form(request, pk):
	try:
		surgical_sel = Vaccination_Form.objects.get(pk = pk)
	except Vaccination_Form.DoesNotExist:
		return redirect('index')
	vaccination_form = VaccinationForm(request.POST or None, instance = surgical_sel)
	if vaccination_form.is_valid():
		vaccination_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':vaccination_form, 'form_name':'Vaccination'})



@user_passes_test(vet_check, login_url='vet-login')
def artificial_form_view(request):
    artificial_approach_forms = Artificial_Insemination_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Artificial Form',
        'forms': artificial_approach_forms
    }    
    return render(request, 'portals/artificialformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_artificial_form(request, pk):
	try:
		surgical_sel = Artificial_Insemination_Form.objects.get(pk = pk)
	except Artificial_Form.DoesNotExist:
		return redirect('index')
	Artificial_form = ArtificialInseminationForm(request.POST or None, instance = surgical_sel)
	if Artificial_form.is_valid():
		artificial_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':artificial_form, 'form_name':'artificial'})




@user_passes_test(vet_check, login_url='vet-login')
def pregnancy_form_view(request):
    pregnancy_approach_forms = Pregnancy_Diagnosis_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Pregnancy diagnosis Form',
        'forms': pregnancy_approach_forms
    }    
    return render(request, 'portals/pregnancyformview.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def edit_pregnancy_form(request, pk):
	try:
		surgical_sel = Pregnancy_Diagnosis_Form.objects.get(pk = pk)
	except Pregnancy_Diagnosis_Form.DoesNotExist:
		return redirect('index')
	pregnancy_form = PregnancyDiagnosisForm(request.POST or None, instance = surgical_sel)
	if pregnancy_form.is_valid():
		pregnancy_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':Pregnancy_Diagnosis_Form, 'form_name':'pregnancy'})




@user_passes_test(vet_check, login_url='vet-login')
def clinical_approach(request):
    return render(request, 'portals/clinical_approach.html') 

@user_passes_test(vet_check, login_url='vet-login')
def sick_approach(request):
    if request.method == "POST":
        form = SickApproachForm(request.POST)
        if form.is_valid():
            vet_sick_form = Vet_Forms(vet_username=request.user, is_sick_approach_form=True)
            vet_sick_form.save()
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = SickApproachForm()

    context = {
        'form':form,
        'name':'Clinical Approach Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(vet_check, login_url='vet-login')
def dead_approach(request):
    if request.method == "POST":
        form = DeathApproachForm(request.POST)
        if form.is_valid():
            vet_death_form = Vet_Forms(vet_username=request.user, is_dead_approach_form=True)
            vet_death_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = DeathApproachForm()

    context = {
        'form':form,
        'name':'Post Mortem Approach Form'
         }
    return render(request, 'portals/forms.html', context)   

@user_passes_test(vet_check, login_url='vet-login')
def surgical_approach(request):
    if request.method == "POST":
        form = SurgicalApproachForm(request.POST)
        if form.is_valid():
            vet_surgical_form = Vet_Forms(vet_username=request.user, is_surgical_approach_form=True)
            vet_surgical_form.save() 
            form.save()
            messages.success(request, 'Details Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = SurgicalApproachForm()

    context = {
        'form':form,
        'name':'Surgical Approach Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(vet_check, login_url='vet-login')
def deworming(request):
    if request.method == "POST":
        form = DewormingForm(request.POST)
        if form.is_valid():
            vet_deworming_form = Vet_Forms(vet_username=request.user, is_deworming_form=True)
            vet_deworming_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = DewormingForm()

    context = {
        'form':form,
        'name':'Deworming Form'
         }
    return render(request, 'portals/forms.html', context)

@user_passes_test(vet_check, login_url='vet-login')    
def vaccination(request):
    if request.method == "POST":
        form = VaccinationForm(request.POST)
        if form.is_valid():
            vet_vaccination_form = Vet_Forms(vet_username=request.user, is_vaccination_form=True)
            vet_vaccination_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = VaccinationForm()

    context = {
        'form':form,
        'name':'Vaccination Form'
         }
    return render(request, 'portals/forms.html', context)

@user_passes_test(vet_check, login_url='vet-login')
def breeding_record(request):
    ...

@user_passes_test(vet_check, login_url='vet-login')
def artificial_insemination(request):
    if request.method == "POST":
        form = ArtificialInseminationForm(request.POST)
        if form.is_valid():
            vet_ai_form = Vet_Forms(vet_username=request.user, is_artificial_insemination_form=True)
            vet_ai_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = ArtificialInseminationForm()

    context = {
        'form':form,
        'name':'Artificial Insemination Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(farmer_check, login_url='vet-login')
def calf_registration(request):
    if request.method == "POST":
        form = CalfRegistrationForm(request.POST)
        if form.is_valid():
            vet_calf_form = Vet_Forms(is_calf_registration_form=True)
            vet_calf_form.save()
            form = form.save(commit=False)
            form.farmer_username = request.user
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('farmer-portal')    

    else:
        form = CalfRegistrationForm()

    context = {
        'form':form,
        'name':'Calf Registration Form'
         }
    return render(request, 'portals/fforms.html', context) 

@user_passes_test(farmer_check, login_url='vet-login')
def calf_form_view(request):
    calf_forms = Calf_Registration_Form.objects.filter(farmer_username=request.user)
    context = {
        'form_name': 'Calf Registration Form',
        'forms': calf_forms
    }    
    return render(request, 'portals/fformview.html', context)


@user_passes_test(farmer_check, login_url='vet-login')
def edit_calf_registration(request, pk):
	try:
		calf_sel = Calf_Registration_Form.objects.get(pk = pk)
	except Calf_Registration_Form.DoesNotExist:
		return redirect('index')
	calf_form = CalfRegistrationForm(request.POST or None, instance = calf_sel)
	if calf_form.is_valid():
		calf_form.save()
		return redirect('index')
	return render(request, 'portals/editfform.html', {'form':calf_form, 'form_name':'Calf Registration'})


@user_passes_test(farmer_check, login_url='vet-login')
def livestock_inventory(request):
    if request.method == "POST":
        form = LivestockInventoryForm(request.POST)
        if form.is_valid():
            vet_inventory_form = Vet_Forms(is_livestock_inventory_form=True)
            vet_inventory_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('farmer-portal')

    else:
        form = LivestockInventoryForm()

    context = {
        'form':form,
        'name':'Livestock Inventory Form',
         }

    return render(request, 'portals/forms.html', context)

@user_passes_test(farmer_check, login_url='vet-login')
def livestock_inventory_view(request):
    livestock_forms = Livestock_Inventory_Form.objects.filter(farmer_username=request.user)
    context = {
        'form_name': 'Livestock Inventory Form',
        'forms': livestock_forms
    }    
    return render(request, 'portals/livestockformview.html', context)


@user_passes_test(farmer_check, login_url='vet-login')
def edit_livestock_inventory(request, pk):
	try:
		livestock_sel = Livestock_Inventory_Form.objects.get(pk = pk)
	except Livestock_Inventory_Form.DoesNotExist:
		return redirect('index')
	livestock_form = LivestockInventoryForm(request.POST or None, instance = livestock_sel)
	if livestock_form.is_valid():
		livestock_form.save()
		return redirect('index')
	return render(request, 'portals/editfform.html', {'form':livestock_form, 'form_name':'Livestock Inventory Form'})


@user_passes_test(vet_check, login_url='vet-login')
def pregnancy_diagnosis(request):
    if request.method == "POST":
        form = PregnancyDiagnosisForm(request.POST)
        if form.is_valid():
            vet_preg_form = Vet_Forms(vet_username=request.user, is_pregnancy_diagnosis_form=True)
            vet_preg_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = PregnancyDiagnosisForm()

    context = {
        'form':form,
        'name':'Pregnancy Diagnosis Form'
         }
    return render(request, 'portals/forms.html', context)
 

@user_passes_test(vet_check, login_url='vet-login')
def consultation_form_view(request):
    consultation_forms = Farm_Consultation.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Consultation Form',
        'forms': consultation_forms
    }    
    return render(request, 'portals/consultationformview.html', context)
 
    
@user_passes_test(vet_check, login_url='vet-login')
def edit_consultation_form(request, pk):
	try:
		consul_sel = Farm_Consultation.objects.get(pk = pk)
	except Farm_Consultation.DoesNotExist:
		return redirect('index')
	consultation_form = FarmConsultationForm(request.POST or None, instance = consul_sel)
	if consultation_form.is_valid():
		consultation_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':consultation_form, 'form_name':'Consultation'})

@user_passes_test(vet_check, login_url='vet-login')
def consultation(request):
    if request.method == "POST":
        form = FarmConsultationForm(request.POST)
        if form.is_valid():
            consultation_form = Vet_Forms(is_farm_consultation=True)
            consultation_form.save() 
            consul_form = Vet_Forms(vet_username=request.user, is_farm_consultation=True)
            consul_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = FarmConsultationForm()

    context = {
        'form':form,
        'name':'Farm consultation form'
         }
    return render(request, 'portals/forms.html', context)



@user_passes_test(vet_check, login_url='vet-login')
def vet_billing_form_view(request):
    bill_forms = Veterinary_Billing_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Vet Billing Form',
        'forms': bill_forms
    }    
    return render(request, 'portals/vetbillformview.html', context)
 
    
@user_passes_test(vet_check, login_url='vet-login')
def edit_vet_billing_form(request, pk):
	try:
		bill_sel = Veterinary_Billing_Form.objects.get(pk = pk)
	except Veterinary_Billing_Form.DoesNotExist:
		return redirect('index')
	billing_form = VeterinaryBillingForm(request.POST or None, instance = bill_sel)
	if billing_form.is_valid():
		billing_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':billing_form, 'form_name':'Vet Billing'})

@user_passes_test(vet_check, login_url='vet-login')
def vet_billing(request):
    if request.method == "POST":
        form = VeterinaryBillingForm(request.POST)
        if form.is_valid():
            billing_form = Vet_Forms(is_vet_billing_form=True)
            billing_form.save() 
            bill_form = Vet_Forms(vet_username=request.user, is_vet_billing_form=True)
            bill_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = VeterinaryBillingForm()

    context = {
        'form':form,
        'name':'Vet Billing form'
         }
    return render(request, 'portals/forms.html', context)


@user_passes_test(vet_check, login_url='vet-login')
def lab_form_view(request):
    lab_forms = Laboratory_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Laboratory Form',
        'forms': lab_forms
    }    
    return render(request, 'portals/labformview.html', context)
 
    
@user_passes_test(vet_check, login_url='vet-login')
def edit_lab_form(request, pk):
	try:
		lab_sel = Laboratory_Form.objects.get(pk = pk)
	except Laboratory_Form.DoesNotExist:
		return redirect('index')
	lab_form = LaboratoryForm(request.POST or None, instance = lab_sel)
	if lab_form.is_valid():
		lab_form.save()
		return redirect('index')
	return render(request, 'portals/editform.html', {'form':lab_form, 'form_name':'Laboratory'})

@user_passes_test(vet_check, login_url='vet-login')
def lab(request):
    if request.method == "POST":
        form = LaboratoryForm(request.POST)
        if form.is_valid():
            labo_form = Vet_Forms(is_vet_billing_form=True)
            labo_form.save() 
            lab_form = Vet_Forms(vet_username=request.user, is_lab_form=True)
            lab_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = LaboratoryForm()

    context = {
        'form':form,
        'name':'Laboratory form'
         }
    return render(request, 'portals/forms.html', context)



@user_passes_test(vet_check, login_url='vet-login')
def referral_form_view(request):
    referral_forms = Referral_Form.objects.filter(vet_form__vet_username=request.user)
    context = {
        'form_name': 'Referral Form',
        'forms': referral_forms
    }    
    return render(request, 'portals/referralformview.html', context)



@user_passes_test(vet_check, login_url='vet-login')

@user_passes_test(vet_check, login_url='vet-login') 
def referral_form(request):
    if request.method == "POST":
        form = ReferalForm(request.POST)
        if form.is_valid():
            referral_form = Vet_Forms(is_vet_referral_form=True)
            referral_form.save() 
            referral_form= Vet_Forms(vet_username=request.user, is_referral_form=True)
            referral_form.save() 
            form.save()
            messages.success(request, 'Details  Successfully Saved')
            return redirect('vet-portal')    

    else:
        form = ReferalForm()

    context = {
        'form':form,
        'name':'Referral form'
         }
    return render(request, 'portals/forms.html', context)

class Sick_Form_Pdf(View):

    def get(self, request):
        try:
            sick_forms = Sick_Approach_Form.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')    
        if sick_forms:
            params = {
                'today':timezone.now,
                'forms': sick_forms,
                'request': request
            }
            return Render.render('portals/sick_form_pdf.html', params)
        else:
            messages.warning(self.request, f'No Sick form available for {self.request.user}')
            return redirect('index')    


class Sick_Form_Pdf_Vet(View):

    def get(self, request):
        try:
            sick_forms = Sick_Approach_Form.objects.filter(vet_form__vet_username=self.request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('vet-portal')    
        if sick_forms:
            params = {
                'today':timezone.now,
                'forms': sick_forms,
                'request': request
            }
            return Render.render('portals/sick_form_pdf.html', params)
        else:
            messages.warning(self.request, f'No Sick form available for {self.request.user}')
            return redirect('index') 

class Dead_Form_Pdf(View):

    def get(self, request):
        try:
            dead_forms = Death_Approach_Form.objects.filter(farmer_username=request.user)
        except: 
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if dead_forms:
            params = {
                'today':timezone.now,
                'forms': dead_forms,
                'request': request
            }
            return Render.render('portals/dead_form_pdf.html',params)
        else:
            messages.warning(self.request,f'No dead form available for {self.request.user}')
            return redirect('index')


class Dead_Form_Pdf_Vet(View):

    def get(self, request):
        try:
            dead_forms = DeathApproachForm.objects.filter(vet_form__vet_username=self.request.user)
        except:
            messages.warning(self.request, f'Death approach form for {request.user} not available')
            return redirect('vet-portal')    
        if dead_forms:
            params = {
                'today':timezone.now,
                'forms': dead_forms,
                'request': request
            }
            return Render.render('portals/dead_form_pdf.html', params)
        else:
            messages.warning(self.request, f'No Sick form available for {self.request.user}')
            return redirect('index') 


class Surgical_Form_Pdf(View):

    def get(self, request):
        try:
            surgical_forms = Surgical_Approach_Form.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if surgical_forms:
            params = {
                'today':timezone.now,
                'forms': surgical_forms,
                'request': request
            }
            return Render.render('portals/surgical_form_pdf.html',params)
        else:
            messages.warning(self.request,f'No surgical form available for {self.request.user}')
            return redirect('index')


class Deworming_Form_Pdf(View):

    def get(self, request):
        try:
            deworming_forms = Deworming_Form.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if deworming_forms:
            params = {
                'today':timezone.now,
                'forms': deworming_forms,
                'request': request
            }
            return Render.render('portals/deworming_form_pdf.html', params)
        else:
            messages.warning(self.request, f'No deworming form available for {self.request.user}')
            return redirect('index')    


class Vaccination_Form_Pdf(View):

    def get(self, request):
        try:
            vaccination_forms = Vaccination_Form.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if vaccination_forms:
            params = {
                'today':timezone.now,
                'forms': vaccination_forms,
                'request': request
            }
            return Render.render('portals/vaccination_pdf_form.html', params)
        else:
            messages.warning(self.request, f'No vaccination form available for {self.request.user}')
            return redirect('index') 


class Artificial_Insemination_Form_Pdf(View):

    def get(self, request):
        try:
            Artificial_forms = Artificial_Insemination_Form.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if Artificial_forms:
            params = {
                'today':timezone.now,
                'forms': Artificial_forms,
                'request': request
            }
            return Render.render('portals/artificial_form_pdf.html', params)
        else:
            messages.warning(self.request, f'No artificial form available for {self.request.user}')
            return redirect('index') 



class Farm_Consultation_Form_Pdf(View):

    def get(self, request):
        try:
            consultation_forms = Farm_Consultation.objects.filter(farmer_username=request.user)
        except:
            messages.warning(self.request, f'Sick approach form for {request.user} not available')
            return redirect('farmer-portal')
        if consultation_forms:
            params = {
                'today':timezone.now,
                'forms': consultation_forms,
                'request': request
            }
            return Render.render('portals/consultation_form.html', params)
        else:
            messages.warning(self.request, f'No consultation form available for {self.request.user}')
            return redirect('index') 


class Pregnancy_Diagnosis_Form_Pdf(View):

    def get(self, request):
        diagnosis_forms = Pregnancy_Diagnosis_Form.objects.filter(farmer_username=request.user)
        if diagnosis_forms:
            params = {
                'today':timezone.now,
                'forms': diagnosis_forms,
                'request': request
            }
            return Render.render('portals/diagnosis_form.html', params)
        else:
            messages.warning(self.request, f'No pregnancy form available for {self.request.user}')
            return redirect('index') 

class Calf_Registration_Form_Pdf(View):

    def get(self, request):
        calf_reg_forms = Calf_Registration_Form.objects.filter(farmer_username=request.user)
        if calf_reg_forms:
            params = {
                'today':timezone.now,
                'forms': calf_reg_forms,
                'request': request
            }
            return Render.render('portals/calf_reg_form.html', params)
        else:
            messages.warning(self.request, f'No Calf registration form available for {self.request.user}')
            return redirect('index') 

class Livestock_Form_Pdf(View):

    def get(self, request):
        livestock_forms = Livestock_Inventory_Form.objects.filter(farmer_username=request.user)
        if livestock_forms:
            params = {
                'today':timezone.now,
                'forms': livestock_forms,
                'request': request
            }
            return Render.render('portals/livestock_form.html', params)
        else:
            messages.warning(self.request, f'No Livestock form available for {self.request.user}')
            return redirect('index') 



def display_images(request):
    inventory = Livestock_Inventory_Form.objects.get(farmer_username=request.user)
    context = {
        'img_obj': inventory
    }
    return render(request, 'portals/gallery.html', context)



     