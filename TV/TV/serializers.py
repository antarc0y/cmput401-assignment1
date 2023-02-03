from rest_framework import serializers
from .models import Show
class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ['id','name','rating','network']
    # override default save    
    def save(self, validated_data):
        shows = Show.objects.all()
        if not shows:
            next_id = 0
        else:
            last_show = shows.last()
            next_id = last_show.id + 1
        show = Show.objects.create(id=next_id, **validated_data)
        return show

class ShowSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ['id','name', 'description','network','episodes','cast','rating']