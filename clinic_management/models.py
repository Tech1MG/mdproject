from django.db import models
from datetime import datetime

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone_num = models.CharField(max_length=20)
    note = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    @property
    def birth_year(self):
        today = datetime.now()
        birth_year = int(
            today.year
            - (self.age)
        )
        return birth_year

    def __str__(self):
        return self.name + " | Age: " + str(self.age) + " | Phone: " +self.phone_num
    

class Appointment(models.Model):
    visit_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    case_description = models.TextField()
    followup_note = models.TextField()
    
    class Meta:
        ordering = ('visit_date', )

class History(models.Model):
    disease = models.CharField(max_length=150)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="histories")
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient.name+ " | Age: " + str(self.patient.age) + " | Phone: " +self.patient.phone_num) + " | Desease: " + self.disease

    class Meta:
        ordering = ('patient', )
        verbose_name_plural = "Histories"

class Allergy(models.Model):
    drug = models.CharField(max_length=150)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="allergies")
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient.name+ " | Age: " + str(self.patient.age) + " | Phone: " +self.patient.phone_num) + " | Drug Allergies: " + self.drug

    class Meta:
        ordering = ('patient', )
        verbose_name_plural = "Allergies"

class Medication(models.Model):
    medication = models.CharField(max_length=150)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medications")
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient.name+ " | Age: " + str(self.patient.age) + " | Phone: " +self.patient.phone_num) + " | Medications: " + self.medication


    class Meta:
        ordering = ('patient', )



class Diagnosis(models.Model):
    title = models.CharField(max_length=150)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="diagnosis")
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('appointment', )
        verbose_name_plural = "Diagnosis"

class Prescription(models.Model):
    title = models.CharField(max_length=150)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="prescriptions")
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('appointment', )