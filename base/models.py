from functools import update_wrapper
from django.db import models


# Create your models here.

edu_level = (('undergraduate', 'undergraduate'),
             ('masters', 'masters'), ('doctorate', 'doctorate'))

bg = (('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'),
      ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'))

vaccine = (('biontech', 'biontech'), ('sinovac', 'sinovac'))

days_of_the_week = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)


class Employee(models.Model):
    tc = models.CharField(max_length=11, primary_key=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    blood_group = models.CharField(max_length=3, null=False, choices=bg)
    city = models.CharField(max_length=30, null=False)
    pos = models.CharField(max_length=30, null=True, blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    hobbies = models.TextField(null=True)
    level_of_education = models.CharField(
        max_length=30, null=False, choices=edu_level)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Drug(models.Model):
    name = models.CharField(max_length=30, null=False, primary_key=True)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    pcode = models.CharField(max_length=5, primary_key=True)
    drugs = models.ManyToManyField(Drug, blank=True)

    def __str__(self):
        return self.pcode


class Symptom(models.Model):
    title = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.title


class Disease(models.Model):
    dcode = models.CharField(max_length=5, primary_key=True)
    dname = models.CharField(max_length=30, null=False)
    symptoms = models.ManyToManyField(Symptom, blank=True)
    date_of_disease = models.DateField(
        auto_now=False, auto_now_add=False, null=False)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    p = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.dname + '(' + str(self.emp) + ')'


class ContactedPersons(models.Model):
    id = models.AutoField(primary_key=True)
    em = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.em)


class ChronicDisease(models.Model):
    title = models.CharField(max_length=60, primary_key=True)


class Covid(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    symptoms = models.ManyToManyField(Symptom, blank=True)
    p_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    n_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    contacted_persons = models.ManyToManyField(ContactedPersons, blank=True)
    vaccinated = models.BooleanField(null=False)
    vaccine_type = models.CharField(
        max_length=30, choices=vaccine, null=True, blank=True)
    doz = models.IntegerField(null=True, blank=True)
    cd = models.ManyToManyField(ChronicDisease, blank=True)

    def __str__(self):
        return str(self.emp) + ' ' + '(' + str(self.p_date) + ')'


class TimeTable(models.Model):
    day = models.CharField(max_length=32, null=False, choices=days_of_the_week)
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.day + "(" + str(self.emp) + ")"


class EduCovidStat(models.Model):
    level_of_education = models.CharField(
        max_length=30, null=False, choices=edu_level, primary_key=True)
    mycount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'edu_covid_stat'

    def __str__(self):
        return str(self.level_of_education) + '(' + str(self.mycount) + ')'


class MostCommonDisease(models.Model):
    dname = models.CharField(max_length=30, primary_key=True, null=False)
    d_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "most_common_disease"

    def __str__(self):
        return self.dname + '(' + str(self.d_count) + ')'


class MostCommonDiseaseEmp(models.Model):
    tc = models.CharField(primary_key=True, max_length=11, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    dname = models.CharField(max_length=30, null=False)

    class Meta:
        managed = False
        db_table = "most_common_disease_emp"

    def __str__(self):
        return self.tc + '(' + str(self.dname) + ')'


class CityCommonDisease(models.Model):
    city = models.CharField(primary_key=True, max_length=30, null=False)
    dname = models.CharField(max_length=30, null=False)
    d_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "city_common_diseases"
        unique_together = ("city", "dname")

    def __str__(self):
        return self.city + " - " + self.dname


class BloodGroupCovidFreq(models.Model):
    blood_group = models.CharField(primary_key=True, max_length=3)
    covid_freq = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = "blood_group_covid_freq"

    def __str__(self):
        return self.blood_group + " - " + str(self.covid_freq)


class CovidEmpWorkingHoursStat(models.Model):
    hours_per_week = models.DecimalField(
        max_digits=5, decimal_places=2, primary_key=True)
    num_of_emps = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "covid_emp_working_hours_stat"

    def __str__(self):
        return str(self.hours_per_week) + " - " + str(self.num_of_emps)


class MostCommonCovidSymptom(models.Model):
    symptom = models.CharField(max_length=30, primary_key=True)
    symptom_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "most_common_covid_symptoms"

    def __str__(self):
        return str(self.symptom) + " - " + str(self.symptom_count
                                               )


class MostContactedPerson(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "most_contacted_persons_list"

    def __str__(self):
        return self.tc + " - " + self.first_name + " " + self.last_name + "(" + str(self.contact_count) + ")"


class BiontechCovidEmp(models.Model):
    total_time = models.DecimalField(
        max_digits=6, decimal_places=2, primary_key=True)
    num_of_emps = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "biontech_covid_emps"

    def __str__(self):
        return str(self.total_time) + "(" + str(self.num_of_emps) + ")"


class SinovacCovidEmp(models.Model):
    total_time = models.DecimalField(
        max_digits=6, decimal_places=2, primary_key=True)
    num_of_emps = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "sinovac_covid_emps"

    def __str__(self):
        return str(self.total_time) + "(" + str(self.num_of_emps) + ")"


class WeekendsWorker(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    day = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = "weekends_workers"

    def __str__(self):
        return self.tc + " - " + self.first_name + " " + self.last_name


class WeekendsWorkersCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "weekends_workers_covid"

    def __str__(self):
        return self.tc + " - " + self.first_name + " " + self.last_name


class MostFreqillEmp(models.Model):
    emp_id = models.CharField(max_length=11, primary_key=True)
    disease_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "most_freq_ill_emps"

    def __str__(self):
        return self.tc + " - " + str(self.disease_count)


class MostFreqillEmpsCovid(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "most_freq_ill_emps_covid"

    def __str__(self):
        return self.tc + " - " + self.first_name + " " + self.last_name


class NonVaccinatedEmp(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    covid_d = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = "non_vaccinated_emp"

    def __str__(self):
        return self.tc + " - " + self.first_name + " " + self.last_name


class NonVaccinatedEmpDisPre(models.Model):
    dname = models.CharField(max_length=30)
    p_id = models.CharField(max_length=5, primary_key=True)

    class Meta:
        managed = False
        db_table = "non_vaccinated_emp_diseases"

    def __str__(self):
        return self.dname + " - " + self.prescription_id


class MostCommonlyUsedDrug(models.Model):
    dname = models.CharField(max_length=30, primary_key=True)
    d_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = "most_common_drugs"


class MostCommonlyUsedDrugsUser(models.Model):
    tc = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "most_common_drugs_users"
