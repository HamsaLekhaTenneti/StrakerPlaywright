import requests, pytest

URL = "https://jsonplaceholder.typicode.com/posts/1"

@pytest.fixture
def create_book():
    return {"title": "The Hobbit", "author": "J.R.R. Tolkien"}


def test_get_call_verification():
    response = requests.get(url=URL)

    status_code = response.status_code
    response_body = response.json()

    # Verifying status code
    assert status_code == 200

    # Verifying response body
    assert response_body["userId"] == 1
    assert response_body["id"] == 1


def test_create_book(create_book):

    url = "https://run.mocky.io/v3/628dca34-286a-4850-902b-b5fdd89e0ce3/books"  # Replace with your mock API URL
    response = requests.post(url, json=create_book)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

    # Check if the book was created (specifics depend on your mock API's response)
    data = response.json()
    assert "id" in data 
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"
