from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.urls import reverse_lazy,reverse
from .models import Listing
from django.http import HttpResponseRedirect
import joblib
import numpy as np
import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster

from django.views.generic import TemplateView





def like(request,pk):
    listing = get_object_or_404(Listing, id=pk )
    listing.likes.add(request.user)
    return HttpResponseRedirect(reverse('listing', args=[str(pk)]))


def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  likes = get_object_or_404(Listing, pk=listing_id)
  total_likes = likes.total_likes()
  model = joblib.load('empyreal.sav')

  bedrooms = listing.bedrooms
  bathrooms = listing.bathrooms
  sqft_living = listing.sqft_living
  sqft_lot = listing.lot_size
  floors = listing.floors
  waterfront =listing.waterfront
  view = listing.view
  condition =listing.condition
  grade = listing.grade
  sqft_above =listing.sqft_above
  sqft_basement =listing.sqft_basement
  yr_built =listing.yr_built
  yr_renovated =listing.yr_renovated
  zipcode= listing.zipcode
  location_lat= float(listing.location_lat)
  location_lon= float(listing.location_lon)
  sqft_living15=listing.sqft_living15
  sqft_lot15=listing.sqft_lot15

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

  listed_price = format(float(listing.price),'.2f')

  data= pd.read_csv('kc_house_data.csv')
  data["weight"] = .5
  lat_lon = data[["lat","long"]].values[:2500]
  map = folium.Map(location=[47.5480,-121.9836],zoom_start=12)
  HeatMap(lat_lon,radius=10).add_to(map)
  test = folium.Html('<b>Hello world</b>', script=True)
  popup = folium.Popup(test, max_width=2650)
  folium.Marker(location=[47.5480,-121.9836], popup=popup).add_to(map)
  map=map._repr_html_()

#https://opendata.arcgis.com/datasets/e6c555c6ae7542b2bdec92485892b6e6_113.geojson

  context = {
    'listing': listing,
    'total_likes' : total_likes,
    'predict_value':predict_value,
    'listed_price':listed_price,
    'my_map': map
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__gte=bedrooms).order_by('bedrooms')

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price).order_by('-price')

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }


  return render(request, 'listings/search.html', context)
