from django.db import models

class Team(models.Model):
	logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
	name = models.CharField(max_length=100)
	class_year = models.IntegerField()
	captain = models.CharField(max_length=100)
	coach = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' '+ self.team.name

class Matches(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.date}"

class Fixture(models.Model):
    season = models.CharField(max_length=100)
    week = models.IntegerField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
   
    def __str__(self):
        return f"{self.season} {self.week}- {self.date}"



class Goal(models.Model):
    scorer = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    num_goals = models.IntegerField()
    match_detail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.scorer.name} {self.num_goals} scored in {self.match_detail}"

class Result(models.Model):
    date = models.CharField(max_length=100)
    team_home = models.CharField(max_length=100)
    team_away = models.CharField(max_length=100)
    team_home_score = models.IntegerField()
    team_away_score = models.IntegerField()
    team_home_points = models.IntegerField()
    team_away_points = models.IntegerField()

class Point(models.Model):
    date = models.CharField(max_length=100)
    match_detail = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points_got = models.IntegerField()
    

class Table(models.Model):
    date = models.CharField(max_length=100)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    matches_won = models.IntegerField()
    matches_drawn = models.IntegerField()
    matches_lost = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    points = models.IntegerField()


    @property
    def goal_difference(self):
        # Perform calculations here based on other fields
        GD = self.goals_for - self.goals_against
        return GD
