from rest_framework import serializers
from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors
from django.utils import timezone

def calculate_full_value(high, low):
    return (high[0] + low[0])*2

class BaseSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(required=False)

    def validate_timestamp(self, value):
        """Встановлює поточний час, якщо поле timestamp відсутнє."""
        return value or timezone.now()

class InverterDataSerializer(BaseSerializer):
    class Meta:
        model = InverterData
        fields = '__all__'
    
    def to_internal_value(self, data):
        # Перевизначення назв параметрів
        data = {
            'battery_voltage': data.get('Battery voltage'),
            'inverter_voltage': data.get('Inverter voltage'),
            'grid_voltage': data.get('Grid voltage'),
            'bus_voltage': data.get('BUS voltage'),
            'control_current': data.get('Control current') * 2 if data.get('Control current') else 0,
            'inverter_current': data.get('Inverter current') * 2 if data.get('Inverter current') else 0,
            'grid_current': data.get('Grid current') * 2 if data.get('Grid current') else 0,
            'load_current': data.get('Load current') * 2 if data.get('Load current') else 0,
            'p_inverter': data.get('PInverter') * 2 if data.get('PInverter') else 0,
            'p_grid': data.get('PGrid') * 2 if data.get('PGrid') else 0,
            'p_load': data.get('PLoad') * 2 if data.get('PLoad') else 0,
            'load_percent': data.get('Load percent'),
            's_inverter': data.get('SInverter') * 2 if data.get('SInverter') else 0,
            's_grid': data.get('SGrid') * 2 if data.get('SGrid') else 0,
            's_load': data.get('Sload') * 2 if data.get('Sload') else 0,
            'q_inverter': data.get('Qinverter') * 2 if data.get('Qinverter') else 0,
            'q_grid': data.get('Qgrid') * 2 if data.get('Qgrid') else 0,
            'q_load': data.get('Qload') * 2 if data.get('Qload') else 0,
            'inverter_frequency': data.get('Inverter frequency'),
            'grid_frequency': data.get('Grid frequency'),
            'ac_radiator_temperature': data.get('AC radiator temperature'),
            'transformer_temperature': data.get('Transformer temperature'),
            'dc_radiator_temperature': data.get('DC radiator temperature'),
            'pv_voltage': data.get('PV voltage'),
            'charger_current': round(data.get('Charger current') * 1.75, 2) if data.get('Charger current') else 0,
            'charger_power': round(data.get('Charger power') * 1.75, 2) if data.get('Charger power') else 0,
        }
        return super().to_internal_value(data)
    
class InverterAccumulatedDataSerializer(BaseSerializer):
    class Meta:
        model = InverterAccumulatedData
        fields = '__all__'
    
    def to_internal_value(self, data):
        data = {
            'accumulated_charger_power': calculate_full_value(
                data.get('Accumulated charger power high'), data.get('Accumulated charger power low')
            ),
            'accumulated_discharger_power': calculate_full_value(
                data.get('Accumulated discharger power high'), data.get('Accumulated discharger power low')
            ),
            'accumulated_buy_power': calculate_full_value(
                data.get('Accumulated buy power high'), data.get('Accumulated buy power low')
            ),
            'accumulated_sell_power': calculate_full_value(
                data.get('Accumulated sell power high'), data.get('Accumulated sell power low')
            ),
            'accumulated_load_power': calculate_full_value(
                data.get('Accumulated load power high'), data.get('Accumulated load power low')
            ),
            'accumulated_self_use_power': calculate_full_value(
                data.get('Accumulated self_use power high'), data.get('Accumulated self_use power low')
            ),
            'accumulated_pv_sell_power': calculate_full_value(
                data.get('Accumulated PV_sell power high'), data.get('Accumulated PV_sell power low')
            ),
            'accumulated_grid_charger_power': calculate_full_value(
                data.get('Accumulated grid_charger power high'), data.get('Accumulated grid_charger power low')
            ),
            'accumulated_pv_power': calculate_full_value(
                data.get('Accumulated PV power high'), data.get('Accumulated PV power low')
            ),
            'accumulated_day': data.get('Accumulated day')[0] if data.get('Accumulated day') else 0,
            'accumulated_hour': data.get('Accumulated hour')[0] if data.get('Accumulated hour') else 0,
            'accumulated_minute': data.get('Accumulated minute')[0] if data.get('Accumulated minute') else 0,
        }
        return super().to_internal_value(data)
    
class InverterBaseConfigSerializer(BaseSerializer):
    class Meta:
        model = InverterBaseConfig
        fields = '__all__'
    
    def to_internal_value(self, data):
        data = {
            'ac_voltage_grade': data.get('AC voltage grade')[0] if data.get('AC voltage grade') else 0,
            'rated_power_va': data.get('Rated power(VA)')[0] if data.get('Rated power(VA)') else 0,
            'batt_voltage_grade': data.get('Batt voltage grade')[0] if data.get('Batt voltage grade') else 0,
            'rated_power_w': data.get('Rated power(W)')[0] if data.get('Rated power(W)') else 0,
            'battvol_grade': data.get('BattVol Grade')[0] if data.get('BattVol Grade') else 0,
            'rated_current_a': data.get('Rated Current')[0] if data.get('Rated Current') else 0,
        }
        return super().to_internal_value(data)


class InverterParamStateSerializer(BaseSerializer):
    class Meta:
        model = InverterParamState
        fields = '__all__'
    
    def to_internal_value(self, data):
        data = {
            'work_state': data.get('work state'),
            'inverter_relay_state': data.get('Inverter relay state'),
            'grid_relay_state': data.get('Grid relay state'),
            'load_relay_state': data.get('Load relay state'),
            'n_line_relay_state': data.get('N_Line relay state'),
            'dc_relay_state': data.get('DC relay state'),
            'earth_relay_state': data.get('Earth relay state'),
            'charger_work_state': data.get('Charger workstate'),
            'mppt_state': data.get('Mppt state'),
            'charging_state': data.get('charging state'),
        }
        return super().to_internal_value(data)


class InverterErrorsSerializer(BaseSerializer):
    class Meta:
        model = InverterErrors
        fields = '__all__'
    
    def to_internal_value(self, data):
        data = {
            'error_message_1': data.get('Error message 1'),
            'error_message_2': data.get('Error message 2'),
            'error_message_3': data.get('Error message 3'),
            'warning_message_1': data.get('Warning message 1'),
            'warning_message_2': data.get('Warning message 2'),
            'charger_error_message': data.get('Error message, Refer to frame Charger Error message 1'),
            'charger_warning_message': data.get('Warning message, Refer to frame Charger Warning message 1'),
        }
        return super().to_internal_value(data)


class DataCollectorSerializer(serializers.Serializer):
    avg_inv_data = InverterDataSerializer(required=True)
    inverters_accumulated_data = InverterAccumulatedDataSerializer(required=True)
    inverters_base_config = InverterBaseConfigSerializer(required=True)
    inverters_param_states = InverterParamStateSerializer(required=True)
    inverters_errors = InverterErrorsSerializer(required=True)
