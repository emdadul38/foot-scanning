from rest_framework import status
from django.core.serializers import serialize 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Organization, Professional, Patient
from .serializers import OrganizationSerializer, ProfessionalSerializer, PatientSerializer

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
