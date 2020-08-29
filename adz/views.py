from django.shortcuts import render
from django.contrib import messages
from listings.models import Listing
from.forms import AdzForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def advertise(request):
    if request.method == 'GET':
        return render(request,'adz/advertise.html',{'form':AdzForm()})
    else:
        form = AdzForm(request.POST,request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            messages.success(request, 'Your Listing is created')
        return render(request,'adz/advertise.html',{'form':AdzForm()})
