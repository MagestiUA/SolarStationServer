from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login_redirect, base_page, api_login, api_register, api_logout
from SolarStationServer.views import data_collector, get_current_data
from telegram.views import telegram
from graphene_django.views import GraphQLView

class UrlsTestCase(SimpleTestCase):
    def test_login_redirect_url(self):
        url = reverse("login_redirect")
        self.assertEqual(resolve(url).func, login_redirect)

    def test_base_page_url(self):
        url = reverse("base_page")
        self.assertEqual(resolve(url).func, base_page)

    def test_api_login_url(self):
        url = reverse("api_login")
        self.assertEqual(resolve(url).func, api_login)

    def test_data_collector_url(self):
        url = reverse("data_collector")
        self.assertEqual(resolve(url).func, data_collector)

    def test_get_current_data_url(self):
        url = reverse("get_current_data")
        self.assertEqual(resolve(url).func, get_current_data)

    def test_telegram_url(self):
        url = reverse("telegram")
        self.assertEqual(resolve(url).func, telegram)

    def test_graphql_url(self):
        url = reverse("graphql")
        self.assertEqual(resolve(url).func.view_class, GraphQLView)
