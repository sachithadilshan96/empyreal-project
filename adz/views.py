from django.shortcuts import render
from django.contrib import messages
from listings.models import Listing
from.forms import AdzForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse

#create advertisement
@login_required(login_url='/accounts/login')
def advertise(request):
    if request.method == 'GET':
        return render(request,'adz/advertise.html',{'form':AdzForm()})
    else:
        #getting inputs from user
        form = AdzForm(request.POST,request.FILES or None)
        #validate user inputs and save to database
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            messages.success(request, 'Your Listing is created')
            return HttpResponseRedirect(reverse('advertise'))
        return render(request,'adz/advertise.html',{'form':AdzForm()})
