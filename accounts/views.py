from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Listing
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import yesno
from.models import UserProfile
from.forms import UserProfileForm
from adz.forms import AdzForm
from django.urls import reverse_lazy,reverse
from datetime import datetime
from services.models import Mortgage,Legal,Builder


def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('userlistings')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='/accounts/register')
def userlistings (request):
    today = datetime.now()
    user_listing = Listing.objects.filter(user=request.user)
    user_mortagage = Mortgage.objects.filter(user=request.user)
    user_legal= Legal.objects.filter(user=request.user)
    user_builder = Builder.objects.filter(user=request.user)

    this_month_listings = Listing.objects.filter(list_date__year=today.year,list_date__month=today.month).count()
    this_month_mortagage = Mortgage.objects.filter(list_date__year=today.year,list_date__month=today.month).count()
    this_month_legal = Legal.objects.filter(list_date__year=today.year,list_date__month=today.month).count()
    this_month_builder = Builder.objects.filter(list_date__year=today.year,list_date__month=today.month).count()

    total_users = User.objects.count()
    total_listings = Listing.objects.count()
    total_mortagage = Mortgage.objects.count()
    total_legal = Legal.objects.count()
    total_builder = Builder.objects.count()


    this_year_jan = Listing.objects.filter(list_date__year=today.year,list_date__month=1).count()
    this_year_feb = Listing.objects.filter(list_date__year=today.year,list_date__month=2).count()
    this_year_mar = Listing.objects.filter(list_date__year=today.year,list_date__month=3).count()
    this_year_apr = Listing.objects.filter(list_date__year=today.year,list_date__month=4).count()
    this_year_may = Listing.objects.filter(list_date__year=today.year,list_date__month=5).count()
    this_year_jun = Listing.objects.filter(list_date__year=today.year,list_date__month=6).count()
    this_year_jul = Listing.objects.filter(list_date__year=today.year,list_date__month=7).count()
    this_year_aug = Listing.objects.filter(list_date__year=today.year,list_date__month=8).count()
    this_year_sep = Listing.objects.filter(list_date__year=today.year,list_date__month=9).count()
    this_year_oct = Listing.objects.filter(list_date__year=today.year,list_date__month=10).count()
    this_year_nov = Listing.objects.filter(list_date__year=today.year,list_date__month=11).count()
    this_year_dec = Listing.objects.filter(list_date__year=today.year,list_date__month=12).count()


    context = {
      'user_listing': user_listing,
      'this_month_listings': this_month_listings,
      'this_month_mortagage': this_month_mortagage,
      'this_month_legal': this_month_legal,
      'this_month_builder': this_month_builder,
      'this_year_jan':this_year_jan,
      'this_year_feb':this_year_feb,
      'this_year_mar':this_year_mar,
      'this_year_apr':this_year_apr,
      'this_year_may':this_year_may,
      'this_year_jun':this_year_jun,
      'this_year_jul':this_year_jul,
      'this_year_aug':this_year_aug,
      'this_year_sep':this_year_sep,
      'this_year_oct':this_year_oct,
      'this_year_nov':this_year_nov,
      'this_year_dec':this_year_dec,
      'today':today,
      'total_listings': total_listings,
      'total_mortagage':total_mortagage,
      'total_legal' :total_legal,
      'total_builder':total_legal,
      'total_users':total_users,
      'user_mortagage':user_mortagage,
      'user_legal':user_legal,
      'user_builder':user_builder,

    }
    return render(request, 'accounts/userlistings.html', context)

@login_required
def deletelistings (request,listing_id):
    delete_listing = get_object_or_404(Listing,pk=listing_id)
    if request.method == 'POST':

        delete_listing.delete()
        return HttpResponseRedirect(reverse('userlistings'))

@login_required
def editlistings (request,listing_id):
    view_listings = get_object_or_404(Listing,pk=listing_id)
    if request.method == 'GET':
        form = AdzForm(instance=view_listings)
        return render(request,'accounts/editlisting.html',{'view_listings':view_listings, 'form':form})

    else:

        form = AdzForm(request.POST,instance=view_listings)
        if form.is_valid():
                newform = form.save(commit=False)
                newform.user = request.user
                newform.save()
                return render(request,'accounts/editlisting.html',{'view_listings':view_listings, 'form':form})





@login_required
def profile (request):
    pro = UserProfile.objects.filter(user=request.user)
    user_listing = Listing.objects.filter(user=request.user)
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
      'user_listing': user_listing,
      'pro':pro,
      'contacts': user_contacts,
    }
    return render(request,'accounts/profile.html', context)

@login_required(login_url='/accounts/login')
def userprofile (request):
    if request.method == 'GET':
            return render(request,'accounts/userprofile.html',{'form':UserProfileForm()})
    else:
        form = UserProfileForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_UserProfileForm = form.save(commit=False)
            new_UserProfileForm.user = request.user
            new_UserProfileForm.save()
        return render(request,'accounts/userprofile.html',{'form':UserProfileForm()})
