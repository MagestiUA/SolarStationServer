from django.contrib import admin
from .models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors

# Налаштування для InverterData
@admin.register(InverterData)
class InverterDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'battery_voltage', 'inverter_voltage', 'load_percent', 's_load', 'pv_voltage', 'charger_current', 'charger_power', )
    list_filter = ('timestamp', 'battery_voltage', 'inverter_voltage', 'grid_voltage')

# Налаштування для InverterAccumulatedData
@admin.register(InverterAccumulatedData)
class InverterAccumulatedDataAdmin(admin.ModelAdmin):
    list_display = ('accumulated_charger_power', 'accumulated_discharger_power', 'accumulated_buy_power', 'timestamp')
    list_filter = ('timestamp',)

# Налаштування для InverterBaseConfig
@admin.register(InverterBaseConfig)
class InverterBaseConfigAdmin(admin.ModelAdmin):
    list_display = ('ac_voltage_grade', 'rated_power_va', 'batt_voltage_grade', 'timestamp')
    list_filter = ('ac_voltage_grade', 'rated_power_va', 'timestamp', )

# Налаштування для InverterParamState
@admin.register(InverterParamState)
class InverterParamStateAdmin(admin.ModelAdmin):
    list_display = ('work_state', 'inverter_relay_state', 'grid_relay_state', 'timestamp', )
    list_filter = ('work_state', 'inverter_relay_state', 'grid_relay_state', 'timestamp', )

# Налаштування для InverterError
@admin.register(InverterErrors)
class InverterErrorsAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'error_message_1', 'warning_message_1')
    list_filter = ('timestamp', 'error_message_1', 'warning_message_1')
