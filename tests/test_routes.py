import unittest
from service import app
from service.models import Account


class TestAccounts(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        Account.accounts = []

    def test_create_account(self):
        response = self.app.post(
            "/accounts",
            json={
                "name": "Khalil",
                "email": "khalil@test.com"
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_list_accounts(self):
        self.app.post(
            "/accounts",
            json={
                "name": "Khalil",
                "email": "khalil@test.com"
            }
        )

        response = self.app.get("/accounts")

        self.assertEqual(response.status_code, 200)

    def test_read_account(self):
        self.app.post(
            "/accounts",
            json={
                "name": "Khalil",
                "email": "khalil@test.com"
            }
        )

        response = self.app.get("/accounts/1")

        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        self.app.post(
            "/accounts",
            json={
                "name": "Khalil",
                "email": "old@test.com"
            }
        )

        response = self.app.put(
            "/accounts/1",
            json={
                "name": "Updated",
                "email": "new@test.com"
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_account(self):
        self.app.post(
            "/accounts",
            json={
                "name": "Khalil",
                "email": "test@test.com"
            }
        )

        response = self.app.delete("/accounts/1")

        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
