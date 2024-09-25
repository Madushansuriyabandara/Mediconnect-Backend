# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.getRoutes),
#     path('users/',views.getUsers),
#     path('users/create/',views.createUser),
#     path('users/<str:pk>/',views.getUserById),
#     path('users/<str:pk>/update/',views.updateUser),
#     path('users/<str:pk>/delete/',views.deleteUser),

#     path('patients/',views.getPatients),
#     path('patients/create/',views.createPatient),
#     path('patients/<str:pk>/',views.getPatientById),
#     path('patients/<str:pk>/update/',views.updatePatient),
#     path('patients/<str:pk>/delete/',views.deletePatient),

from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('verify-email/', views.verify_email, name='verify-email'),
    path('update-role/', views.update_user_role, name='update-role'),
    path('register-patient/', views.register_patient, name='register-patient'),
    path('register-doctor/', views.register_doctor, name='register-doctor'),
    path('search-doctors/', views.search_doctors, name='search-doctors'),
    path('available-tokens/<int:doctor_id>/<str:date>/', views.get_available_tokens, name='available-tokens'),
    path('book-appointment/', views.book_appointment, name='book-appointment'),
    path('update-doctor-schedule/', views.update_doctor_schedule, name='update-doctor-schedule'),
    path('update-appointment-times/', views.update_appointment_times, name='update-appointment-times'),
    path('add-prescription/', views.add_prescription, name='add-prescription'),
    path('add-medicine-instructions/', views.add_medicine_instructions, name='add-medicine-instructions'),
    path('patient-prescriptions/', views.get_patient_prescriptions, name='patient-prescriptions'),
    path('add-note/', views.add_note, name='add-note'),
    path('user-notes/', views.get_user_notes, name='user-notes'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('patients/<str:pk>/',views.getPatientById),
    path('users/login/', views.login_user, name='login_user'),
    # Google login
    path('users/google-login/', views.google_login, name='google_login'),
    # Facebook login
    path('users/facebook-login/', views.facebook_login, name='facebook_login'),
]