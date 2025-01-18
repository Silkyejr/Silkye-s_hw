import pytest
from app import app, load_words, save_words, word_dict

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_words(client):
    response = client.get('/api/words')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_add_word(client):
    new_word = {"word": "hello", "definition": "привет"}
    response = client.post('/api/words', json=new_word)
    assert response.status_code == 201
    assert response.json["message"] == "Word 'hello' added successfully!"

    # Проверяем, что слово добавилось в словарь
    assert "hello" in load_words()
    assert load_words()["hello"] == "привет"