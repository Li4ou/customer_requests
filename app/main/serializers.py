from rest_framework import serializers
from main.models import Bid, Responsible, Client

class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    responsible = ResponsibleSerializer()
    client = ClientSerializer()

    class Meta:
        model = Bid
        fields = ['id','text','date', 'responsible', 'client',]


class BidSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id','text','date', 'responsible', 'client',]



