from rest_framework import serializers

from.models import Super
from.models import SuperType


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name','alter_ego', 'primary_ability', 'secondary_ability','catchphrase','type']
        depth = 1

type = serializers.IntegerField(write_only = True)