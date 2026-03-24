from rest_framework import serializers
from accounts.models import SchoolSettings
from accounts.models import AboutUs

        
#about_us
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        