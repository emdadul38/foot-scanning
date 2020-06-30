from rest_framework import status
from django.core.serializers import serialize 
from django.http import Http404
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
    
    def get_patient_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404
    
    def get_user_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request):
        user_id = request.user.id
        queryset = Patient.objects.filter(practitioner=user_id,)
        serializer = PatientSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        p_serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and p_serializer.is_valid(raise_exception=True):
            data = request.data
            shipping_address_id = None
            billing_address_id = None
            organization_id = None
            
                
            if 'shipping_address' in data:
                shipping_address = Address.objects.create(street_1= data['shipping_address']['street_1'], street_2= data['shipping_address']['street_2'], city= data['shipping_address']['city'], zipcode= data['shipping_address']['zipcode'], country= data['shipping_address']['country'])
                shipping_address.save()
                shipping_address_serializer = AddressSerializer(shipping_address)
                shipping_address_id = shipping_address.id
            
            if 'billing_address' in data:
                billing_address = Address.objects.create(street_1= data['shipping_address']['street_1'], street_2= data['shipping_address']['street_2'], city= data['shipping_address']['city'], zipcode= data['shipping_address']['zipcode'], country= data['shipping_address']['country'])
                billing_address.save()
                billing_address_serializer = AddressSerializer(billing_address)
                billing_address_id = billing_address.id
            
            if 'organization' in data:
                organization_id = data['organization']
                
            new_patient_user = User.objects.create(email= data['email'], username= data['username'], first_name= data['first_name'], middle_name= data['middle_name'], last_name= data['last_name'], gender= data['gender'], birth_date= data['birth_date'], phone= data['phone'], shipping_address= Address.objects.get(id=shipping_address_id), billing_address = Address.objects.get(id=billing_address_id), organization = Organization.objects.get(id=organization_id))
        
            users_serializer = UserSerializer(new_patient_user)               
            user_id = users_serializer.data['id']
            
            
            new_patient = Patient.objects.create(user= User.objects.get(id=user_id), practitioner= Professional.objects.get(id= data['practitioner']), height= data['height'], weight= data['weight'])
            
            patient_serialzer = PatientSerializer(new_patient)
            print(patient_serialzer.data)
            
            return Response(patient_serialzer.data)
        # return Response(data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        patient_snippet = self.get_patient_object(pk)
        patient_serializer = PatientSerializer(patient_snippet, data=request.data)
        if patient_serializer.is_valid():
            patient_serializer.save()
        else: 
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # User Update Sections 
        data = request.data 
        if 'user_id' in data:
            user_snippet = self.get_user_object(data['user_id'])
            print(user_snippet)
            
            user_serializer = UserSerializer(user_snippet, data=request.data)
            
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(patient_serializer.data)        
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            error = {
                "user_id": [
                    "This field is required."
                ]
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)