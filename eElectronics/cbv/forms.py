import django.forms as form
from .models import Employee

class EmployeeForm(form.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'