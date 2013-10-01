import unittest
import airbrite

CURRENT_END_POINT = 'https://api.airbrite.io/v2/'


class ConnectionTestCase(unittest.TestCase):

    def test_defaults_to_test_API_KEY(self):
        self.assertEqual(airbrite.API_KEY, airbrite.TEST_API_KEY)

    def test_endpoint(self):
        self.assertEqual(airbrite.END_POINT, CURRENT_END_POINT)

    def test_can_connect(self):
        ret = airbrite.test_connection()
        self.assertTrue(ret)
