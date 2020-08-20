from django.shortcuts import render

from listings.models import Listing
from.forms import AdzForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/register')
def advertise(request):
    if request.method == 'GET':
        return render(request,'adz/advertise.html',{'form':AdzForm()})
    else:
        form = AdzForm(request.POST,request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.save()
        return render(request,'adz/advertise.html',{'form':AdzForm()})
