from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Course list page
    path('', views.CourseListView.as_view(), name='index'),

    # User authentication
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('registration/', views.registration_request, name='registration'),

    # Course detail page
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enroll in course
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Submit exam
    path('course/<int:course_id>/submit/', views.submit, name='submit'),

    # Show exam result
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]
