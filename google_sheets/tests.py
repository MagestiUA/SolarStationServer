from unittest import TestCase
from unittest.mock import patch, MagicMock
from google_sheets import service


class GoogleSheetsServiceTest(TestCase):
	
	@patch("google_sheets.service.gspread.authorize")
	def test_get_google_sheets_client(self, mock_authorize):
		mock_authorize.return_value = MagicMock()
		client = service.get_google_sheets_client()
		self.assertIsNotNone(client)
		mock_authorize.assert_called_once()
	
	@patch("google_sheets.service.gspread.Client")
	@patch("google_sheets.service.gspread.authorize")
	def test_read_from_sheet(self, mock_authorize, mock_client):
		mock_client_instance = mock_client.return_value
		mock_authorize.return_value = mock_client_instance
		mock_spreadsheet = mock_client_instance.open_by_key.return_value
		mock_spreadsheet.values_get.return_value = {"values": [["Test Value"]]}
		
		result = service.read_from_sheet("A1:B2")
		self.assertEqual(result, {"values": [["Test Value"]]})
		mock_spreadsheet.values_get.assert_called_once_with("A1:B2")
	
	@patch("google_sheets.service.gspread.Client")
	@patch("google_sheets.service.gspread.authorize")
	def test_write_to_sheet(self, mock_authorize, mock_client):
		mock_client_instance = mock_client.return_value
		mock_authorize.return_value = mock_client_instance
		mock_spreadsheet = mock_client_instance.open_by_key.return_value
		
		data = [["Test Write", "Value"]]
		result = service.write_to_sheet("A1:B2", data)
		self.assertIsNotNone(result)
		mock_spreadsheet.values_update.assert_called_once_with(
			"A1:B2",
			params={'valueInputOption': 'RAW'},
			body={'values': data}
		)
