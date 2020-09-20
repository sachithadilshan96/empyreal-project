from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.urls import reverse_lazy,reverse
from .models import Listing
from django.http import HttpResponseRedirect
#ML Imports
import joblib
import numpy as np
import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import json

from django.views.generic import TemplateView




#like button
def like(request,pk):
    listing = get_object_or_404(Listing, id=pk )
    listing.likes.add(request.user)
    return HttpResponseRedirect(reverse('listing', args=[str(pk)]))

#listings home
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

#single listing view
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





  context = {
    'listing': listing,
    'total_likes' : total_likes,
    'predict_value':predict_value,
    'listed_price':listed_price,

  }

  return render(request, 'listings/listing.html', context)


#property heat map
def map(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    location_lat= float(listing.location_lat)
    location_lon= float(listing.location_lon)
    location= listing.location
    address=listing.address


    data= pd.read_csv('kc_house_data.csv')
    data["weight"] = .8
    lat_lon = data[["lat","long"]].values[:15000]
    map = folium.Map(location=[47.4081, -121.9949],zoom_start=8.5,)
    HeatMap(lat_lon,radius=10).add_to(map)
    test = folium.Html('<h1>Property Location</h1>'+location+address, script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.Marker(location=[location_lat,location_lon], popup=popup, icon=folium.Icon(color="red",icon="home", prefix='fa')).add_to(map)

    marker_cluster = MarkerCluster().add_to(map)

    for point in range(0, len(lat_lon)):
        folium.Marker(lat_lon[point],popup=data['price'][point]).add_to(marker_cluster)

    map=map._repr_html_()
    context = {

      'my_map': map,
      'location': location
    }

    return render(request, 'listings/maps.html', context)


#avg price map
def avmap(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    location_lat= float(listing.location_lat)
    location_lon= float(listing.location_lon)
    location= listing.location
    address = listing.address

    data= pd.read_csv('kc_house_data.csv')
    data_map = data.groupby('zipcode')[['price']].mean().reset_index()
    data_map['zipcode'] = data_map['zipcode'].astype(str)
    k_c='new.json'

    map=folium.Map(
    location=[47.5577, -122.1277],
    zoom_start=10.5,
    detect_retina=True,
    control_scale=False,
    )
    choropleth=folium.Choropleth(
    geo_data=k_c,
    name='choropleth',
    data=data_map,
    columns=['zipcode','price'],
    key_on='feature.properties.ZIPCODE',
    fill_color='Blues',
    line_color='red',
    fill_opacity=0.9,
    line_opacity=0.5,
    highlight=True,
    legend_name='Average Price ($)').add_to(map)
    folium.LayerControl().add_to(map)
    choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['ZIPCODE'],labels=False)).add_to(map)

    city = folium.Html('<b>Seattle</b>',script=True)
    pin = folium.Html('<h1>Property Location -</h1>'+location+address, script=True)
    popup_1 = folium.Popup(pin, max_width=2650)
    popup_2 = folium.Popup(city, max_width=2650)
    folium.Marker(location=[location_lat,location_lon], popup=popup_1,icon=folium.Icon(color="red",icon="home", prefix='fa')).add_to(map)
    folium.CircleMarker(
    location=[47.6062, -122.3321],
    radius=10,
    popup=popup_2,
    color='#FF0000',
    fill=True,
    fill_color='#FF0000').add_to(map)
    map=map._repr_html_()
    context = {

      'my_map': map,
      'location': location
    }

    return render(request, 'listings/maps.html', context)

#search bar
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
