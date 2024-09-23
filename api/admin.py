from django.contrib import admin
from .models import (
    Patient, User, Doctor, Appointment, Prescription, Note,
    Hospital, QUEUEDOCHOS, DocRecord, Session, Medicine,
    Pharmacy, Report, Schedule, Queue, Feedback, NoteUser
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Note)
admin.site.register(Hospital)
admin.site.register(QUEUEDOCHOS)
admin.site.register(DocRecord)
admin.site.register(Session)
admin.site.register(Medicine)
admin.site.register(Pharmacy)
admin.site.register(Report)
admin.site.register(Schedule)
admin.site.register(Queue)
admin.site.register(Feedback)
admin.site.register(NoteUser)
