from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
           title ="HelloTitle",
           subtitle="HelloSubtitle",
           author="ajrou",
           isbn = "1234567890123", 
        )

        def test_book_content(self):
            self.assertEqual(self.book.title, "HelloTitle")
            self.assertEqual(self.book.subtitle, "HelloSubtitle")
            self.assertEqual(self.book.author, "ajrou")
            self.assertEqual(self.book.isbn, "1234567890123")
        
        def test_book_listview(self):
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "excellent subtitle")
            self.assertTemplateUsed(response, "books/book_list.html")


# Create your tests here.
