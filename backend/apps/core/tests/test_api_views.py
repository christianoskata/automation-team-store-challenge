import pytest


@pytest.mark.django_db()
class TestShoesViewSetGet:

    def test_must_return_success(self, api_client, shoe, shoe_data):
        response = api_client.get('/api/v1/shoes/1/')

        assert 200 == response.status_code

        shoe = response.json()

        for key, value in shoe_data.items():
            assert value == shoe.get(f'{key}')
        assert '180.00' == shoe.get('gross_price')

    def test_must_return_not_found(self, api_client):
        response = api_client.get('/api/v1/shoes/1/')
        assert 404 == response.status_code


@pytest.mark.django_db()
class TestShoesViewSetList:

    def test_must_return_success(self, api_client, shoes):
        response = api_client.get('/api/v1/shoes/')

        assert 200 == response.status_code
        assert 10 == len(response.data)

    def test_filter_success(self, api_client, shoes):
        filter_name = api_client.get('/api/v1/shoes/?search=Tenis Bolado New')
        filter_brand = api_client.get('/api/v1/shoes/?search=Nid')
        filter_name_brand = api_client.get('/api/v1/shoes/?search=Tenis Bolado Nide')

        assert 1 == len(filter_name.data)
        for data in filter_name.data:
            assert 'Tenis Bolado' in data.get('name')

        assert 4 == len(filter_brand.data)
        for data in filter_brand.data:
            assert 'Nide' == data.get('brand')

        assert 3 == len(filter_name_brand.data)
        for data in filter_name_brand.data:
            assert 'Tenis Bolado' in data.get('name')
            assert 'Nide' == data.get('brand')


@pytest.mark.django_db()
class TestShoesViewSetPatch:

    def test_must_return_success(self, api_client, shoe, shoe_data):
        response = api_client.patch(f'/api/v1/shoes/{shoe["id"]}/', data={'size': 50})

        assert 200 == response.status_code

        shoe = response.json()
        del shoe_data['size']

        for key, value in shoe_data.items():
            assert value == shoe.get(f'{key}')
        assert 50 == shoe.get('size')

    def test_must_return_not_found(self, api_client):
        response = api_client.patch('/api/v1/shoes/unknown_id/', data={'size': 50})
        assert 404 == response.status_code


class TestShoesViewSetPost:
    def test_must_return_success(self, api_client, shoe_data):
        response = api_client.post('/api/v1/shoes/', data=shoe_data)

        assert 201 == response.status_code


class TestShoesViewSetPut:
    def test_must_return_success(self, api_client, shoe, shoe_data):
        shoe_data['size'] = 50
        response = api_client.put(f'/api/v1/shoes/{shoe["id"]}/', data=shoe_data)

        assert 200 == response.status_code


class TestShoesViewSetDelete:
    def test_must_return_success_no_content(self, api_client, shoe):
        response = api_client.delete(f'/api/v1/shoes/{shoe["id"]}/')

        assert 204 == response.status_code


class TestShoesUploadAPIViewPost:
    def test_must_return_success(self, api_client, csv_file):
        response = api_client.post('/api/v1/shoes/csv/', data=csv_file.new())

        assert 201 == response.status_code
        assert 10 == len(response.data)

    def test_must_not_duplicate_data(self, api_client, csv_file):
        api_client.post('/api/v1/shoes/csv/', data=csv_file.new())
        response = api_client.post('/api/v1/shoes/csv/', data=csv_file.new())

        assert 201 == response.status_code
        assert 0 == len(response.data)
