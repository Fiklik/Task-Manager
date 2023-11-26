from django.test import TestCase, Client


class TestUsersForms(TestCase):
    def test_registration_valid_form(self):
        c = Client()
        response = c.post(
            "/users/create/",
            {
                "first_name": "Test",
                "last_name": "User",
                "username": "TestUser",
                "password1": "hexlet1234",
                "password2": "hexlet1234",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")

    def test_registration_invalid_form(self):
        c = Client()
        response = c.post(
            "/users/create/",
            {
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, 200)
