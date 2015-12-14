from django.apps import AppConfig
from watson import search as watson

class WorldCupWatsonConfig(AppConfig):
	name = "app"

	def ready(self):
		Country = self.get_model("Country")
		Player = self.get_model("Player")
		Match = self.get_model("Match")
		watson.register(Country,fields=("country_name","country_code","article", "continent"))
		watson.register(Player,fields=("sur_name","full_name","clubname","position","biography"))
		watson.register(Match,fields=("winner","score","location"))