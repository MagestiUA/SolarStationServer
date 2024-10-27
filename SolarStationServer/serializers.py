from rest_framework import serializers
from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors
from django.utils import timezone

class BaseSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(required=False)

    def validate_timestamp(self, value):
        """Встановлює поточний час, якщо поле timestamp відсутнє."""
        return value or timezone.now()

class InverterDataSerializer(BaseSerializer):
    class Meta:
        model = InverterData
        fields = '__all__'

class InverterAccumulatedDataSerializer(BaseSerializer):
    class Meta:
        model = InverterAccumulatedData
        fields = '__all__'

class InverterBaseConfigSerializer(BaseSerializer):
    class Meta:
        model = InverterBaseConfig
        fields = '__all__'

class InverterParamStateSerializer(BaseSerializer):
    class Meta:
        model = InverterParamState
        fields = '__all__'

class InverterErrorsSerializer(BaseSerializer):
    class Meta:
        model = InverterErrors
        fields = '__all__'

class DataCollectorSerializer(serializers.Serializer):
    avg_inv_data = InverterDataSerializer(required=True)
    inverters_accumulated_data = InverterAccumulatedDataSerializer(required=True)
    inverters_base_config = InverterBaseConfigSerializer(required=True)
    inverters_param_states = InverterParamStateSerializer(required=True)
    inverters_errors = InverterErrorsSerializer(required=True)
