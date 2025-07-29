from rest_framework import serializers
from .models import Match, Player

class PlayerShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'rank', 'photo']

class MatchSerializer(serializers.ModelSerializer):
    player1 = PlayerShortSerializer(read_only=True)
    player2 = PlayerShortSerializer(read_only=True)
    winner = PlayerShortSerializer(read_only=True)
    tournament = serializers.StringRelatedField() # или TournamentShortSerializer

    class Meta:
        model = Match
        fields = '__all__'