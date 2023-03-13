from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import Food,AddFile,Employee
from .forms import EmployeeForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
class FoodCreateView(CreateView):
    fields  ='__all__'
    model = Food
    template_name = 'cbv/foodcreate.html'
    success_url = '/cbv/list'

class FoodListView(ListView):
    model = Food
    template_name = 'cbv/foodlist.html'
    context_object_name = 'foodlist'

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'cbv/fooddelete.html'
    success_url = '/cbv/list'  


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'cbv/foodupdate.html'
    fields = '__all__'
    success_url = '/cbv/list'      
    
class FoodDetailView(DetailView):
    model = Food
    template_name = 'cbv/fooddetail.html'
    context_object_name = 'fooddetail'
    
class AddFileView(CreateView):
    model = AddFile
    template_name = 'cbv/addfile.html'
    success_url = '/cbv/filelist'
    fields = '__all__'
    
class FileListView(ListView):
    model = AddFile
    template_name = 'cbv/filelist.html'
    context_object_name = 'filelist'
    
class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'cbv/employeemail.html'
    #fields = '__all__'
    
    def from_valid(self,form):
        
        emp_email = form.cleaned_data[EmployeeForm]
        
        subject = 'welcome to django'
        message = 'hello intern'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [emp_email]
        res = send_mail(subject,message,email_form,recipient_list)
        if res>0:
            print('mail sent')
        else:
            print('mail does not sent')
        print(res)
        return super(EmployeeCreateView,self).form_valid(form)
        
    
    
    