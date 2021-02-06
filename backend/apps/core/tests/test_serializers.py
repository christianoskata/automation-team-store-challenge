from apps.core.serializers import ShoesSerializer, ShoesUploadSerializer


class TestShoesSerializer:

    def test_payload_is_valid(self, shoe_data):
        serializer = ShoesSerializer(data=shoe_data)
        assert serializer.is_valid() is True

    def test_payload_without_required_data_is_not_valid(self, shoe_data):
        required = [
            'name',
            'brand',
            'ref',
            'material',
            'color',
            'size',
            'quantity',
            'net_price',
            'tax'
        ]

        for item in required:
            copy_shoe = dict(shoe_data)
            del copy_shoe[item]
            serializer = ShoesSerializer(data=copy_shoe)
            assert serializer.is_valid() is False

    def test_calculate_gross_price(self, shoe_data):
        serializer = ShoesSerializer(data=shoe_data)
        serializer.is_valid()
        assert serializer.data['gross_price'] == '180.00'


class TestShoesUploadSerializer:

    def test_payload_is_valid(self, csv_file):
        serializer = ShoesUploadSerializer(data=csv_file.new())
        assert serializer.is_valid() is True
