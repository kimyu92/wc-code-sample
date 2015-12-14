from tastypie.resources import ModelResource
from app.models import *


class MyModelResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        allowed_methods = ['get']