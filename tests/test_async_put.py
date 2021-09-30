import asyncio
from aioaerospike.client import AerospikeClient
import numpy as np
import pytest


HOST = '127.0.0.1'
USER = 'admin'
PASSWORD = 'admin'
PORT = 3000
NAMESPACE = 'bar'
N_PIDS = 50000
N_TASK = 10
SET = 'profiles_async'


@pytest.mark.asyncio
async def get_aio_client():
    client = AerospikeClient(HOST, USER, PASSWORD, port=PORT)
    await client.connect()
    return client


@pytest.mark.asyncio
async def sanity_put(client, split_pids):
    for key in split_pids:
        await client.put_key(NAMESPACE, SET, str(key), {'vvv': 41, 'vvvvv': 11})


@pytest.mark.asyncio
async def main():
    tasks = []
    arr = np.array([i for i in range(N_PIDS)])
    arr_split = np.split(arr, N_TASK)
    for i in range(N_TASK):
        client = await get_aio_client()
        tasks.append(asyncio.create_task(sanity_put(client, arr_split[i])))
    await asyncio.gather(*tasks)


@pytest.mark.asyncio
async def test_run_put_main():
    await main()
