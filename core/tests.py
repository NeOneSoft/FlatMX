from rest_framework.test import RequestsClient


def test_server_branches():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/api/v1/branches/')

    assert response.status_code == 500


def test_server_commits():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/api/v1/commits/')

    assert response.status_code == 500


def test_server_pulls():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/api/v1/pulls/')

    assert response.status_code == 500


def test_server_authors():
    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/api/v1/authors/')

    assert response.status_code == 500
