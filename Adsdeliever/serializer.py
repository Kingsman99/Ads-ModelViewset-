from rest_framework import serializers
from .models import Ads


class AdModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Ads 
		fiels='__all__'