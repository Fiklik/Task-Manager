from django.test import TestCase
from task_manager.labels.models import Label


class TestLabel(TestCase):
    def setUp(self):
        self.obj = Label.objects.create(name="Test Label")

    def test_create_label(self):
        new_obj = Label.objects.create(name="Another Test Label")

        self.assertEqual(new_obj.name, "Another Test Label")

    def test_read_label(self):
        read_obj = Label.objects.get(id=self.obj.id)

        self.assertEqual(read_obj.name, "Test Label")

    def test_update_label(self):
        self.obj.name = "New Test Label Name"
        self.obj.save()

        updated_obj = Label.objects.get(id=self.obj.id)

        self.assertEqual(updated_obj.name, "New Test Label Name")

    def test_delete_label(self):
        self.obj.delete()

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(id=self.obj.id)
