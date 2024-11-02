import json
import os
from pathlib import Path
import environ
import gspread
from oauth2client.service_account import ServiceAccountCredentials


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

google_sheets_auth = json.loads(env("GOOGLE_SHEETS_AUTH"))
google_sheets_auth['private_key'] = google_sheets_auth['private_key'].replace("\\n", "\n")
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_sheets_auth, scope)
SPREADSHEET_ID = env("SPREADSHEET_ID")

def get_google_sheets_client():
    return gspread.authorize(credentials)


def read_from_sheet(range):
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    return spreadsheet.values_get(range)


def write_to_sheet(range, data):
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    return spreadsheet.values_update(
        range,
        params={'valueInputOption': 'RAW'},
        body={'values': data}
    )


if __name__ == "__main__":
    print(read_from_sheet("A1:B2"))