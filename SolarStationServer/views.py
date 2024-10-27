import datetime
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework_api_key.permissions import HasAPIKey
from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors
import json
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


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