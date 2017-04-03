from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Address, Contact


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'city', 'state', 'zip')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    address = serializers.RelatedField(queryset=Address.objects.all())
    group = serializers.RelatedField(queryset=Contact.objects.all())
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'birthdate', 'phone', 'email', 'address', 'group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)