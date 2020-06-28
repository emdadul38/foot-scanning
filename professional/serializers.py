from rest_framework import serializers
from .models import Organization, Professional, Patient, User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name')
        
class ProfessionalSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    username = serializers.ReadOnlyField(source='user.username')
    shipping_address = serializers.ReadOnlyField(source='user.shipping_address.street_1')
    # print(professional_users)
    class Meta:
        model = Professional
        # read_only_fields = ('id', 'email', 'username')
        fields =  "__all__" # ('id', 'user_name', 'facility', 'unit_weight', 'unit_size', 'user_type',)
        
class PatientSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    username = serializers.ReadOnlyField(source='user.username')
    shipping_address = serializers.ReadOnlyField(source='user.shipping_address.street_1')
    
    user_type = serializers.ReadOnlyField(source='practitioner.user_type')
    
    class Meta:
        model = Patient
        fields = "__all__"