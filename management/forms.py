# employees/forms.py
from django import forms
from .models import Employee,AdminUser

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'emp_no': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'emp_start_date': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'emp_end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'required': 'true'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
          
        }

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
        }

class Editprofileform(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

