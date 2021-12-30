from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path("", EmployeeList.as_view(), name="employees-list"),
    path("create-employee", CreateEmployee.as_view(), name="create-employee"),
    path("employees/update/<str:pk>/",
         UpdateEmployee.as_view(), name="update-employee"),
    path("employees/delete/<str:pk>/",
         DeleteEmployee.as_view(), name="delete-employee"),
    path("disease-list", DiseaseList.as_view(), name="disease-list"),
    path("add-disease", CreateDisease.as_view(), name="add-disease"),
    path("diseases/update/<str:pk>/",
         UpdateDisease.as_view(), name="update-disease"),
    path("diseases/delete/<str:pk>/",
         DeleteDisease.as_view(), name="delete-disease"),
    path("covid-list", CovidList.as_view(), name="covid-list"),
    path("add-covid", CreateCovid.as_view(), name="add-covid"),
    path("covid/update/<int:pk>/", UpdateCovid.as_view(), name="update-covid"),
    path("covid/delete/<int:pk>/", DeleteCovid.as_view(), name="delete-covid"),
    path("time-table", TimeTableList.as_view(), name="time-table"),
    path("add-time-table", CreateTimeTable.as_view(), name="add-time-table"),
    path("time-time/update/<int:pk>/",
         UpdateTimeTable.as_view(), name="update-time-table"),
    path("time-table/delete/<int:pk>/",
         DeleteTimeTable.as_view(), name="delete-time-table"),
    path("covid-analysis/covid-edu-stat",
         edu_covid_stat, name="edu-covid-stat"),
    path("covid-analysis/vac-vs-non-vac",
         vac_non_vac_ratio, name="vac-vs-non-vac"),
    path("covid-analysis/blood-group-covid-stat",
         blood_group_covid_stat, name="blood-group-covid-stat"),
    path("covid-analysis/working-hours-covid-stat",
         working_hours_covid_stat, name="working-hours-covid-stat"),
    path("covid-analysis/most-common-covid-symptoms",
         most_common_covid_symptoms, name="most-common-covid-symptoms"),
    path("covid-analysis/most-contacted-persons",
         most_contacted_persons, name="most-contacted-persons"),
    path("covid-analysis/biontech-vs-sinovac",
         biontech_sinovac_comp, name="biontech-vs-sinovac"),
    path("covid-analysis/weekends-workers-covid-stat",
         weekends_workers_covid_report, name="weekends-workers-covid-stat"),
    path("covid-analysis/most-freq-ill-emps-covid",
         most_freq_ill_emps_covid, name="most-freq-ill-emps-covid"),
    path("disease-analysis/top-three-common-diseases",
         most_common_diseases, name="top-three-common-diseases"),
    path("disease-analysis/city-common-diseases",
         city_common_diseases, name="city-common-diseases"),
    path("disease-analysis/most-commonly-used-drugs-emps",
         most_used_drugs_emps, name="most-commonly-used-drugs-emps"),
    path("disease-analysis/non-vaccinated-emp-dis-pres",
         non_vaccinated_emp_dis_pres, name="non-vaccinated-emp-dis-pres"),







]
