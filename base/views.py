from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import *

# Create your views here.

# employee


class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'base/employee-list.html'


class CreateEmployee(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employees-list')
    template_name = 'base/employee-form.html'


class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employees-list')
    template_name = 'base/employee-form.html'


class DeleteEmployee(DeleteView):
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employees-list')
    template_name = 'base/employee-delete.html'


# disease
class DiseaseList(ListView):
    model = Disease
    context_object_name = 'diseases'
    template_name = 'base/disease-list.html'


class CreateDisease(CreateView):
    model = Disease
    fields = '__all__'
    success_url = reverse_lazy('disease-list')
    template_name = 'base/disease-form.html'


class UpdateDisease(UpdateView):
    model = Disease
    fields = '__all__'
    success_url = reverse_lazy('disease-list')
    template_name = 'base/disease-form.html'


class DeleteDisease(DeleteView):
    model = Disease
    context_object_name = 'disease'
    success_url = reverse_lazy('disease-list')
    template_name = 'base/disease-delete.html'


# covid
class CovidList(ListView):
    model = Covid
    context_object_name = 'covids'
    template_name = 'base/covid-list.html'


class CreateCovid(CreateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid-list')
    template_name = 'base/covid-form.html'


class UpdateCovid(UpdateView):
    model = Covid
    fields = '__all__'
    success_url = reverse_lazy('covid-list')
    template_name = 'base/covid-form.html'


class DeleteCovid(DeleteView):
    model = Covid
    context_object_name = 'covid'
    success_url = reverse_lazy('covid-list')
    template_name = 'base/covid-delete.html'


# time table
class TimeTableList(ListView):
    model = TimeTable
    context_object_name = 'time_table'
    template_name = 'base/time-table.html'


class CreateTimeTable(CreateView):
    model = TimeTable
    fields = '__all__'
    success_url = reverse_lazy('time-table')
    template_name = 'base/time-table-form.html'


class UpdateTimeTable(UpdateView):
    model = TimeTable
    fields = '__all__'
    success_url = reverse_lazy('time-table')
    template_name = 'base/time-table-form.html'


class DeleteTimeTable(DeleteView):
    model = TimeTable
    context_object_name = 'time_table'
    success_url = reverse_lazy('time-table')
    template_name = 'base/time-table-delete.html'


# class PrescriptionList(ListView):
#     model = Prescription
#     context_object_name = 'prescriptions'
#     template_name = 'base/presciption-list.html'


# class CreatePrescription(CreateView):
#     model = Prescription
#     context_object_name = 'prescription'
#     success_url = reverse_lazy('prescriptions')
#     template_name = 'base/prescription-form'


# class SymptomsList(ListView):
#     model = Prescription
#     context_object_name = 'symptoms'
#     template_name = 'base/symptoms-list.html'


# class CreateSymptom(CreateView):
#     model = Symptom
#     context_object_name = 'symptom'
#     success_url = reverse_lazy('symptoms')
#     template_name = 'base/symptom-form'


# class DrugsList(ListView):
#     model = Drug
#     context_object_name = 'drugs'
#     template_name = 'base/drugs-list.html'


# class CreateDrug(CreateView):
#     model = Drug
#     context_object_name = 'drug'
#     success_url = reverse_lazy('drugs')
#     template_name = 'base/drug-form'


# class ChronicDiseaseList(ListView):
#     model = ChronicDisease
#     context_object_name = 'chronic_diseases'
#     template_name = 'base/chronic-disease-list.html'


# class CreateChronicDisease(CreateView):
#     model = ChronicDisease
#     context_object_name = 'chronic_disease'
#     success_url = reverse_lazy('chronic-diseases')
#     template_name = 'base/chronic-disease-form'


def edu_covid_stat(request):
    groups = EduCovidStat.objects.all()
    undergra_cnt = 0
    masters_cnt = 0
    doctorate_cnt = 0
    undergra_p = 0
    masters_p = 0
    doctorate_p = 0
    total = 0
    for group in groups:
        if group.level_of_education == "doctorate":
            doctorate_cnt = group.mycount
        if group.level_of_education == "masters":
            masters_cnt = group.mycount
        if group.level_of_education == "undergraduate":
            undergra_cnt = group.mycount

    total = undergra_cnt + masters_cnt + doctorate_cnt
    doctorate_p = (doctorate_cnt * 100) / total
    masters_p = (masters_cnt * 100) / total
    undergra_p = (undergra_cnt * 100) / total

    context = {
        'doctorate_p': doctorate_p,
        'masters_p': masters_p,
        'undergra_p': undergra_p,
        'doctorate_cnt': doctorate_cnt,
        'masters_cnt': masters_cnt,
        'undergra_cnt':  undergra_cnt
    }

    return render(request, 'base/edu-covid-stat.html', context)


def most_common_diseases(request):
    diseases = MostCommonDisease.objects.all()
    # max_cnt1 = 0
    # max_cnt2 = 0
    # max_cnt3 = 0
    # for group in diseases:
    #     if group.disease_count >= max_cnt1 or (group.disease_count >= max_cnt2):
    #         max_cnt3 = max_cnt2
    #         if group.disease_count >= max_cnt1:
    #             max_cnt2 = max_cnt1
    #             max_cnt1 = group.disease_count
    #         elif group.disease_count >= max_cnt2:
    #             max_cnt2 = group.disease_count
    # selected_d = []
    # for group in diseases:
    #     if group.disease_count == max_cnt1 or group.disease_count == max_cnt2 or group.disease_count == max_cnt3:
    #         selected_d.append(group)
    employees = MostCommonDiseaseEmp.objects.all()

    context = {
        'selected_d': diseases,
        'employees': employees
    }

    return render(request, 'base/common-diseases-emp.html', context)


def city_common_diseases(request):
    common_diseases = CityCommonDisease.objects.all()
    city = ''
    pre_city = ''
    cnt = 0
    selected_d = []
    for disease in common_diseases:
        pre_city = city
        city = disease.city
        if pre_city != city:
            for disease in common_diseases:
                if city == disease.city and cnt < 4:
                    selected_d.append(disease)
                    cnt += 1

            cnt = 0
    context = {
        'selected_d': selected_d,
    }
    return render(request, 'base/city_common_diseases.html', context)


def most_used_drugs_emps(request):
    commonly_used_drugs = MostCommonlyUsedDrug.objects.all()
    commonly_used_drugs_users = MostCommonlyUsedDrugsUser.objects.all()
    context = {
        'commonly_used_drugs': commonly_used_drugs,
        'commonly_used_drugs_users': commonly_used_drugs_users
    }
    return render(request, 'base/most-commonly-used-drugs-emps.html', context)


def vac_non_vac_ratio(request):
    vaccinated_cnt = 0
    non_vaccinated_cnt = 0
    total = 0
    covid_emps = Covid.objects.all()
    for emp in covid_emps:
        if(emp.vaccinated == True):
            vaccinated_cnt += 1

        else:
            non_vaccinated_cnt += 1
    total = (vaccinated_cnt + non_vaccinated_cnt)
    if total != 0:  # check against zero division
        vaccinated_per = (vaccinated_cnt/total) * 100
        non_vaccinated_per = (non_vaccinated_cnt/total) * 100

    context = {
        "vaccinated_per": vaccinated_per,
        "non_vaccinated_per": non_vaccinated_per,
        "vaccinated_cnt": vaccinated_cnt,
        "non_vaccinated_cnt": non_vaccinated_cnt
    }
    return render(request, 'base/vaccination_stats.html', context)


def blood_group_covid_stat(request):
    emp_groups = BloodGroupCovidFreq.objects.all()
    context = {
        'emp_groups': emp_groups
    }
    return render(request, "base/blood-group-covid-stat.html", context)


def working_hours_covid_stat(request):
    emp_groups = CovidEmpWorkingHoursStat.objects.all()
    context = {
        'emp_groups': emp_groups
    }
    return render(request, "base/working-hours-covid-stat.html", context)


def most_common_covid_symptoms(request):
    symptoms = MostCommonCovidSymptom.objects.all()
    context = {
        'symptoms': symptoms
    }
    return render(request, "base/most-common-covid-symptoms.html", context)


def most_contacted_persons(request):
    emps = MostContactedPerson.objects.all()
    context = {
        'emps': emps
    }
    return render(request, "base/most-contacted-persons.html", context)


def biontech_sinovac_comp(request):
    biontech = BiontechCovidEmp.objects.all()
    sinovac = SinovacCovidEmp.objects.all()
    biontech_avg = 0
    biontech_total_days = 0
    biontech_num_of_emps = 0

    sinovac_avg = 0
    sinovac_total_days = 0
    sinovac_num_of_emps = 0

    for emp in biontech:
        biontech_total_days += emp.total_time  # here time is measured in days
        biontech_num_of_emps += emp.num_of_emps  # here time is measured in days

    for emp in sinovac:
        sinovac_total_days += emp.total_time
        sinovac_num_of_emps += emp.num_of_emps
    if biontech_num_of_emps != 0:
        biontech_avg = biontech_total_days/biontech_num_of_emps
    if sinovac_num_of_emps != 0:
        sinovac_avg = sinovac_total_days/sinovac_num_of_emps

    context = {
        'biontech_total_days': biontech_total_days,
        'biontech_num_of_emps': biontech_num_of_emps,
        'biontech_avg': biontech_avg,
        'sinovac_total_days': sinovac_total_days,
        'sinovac_num_of_emps': sinovac_num_of_emps,
        'sinovac_avg': sinovac_avg
    }
    return render(request, "base/biontech-sinovac.html", context)


def weekends_workers_covid_report(request):
    employees = WeekendsWorker.objects.all()
    covid_emps = WeekendsWorkersCovid.objects.all()

    context = {
        'all_emps': employees,
        'covid_emps': covid_emps
    }

    return render(request, "base/weekends-workers-covid-report.html", context)


def most_freq_ill_emps_covid(request):
    emps = MostFreqillEmp.objects.all()
    covid_emps = MostFreqillEmpsCovid.objects.all()

    context = {
        'emps': emps,
        'covid_emps': covid_emps
    }

    return render(request, "base/most-freq-ill-emps-covid.html", context)


def non_vaccinated_emp_dis_pres(request):
    emp = NonVaccinatedEmp.objects.all()
    dis_pres = NonVaccinatedEmpDisPre.objects.all()

    context = {
        'emp': emp,
        'dis_pres': dis_pres
    }

    return render(request, "base/non-vaccinated-emp-dis-pres.html", context)
