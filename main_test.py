import main

# Test function


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert '{"greeting":"hello world"}' in r.data.decode('utf-8')
