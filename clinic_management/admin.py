from django.contrib import admin

from .models import Patient, Appointment, History, Allergy, Medication, Diagnosis, Prescription


class AppointmentItems(admin.TabularInline):
    model = Appointment
    raw_id_fields = ['patient']


class HistoryItems(admin.TabularInline):
    model = History
    raw_id_fields = ['patient']


class AllergyItems(admin.TabularInline):
    model = Allergy
    raw_id_fields = ['patient']


class MedicationItems(admin.TabularInline):
    model = Medication
    raw_id_fields = ['patient']


class PatientAdmin (admin.ModelAdmin):
    list_display = ('name', 'age', 'birth_year', 'phone_num')
    search_fields = ['name', 'phone_num']
    inlines = [AppointmentItems, HistoryItems, AllergyItems, MedicationItems]

    # prepopulated_fields = {'birth_year': (1990, )}

class DiagnosisItems(admin.TabularInline):
    model = Diagnosis
    raw_id_fields = ['appointment']

class PrescriptionItems(admin.TabularInline):
    model = Prescription
    raw_id_fields = ['appointment']

class AppointmentAdmin (admin.ModelAdmin):
    search_fields = ['patient__name']
    list_display = ( 'visit_date', 'patient',)
    inlines = [DiagnosisItems, PrescriptionItems]

class AllergyAdmin (admin.ModelAdmin):
    search_fields = ['patient__name']

class HistoryAdmin (admin.ModelAdmin):
    search_fields = ['patient__name']

class MedicationAdmin (admin.ModelAdmin):
    search_fields = ['patient__name']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Allergy, AllergyAdmin)
admin.site.register(Medication, MedicationAdmin)
# admin.site.register(Diagnosis)
