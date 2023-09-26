import pytest
from flask import json
from src.main.server.server import app


@pytest.fixture
def client():
    return app.test_client()


def test_first_calculator_success(client):
    values = [10, 20, 30]

    data = json.dumps({"values": values})

    response = client.post('/calculate/first', data=data,
                           content_type='application/json')

    assert response.status_code == 200
    assert b'Sucesso' in response.data
