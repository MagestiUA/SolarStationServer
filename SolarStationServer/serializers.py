# from rest_framework import serializers
# from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors
# from django.utils import timezone
#
# def calculate_full_value(high, low):
#     if not high or not low:
#         return 0
#     return (high[0] + low[0])*2
#
#
# class BaseSerializer(serializers.ModelSerializer):
#     def to_internal_value(self, data):
#         if 'timestamp' not in data or not data['timestamp']:
#             data['timestamp'] = timezone.now()
#
#         return super().to_internal_value(data)
#
# class InverterDataSerializer(BaseSerializer):
#     class Meta:
#         model = InverterData
#         fields = '__all__'
#
#     def to_internal_value(self, data):
#         # Перевизначення назв параметрів
#         data = {
#             'battery_voltage': data.get('Battery voltage') if data.get('Battery voltage') else 0,
#             'inverter_voltage': data.get('Inverter voltage') if data.get('Inverter voltage') else 0,
#             'grid_voltage': data.get('Grid voltage') if data.get('Grid voltage') else 0,
#             'bus_voltage': data.get('BUS voltage') if data.get('BUS voltage') else 0,
#             'control_current': data.get('Control current') * 2 if data.get('Control current') else 0,
#             'inverter_current': data.get('Inverter current') * 2 if data.get('Inverter current') else 0,
#             'grid_current': data.get('Grid current') * 2 if data.get('Grid current') else 0,
#             'load_current': data.get('Load current') * 2 if data.get('Load current') else 0,
#             'p_inverter': data.get('PInverter') * 2 if data.get('PInverter') else 0,
#             'p_grid': data.get('PGrid') * 2 if data.get('PGrid') else 0,
#             'p_load': data.get('PLoad') * 2 if data.get('PLoad') else 0,
#             'load_percent': data.get('Load percent') if data.get('Load percent') else 0,
#             's_inverter': data.get('SInverter') * 2 if data.get('SInverter') else 0,
#             's_grid': data.get('SGrid') * 2 if data.get('SGrid') else 0,
#             's_load': data.get('Sload') * 2 if data.get('Sload') else 0,
#             'q_inverter': data.get('Qinverter') * 2 if data.get('Qinverter') else 0,
#             'q_grid': data.get('Qgrid') * 2 if data.get('Qgrid') else 0,
#             'q_load': data.get('Qload') * 2 if data.get('Qload') else 0,
#             'inverter_frequency': data.get('Inverter frequency') if data.get('Inverter frequency') else 50,
#             'grid_frequency': data.get('Grid frequency') if data.get('Grid frequency') else 50,
#             'ac_radiator_temperature': data.get('AC radiator temperature') if data.get('AC radiator temperature') else 0,
#             'transformer_temperature': data.get('Transformer temperature') if data.get('Transformer temperature') else 0,
#             'dc_radiator_temperature': data.get('DC radiator temperature') if data.get('DC radiator temperature') else 0,
#             'pv_voltage': data.get('PV voltage') if data.get('PV voltage') else 0,
#             'charger_current': round(data.get('Charger current') * 1.75, 2) if data.get('Charger current') else 0,
#             'charger_power': round(data.get('Charger power') * 1.75, 2) if data.get('Charger power') else 0,
#         }
#         return super().to_internal_value(data)
#
# class InverterAccumulatedDataSerializer(BaseSerializer):
#     class Meta:
#         model = InverterAccumulatedData
#         fields = '__all__'
#
#     def to_internal_value(self, data):
#         data = {
#             'accumulated_charger_power': calculate_full_value(
#                 data.get('Accumulated charger power high'), data.get('Accumulated charger power low')
#             ),
#             'accumulated_discharger_power': calculate_full_value(
#                 data.get('Accumulated discharger power high'), data.get('Accumulated discharger power low')
#             ),
#             'accumulated_buy_power': calculate_full_value(
#                 data.get('Accumulated buy power high'), data.get('Accumulated buy power low')
#             ),
#             'accumulated_sell_power': calculate_full_value(
#                 data.get('Accumulated sell power high'), data.get('Accumulated sell power low')
#             ),
#             'accumulated_load_power': calculate_full_value(
#                 data.get('Accumulated load power high'), data.get('Accumulated load power low')
#             ),
#             'accumulated_self_use_power': calculate_full_value(
#                 data.get('Accumulated self_use power high'), data.get('Accumulated self_use power low')
#             ),
#             'accumulated_pv_sell_power': calculate_full_value(
#                 data.get('Accumulated PV_sell power high'), data.get('Accumulated PV_sell power low')
#             ),
#             'accumulated_grid_charger_power': calculate_full_value(
#                 data.get('Accumulated grid_charger power high'), data.get('Accumulated grid_charger power low')
#             ),
#             'accumulated_pv_power': calculate_full_value(
#                 data.get('Accumulated PV power high'), data.get('Accumulated PV power low')
#             ),
#             'accumulated_day': data.get('Accumulated day')[0] if data.get('Accumulated day') else 0,
#             'accumulated_hour': data.get('Accumulated hour')[0] if data.get('Accumulated hour') else 0,
#             'accumulated_minute': data.get('Accumulated minute')[0] if data.get('Accumulated minute') else 0,
#         }
#         return super().to_internal_value(data)
#
# class InverterBaseConfigSerializer(BaseSerializer):
#     class Meta:
#         model = InverterBaseConfig
#         fields = '__all__'
#
#     def to_internal_value(self, data):
#         data = {
#             'ac_voltage_grade': data.get('AC voltage grade')[0] if data.get('AC voltage grade') else 0,
#             'rated_power_va': data.get('Rated power(VA)')[0] if data.get('Rated power(VA)') else 0,
#             'batt_voltage_grade': data.get('Batt voltage grade')[0] if data.get('Batt voltage grade') else 0,
#             'rated_power_w': data.get('Rated power(W)')[0] if data.get('Rated power(W)') else 0,
#             'battvol_grade': data.get('BattVol Grade')[0] if data.get('BattVol Grade') else 0,
#             'rated_current_a': data.get('Rated Current')[0] if data.get('Rated Current') else 0,
#         }
#         return super().to_internal_value(data)
#
#
# class InverterParamStateSerializer(BaseSerializer):
#     class Meta:
#         model = InverterParamState
#         fields = '__all__'
#
#     def to_internal_value(self, data):
#         data = {
#             'work_state': data.get('work state') if data.get('work state') else 'OffGrid',
#             'inverter_relay_state': data.get('Inverter relay state') if data.get('Inverter relay state') else 'NONE',
#             'grid_relay_state': data.get('Grid relay state') if data.get('Grid relay state') else 'NONE',
#             'load_relay_state': data.get('Load relay state') if data.get('Load relay state') else 'NONE',
#             'n_line_relay_state': data.get('N_Line relay state') if data.get('N_Line relay state') else 'NONE',
#             'dc_relay_state': data.get('DC relay state') if data.get('DC relay state') else 'NONE',
#             'earth_relay_state': data.get('Earth relay state') if data.get('Earth relay state') else 'NONE',
#             'charger_work_state': data.get('Charger workstate') if data.get('Charger workstate') else 'OffGrid',
#             'mppt_state': data.get('Mppt state') if data.get('Mppt state') else 'OffGrid',
#             'charging_state': data.get('charging state') if data.get('charging state') else 'OffGrid',
#         }
#         return super().to_internal_value(data)
#
#
# class InverterErrorsSerializer(BaseSerializer):
#     class Meta:
#         model = InverterErrors
#         fields = '__all__'
#
#     def to_internal_value(self, data):
#         data = {
#             'error_message_1': data.get('Error message 1') if data.get('Error message 1') else 0,
#             'error_message_2': data.get('Error message 2') if data.get('Error message 2') else 0,
#             'error_message_3': data.get('Error message 3') if data.get('Error message 3') else 0,
#             'warning_message_1': data.get('Warning message 1') if data.get('Warning message 1') else 0,
#             'warning_message_2': data.get('Warning message 2') if data.get('Warning message 2') else 0,
#             'charger_error_message': data.get('Error message, Refer to frame Charger Error message 1') if data.get('Error message, Refer to frame Charger Error message 1') else 0,
#             'charger_warning_message': data.get('Warning message, Refer to frame Charger Warning message 1') if data.get('Warning message, Refer to frame Charger Warning message 1') else 0,
#         }
#         return super().to_internal_value(data)
#
#
# class DataCollectorSerializer(serializers.Serializer):
#     avg_inv_data = InverterDataSerializer(required=True)
#     inverters_accumulated_data = InverterAccumulatedDataSerializer(required=True)
#     inverters_base_config = InverterBaseConfigSerializer(required=True)
#     inverters_param_states = InverterParamStateSerializer(required=True)
#     inverters_errors = InverterErrorsSerializer(required=True)
from rest_framework import serializers
from django.utils import timezone
from inverter_db.models import (
    InverterData, InverterAccumulatedData,
    InverterBaseConfig, InverterParamState, InverterErrors
)

