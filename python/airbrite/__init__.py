import requests

END_POINT = 'https://api.airbrite.io/v2/'

TEST_API_KEY = 'sk_test_a805be8b2add854f09976b3b5c0f5bd06c14617c'
API_KEY = TEST_API_KEY


def test_connection():
    """Returns True if the API is operational, False otherwise"""
    # TODO: implement a cheaper test

    # Connection test based on assumption that the test API key is used, and
    # that there's at least one product registered.
    result = requests.get(END_POINT + 'products', auth=(API_KEY, ''))
    if result.status_code == 200:
        return True
    return False
