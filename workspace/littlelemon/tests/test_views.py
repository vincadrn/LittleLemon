from django.test import TestCase, RequestFactory
from django.core import serializers
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Beef steak', price=25, inventory=10)
        Menu.objects.create(title='Orange juice', price=2, inventory=2)
    
    def test_get_all(self):
        menu = Menu.objects.all()
        serialized_menu = MenuSerializer(menu, many=True)
        request = RequestFactory().get('/restaurant/menu')
        response = MenuItemView.as_view()(request)

        self.assertEqual(response.data, serialized_menu.data)
