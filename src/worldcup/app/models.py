from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    # -------------
    # Country_model
    # -------------

class Country(models.Model):
    """
    The model contains a country name, the country code, the rank, flag, symbol_flag,
    map_url, team_logo_url, team_video_url, an article, and continent of the country.
    Country stats like matches_played and goals_scored have been added. The stats are
    too numberous to list out here.
    The __str__ method is used to return the name of the country as string.
    """
    class Meta:
        db_table = 'Country'

    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=20)
    rank = models.IntegerField(default=0)
    flag = models.CharField(max_length=500)
    symbol_flag = models.CharField(max_length=500)
    map_url = models.CharField(max_length=500)
    team_logo_url = models.CharField(max_length=600)
    team_video_url = models.CharField(max_length=600)
    article = models.CharField(max_length=6000)
    continent = models.CharField(max_length=500)

    # Country Statistics
    matches_played = models.CharField(max_length=20)
    goals_scored = models.CharField(max_length=20)
    attempts_on_target = models.CharField(max_length=20)
    distance_covered = models.CharField(max_length=20)
    one_g_freq_min = models.CharField(max_length=20)
    one_g_freq_attempts = models.CharField(max_length=20)
    scoring_method_total = models.CharField(max_length=20)
    open_play_goals = models.CharField(max_length=20)
    set_piece_goals = models.CharField(max_length=20)
    att_attempts = models.CharField(max_length=20)
    attempts_off_target = models.CharField(max_length=20)
    att_shots_saved = models.CharField(max_length=20)
    att_goals_scored = models.CharField(max_length=20)
    att_shots_blocked = models.CharField(max_length=20)
    tournament_average = models.CharField(max_length=20)
    att_dribble_penalty_area = models.CharField(max_length=20)
    att_dribble_penalty_area_ta = models.CharField(max_length=20)
    att_deliveries_penalty_area = models.CharField(max_length=20)
    att_deliveries_penalty_area_ta = models.CharField(max_length=20)
    att_crosses = models.CharField(max_length=20)
    att_crosses_ta = models.CharField(max_length=20)
    att_crosses_completed = models.CharField(max_length=20)
    att_crosses_completed_ta = models.CharField(max_length=20)
    att_offsides = models.CharField(max_length=20)
    att_offsides_ta = models.CharField(max_length=20)
    def_total_defense = models.CharField(max_length=20)
    def_tackles = models.CharField(max_length=20)
    def_saves = models.CharField(max_length=20)
    def_blocks = models.CharField(max_length=20)
    def_saves = models.CharField(max_length=20)
    def_saves_ta = models.CharField(max_length=20)
    def_attempted_clearances = models.CharField(max_length=20)
    def_attempted_clearances_ta = models.CharField(max_length=20)
    def_completed_clearances = models.CharField(max_length=20)
    def_completed_clearances_ta = models.CharField(max_length=20)
    def_recovered_balls = models.CharField(max_length=20)
    def_recovered_balls_ta = models.CharField(max_length=20)
    def_tackles_tol = models.CharField(max_length=20)
    def_tackles_tol_ta = models.CharField(max_length=20)
    def_tackles_won = models.CharField(max_length=20)
    def_tackles_won_ta = models.CharField(max_length=20)
    def_tackles_lost = models.CharField(max_length=20)
    def_tackles_lost_ta = models.CharField(max_length=20)
    def_offsides_given = models.CharField(max_length=20)
    def_offsides_given_ta = models.CharField(max_length=20)
    pass_total = models.CharField(max_length=20)
    pass_short_passes_complete = models.CharField(max_length=20)
    pass_medium_passes_complete = models.CharField(max_length=20)
    pass_long_passes_complete = models.CharField(max_length=20)
    pass_ta = models.CharField(max_length=20)
    pass_crosses = models.CharField(max_length=20)
    pass_crosses_ta = models.CharField(max_length=20)
    pass_throw_ins = models.CharField(max_length=20)
    pass_throw_ins_ta = models.CharField(max_length=20)




    def get_absolute_url(self):
        return "/countries/%s/" % self.country_name

    def __str__ (self):
        return self.country_name


    # ------------
    # Player_model
    # ------------

class Player(models.Model):
    """
    The model contains a country name (which is foreign key that comes from the country model), player surname, full name,
    club the player plays for, the position the player plays and his date of birth_date. Mores fields have been added such
    as shirt_number, player_image, international_caps, goals, height, first_international_appearance, biography, and 
    twitter_name.
    The __str__ method is used to return the name of the player.
    The get_absolute_url method overrides the default url so that watson get the correct url as a link.
    """
    
    class Meta:
        db_table = 'Player'

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sur_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    clubname = models.CharField(max_length=200)
    position = models.CharField(max_length=64)
    shirt_number = models.IntegerField(default=0)
    birth_date = models.DateField()
    player_image = models.CharField(max_length=500)
    #add
    international_caps = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    first_international_appearance = models.CharField(max_length=500)
    biography = models.CharField(max_length=5000)
    twitter_name = models.CharField(max_length=500)

    def get_absolute_url(self):
        url_name = self.full_name.replace(' ', '_')
        return "/players/%s/" % url_name

    def __str__ (self):
        return self.full_name

    # ------------
    # Match_model
    # ------------

class Match(models.Model):
    """
    The model contains a match number, the two countries that are facing each other (both of the countries are foreign keys), the winner of the match, 
    the score of the match, the location of the match and the date when the match was held.
    
    Mores fields have been added such as match_date, merge_flag, map_location, and highlight_url.

    The __str__ method is used to return the two countries facing each other and the score.
    The get_absolute_url method overrides the default url so that watson get the correct url as a link. 
    """
    class Meta:
        db_table = 'Match'

    match_num = models.IntegerField(default=0, primary_key=True)
    country_A = models.ForeignKey(Country, related_name='country_A', on_delete=models.CASCADE)
    country_B = models.ForeignKey(Country, related_name='country_B', on_delete=models.CASCADE)
    winner = models.CharField(max_length=200)
    score = models.CharField(max_length=64)
    location = models.CharField(max_length=200)
    match_date = models.DateField()
    merge_flag = models.CharField(max_length=500)
    map_location = models.CharField(max_length=500)
    highlight_url = models.CharField(max_length=500)

    def get_absolute_url(self):
        return "/matches/%d/" % self.match_num

    def __str__ (self):
        return self.country_A.country_name + " " + self.country_B.country_name + " " + self.score
