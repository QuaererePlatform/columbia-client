from columbia_client import ColumbiaClient


class TestClient:

    def test_instantiation(self):
        base_url = 'http://columbia.quaerere.local:5000/api'
        client = ColumbiaClient(base_url)

        assert client.url_base == base_url
        assert client.v1.version == 'v1'
