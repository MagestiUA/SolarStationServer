from rest_framework import serializers
from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors

class InverterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterData
        fields = '__all__'

class InverterAccumulatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterAccumulatedData
        fields = '__all__'

class InverterBaseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterBaseConfig
        fields = '__all__'

class InverterParamStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterParamState
        fields = '__all__'

class InverterErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterErrors
        fields = '__all__'

class DataCollectorSerializer(serializers.Serializer):
    avg_inv_data = InverterDataSerializer(required=True)
    inverters_accumulated_data = InverterAccumulatedDataSerializer(required=True)
    inverters_base_config = InverterBaseConfigSerializer(required=True)
    inverters_param_states = InverterParamStateSerializer(required=True)
    inverters_errors = InverterErrorsSerializer(required=True)
