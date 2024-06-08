from rest_framework import serializers
from api.models import WatchedMovie

class MostWatchedMovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    watch_count = serializers.IntegerField()