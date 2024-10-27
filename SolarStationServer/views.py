import datetime
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework_api_key.permissions import HasAPIKey
from inverter_db.models import InverterData  # InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors
import json
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


def calculate_full_value(high, low):
    return (high[0] + low[0])*2


from .serializers import (
    DataCollectorSerializer,
    InverterDataSerializer,
    InverterAccumulatedDataSerializer,
    InverterBaseConfigSerializer,
    InverterParamStateSerializer,
    InverterErrorsSerializer
)


@swagger_auto_schema(
    method='post',
    request_body=DataCollectorSerializer,
    responses={
        status.HTTP_201_CREATED: 'Data saved successfully',
        status.HTTP_400_BAD_REQUEST: 'Invalid data',
    }
)
@api_view(['POST'])
@permission_classes([HasAPIKey])
# def data_collector(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             avg_inv_data = data['avg_inv_data']
#             iad = data['inverters_accumulated_data']
#             inverters_base_config = data['inverters_base_config']
#             inverters_param_states = data['inverters_param_states']
#             inverters_errors = data['inverters_errors']
#             timestamp = timezone.now()
#             if len(avg_inv_data.keys()) > 0:
#                 inverter_data = InverterData(
#                     timestamp=timestamp,
#                     battery_voltage=avg_inv_data['Battery voltage'],
#                     inverter_voltage=avg_inv_data['Inverter voltage'],
#                     grid_voltage=avg_inv_data['Grid voltage'],
#                     bus_voltage=avg_inv_data['BUS voltage'],
#                     control_current=avg_inv_data['Control current']*2,
#                     inverter_current=avg_inv_data['Inverter current']*2,
#                     grid_current=avg_inv_data['Grid current']*2,
#                     load_current=avg_inv_data['Load current']*2,
#                     p_inverter=avg_inv_data['PInverter']*2,
#                     p_grid=avg_inv_data['PGrid']*2,
#                     p_load=avg_inv_data['PLoad']*2,
#                     load_percent=avg_inv_data['Load percent'],
#                     s_inverter=avg_inv_data['SInverter']*2,
#                     s_grid=avg_inv_data['SGrid']*2,
#                     s_load=avg_inv_data['Sload']*2,
#                     q_inverter=avg_inv_data['Qinverter']*2,
#                     q_grid=avg_inv_data['Qgrid']*2,
#                     q_load=avg_inv_data['Qload']*2,
#                     inverter_frequency=avg_inv_data['Inverter frequency'],
#                     grid_frequency=avg_inv_data['Grid frequency'],
#                     ac_radiator_temperature=avg_inv_data['AC radiator temperature'],
#                     transformer_temperature=avg_inv_data['Transformer temperature'],
#                     dc_radiator_temperature=avg_inv_data['DC radiator temperature'],
#                     # batt_power=avg_inv_data['Batt power']*2,
#                     # batt_current=avg_inv_data['Batt current']*2,
#                     pv_voltage=avg_inv_data['PV voltage'],
#                     charger_current=round(avg_inv_data['Charger current']*1.75, 2),
#                     charger_power=round(avg_inv_data['Charger power']*1.75, 2),
#                 )
#                 inverter_data.save()
#
#
#             if len(iad.keys()) > 0:
#                 accumulated_data = InverterAccumulatedData(
#                     timestamp=timestamp,
#                     accumulated_charger_power=calculate_full_value(iad['Accumulated charger power high'], iad['Accumulated charger power low']),
#                     accumulated_discharger_power=calculate_full_value(iad['Accumulated discharger power high'], iad['Accumulated discharger power low']),
#                     accumulated_buy_power=calculate_full_value(iad['Accumulated buy power high'], iad['Accumulated buy power low']),
#                     accumulated_sell_power=calculate_full_value(iad['Accumulated sell power high'], iad['Accumulated sell power low']),
#                     accumulated_load_power=calculate_full_value(iad['Accumulated load power high'], iad['Accumulated load power low']),
#                     accumulated_self_use_power=calculate_full_value(iad['Accumulated self_use power high'], iad['Accumulated self_use power low']),
#                     accumulated_pv_sell_power=calculate_full_value(iad['Accumulated PV_sell power high'], iad['Accumulated PV_sell power low']),
#                     accumulated_grid_charger_power=calculate_full_value(iad['Accumulated grid_charger power high'], iad['Accumulated  grid_charger power low']),
#                     accumulated_pv_power=calculate_full_value(iad['Accumulated PV power high'], iad['Accumulated PV power low']),
#                     accumulated_day=iad['Accumulated day'][0],
#                     accumulated_hour=iad['Accumulated hour'][0],
#                     accumulated_minute=iad['Accumulated minute'][0],
#                 )
#                 accumulated_data.save()
#             if len(inverters_base_config.keys()) > 0:
#                 base_config = InverterBaseConfig(
#                     timestamp=timestamp,
#                     ac_voltage_grade=inverters_base_config['AC voltage grade'][0],
#                     rated_power_va=inverters_base_config['Rated power(VA)'][0],
#                     batt_voltage_grade=inverters_base_config['Batt voltage grade'][0],
#                     rated_power_w=inverters_base_config['Rated power(W)'][0],
#                     battvol_grade=inverters_base_config['BattVol Grade'][0],
#                     rated_current_a=inverters_base_config['Rated Current'][0]
#                 )
#                 base_config.save()
#             if len(inverters_param_states.keys()) > 0:
#                 param_state = InverterParamState(
#                     timestamp=timestamp,
#                     work_state=inverters_param_states['work state'],
#                     inverter_relay_state=inverters_param_states['Inverter relay state'],
#                     grid_relay_state=inverters_param_states['Grid relay state'],
#                     load_relay_state=inverters_param_states['Load relay state'],
#                     n_line_relay_state=inverters_param_states['N_Line relay state'],
#                     dc_relay_state=inverters_param_states['DC relay state'],
#                     earth_relay_state=inverters_param_states['Earth relay state'],
#                     charger_work_state=inverters_param_states['Charger workstate'],
#                     mppt_state=inverters_param_states['Mppt state'],
#                     charging_state=inverters_param_states['charging state'],
#                 )
#                 param_state.save()
#             if len(inverters_errors.keys()) > 0:
#                 inverter_error = InverterErrors(
#                     timestamp=timestamp,
#                     error_message_1=inverters_errors['Error message 1'],
#                     error_message_2=inverters_errors['Error message 2'],
#                     error_message_3=inverters_errors['Error message 3'],
#                     warning_message_1=inverters_errors['Warning message 1'],
#                     warning_message_2=inverters_errors['Warning message 2'],
#                     charger_error_message=inverters_errors['Error message, Refer to frame Charger Error message 1'],
#                     charger_warning_message=inverters_errors['Warning message, Refer to frame Charger Warning message 1']
#                 )
#                 inverter_error.save()
#
#
#             return JsonResponse({'status': 'success', 'message': 'Data saved successfully'}, status=201)
#
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
def data_collector(request):
    serializer = DataCollectorSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        
        # Збереження avg_inv_data в InverterData
        inverter_data_serializer = InverterDataSerializer(data=data['avg_inv_data'])
        if inverter_data_serializer.is_valid():
            inverter_data_serializer.save()
        
        # Збереження inverters_accumulated_data в InverterAccumulatedData
        accumulated_data_serializer = InverterAccumulatedDataSerializer(data=data['inverters_accumulated_data'])
        if accumulated_data_serializer.is_valid():
            accumulated_data_serializer.save()
        
        # Збереження inverters_base_config в InverterBaseConfig
        base_config_serializer = InverterBaseConfigSerializer(data=data['inverters_base_config'])
        if base_config_serializer.is_valid():
            base_config_serializer.save()
        
        # Збереження inverters_param_states в InverterParamState
        param_state_serializer = InverterParamStateSerializer(data=data['inverters_param_states'])
        if param_state_serializer.is_valid():
            param_state_serializer.save()
        
        # Збереження inverters_errors в InverterErrors
        errors_serializer = InverterErrorsSerializer(data=data['inverters_errors'])
        if errors_serializer.is_valid():
            errors_serializer.save()
        
        return JsonResponse({'status': 'success', 'message': 'Data saved successfully'}, status=201)
    
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_current_data(request):
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            
            field_filter = request.GET.get('field_filter', None)
            
            seven_days_ago = timezone.now() - datetime.timedelta(days=7)
            
            data_query = InverterData.objects.filter(timestamp__gte=seven_days_ago)
            
            if field_filter:
                data_query = data_query.filter(field_name=field_filter)
            
            data_query = data_query.order_by('-timestamp')
            
            start = (page - 1) * page_size
            end = start + page_size
            data_paginated = data_query[start:end]
            
            data_list = list(data_paginated.values())
            
            return JsonResponse({'status': 'success', 'data': data_list}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)