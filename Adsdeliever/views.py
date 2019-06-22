
from rest_framework.viewsets import ModelViewSet
from .models import Ads
from .serializer import AdModelSerializer

class  AdsModelView(ModelViewSet):
	serializer_class = AdModelSerializer
	model = Ads
	permission_class = ()
	queryset = Ads.objects.all()
