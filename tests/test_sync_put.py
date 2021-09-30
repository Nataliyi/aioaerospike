import aerospike


NAMESPACE = 'bar'
SET = 'profiles_sync'
HOST = '127.0.0.1:3000'
N_PIDS = 500000


# create aerospike connection
def get_aerospike_client(hosts):
    aerospike_hosts = list(map(lambda x: (x.split(':')[0], int(x.split(':')[1])), hosts.split(',')))
    config = {'hosts': aerospike_hosts}
    aerospike_client = aerospike.client(config)
    return aerospike_client.connect()


def test_put_many():
    client = get_aerospike_client(HOST)
    for i in range(N_PIDS):
        client.put((NAMESPACE, SET, i), {'vvv': 41, 'vvvvv': 11})
