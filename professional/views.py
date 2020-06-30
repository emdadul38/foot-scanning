from rest_framework import status
from django.core.serializers import serialize 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Organization, Professional, Patient, User, Address
from .serializers import OrganizationSerializer, ProfessionalSerializer, PatientSerializer, UserSerializer, AddressSerializer

# Create your views here.

class OrganizationView(viewsets.ModelViewSet):
    # serializer_class = OrganizationSerializer
    # queryset = Organization.objects.all()
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()

class ProfessionalView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user_id = request.user.id
        queryset = Professional.objects.filter( user_type="Practitioner") #user=user_id,
        serializer = ProfessionalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PatientView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user_id = request.user.id
        queryset = Patient.objects.filter(user=user_id,)
        serializer = PatientSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        # shipping_address_id = None
        # billing_address_id = None
        
            
        # if 'shipping_address' in data:
        #     shipping_address = Address.objects.create(street_1= data['shipping_address']['street_1'], street_2= data['shipping_address']['street_2'], city= data['shipping_address']['city'], zipcode= data['shipping_address']['zipcode'], country= data['shipping_address']['country'])
        #     shipping_address.save()
        #     shipping_address_serializer = AddressSerializer(shipping_address)
        #     shipping_address_id = shipping_address.id
        
        # if 'billing_address' in data:
        #     billing_address = Address.objects.create(street_1= data['shipping_address']['street_1'], street_2= data['shipping_address']['street_2'], city= data['shipping_address']['city'], zipcode= data['shipping_address']['zipcode'], country= data['shipping_address']['country'])
        #     billing_address.save()
        #     billing_address_serializer = AddressSerializer(billing_address)
        #     billing_address_id = billing_address.id
            
        # new_user = User.objects.create(email= data['email'], username= data['username'], first_name= data['first_name'], middle_name= data['middle_name'], last_name= data['last_name'], gender= data['gender'], birth_date= data['birth_date'], phone= data['phone'], shipping_address= Address.objects.get(id=shipping_address_id), billing_address = Address.objects.get(id=billing_address_id))
    
        # users_serializer = UserSerializer(new_user)               
        # user_id = users_serializer.data['id']
        
        # if 'practitioner' in data:
        #     new_patient = Patient.objects.create(user= User.objects.get(id=user_id), practitioner= Professional.objects.get(id= data['practitioner']), height= data['height'], weight= data['weight'])
        
         
        # return Response(users_serializer.data)
        return Response(data)
 