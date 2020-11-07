from django.shortcuts import render
from rest_framework import viewsets
from main.models import Bid, Client, Responsible
from main.serializers import BidSerializer, BidSerializerCreate, ClientSerializer, ResponsibleSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


CACHE_TTL = 60 * 5

@method_decorator(cache_page(CACHE_TTL), name='list')
@method_decorator(cache_page(CACHE_TTL), name='retrieve')
class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    http_method_names = ['get', 'delete']

# Create your views here.

class BidViewSetCreateUpdate(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializerCreate
    http_method_names = ['post', 'patch']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get','post', 'patch', 'delete']

class ResponsiblerViewSet(viewsets.ModelViewSet):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
    http_method_names = ['get','post', 'patch', 'delete']

