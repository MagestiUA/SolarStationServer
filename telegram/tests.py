from django.test import TestCase
import json
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from rest_framework.test import APIClient
from telegram.telegram_bot import send_telegram_message


class TelegramTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.chat_id = 123456789
		self.message_text = "Test message"
	
	@patch('telegram.telegram_bot.requests.post')
	def test_send_telegram_message(self, mock_post):
		mock_post.return_value.json.return_value = {"ok": True, "result": {"message_id": 1}}
		send_telegram_message(self.chat_id, self.message_text)
		
		mock_post.assert_called_once_with(
			f'https://api.telegram.org/bot{send_telegram_message.token}/sendMessage',
			json={'chat_id': self.chat_id, 'text': self.message_text}
		)
	
	@patch('telegram.telegram_bot.send_battery_voltage.delay')
	def test_telegram_battery_command(self, mock_send_battery_voltage):
		response = self.client.post(
			reverse('telegram'),
			data=json.dumps({
				"message": {
					"chat": {"id": self.chat_id},
					"text": "battery"
				}
			}),
			content_type="application/json"
		)
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content.decode(), "OK!")
		mock_send_battery_voltage.assert_called_once_with(user_id=self.chat_id)
	
	@patch('telegram.telegram_bot.send_telegram_message')
	def test_telegram_echo_message(self, mock_send_telegram_message):
		response = self.client.post(
			reverse('telegram'),
			data=json.dumps({
				"message": {
					"chat": {"id": self.chat_id},
					"text": "Hello!"
				}
			}),
			content_type="application/json"
		)
		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content.decode(), "OK!")
		mock_send_telegram_message.assert_called_once_with(self.chat_id, "I listens to you! Hello!")
