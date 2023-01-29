from dataclasses import field
from rest_framework.serializers import ModelSerializer,RelatedField
from .models import *

class IcraSerializer(ModelSerializer):
    
    class Meta:
        model = Icra
        fields = '__all__'

class DavaSerializer(ModelSerializer):
    
    class Meta:
        model = Dava
        fields = '__all__'

class NoteSerializer(ModelSerializer):
    
    class Meta:
        model = Note
        fields = '__all__'

class AppointmentSerializer(ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'

class OurServiceSerializer(ModelSerializer):
    
    class Meta:
        model = OurService
        fields = '__all__'

class ArticleAndNewSerializer(ModelSerializer):
    
    class Meta:
        model = ArticleAndNew
        fields = '__all__'

class LawyerSerializer(ModelSerializer):
    
    class Meta:
        model = Lawyer
        fields = '__all__'

class ReferenceSerializer(ModelSerializer):
    
    class Meta:
        model = Reference
        fields = '__all__'

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'