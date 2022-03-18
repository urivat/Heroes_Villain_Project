from rest_framework import serializers

import supers_types
from.models import Super
from.models import SuperType


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name','alter_ego', 'primary_ability', 'secondary_ability','catchphrase','supers_types_id']
        depth = 1

supers_types_id = serializers.IntegerField(write_only = True)