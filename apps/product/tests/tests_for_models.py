from django.test import TestCase
from apps.product.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        # Set up a sample product
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

    def test_product_str(self):
        """Test the string representation of the Product model."""
        expected_str = f"Store: {self.product.store}, Product: {self.product.name}, Price: {self.product.price}{self.product.currency}"
        self.assertEqual(str(self.product), expected_str)

    def test_product_fields(self):
        """Test the Product model fields."""
        self.assertEqual(self.product.store, "Amazon")
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.currency, "USD")
        self.assertEqual(self.product.category, "Electronics")
