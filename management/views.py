# employees/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee,AdminUser
from .forms import EmployeeForm, AdminSignupForm,Editprofileform
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def indexpage(request):
    return render(request, "index.html")
def sign_up(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('employee')
    else:
        form = AdminSignupForm()
    return render(request, 'signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('indexpage')
        else:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def admin_logout(request):
    print("kkk")
    logout(request)
  
    return redirect(admin_login)

@login_required(login_url='adlogin')
def employee_list(request):

    template_name = 'employee_list.html'
    employees = Employee.objects.all()
    context = { 'employees': employees}
    return render(request, template_name, context)


@login_required(login_url='adlogin')
def employee_add(request):
    form = EmployeeForm
    template_name = 'add_employee.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.status = 'Active'
            data.save()
            messages.success(request, 'Employee Successfully Added.', 'alert-success')
            return redirect('employee')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


@login_required(login_url='adlogin')
def employee_edit(request, pk):
    template_name = 'employee_edit.html'
    emp_obj = Employee.objects.get(emp_no=pk)
    form = EmployeeForm(instance=emp_obj)
    context = {'form': form, 'emp_obj': emp_obj}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=emp_obj)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Employee Successfully Updated.', 'alert-success')
            return redirect('employee')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)



@login_required(login_url='adlogin')
def employee_delete(request, pk):
    employee = Employee.objects.get(emp_no=pk)
    
    employee.delete()
    return redirect('employee')

@login_required(login_url='adlogin')
def admin_list(request):

    template_name = 'admin_list.html'
    admin = AdminUser.objects.all()
    context = { 'admin': admin}
    return render(request, template_name, context)
@login_required(login_url='adlogin')
def admin_add(request):
    form = AdminSignupForm
    template_name = 'add_admin.html'
    context = {'form': form}
    if request.method == 'POST':
        form = AdminSignupForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.status = 'Active'
            data.role='Admin'
            data.save()
            messages.success(request, 'Employee Successfully Added.', 'alert-success')
            return redirect('admin_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
@login_required(login_url='adlogin')
def admin_edit(request, id):
    template_name = 'admin_edit.html'
    adm_obj = AdminUser.objects.get(id=id)
    form = AdminSignupForm(instance=adm_obj)
    context = {'form': form, 'emp_obj': adm_obj}
    if request.method == 'POST':
        form = AdminSignupForm(request.POST, request.FILES, instance=adm_obj)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Admin Successfully Updated.', 'alert-success')
            return redirect('admin_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)  


@login_required(login_url='adlogin')    
def admin_delete(request, pk):
    admin = AdminUser.objects.get(id=pk)
    
    admin.delete()
    return redirect('admin_list')

@login_required
def edit_profile(request):
   
    user = request.user
    logged_user = AdminUser.objects.get(username=user.username)
    print(logged_user)
    if request.method == 'POST':
        form = Editprofileform(request.POST,  instance=logged_user)
        context = {'form': form, 'user': user}
        if form.is_valid():
            try:
              
                form.save()
                messages.success(request, 'profile edited successfully', 'alert-danger')
                return redirect('indexpage')
            except:
                messages.success(request, 'Something went wrong,Try again', 'alert-danger')
                return render(request, 'edit_profile.html', context)

        else:
            messages.success(request, 'Invalid Data', 'alert-danger')
    else:
        form = Editprofileform(instance=request.user)
        context = {'form': form, 'user': user}
    return render(request, 'edit_profile.html', context)
