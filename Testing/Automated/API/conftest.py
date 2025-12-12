import pytest
import httpx

BASE_URL = "http://localhost:80"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
async def client():
    async with httpx.AsyncClient() as client:
        yield client