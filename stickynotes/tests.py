from django.test import TestCase
from django.urls import reverse
from .models import Stickynote


# class StickynoteTest(TestCase):
#     # If your tests aren't passing for any strange reason try this instead
#     # setUp()
#     @classmethod
#     def setUpTestData(cls):
#         Stickynote.objects.create(
#         name='Stickynote 1', description='Description 1', sets=10,
#         creator="Test")

#     # def setUp(self):
#     #     Stickynote.objects.create(
#     #     name='Stickynote 1', description='Description 1', sets=10,
#           creator="Test")
#     def test_stickynote_has_name(self):
#         stickynote = Stickynote.objects.get(id=1)
#         self.assertEqual(stickynote.name, 'Stickynote 1')

#     def test_stickynote_has_description(self):
#         stickynote = Stickynote.objects.get(id=1)
#         self.assertEqual(stickynote.description, 'Description 1')

#     def test_stickynote_has_sets(self):
#         stickynote = Stickynote.objects.get(id=1)
#         self.assertEqual(stickynote.sets, 10)

#     def test_stickynote_has_creator(self):
#         stickynote = Stickynote.objects.get(id=1)
#         self.assertEqual(stickynote.creator, 'Test')

class StickynoteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an object for testing
        Stickynote.objects.create(
         name='Stickynote 1', description='Description 1', sets=10,
         creator="Test")

    def test_stickynote_get_all_returns_all_stickynotes(self):
        # Test the post-list view
        response = self.client.get(reverse('stickynotes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Stickynote 1')

    def test_stickynote_get_returns_stickynote(self):
        # Test the post-detail view
        stickynote = Stickynote.objects.get(id=1)
        response = self.client.get(reverse('stickynote', args=[stickynote.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Stickynote 1')

    def test_delete_should_remove_item(self):
        # Test the post-delete view
        stickynotes = Stickynote.objects.all()
        init_length = stickynotes.count()

        stickynote = Stickynote.objects.get(id=1)

        response = self.client.get(reverse('delete_stickynote',
                                   args=[stickynote.id]))

        # Final length check
        final_length = Stickynote.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(init_length, final_length)
