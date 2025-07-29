from django.db import models
from tournaments.models import Tournament
from players.models import Player

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    date = models.DateTimeField()
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='match_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='match_player2')
    score = models.CharField(max_length=50, blank=True)  # Например: "6-4, 3-6, 7-6"
    winner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_matches')

    def __str__(self):
        return f'{self.player1} vs {self.player2} ({self.tournament})'