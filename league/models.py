from django.db import models

MAX_NAME_LENGTH = 100

class Player(models.Model):
    """ Stores player data. """
    first_name = models.CharField(max_length=MAX_NAME_LENGTH)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH)
    elo = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Match(models.Model):
    """ Stores individual match data. """
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_1_matches")
    player_1_score = models.IntegerField()
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_2_matches")
    player_2_score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.timestamp} | {self.player_1} {self.player_1_score} vs {self.player_2}"
                f" {self.player_2_score}")
