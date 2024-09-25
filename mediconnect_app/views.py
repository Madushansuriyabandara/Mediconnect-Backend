from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .dtos import *
from .models import *
from .serializers import *

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [ ###
#     ]
#     return Response(routes)


# @api_view(['GET'])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def createUser(request):
#     data = request.data
#     user = User.objects.create(
#         User_ID = data['User_ID'],
#         Username = data['Username'],
#         Role = data['Role'],
#         Email = data['Email'],
#         Password = data['Password'],
#         NIC = data['NIC'],
#         Device_ID = data['Device_ID'],
#         Birthday = data['Birthday'],
#         First_name = data['First_name'],
#         Last_name = data['Last_name'],
#     )
#     serializer = UserSerializer(user)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUserById(request, pk):
#     user = User.objects.get(User_ID=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateUser(request, pk):
#     data = request.data
#     user = User.objects.get(User_ID=pk)
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteUser(request, pk):
#     user = User.objects.get(User_ID=pk)
#     user.delete()
#     return Response('User deleted')



# @api_view(['GET'])
# def getPatients(request):
#     patients = Patient.objects.all()
#     serializer = PatientDTOSerializer(patients, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createPatient(request):
#     data = request.data
#     user = get_object_or_404(User, User_ID=data['User_ID'])
#     patient = Patient.objects.create(
#         User_ID = user,
#         Patient_ID = data['Patient_ID'],
#         Breakfast_time = data['Breakfast_time'],
#         Lunch_time = data['Lunch_time'],
#         Dinner_time = data['Dinner_time'],
#     )
#     return Response('Patient created')

from mediconnect_app.dtos import PatientDTO


@api_view(['GET'])
def getPatientById(request, pk):
    patient = Patient.objects.get(Patient_ID=pk)
    patientDto = PatientDTO(
        User_ID = patient.User_ID.User_ID,
        Patient_ID = patient.Patient_ID,
        Breakfast_time = patient.Breakfast_time,
        Lunch_time = patient.Lunch_time,
        Dinner_time = patient.Dinner_time,
    )
    serializer = PatientDTOSerializer(patientDto, many=False)
    return Response(serializer.data)

# @api_view(['PUT'])
# def updatePatient(request, pk):
#     data = request.data
#     user = get_object_or_404(User, User_ID=data['User_ID'])
#     Patient.objects.filter(Patient_ID=pk).update(
#         User_ID = user,
#         Breakfast_time = data['Breakfast_time'],
#         Lunch_time = data['Lunch_time'],
#         Dinner_time = data['Dinner_time'],
#     )
#     return Response('Patient updated')


# @api_view(['DELETE'])
# def deletePatient(request, pk):
#     patient = Patient.objects.get(Patient_ID=pk)
#     patient.delete()
#     return Response('Patient deleted')


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.authtoken.models import Token
# from django.db import transaction
# from .models import *
# from .serializers import *
# from django.core.mail import send_mail


# # ---------------- User Management and Authentication ---------------- #
# @api_view(['POST'])
# def registerUser(request):
#     """ Register a new user and create either a Doctor or Patient profile """
#     data = request.data
#     serializer = UserSerializer(data=data)
#     if serializer.is_valid():
#         user = serializer.save()
        
#         # Create doctor or patient profile based on the role
#         if data['Role'] == 'Doctor':
#             Doctor.objects.create(User_ID=user, Specialization=data.get('Specialization'))
#         elif data['Role'] == 'Patient':
#             Patient.objects.create(User_ID=user, Breakfast_time=data.get('Breakfast_time'),
#                                    Lunch_time=data.get('Lunch_time'),
#                                    Dinner_time=data.get('Dinner_time'))

#         # Send verification email (placeholder for actual functionality)
#         send_mail(
#             'Welcome to MediConnect',
#             'Thank you for registering. Please verify your email.',
#             'noreply@mediconnect.com',
#             [user.Email],
#             fail_silently=False,
#         )
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def loginUser(request):
#     """ Login the user and return the token """
#     data = request.data
#     user = authenticate(request, email=data['email'], password=data['password'])
#     if user is not None:
#         # Check if the user has logged in from another device and logout from that device
#         token, created = Token.objects.get_or_create(user=user)
#         login(request, user)
#         return Response({'token': token.key, 'role': user.Role}, status=status.HTTP_200_OK)
#     return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def logoutUser(request):
#     """ Logout and destroy token """
#     request.user.auth_token.delete()
#     logout(request)
#     return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def updateUserRole(request, pk):
#     """ Update the user role """
#     user = get_object_or_404(User, pk=pk)
#     user.Role = request.data.get('Role')
#     user.save()
#     return Response({"message": "User role updated"}, status=status.HTTP_200_OK)


# # ---------------- Session Management ---------------- #
# @api_view(['POST'])
# def createSession(request):
#     """ Create a session between doctor and patient """
#     data = request.data
#     doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
#     patient = get_object_or_404(Patient, pk=data['Patient_ID'])
#     session = Session.objects.create(Doctor_ID=doctor, Patient_ID=patient, Diagnosis=data['Diagnosis'])
#     serializer = SessionSerializer(session)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def getSessionById(request, pk):
#     """ Retrieve session by ID """
#     session = get_object_or_404(Session, pk=pk)
#     serializer = SessionSerializer(session)
#     return Response(serializer.data)


# # ---------------- Doctor's Availability and Plans ---------------- #
# @api_view(['POST'])
# def createDoctorPlan(request):
#     """ Create or update the doctor's weekly plan """
#     data = request.data
#     doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])

#     # Delete the existing plan for this doctor (optional, based on how you want to handle it)
#     Schedule.objects.filter(Doctor_ID=doctor).delete()

#     # Create new schedules for each day
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     for day in days:
#         if data.get(day):
#             Schedule.objects.create(
#                 Doctor_ID=doctor,
#                 Hospital_ID=get_object_or_404(Hospital, pk=data['Hospital_ID']),
#                 Start_time=data['Start_time'],
#                 End_time=data['End_time'],
#                 Frequency=data['Frequency'],
#                 **{day: True}  # Enable the respective day
#             )
#     return Response({"message": "Doctor plan created/updated"}, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def handleDoctorPlanConflict(request):
#     """ Handle conflicts when the doctor changes his plan """
#     data = request.data
#     doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
#     # Check for schedule clashes
#     conflicting_appointments = Appointment.objects.filter(Doctor_ID=doctor, Date=data['Date'])
    
#     if conflicting_appointments.exists():
#         if data['action'] == 'remove_existing':
#             conflicting_appointments.delete()
#         elif data['action'] == 'postpone_existing':
#             for appointment in conflicting_appointments:
#                 appointment.Start_time = data['new_start_time']
#                 appointment.save()
#         # Notify patients about the changes (not shown: sending email logic)
#         return Response({"message": "Conflicts resolved"}, status=status.HTTP_200_OK)
    
#     return Response({"message": "No conflicts found"}, status=status.HTTP_200_OK)


# # ---------------- Appointment Management ---------------- #
# @api_view(['POST'])
# def createAppointment(request):
#     """ Create an appointment for a patient with a doctor """
#     data = request.data
#     doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
#     patient = get_object_or_404(Patient, pk=data['Patient_ID'])
    
#     # Display available tokens (based on doctor's current queue or doc records)
#     available_tokens = DocRecord.objects.filter(Doctor_ID=doctor).first()
#     if available_tokens.Current_token_no < available_tokens.Max_count:
#         token_no = available_tokens.Current_token_no + 1
#         available_tokens.Current_token_no = token_no
#         available_tokens.save()
        
#         # Create the appointment
#         appointment = Appointment.objects.create(
#             Doctor_ID=doctor,
#             Patient_ID=patient,
#             Start_time=data['Start_time'],
#             End_time=data['End_time'],
#             Token_no=token_no,
#             Status='Scheduled',
#             Date=data['Date']
#         )
#         serializer = AppointmentSerializer(appointment)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     return Response({"message": "No available tokens"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def updateAppointmentTime(request, pk):
#     """ Update the appointment time based on doctor's arrived time """
#     appointment = get_object_or_404(Appointment, pk=pk)
#     appointment.Start_time = request.data.get('Start_time')
#     appointment.End_time = request.data.get('End_time')
#     appointment.save()
#     return Response({"message": "Appointment time updated"}, status=status.HTTP_200_OK)


# # ---------------- Prescription and Pharmacy Instructions ---------------- #
# @api_view(['POST'])
# def createPrescription(request):
#     """ Create a prescription for a session """
#     data = request.data
#     session = get_object_or_404(Session, pk=data['Session_ID'])
#     prescription = Prescription.objects.create(Session_ID=session, Notes=data['Notes'])
    
#     # Add medicines
#     for med in data['Medicines']:
#         Medicine.objects.create(
#             Prescription_ID=prescription,
#             Medicine=med['name'],
#             Quantity=med['quantity'],
#             Strength=med['strength'],
#             Notes=med['notes']
#         )
#     serializer = PrescriptionSerializer(prescription)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def setPharmacyInstructions(request, pk):
#     """ Set instructions on how a patient should take prescribed medicines """
#     medicine = get_object_or_404(Medicine, pk=pk)
#     data = request.data
#     pharmacy = Pharmacy.objects.create(
#         Medicine_ID=medicine,
#         Interval=data['interval'],
#         Times_per_day=data['times_per_day'],
#         Monday=data['Monday'],
#         Tuesday=data['Tuesday'],
#         Wednesday=data['Wednesday'],
#         Thursday=data['Thursday'],
#         Friday=data['Friday'],
#         Saturday=data['Saturday'],
#         Sunday=data['Sunday'],
#         Before_meal=data['before_meal'],
#         Quantity=data['quantity'],
#         Turn_off_after=data['turn_off_after'],
#         Notes=data['notes']
#     )
#     return Response({"message": "Pharmacy instructions saved"}, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def getPharmacyInstructions(request, pk):
#     """ Retrieve pharmacy instructions for a medicine """
#     pharmacy = get_object_or_404(Pharmacy, pk=pk)
#     serializer = PharmacySerializer(pharmacy)
#     return Response(serializer.data)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import User, Patient, Doctor, Hospital, Schedule, Appointment, Prescription, Medicine, NoteUser, Note
from .serializers import PatientDTOSerializer, UserSerializer, PatientSerializer, DoctorSerializer, HospitalSerializer, ScheduleSerializer, AppointmentSerializer, PrescriptionSerializer, MedicineSerializer, NoteUserSerializer, NoteSerializer
import jwt
import datetime
import random
import string
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view

def generate_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    device_id = request.data.get('device_id')

    user = authenticate(email=email, password=password)
    if user is not None:
        # Check if user is logged in on another device
        if user.device_id and user.device_id != device_id:
            # Log out user from other device (you might want to send a push notification here)
            user.device_id = None
            user.save()

        # Update device ID
        user.device_id = device_id
        user.save()

        # Generate JWT token
        token = jwt.encode({
            'user_id': user.User_ID,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'token': token,
            'user_id': user.User_ID,
            'role': user.Role
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Send verification email
        token = generate_token()
        user.email_token = token
        user.save()
        
        send_mail(
            'Verify your email',
            f'Your verification code is: {token}',
            settings.EMAIL_HOST_USER,
            [user.Email],
            fail_silently=False,
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email(request):
    email = request.data.get('email')
    token = request.data.get('token')
    
    user = get_object_or_404(User, Email=email)
    if user.email_token == token:
        user.is_verified = True
        user.email_token = None
        user.save()
        return Response({'message': 'Email verified successfully'})
    return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_role(request):
    user = request.user
    role = request.data.get('role')
    
    if role not in ['patient', 'doctor']:
        return Response({'error': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)
    
    user.Role = role
    user.save()
    
    if role == 'patient':
        Patient.objects.create(User_ID=user)
    elif role == 'doctor':
        Doctor.objects.create(User_ID=user)
    
    return Response({'message': f'User role updated to {role}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_patient(request):
    patient = get_object_or_404(Patient, User_ID=request.user)
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_doctor(request):
    doctor = get_object_or_404(Doctor, User_ID=request.user)
    serializer = DoctorSerializer(doctor, data=request.data, partial=True)
    if serializer.is_valid():
        doctor = serializer.save()
        
        # Create doctor's schedule
        schedule_data = request.data.get('schedule', [])
        for schedule in schedule_data:
            Schedule.objects.create(Doctor_ID=doctor, **schedule)
        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_doctors(request):
    specialization = request.query_params.get('specialization')
    date = request.query_params.get('date')
    
    doctors = Doctor.objects.filter(Specialization=specialization)
    available_doctors = []
    
    for doctor in doctors:
        schedules = Schedule.objects.filter(Doctor_ID=doctor, Date=date)
        if schedules.exists():
            available_doctors.append(doctor)
    
    serializer = DoctorSerializer(available_doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_available_tokens(request, doctor_id, date):
    doctor = get_object_or_404(Doctor, Doctor_ID=doctor_id)
    schedule = get_object_or_404(Schedule, Doctor_ID=doctor, Date=date)
    
    appointments = Appointment.objects.filter(Doctor_ID=doctor, Date=date).order_by('Start_time')
    available_tokens = []
    current_time = schedule.Start_time
    
    while current_time < schedule.End_time:
        if not appointments.filter(Start_time=current_time).exists():
            available_tokens.append(current_time)
        current_time += datetime.timedelta(minutes=doctor.Average_time)
    
    return Response({'available_tokens': available_tokens})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    patient = get_object_or_404(Patient, User_ID=request.user)
    doctor_id = request.data.get('doctor_id')
    date = request.data.get('date')
    start_time = request.data.get('start_time')
    
    doctor = get_object_or_404(Doctor, Doctor_ID=doctor_id)
    
    # Check if the appointment slot is available
    if Appointment.objects.filter(Doctor_ID=doctor, Date=date, Start_time=start_time).exists():
        return Response({'error': 'This appointment slot is not available'}, status=status.HTTP_400_BAD_REQUEST)
    
    end_time = (datetime.datetime.combine(datetime.date.today(), start_time) + 
                datetime.timedelta(minutes=doctor.Average_time)).time()
    
    appointment = Appointment.objects.create(
        Patient_ID=patient,
        Doctor_ID=doctor,
        Date=date,
        Start_time=start_time,
        End_time=end_time,
        Status='Scheduled'
    )
    
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_doctor_schedule(request):
    doctor = get_object_or_404(Doctor, User_ID=request.user)
    new_schedule = request.data.get('schedule', [])
    
    for schedule_item in new_schedule:
        date = schedule_item['Date']
        start_time = schedule_item['Start_time']
        end_time = schedule_item['End_time']
        
        existing_appointments = Appointment.objects.filter(
            Doctor_ID=doctor,
            Date=date,
            Start_time__gte=start_time,
            End_time__lte=end_time
        )
        
        if existing_appointments.exists():
            # Handle conflicts
            for appointment in existing_appointments:
                action = request.data.get('conflict_action', 'postpone')
                if action == 'remove':
                    appointment.delete()
                    # Notify patient about cancellation
                elif action == 'postpone':
                    # Find next available slot
                    new_start_time = end_time
                    new_end_time = (datetime.datetime.combine(datetime.date.today(), new_start_time) + 
                                    datetime.timedelta(minutes=doctor.Average_time)).time()
                    appointment.Start_time = new_start_time
                    appointment.End_time = new_end_time
                    appointment.save()
                    # Notify patient about rescheduling
        
        # Update or create schedule
        Schedule.objects.update_or_create(
            Doctor_ID=doctor,
            Date=date,
            defaults={'Start_time': start_time, 'End_time': end_time}
        )
    
    return Response({'message': 'Schedule updated successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_appointment_times(request):
    doctor = get_object_or_404(Doctor, User_ID=request.user)
    arrived_time = request.data.get('arrived_time')
    date = request.data.get('date')
    
    appointments = Appointment.objects.filter(Doctor_ID=doctor, Date=date).order_by('Start_time')
    
    current_time = arrived_time
    for appointment in appointments:
        appointment.Start_time = current_time
        current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + 
                        datetime.timedelta(minutes=doctor.Average_time)).time()
        appointment.End_time = current_time
        appointment.save()
        # Notify patient about updated time
    
    return Response({'message': 'Appointment times updated successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_prescription(request):
    doctor = get_object_or_404(Doctor, User_ID=request.user)
    appointment_id = request.data.get('appointment_id')
    medicines = request.data.get('medicines', [])
    
    appointment = get_object_or_404(Appointment, Appointment_ID=appointment_id, Doctor_ID=doctor)
    
    prescription = Prescription.objects.create(
        Doctor_ID=doctor,
        Patient_ID=appointment.Patient_ID,
        Date=timezone.now().date()
    )
    
    for medicine_data in medicines:
        Medicine.objects.create(Prescription_ID=prescription, **medicine_data)
    
    serializer = PrescriptionSerializer(prescription)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_medicine_instructions(request):
    medicine_id = request.data.get('medicine_id')
    instructions = request.data.get('instructions')
    
    medicine = get_object_or_404(Medicine, Medicine_ID=medicine_id)
    medicine.Instructions = instructions
    medicine.save()
    
    serializer = MedicineSerializer(medicine)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_prescriptions(request):
    patient = get_object_or_404(Patient, User_ID=request.user)
    prescriptions = Prescription.objects.filter(Patient_ID=patient)
    serializer = PrescriptionSerializer(prescriptions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):
    user = request.user
    note_text = request.data.get('note')
    
    note = Note.objects.create(Note=note_text)
    NoteUser.objects.create(Notification_ID=note, User_ID=user)
    
    serializer = NoteSerializer(note)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_notes(request):
    user = request.user
    note_users = NoteUser.objects.filter(User_ID=user)
    notes = [note_user.Notification_ID for note_user in note_users]
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    
    if user is not None:
        # Return success response
        return JsonResponse({'message': 'Login successful'}, status=200)
    else:
        # Invalid credentials
        return JsonResponse({'message': 'Invalid credentials'}, status=401)

@api_view(['POST'])
def google_login_view(request):
    token = request.data.get('token')
    # Verify the 
    #  token
    response = request.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={token}')
    
    if response.status_code == 200:
        # Token is valid
        return JsonResponse({'message': 'Google login successful'}, status=200)
    else:
        return JsonResponse({'message': 'Google login failed'}, status=400)

@api_view(['POST'])
def facebook_login_view(request):
    token = request.data.get('token')
    # Verify the Facebook token
    response = request.get(f'https://graph.facebook.com/me?access_token={token}')
    
    if response.status_code == 200:
        return JsonResponse({'message': 'Facebook login successful'}, status=200)
    else:
        return JsonResponse({'message': 'Facebook login failed'}, status=400)