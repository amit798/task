from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from .models import Employee
from .forms import EmplyoeeForm ,EmployeeSearchForm
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.
def employee_save(request):
    if request.method == 'POST':
        form=EmplyoeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Employee successfully added...')
            return redirect('employee')
    else:
        form=EmplyoeeForm()
    users=Employee.objects.all()
    return render(request,'employee.html',{'form':form,'users':users})

def delete_employee(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request,'Employee record successfully deleted...')
        return redirect('employee')
    return render(request,'employee_confirm_delete.html',{'object':employee})


def update_employee(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    form=EmplyoeeForm(request.POST or None ,instance=employee)
    if form.is_valid():
        form.save()
        messages.success(request,'Employee record successfully updated...')
        return redirect('employee')
    return render(request,'employee.html',{'form':form,'msg':'Successfully updated....'})

class EmployeeSearchView(ListView):
    model = Employee
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Employee.objects.filter(Q(name__icontains=query))
        return object_list

