from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import time
from society_project.settings import BASE_DIR
from django.contrib.auth.decorators import login_required
import matplotlib as mpl


mpl.use('Agg')


# utility functions:
def username_present(username):
    if User.objects.filter(username=username).exists():
        return True

    return False


def total_number_employees():
    qs = User.objects.all()
    return (len(qs) - 1)
    # -1 to account for Admin Panel


import time

def days_used(start_time_str):
    start_time = time.mktime(time.strptime(start_time_str, "%Y-%m-%d"))  # Convert start time string to timestamp
    current_time = time.time()
    num_seconds = current_time - start_time
    num_days = num_seconds / (60 * 60 * 24)  # Convert seconds to days
    return int(num_days)


# Creating api here
# To display for Users
def home(request):

    return render(request, 'recognition/home.html')


# For login page
@login_required
def dashboard(request):
    if(request.user.username == 'admin'):
        print("admin")
        total_num_of_emp = total_number_employees()
        #emp_present_today = employees_present_today()
        #emp_absent_today =  total_num_of_emp - emp_present_today
        #present_percent = (  emp_present_today / total_num_of_emp) * 100
        #absent_percent = (emp_absent_today / total_num_of_emp) * 100
        
        start_time = '2024-04-01'
        num_days_used = days_used(start_time)

        return render(request, 'recognition/admin_dashboard.html',{
            'total_num_of_emp': total_num_of_emp, 
            #'emp_present_today': emp_present_today, 'emp_absent_today':emp_absent_today,
            #'emp_present_percent':present_percent,'emp_absent_percent':absent_percent,
            'days_used':num_days_used
            })
    else:
        print("not admin")

        return render(request, 'recognition/employee_dashboard.html')



@login_required
def not_authorised(request):
    return render(request, 'recognition/not_authorised.html')
