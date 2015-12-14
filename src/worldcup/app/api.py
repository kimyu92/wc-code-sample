from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from app.models import *
from app.prettyPrint import *
from tastypie.constants import * 
from django.conf.urls import *

class CountryResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'countries'
        authorization = Authorization()
        serializer = PrettyJSONSerializer()
        filtering = {
            "country_name" : ALL,
            "country_code" : ALL
        }
        detail_uri_name = 'country_name'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<country_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

    def determine_format(self, request):
        return "application/json"

# class CountryResoucre(ModelResource):
#     class Meta:
#         queryset = Country.objects.all().filter(country_code = var)
#         resource_name = 'countries'
#         authorization = Authorization()
#         serializer = PrettyJSONSerializer()

#     def determine_format(self, request):
#         return "application/json"
 

class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        resource_name = 'players'
        authorization = Authorization()
        serializer = PrettyJSONSerializer()

        filtering = {
            "full_name" : ALL,
            "position" : ALL
        }
        detail_uri_name = 'full_name'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<full_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]


    def determine_format(self, request):
        return "application/json"


class MatchResource(ModelResource):
    class Meta:
        queryset = Match.objects.all()
        resource_name = 'matches'
        authorization = Authorization()
        serializer = PrettyJSONSerializer()

        filtering = {
            "winner" : ALL,
            "match_num" : ALL,
            "country_A" : ALL,
            "country_B" : ALL
        }
        detail_uri_name = 'match_num'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<match_num>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]


    def determine_format(self, request):
        return "application/json"