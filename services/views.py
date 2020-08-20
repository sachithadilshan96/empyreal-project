from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from.forms import MortgageForm
from.models import Mortgage

@login_required(login_url='/accounts/register')
def mortgage (request):
    if request.method == 'GET':
            return render(request,'services/mortgage.html',{'form':MortgageForm()})
    else:
        form = MortgageForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_mortgage = form.save(commit=False)
            new_mortgage.user = request.user
            new_mortgage.save()
        return render(request,'services/mortgage.html',{'form':MortgageForm()})

def services(request):
    return render(request, 'services/services.html')
