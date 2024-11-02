from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from telegram.telegram_bot import send_telegram_message
from SolarStationServer.tasks import send_battery_voltage


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def telegram(request: Request):
    data = request.data
    chat_id = data['message']['chat']['id']
    if data['message']['text'] == ' ':
        send_battery_voltage.delay(user_id=chat_id)
        return Response('OK!')
    text = 'I listens to you! ' + data['message']['text']
    send_telegram_message(chat_id, text)
    return Response('OK!')