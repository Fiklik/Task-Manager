from django.test import TestCase, modify_settings
from task_manager.labels.models import Label


remove_rollbar = modify_settings(
    MIDDLEWARE={
        "remove": [
            "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
        ]
    }
)


@remove_rollbar
class TestLabelModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Label.objects.create(name="Test Label")

    def test_model(self):
        test_model = Label.objects.get(name="Test Label")

        self.assertEqual(test_model.__str__(), "Test Label")

        self.assertEqual(test_model.name, "Test Label")

        test_model.save()
        saved_model = Label.objects.get(name="Test Label")

        self.assertEqual(saved_model.name, "Test Label")
