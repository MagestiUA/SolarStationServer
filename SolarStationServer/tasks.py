from celery import shared_task
from google_sheets.service import write_to_sheet
from telegram.telegram_bot import send_telegram_message
from inverter_db.models import InverterData


@shared_task
def update_battery_voltage():
	latest_data = InverterData.objects.order_by('-timestamp').first()
	if latest_data:
		battery_voltage = latest_data.battery_voltage
		range = "BatteryVoltage!B1"
		write_to_sheet(range, [[str(battery_voltage)]])
		send_telegram_message(user_id=710346358, message=f"Поточна напруга батареї: {battery_voltage} В")

@shared_task
def send_battery_voltage(user_id):
	latest_data = InverterData.objects.order_by('-timestamp').first()
	if latest_data:
		battery_voltage = latest_data.battery_voltage
		send_telegram_message(user_id=user_id, message=f"Поточна напруга батареї: {battery_voltage} В")