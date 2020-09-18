from rest_framework import serializers
from nbvnb.models import Bngvnbvnb


class BngvnbvnbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bngvnbvnb
        fields = "__all__"
