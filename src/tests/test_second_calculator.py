import pytest
from flask import json
from src.main.server.server import app


@pytest.fixture
def client():
    return app.test_client()


def test_second_calculator_success(client):
    values = [10, 20, 30]

    data = json.dumps({"values": values})

    response = client.post('/calculate/second', data=data, content_type='application/json')

    assert response.status_code == 200
    assert b'Sucesso' in response.data


def test_second_calculator_fail(client):
    values = [1, 1, 1]

    data = json.dumps({"values": values})

    response = client.post('/calculate/second', data=data, content_type='application/json')

    assert response.status_code == 200
    assert b'Falha' in response.data
