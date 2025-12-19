import uuid
import requests

BASE_URL = "http://localhost:4322/api"

def register_and_get_headers():
    username = f"todouser_{uuid.uuid4().hex[:6]}"
    password = "testpassword"

    response = requests.post(
        f"{BASE_URL}/users/",
        json={"username": username, "password": password}
    )
    assert response.status_code == 200

    tokens = response.json()
    return {
        "Authorization": f"Bearer {tokens['accessToken']}"
    }

def test_find_todo_list_roles():
    headers = register_and_get_headers()

    response = requests.get(
        f"{BASE_URL}/todo-lists/roles",
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

def test_create_todo_list():
    headers = register_and_get_headers()

    payload = {
        "name": "My First Todo List"
    }

    response = requests.post(
        f"{BASE_URL}/todo-lists/",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["name"] == payload["name"]

    return data

def test_find_todo_lists():
    headers = register_and_get_headers()

    requests.post(
        f"{BASE_URL}/todo-lists/",
        json={"name": "List A"},
        headers=headers
    )

    response = requests.get(
        f"{BASE_URL}/todo-lists/",
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1

def test_find_todo_list_by_id():
    headers = register_and_get_headers()

    create_response = requests.post(
        f"{BASE_URL}/todo-lists/",
        json={"name": "Single List"},
        headers=headers
    )
    todo_list = create_response.json()

    response = requests.get(
        f"{BASE_URL}/todo-lists/{todo_list['id']}",
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == todo_list["id"]
    assert data["name"] == "Single List"

def test_update_todo_list():
    headers = register_and_get_headers()

    create_response = requests.post(
        f"{BASE_URL}/todo-lists/",
        json={"name": "Old Name"},
        headers=headers
    )
    todo_list = create_response.json()

    update_payload = {
        "name": "Updated Name"
    }

    response = requests.put(
        f"{BASE_URL}/todo-lists/{todo_list['id']}",
        json=update_payload,
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Updated Name"

def test_clone_todo_list():
    headers = register_and_get_headers()

    create_response = requests.post(
        f"{BASE_URL}/todo-lists/",
        json={"name": "Original List"},
        headers=headers
    )
    todo_list = create_response.json()

    clone_payload = {
        "name": "Cloned List"
    }

    response = requests.post(
        f"{BASE_URL}/todo-lists/{todo_list['id']}/clone",
        json=clone_payload,
        headers=headers
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Cloned List"
    assert data["id"] != todo_list["id"]