# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .dtos import *
# from .models import *
# from .serializers import *

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

# @api_view(['GET'])
# def getPatientById(request, pk):
#     patient = Patient.objects.get(Patient_ID=pk)
#     patientDto = PatientDTO(
#         User_ID = patient.User_ID.User_ID,
#         Patient_ID = patient.Patient_ID,
#         Breakfast_time = patient.Breakfast_time,
#         Lunch_time = patient.Lunch_time,
#         Dinner_time = patient.Dinner_time,
#     )
#     serializer = PatientDTOSerializer(patientDto, many=False)
#     return Response(serializer.data)

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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.db import transaction
from .models import *
from .serializers import *
from django.core.mail import send_mail


# ---------------- User Management and Authentication ---------------- #
@api_view(['POST'])
def registerUser(request):
    """ Register a new user and create either a Doctor or Patient profile """
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Create doctor or patient profile based on the role
        if data['Role'] == 'Doctor':
            Doctor.objects.create(User_ID=user, Specialization=data.get('Specialization'))
        elif data['Role'] == 'Patient':
            Patient.objects.create(User_ID=user, Breakfast_time=data.get('Breakfast_time'),
                                   Lunch_time=data.get('Lunch_time'),
                                   Dinner_time=data.get('Dinner_time'))

        # Send verification email (placeholder for actual functionality)
        send_mail(
            'Welcome to MediConnect',
            'Thank you for registering. Please verify your email.',
            'noreply@mediconnect.com',
            [user.Email],
            fail_silently=False,
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginUser(request):
    """ Login the user and return the token """
    data = request.data
    user = authenticate(request, email=data['email'], password=data['password'])
    if user is not None:
        # Check if the user has logged in from another device and logout from that device
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key, 'role': user.Role}, status=status.HTTP_200_OK)
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logoutUser(request):
    """ Logout and destroy token """
    request.user.auth_token.delete()
    logout(request)
    return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def updateUserRole(request, pk):
    """ Update the user role """
    user = get_object_or_404(User, pk=pk)
    user.Role = request.data.get('Role')
    user.save()
    return Response({"message": "User role updated"}, status=status.HTTP_200_OK)


# ---------------- Session Management ---------------- #
@api_view(['POST'])
def createSession(request):
    """ Create a session between doctor and patient """
    data = request.data
    doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
    patient = get_object_or_404(Patient, pk=data['Patient_ID'])
    session = Session.objects.create(Doctor_ID=doctor, Patient_ID=patient, Diagnosis=data['Diagnosis'])
    serializer = SessionSerializer(session)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getSessionById(request, pk):
    """ Retrieve session by ID """
    session = get_object_or_404(Session, pk=pk)
    serializer = SessionSerializer(session)
    return Response(serializer.data)


# ---------------- Doctor's Availability and Plans ---------------- #
@api_view(['POST'])
def createDoctorPlan(request):
    """ Create or update the doctor's weekly plan """
    data = request.data
    doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])

    # Delete the existing plan for this doctor (optional, based on how you want to handle it)
    Schedule.objects.filter(Doctor_ID=doctor).delete()

    # Create new schedules for each day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        if data.get(day):
            Schedule.objects.create(
                Doctor_ID=doctor,
                Hospital_ID=get_object_or_404(Hospital, pk=data['Hospital_ID']),
                Start_time=data['Start_time'],
                End_time=data['End_time'],
                Frequency=data['Frequency'],
                **{day: True}  # Enable the respective day
            )
    return Response({"message": "Doctor plan created/updated"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def handleDoctorPlanConflict(request):
    """ Handle conflicts when the doctor changes his plan """
    data = request.data
    doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
    # Check for schedule clashes
    conflicting_appointments = Appointment.objects.filter(Doctor_ID=doctor, Date=data['Date'])
    
    if conflicting_appointments.exists():
        if data['action'] == 'remove_existing':
            conflicting_appointments.delete()
        elif data['action'] == 'postpone_existing':
            for appointment in conflicting_appointments:
                appointment.Start_time = data['new_start_time']
                appointment.save()
        # Notify patients about the changes (not shown: sending email logic)
        return Response({"message": "Conflicts resolved"}, status=status.HTTP_200_OK)
    
    return Response({"message": "No conflicts found"}, status=status.HTTP_200_OK)


# ---------------- Appointment Management ---------------- #
@api_view(['POST'])
def createAppointment(request):
    """ Create an appointment for a patient with a doctor """
    data = request.data
    doctor = get_object_or_404(Doctor, pk=data['Doctor_ID'])
    patient = get_object_or_404(Patient, pk=data['Patient_ID'])
    
    # Display available tokens (based on doctor's current queue or doc records)
    available_tokens = DocRecord.objects.filter(Doctor_ID=doctor).first()
    if available_tokens.Current_token_no < available_tokens.Max_count:
        token_no = available_tokens.Current_token_no + 1
        available_tokens.Current_token_no = token_no
        available_tokens.save()
        
        # Create the appointment
        appointment = Appointment.objects.create(
            Doctor_ID=doctor,
            Patient_ID=patient,
            Start_time=data['Start_time'],
            End_time=data['End_time'],
            Token_no=token_no,
            Status='Scheduled',
            Date=data['Date']
        )
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({"message": "No available tokens"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateAppointmentTime(request, pk):
    """ Update the appointment time based on doctor's arrived time """
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.Start_time = request.data.get('Start_time')
    appointment.End_time = request.data.get('End_time')
    appointment.save()
    return Response({"message": "Appointment time updated"}, status=status.HTTP_200_OK)


# ---------------- Prescription and Pharmacy Instructions ---------------- #
@api_view(['POST'])
def createPrescription(request):
    """ Create a prescription for a session """
    data = request.data
    session = get_object_or_404(Session, pk=data['Session_ID'])
    prescription = Prescription.objects.create(Session_ID=session, Notes=data['Notes'])
    
    # Add medicines
    for med in data['Medicines']:
        Medicine.objects.create(
            Prescription_ID=prescription,
            Medicine=med['name'],
            Quantity=med['quantity'],
            Strength=med['strength'],
            Notes=med['notes']
        )
    serializer = PrescriptionSerializer(prescription)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def setPharmacyInstructions(request, pk):
    """ Set instructions on how a patient should take prescribed medicines """
    medicine = get_object_or_404(Medicine, pk=pk)
    data = request.data
    pharmacy = Pharmacy.objects.create(
        Medicine_ID=medicine,
        Interval=data['interval'],
        Times_per_day=data['times_per_day'],
        Monday=data['Monday'],
        Tuesday=data['Tuesday'],
        Wednesday=data['Wednesday'],
        Thursday=data['Thursday'],
        Friday=data['Friday'],
        Saturday=data['Saturday'],
        Sunday=data['Sunday'],
        Before_meal=data['before_meal'],
        Quantity=data['quantity'],
        Turn_off_after=data['turn_off_after'],
        Notes=data['notes']
    )
    return Response({"message": "Pharmacy instructions saved"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getPharmacyInstructions(request, pk):
    """ Retrieve pharmacy instructions for a medicine """
    pharmacy = get_object_or_404(Pharmacy, pk=pk)
    serializer = PharmacySerializer(pharmacy)
    return Response(serializer.data)

