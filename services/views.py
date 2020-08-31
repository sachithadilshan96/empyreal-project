from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from.forms import MortgageForm,LegalForm
from.models import Mortgage,Legal
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contacts.forms import CommentForm
from contacts.models import Comment
from django.urls import reverse_lazy,reverse


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

@login_required(login_url='/accounts/register')
def legal (request):
    if request.method == 'GET':
            return render(request,'services/legal.html',{'form':LegalForm()})
    else:
        form = LegalForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.user = request.user
            new_loan.save()
        return render(request,'services/legal.html',{'form':LegalForm()})

def services(request):
    return render(request, 'services/services.html')

def index(request):
  mortgages = Mortgage.objects.order_by('-list_date')

  paginator = Paginator(mortgages, 3)
  page = request.GET.get('page')
  paged_mortgages = paginator.get_page(page)

  context = {
    'mortgages': paged_mortgages
  }

  return render(request, 'services/mortgagelist.html', context)

def index_2(request):
  legals= Legal.objects.order_by('-list_date')

  paginator = Paginator(legals, 3)
  page = request.GET.get('page')
  paged_legals = paginator.get_page(page)

  context = {
    'legals': paged_legals
  }

  return render(request, 'services/legallist.html', context)



def mortgages(request, mortgage_id):
    if request.method == 'GET':
        mortgagepage = get_object_or_404(Mortgage, pk=mortgage_id)

        comments = Comment.objects.order_by('-created').filter(mortgage_id=mortgage_id,active=True)
        return render(request, 'services/listedmortgage.html',{'form':CommentForm(),'mortgagepage': mortgagepage,'comments':comments})

    if request.method == 'POST':
        mortgagepage = get_object_or_404(Mortgage, pk=mortgage_id)
        comments = Comment.objects.order_by('-created').filter(mortgage_id=mortgage_id,active=True)

        form = CommentForm(request.POST,request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.mortgage_id = mortgage_id
            newform.save()

            return HttpResponseRedirect(reverse('mortgagepage', args=[str(mortgage_id)]))
        return render(request, 'services/listedmortgage.html',{'form':CommentForm(),'mortgagepage': mortgagepage,'comments':comments})





def legals(request, legal_id):
   legalpage = get_object_or_404(Legal, pk=legal_id)

   context = {
     'legalpage': legalpage
   }

   return render(request, 'services/listedlegal.html', context)








@login_required(login_url='/accounts/login')
def comment(request,mortgage_id):
    if request.method == 'GET':
        return render(request,'adz/advertise.html',{'form':CommentForm()})
    else:
        form = CommentForm(request.POST,request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.mortgage_id = mortgage_id
            newform.save()

        return render(request,'adz/advertise.html',{'form':CommentForm()})
