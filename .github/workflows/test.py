def test_app(client):
    """My first test."""

    rv = client.get('/')
    assert b'Hello, Docker!' in rv.data