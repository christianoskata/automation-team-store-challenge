import csv
import io

from .models import Shoes
from rest_framework import serializers


class ShoesSerializer(serializers.ModelSerializer):
    gross_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    @staticmethod
    def calculate_gross_price(data):
        profit = (float(data['net_price']) * float(data['tax'])) / 100
        return float(data['net_price']) + profit

    def to_internal_value(self, data):
        data = super(ShoesSerializer, self).to_internal_value(data)
        validated = data.copy()
        if data.get('net_price') is not None and data.get('tax') is not None:
            validated['gross_price'] = self.calculate_gross_price(data)
        return validated

    class Meta:
        model = Shoes
        fields = ('id', 'name', 'brand', 'ref', 'material',
                  'color', 'description', 'size', 'quantity',
                  'weight', 'net_price', 'tax', 'gross_price',)


class ShoesUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    @staticmethod
    def handler_csv(file):
        with io.TextIOWrapper(file, encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader, None)

            content = []
            for row in reader:
                row_data = {}
                for header, value in zip(headers, row):
                    row_data[header] = value
                content.append(row_data)
            return content

    class Meta:
        fields = ('file',)
