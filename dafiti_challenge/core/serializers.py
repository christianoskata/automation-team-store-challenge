from rest_framework import serializers

from dafiti_challenge.core.models import Shoes


class ShoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoes
        fields = ('id', 'name', 'brand', 'ref', 'material',
                  'color', 'description', 'size', 'quantity',
                  'weight', 'net_price', 'tax', 'gross_price')
