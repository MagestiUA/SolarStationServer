from django.contrib import admin
from .models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterError

# Налаштування для InverterData
@admin.register(InverterData)
class InverterDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'battery_voltage', 'inverter_voltage', 'grid_voltage', 'load_percent')
    list_filter = ('timestamp', 'battery_voltage', 'inverter_voltage', 'grid_voltage')

# Налаштування для InverterAccumulatedData
@admin.register(InverterAccumulatedData)
class InverterAccumulatedDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'accumulated_charger_power', 'accumulated_discharger_power', 'accumulated_buy_power')
    list_filter = ('timestamp',)

# Налаштування для InverterBaseConfig
@admin.register(InverterBaseConfig)
class InverterBaseConfigAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ac_voltage_grade', 'rated_power_va', 'batt_voltage_grade')
    list_filter = ('timestamp', 'ac_voltage_grade', 'rated_power_va')

# Налаштування для InverterParamState
@admin.register(InverterParamState)
class InverterParamStateAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'work_state', 'inverter_relay_state', 'grid_relay_state')
    list_filter = ('timestamp', 'work_state', 'inverter_relay_state', 'grid_relay_state')

# Налаштування для InverterError
@admin.register(InverterError)
class InverterErrorAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'error_message_1', 'warning_message_1')
    list_filter = ('timestamp', 'error_message_1', 'warning_message_1')
