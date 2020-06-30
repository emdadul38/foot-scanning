from rest_framework import serializers
from .models import Organization, Professional, Patient, User, Address

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
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street_1', 'street_2', 'city', 'zipcode', 'country',)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:        
        model=User
        fields = ('id','email', 'username', 'first_name', 'middle_name', 'last_name', 'gender', 'birth_date', 'phone',  'organization',)
        # read_only_fields = ('created','updated')
        depth = 1
    
    def to_representation(self, instance):
        self.fields['shipping_address'] = AddressSerializer(read_only=True)
        self.fields['billing_address'] = AddressSerializer(read_only=True)
        self.fields['organization'] = OrganizationSerializer(read_only=True)
        return super(UserSerializer, self).to_representation(instance)
        
class PatientSerializer(serializers.ModelSerializer):
    # email = serializers.ReadOnlyField(source='user.email')
    # username = serializers.ReadOnlyField(source='user.username')
    # shipping_address = serializers.ReadOnlyField(source='user.shipping_address.street_1')
    
    # user_type = serializers.ReadOnlyField(source='practitioner.user_type')
    
    class Meta:
        model = Patient
        fields = "__all__"
        depth = 1
        
    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        self.fields['practitioner'] = ProfessionalSerializer(read_only=True)
        return super(PatientSerializer, self).to_representation(instance)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of user
        :return: returns a successfully created student record
        """
        user_serializer = UserSerializer(validated_data.get('data'))
        user_serializer.save()
        # user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        # patient, created = Patient.objects.update_or_create(user=user, height=validated_data.pop('height'), weight=validated_data.pop('weight'), practitioner=validated_data.pop('practitioner'))
        return 'OK'