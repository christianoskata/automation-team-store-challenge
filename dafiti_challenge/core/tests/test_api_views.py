import pytest


class TestShoesViewSetGet:

    @pytest.mark.orient_db()
    def test_must_return_success(self, api_client, shoe, shoe_data):
        response = api_client.get('/api/v1/shoes/1/')

        assert 200 == response.status_code

        shoe = response.json()

        for key, value in shoe_data.items():
            assert value == shoe.get(f'{key}')
        assert '180.00' == shoe.get('gross_price')

    @pytest.mark.orient_db()
    def test_must_return_not_found(self, api_client):
        response = api_client.get('/api/v1/shoes/1/')
        assert 404 == response.status_code


class TestShoesViewSetList:

    @pytest.mark.orient_db()
    def test_must_return_success(self, api_client, shoes_list):
        response = api_client.get('/api/v1/shoes/')

        assert 200 == response.status_code
        assert 10 == len(response.data)


class TestShoesViewSetPatch:

    @pytest.mark.orient_db()
    def test_must_return_success(self, api_client, shoe, shoe_data):
        response = api_client.patch('/api/v1/shoes/1/', data={'size': 50})

        assert 200 == response.status_code

        shoe = response.json()
        del shoe_data['size']

        for key, value in shoe_data.items():
            assert value == shoe.get(f'{key}')
        assert 50 == shoe.get('size')

    @pytest.mark.orient_db()
    def test_must_return_not_found(self, api_client):
        response = api_client.patch('/api/v1/shoes/unknown_id/', data={'size': 50})
        assert 404 == response.status_code


class TestShoesViewSetPost:
    def test_must_return_not_allowed(self, api_client, shoe_data):
        response = api_client.post('/api/v1/shoes/', data=shoe_data)

        assert 201 == response.status_code


class TestShoesViewSetPut:
    def test_must_return_not_allowed(self, api_client, shoe, shoe_data):
        shoe_data['size'] = 50
        response = api_client.put('/api/v1/shoes/1/', data=shoe_data)

        assert 200 == response.status_code


class TestShoesViewSetDelete:
    def test_must_return_not_allowed(self, api_client, shoe):
        response = api_client.delete('/api/v1/shoes/1/')

        assert 204 == response.status_code


class TestShoesUploadAPIViewPost:
    def test_must_return_not_allowed(self, api_client, csv_file):
        response = api_client.post('/api/v1/shoes/csv/', data=csv_file)

        assert 201 == response.status_code
        assert 6 == len(response.data)
