import pytest
import uuid


@pytest.mark.asyncio
async def test_register(client, base_url):
    username = f"testuser_{uuid.uuid4().hex[:6]}"
    password = "testpassword"

    response = await client.post(
        f"{base_url}/user/",
        json={"username": username, "password": password}
    )

    assert response.status_code == 200, response.text
    response_data = response.json()

    assert "accessToken" in response_data
    assert "refreshToken" in response_data

    return response_data


@pytest.mark.asyncio
async def test_login(client, base_url):
    username = f"testlogin_{uuid.uuid4().hex[:6]}"
    password = "testpassword"

    await client.post(f"{base_url}/user/", json={"username": username, "password": password})

    response = await client.post(
        f"{base_url}/user/login",
        json={"username": username, "password": password}
    )

    assert response.status_code == 200
    response_data = response.json()

    assert "accessToken" in response_data
    assert "refreshToken" in response_data

    return response_data


@pytest.mark.asyncio
async def test_refresh_token(client, base_url):
    username = f"testrefresh_{uuid.uuid4().hex[:6]}"
    password = "testpassword"

    response1 = await client.post(
        f"{base_url}/user/",
        json={"username": username, "password": password}
    )
    response1_data = response1.json()

    refresh_payload = {
        "accessToken": response1_data["accessToken"],
        "refreshToken": response1_data["refreshToken"]
    }

    response2 = await client.post(
        f"{base_url}/user/refresh-token",
        json=refresh_payload
    )

    assert response2.status_code == 200
    response2_data = response2.json()

    assert "accessToken" in response2_data
    assert "refreshToken" in response2_data