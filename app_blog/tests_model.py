from django.test import TestCase
from .models import Article, Category

class ModelTests(TestCase):
    def test_article_creation(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'Test Content')

    def test_category_creation(self):
        category = Category.objects.create(category='Test Category')
        self.assertEqual(category.category, 'Test Category')







