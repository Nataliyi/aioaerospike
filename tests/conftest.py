import uuid

import pytest

from aioaerospike.client import AerospikeClient


HOST = '127.0.0.1'
USER = 'admin'
PASSWORD = 'admin'
PORT = 3000
NAMESPACE = 'bar'


@pytest.fixture
async def client(scope="module"):
    client = AerospikeClient(HOST, USER, PASSWORD, port=PORT)
    await client.connect()
    return client


@pytest.fixture
def namespace():
    return NAMESPACE


@pytest.fixture
def set_name():
    """
    Randomize name to avoid collision between tests
    """
    return uuid.uuid4().hex[:8]


@pytest.fixture
def key():
    """
    Randomize name to avoid collision between tests
    """
    return uuid.uuid4().hex[:8]