def calculate_full_value(high, low):
    return (high + low) * 2

class InverterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterData
        fields = '__all__'

    def to_internal_value(self, data):
        if all(key in data for key in [
            'Battery voltage', 'Inverter voltage', 'Grid voltage',
            'BUS voltage', 'Control current', 'Inverter current',
            'Grid current', 'Load current', 'PInverter', 'PGrid',
            'PLoad', 'Load percent', 'SInverter', 'SGrid', 'Sload',
            'Qinverter', 'Qgrid', 'Qload', 'Inverter frequency',
            'Grid frequency', 'AC radiator temperature',
            'Transformer temperature', 'DC radiator temperature',
            'PV voltage', 'Charger current', 'Charger power'
        ]):
            internal_data = {
                'battery_voltage': data['Battery voltage'],
                'inverter_voltage': data['Inverter voltage'],
                'grid_voltage': data['Grid voltage'],
                'bus_voltage': data['BUS voltage'],
                'control_current': data['Control current'] * 2,
                'inverter_current': data['Inverter current'] * 2,
                'grid_current': data['Grid current'] * 2,
                'load_current': data['Load current'] * 2,
                'p_inverter': data['PInverter'] * 2,
                'p_grid': data['PGrid'] * 2,
                'p_load': data['PLoad'] * 2,
                'load_percent': data['Load percent'],
                's_inverter': data['SInverter'] * 2,
                's_grid': data['SGrid'] * 2,
                's_load': data['Sload'] * 2,
                'q_inverter': data['Qinverter'] * 2,
                'q_grid': data['Qgrid'] * 2,
                'q_load': data['Qload'] * 2,
                'inverter_frequency': data['Inverter frequency'],
                'grid_frequency': data['Grid frequency'],
                'ac_radiator_temperature': data['AC radiator temperature'],
                'transformer_temperature': data['Transformer temperature'],
                'dc_radiator_temperature': data['DC radiator temperature'],
                'pv_voltage': data['PV voltage'],
                'charger_current': round(data['Charger current'] * 1.75, 2),
                'charger_power': round(data['Charger power'] * 1.75, 2),
                'timestamp': data.get('timestamp') or timezone.now(),
            }
            return super().to_internal_value(internal_data)
        raise serializers.ValidationError("Required fields are missing in 'avg_inv_data'")

class InverterAccumulatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterAccumulatedData
        fields = '__all__'

    def to_internal_value(self, data):
        if all(key in data for key in [
            'Accumulated charger power high', 'Accumulated charger power low',
            'Accumulated discharger power high', 'Accumulated discharger power low',
            'Accumulated buy power high', 'Accumulated buy power low',
            'Accumulated sell power high', 'Accumulated sell power low',
            'Accumulated load power high', 'Accumulated load power low',
            'Accumulated self_use power high', 'Accumulated self_use power low',
            'Accumulated PV_sell power high', 'Accumulated PV_sell power low',
            'Accumulated grid_charger power high', 'Accumulated grid_charger power low',
            'Accumulated PV power high', 'Accumulated PV power low',
            'Accumulated day', 'Accumulated hour', 'Accumulated minute'
        ]):
            internal_data = {
                'accumulated_charger_power': calculate_full_value(
                    data['Accumulated charger power high'],
                    data['Accumulated charger power low']
                ),
                'accumulated_discharger_power': calculate_full_value(
                    data['Accumulated discharger power high'],
                    data['Accumulated discharger power low']
                ),
                'accumulated_buy_power': calculate_full_value(
                    data['Accumulated buy power high'],
                    data['Accumulated buy power low']
                ),
                'accumulated_sell_power': calculate_full_value(
                    data['Accumulated sell power high'],
                    data['Accumulated sell power low']
                ),
                'accumulated_load_power': calculate_full_value(
                    data['Accumulated load power high'],
                    data['Accumulated load power low']
                ),
                'accumulated_self_use_power': calculate_full_value(
                    data['Accumulated self_use power high'],
                    data['Accumulated self_use power low']
                ),
                'accumulated_pv_sell_power': calculate_full_value(
                    data['Accumulated PV_sell power high'],
                    data['Accumulated PV_sell power low']
                ),
                'accumulated_grid_charger_power': calculate_full_value(
                    data['Accumulated grid_charger power high'],
                    data['Accumulated grid_charger power low']
                ),
                'accumulated_pv_power': calculate_full_value(
                    data['Accumulated PV power high'],
                    data['Accumulated PV power low']
                ),
                'accumulated_day': data['Accumulated day'][0],
                'accumulated_hour': data['Accumulated hour'][0],
                'accumulated_minute': data['Accumulated minute'][0],
                'timestamp': data.get('timestamp') or timezone.now(),
            }
            return super().to_internal_value(internal_data)
        raise serializers.ValidationError("Required fields are missing in 'inverters_accumulated_data'")

class InverterBaseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterBaseConfig
        fields = '__all__'

    def to_internal_value(self, data):
        if all(key in data for key in [
            'AC voltage grade', 'Rated power(VA)', 'Batt voltage grade',
            'Rated power(W)', 'BattVol Grade', 'Rated Current'
        ]):
            internal_data = {
                'ac_voltage_grade': data['AC voltage grade'][0],
                'rated_power_va': data['Rated power(VA)'][0],
                'batt_voltage_grade': data['Batt voltage grade'][0],
                'rated_power_w': data['Rated power(W)'][0],
                'battvol_grade': data['BattVol Grade'][0],
                'rated_current_a': data['Rated Current'][0],
                'timestamp': data.get('timestamp') or timezone.now(),
            }
            return super().to_internal_value(internal_data)
        raise serializers.ValidationError("Required fields are missing in 'inverters_base_config'")

class InverterParamStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterParamState
        fields = '__all__'

    def to_internal_value(self, data):
        if all(key in data for key in [
            'work state', 'Inverter relay state', 'Grid relay state',
            'Load relay state', 'N_Line relay state', 'DC relay state',
            'Earth relay state', 'Charger workstate', 'Mppt state', 'charging state'
        ]):
            internal_data = {
                'work_state': data['work state'],
                'inverter_relay_state': data['Inverter relay state'],
                'grid_relay_state': data['Grid relay state'],
                'load_relay_state': data['Load relay state'],
                'n_line_relay_state': data['N_Line relay state'],
                'dc_relay_state': data['DC relay state'],
                'earth_relay_state': data['Earth relay state'],
                'charger_work_state': data['Charger workstate'],
                'mppt_state': data['Mppt state'],
                'charging_state': data['charging state'],
                'timestamp': data.get('timestamp') or timezone.now(),
            }
            return super().to_internal_value(internal_data)
        raise serializers.ValidationError("Required fields are missing in 'inverters_param_states'")

class InverterErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InverterErrors
        fields = '__all__'

    def to_internal_value(self, data):
        if all(key in data for key in [
            'Error message 1', 'Error message 2', 'Error message 3',
            'Warning message 1', 'Warning message 2',
            'Error message, Refer to frame Charger Error message 1',
            'Warning message, Refer to frame Charger Warning message 1'
        ]):
            internal_data = {
                'error_message_1': data['Error message 1'],
                'error_message_2': data['Error message 2'],
                'error_message_3': data['Error message 3'],
                'warning_message_1': data['Warning message 1'],
                'warning_message_2': data['Warning message 2'],
                'charger_error_message': data['Error message, Refer to frame Charger Error message 1'],
                'charger_warning_message': data['Warning message, Refer to frame Charger Warning message 1'],
                'timestamp': data.get('timestamp') or timezone.now(),
            }
            return super().to_internal_value(internal_data)
        raise serializers.ValidationError("Required fields are missing in 'inverters_errors'")
