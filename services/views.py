from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from.forms import MortgageForm,LegalForm,BuilderForm
from.models import Mortgage,Legal,Builder
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contacts.forms import CommentForm,CommentBuilderForm,CommentLegalForm
from contacts.models import Comment,CommentBuilder,CommentLegal
from django.urls import reverse_lazy,reverse
from osm_field.fields import LatitudeField, LongitudeField, OSMField
from .forms import PredictForm
import joblib
import numpy as np
import pandas as pd

def services(request):
    return render(request, 'services/services.html')

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
            return HttpResponseRedirect(reverse('mortgage'))
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
            return HttpResponseRedirect(reverse('legal'))
        return render(request,'services/legal.html',{'form':LegalForm()})

@login_required(login_url='/accounts/register')
def builder (request):
    if request.method == 'GET':
            return render(request,'services/builder.html',{'form':BuilderForm()})
    else:
        form = BuilderForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_builder = form.save(commit=False)
            new_builder.user = request.user
            new_builder.save()
            return HttpResponseRedirect(reverse('builder'))
        return render(request,'services/builder.html',{'form':BuilderForm()})



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


def index_3(request):
  builders= Builder.objects.order_by('-list_date')

  paginator = Paginator(builders, 3)
  page = request.GET.get('page')
  paged_builder = paginator.get_page(page)

  context = {
    'builders': paged_builder
  }

  return render(request, 'services/builderlist.html', context)



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





def legals(request,legal_id):
    if request.method == 'GET':
       legalpage = get_object_or_404(Legal, pk=legal_id)
       comments = CommentLegal.objects.order_by('-created').filter(legal_id=legal_id,active=True)
       return render(request,'services/listedlegal.html',{'form':CommentLegalForm(),'legalpage': legalpage,'comments':comments})
    if request.method == 'POST':
       legalpage = get_object_or_404(Legal, pk=legal_id)
       comments = CommentLegal.objects.order_by('-created').filter(legal_id=legal_id,active=True)
       form = CommentLegalForm(request.POST,request.FILES or None)
       if form.is_valid():
           newform = form.save(commit=False)
           newform.user = request.user
           newform.legal_id = legal_id
           newform.save()

           return HttpResponseRedirect(reverse('legalpage', args=[str(legal_id)]))
       return render(request, 'services/listedlegal.html', {'form':CommentLegalForm(),'legalpage': legalpage,'comments':comments})




def builders(request, builder_id):
    if request.method == 'GET':
        builderpage = get_object_or_404(Builder, pk=builder_id)

        comments = CommentBuilder.objects.order_by('-created').filter(builder_id=builder_id,active=True)
        return render(request, 'services/listedbuilder.html',{'form':CommentBuilderForm(),'builderpage': builderpage,'comments':comments})

    if request.method == 'POST':
        builderpage = get_object_or_404(Builder, pk=builder_id)

        comments = CommentBuilder.objects.order_by('-created').filter(builder_id=builder_id,active=True)

        form = CommentBuilderForm(request.POST,request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.builder_id = builder_id
            newform.save()

            return HttpResponseRedirect(reverse('builderpage', args=[str(builder_id)]))
        return render(request, 'services/listedbuilder.html',{'form':CommentBuilderForm(),'builderpage': builderpage,'comments':comments})



def predict(request):
    if request.method == 'GET':
     return render(request,"predict.html",{'form' : PredictForm()})
    else:
        form= PredictForm(request.POST or None)
        model = joblib.load('empyreal.sav')
        if form.is_valid():
            title= form.cleaned_data.get("title")
            name= form.cleaned_data.get("name")
            bedrooms= form.cleaned_data.get("bedrooms")
            bathrooms= form.cleaned_data.get("bathrooms")
            sqft_living= form.cleaned_data.get("sqft_living")
            sqft_lot= form.cleaned_data.get("sqft_lot")
            floors= form.cleaned_data.get("floors")
            waterfront= form.cleaned_data.get("waterfront")
            view= form.cleaned_data.get("view")
            condition= form.cleaned_data.get("condition")
            grade= form.cleaned_data.get("grade")
            sqft_above= form.cleaned_data.get("sqft_above")
            sqft_basement= form.cleaned_data.get("sqft_basement")
            yr_built= form.cleaned_data.get("yr_built")
            yr_renovated= form.cleaned_data.get("yr_renovated")
            zipcode= form.cleaned_data.get("zipcode")
            location_lat= form.cleaned_data.get("location_lat")
            location_lon= form.cleaned_data.get("location_lon")
            sqft_living15= form.cleaned_data.get("sqft_living15")
            sqft_lot15= form.cleaned_data.get("sqft_lot15")

            ans =model.predict([[
                                    bedrooms,
                                    bathrooms,
                                    sqft_living,
                                    sqft_lot,
                                    floors,
                                    waterfront,
                                    view,
                                    condition,
                                    grade,
                                    sqft_above,
                                    sqft_basement,
                                    yr_built,
                                    yr_renovated,
                                    zipcode,
                                    location_lat,
                                    location_lon,
                                    sqft_living15,
                                    sqft_lot15,

            ]])
            predict_value = float(np.round(ans[0], 2))
            context = {
            'title':title,
            'name':name,
            'bedrooms':bedrooms,
            'bathrooms':bathrooms,
            'sqft_living':sqft_living,
            'sqft_lot':sqft_lot,
            'floors':floors,
            'waterfront':waterfront,
            'view':view,
            'condition':condition,
            'grade':grade,
            'sqft_above':sqft_above,
            'sqft_basement':sqft_basement,
            'yr_built':yr_built,
            'yr_renovated':yr_renovated,
            'zipcode':zipcode,
            'location_lat':location_lat,
            'location_lon':location_lon,
            'sqft_living15':sqft_living15,
            'sqft_lot15':sqft_lot15,
            'predict_value': predict_value,
            }
            #lgb_predict = modelL.predict([[3,1.00,1180,5650,1.0,0,0,3,7,1180,0,1955,0,98178,47.5112,-122.257,1340,5650]])
            #lgb_p = float(np.round(lgb_predict[0], 2))

            print(ans)
            return render(request,"result.html",context)

def predict_results(request):
    if request.method == 'GET':
     return render(request,"result.html")
