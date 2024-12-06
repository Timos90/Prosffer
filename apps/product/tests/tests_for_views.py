from django.test import TestCase, Client
from django.urls import reverse
from apps.product.models import Product

class ProductListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('product-urls:product-list')

        # Create sample products
        self.product1 = Product.objects.create(
            store="Amazon",
            name="Laptop",
            description="A good laptop",
            price=1200.50,
            currency="USD",
            category="Electronics",
            image="http://example.com/laptop.jpg",
            link="http://example.com/laptop",
        )
        self.product2 = Product.objects.create(
            store="eBay",
            name="Smartphone",
            description="A great smartphone",
            price=699.99,
            currency="USD",
            category="Electronics",
            image="http://example.com/smartphone.jpg",
            link="http://example.com/smartphone",
        )

    def test_product_list_view(self):
        """Test the product list view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Smartphone")

    def test_product_list_pagination(self):
        """Test pagination in the product list view."""
        # Simulate pagination
        for i in range(15):
            Product.objects.create(
                store="Store",
                name=f"Product {i}",
                price=10.00 + i,
                currency="USD",
                category="TestCategory",
                image="http://example.com/product.jpg",
                link="http://example.com/product",
            )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('page_obj', response.context)
        self.assertTrue(response.context['is_paginated'])

    def test_product_search_ajax(self):
        """Test the AJAX product list view."""
        url = reverse('product-urls:product_list_ajax')
        response = self.client.get(url, {'product_name': 'Laptop', 'category': 'Electronics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")
        self.assertNotContains(response, "Smartphone")

class ProductSearchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('product-urls:product-search')
        self.product = Product.objects.create(
            store="Amazon",
            name="Test Product",
            description="Test Description",
            price=19.99,
            currency="USD",
            category="Electronics",
            image="http://example.com/image.jpg",
            link="http://example.com/product",
            id_tag="test123",
        )

    def test_product_search_autocomplete(self):
        """Test product search autocomplete."""
        response = self.client.get(self.url, {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.product.name, response.json())

    def test_product_search_no_query(self):
        """Test product search with no query."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
