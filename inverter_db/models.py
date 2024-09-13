from django.db import models


class InverterData(models.Model):
    timestamp = models.DateTimeField(primary_key=True)  # Часова мітка як первинний ключ
    battery_voltage = models.FloatField()  # Напруга батареї
    inverter_voltage = models.FloatField()  # Напруга інвертора
    grid_voltage = models.FloatField()  # Напруга мережі
    bus_voltage = models.FloatField()  # Напруга шини
    control_current = models.FloatField()  # Струм управління
    inverter_current = models.FloatField()  # Струм інвертора
    grid_current = models.FloatField()  # Струм мережі
    load_current = models.FloatField()  # Струм навантаження
    p_inverter = models.FloatField()  # Потужність інвертора (W)
    p_grid = models.FloatField()  # Потужність мережі (W)
    p_load = models.FloatField()  # Потужність навантаження (W)
    load_percent = models.FloatField()  # Процент навантаження
    s_inverter = models.FloatField()  # Очікувана потужність інвертора (VA)
    s_grid = models.FloatField()  # Очікувана потужність мережі (VA)
    s_load = models.FloatField()  # Очікувана потужність навантаження (VA)
    q_inverter = models.FloatField()  # Реактивна потужність інвертора (var)
    q_grid = models.FloatField()  # Реактивна потужність мережі (var)
    q_load = models.FloatField()  # Реактивна потужність навантаження (var)
    inverter_frequency = models.FloatField()  # Частота інвертора (Hz)
    grid_frequency = models.FloatField()  # Частота мережі (Hz)
    ac_radiator_temperature = models.FloatField()  # Температура AC радіатора
    transformer_temperature = models.FloatField()  # Температура трансформатора
    dc_radiator_temperature = models.FloatField()  # Температура DC радіатора
    batt_power = models.FloatField()  # Потужність батареї (W)
    batt_current = models.FloatField()  # Струм батареї (A)
    pv_voltage = models.FloatField()  # Напруга PV (сонячна батарея)
    charger_current = models.FloatField()  # Струм зарядного пристрою
    charger_power = models.FloatField()  # Потужність зарядного пристрою (W)

    def __str__(self):
        return f"Inverter data at {self.timestamp}"

#'inverters_accumulated_data': {'Accumulated charger power high': (0, 'KWH'), 'Accumulated charger power low': (0.0, 'KWH'), 'Accumulated discharger power high': (0, 'KWH'), 'Accumulated discharger power low': (0.7, 'KWH'), 'Accumulated buy power high': (0, 'KWH'), 'Accumulated buy power low': (0.0, 'KWH'), 'Accumulated sell power high': (0, 'KWH'), 'Accumulated sell power low': (0.0, 'KWH'), 'Accumulated load power high': (0, 'KWH'), 'Accumulated load power low': (0.6, 'KWH'), 'Accumulated self_use power high': (0, 'KWH'), 'Accumulated self_use power low': (0.7, 'KWH'), 'Accumulated PV_sell power high': (0, 'KWH'), 'Accumulated PV_sell power low': (0.0, 'KWH'), 'Accumulated grid_charger power high': (0, 'KWH'), 'Accumulated  grid_charger power low': (0.0, 'KWH'), 'Accumulated PV power high': (0, 'KWH'), 'Accumulated PV power low': (0.0, 'KWH'), 'Accumulated day': (175, 'day'), 'Accumulated hour': (2, 'hour'), 'Accumulated minute': (1, 'minute')}

class InverterAccumulatedData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Часова мітка
    accumulated_charger_power = models.FloatField()  # Скільки енергії інвертор "залив" у батарею в KWH
    accumulated_discharger_power = models.FloatField()  # Скільки енергії було витрачено з батареї в KWH
    accumulated_buy_power = models.FloatField()  # Скільки енергії інвертор взяв із мережі в KWH
    accumulated_sell_power = models.FloatField()  # Скільки енергії інвертор передав (продав) у загальну електричну мережу в KWH
    accumulated_load_power = models.FloatField()  # Скільки енергії спожили всі пристрої в будинку в KWH (скільки витратили кВт*год)
    accumulated_self_use_power = models.FloatField()  # Скільки енергії використали інвертори та батареї своєї роботи в KWH
    accumulated_pv_sell_power = models.FloatField()  # Скільки сонячної енергії було передано в мережу в KWH
    accumulated_grid_charger_power = models.FloatField()  # Скільки енергії інвертор використав із мережі для зарядки батареї в KWH
    accumulated_pv_power = models.FloatField()  # загальна кількість енергії, виробленої сонячними панелями (PV), яка була збережена в батареї в KWH
    accumulated_day = models.IntegerField()  # Кількість днів накопичення
    accumulated_hour = models.IntegerField()  # Кількість годин накопичення
    accumulated_minute = models.IntegerField()  # Кількість хвилин накопичення

    def __str__(self):
        return f"Accumulated inverter data at {self.timestamp}"

#'inverters_base_config': {'AC voltage grade': (230, 'V'), 'Rated power(VA)': (5000, 'VA'), 'Batt voltage grade': (48, 'V'), 'Rated power(W)': (5000, 'W'), 'BattVol Grade': (48, 'V'), 'Rated Current': (80.0, 'A')}

class InverterBaseConfig(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Часова мітка
    ac_voltage_grade = models.FloatField()  # Напруга змінного струму
    rated_power_va = models.FloatField()  # Номінальна потужність (ВА)
    batt_voltage_grade = models.FloatField()  # Клас напруги батареї (В)
    rated_power_w = models.FloatField()  # Номінальна потужність (Вт)
    battvol_grade = models.FloatField()  # Клас напруги батареї (В)
    rated_current_a = models.FloatField()  # Номінальний струм (А)

    def __str__(self):
        return f"Base Config at {self.timestamp}"

#'inverters_param_states': {'work state': 'OffGrid', 'Inverter relay state': 'Connect', 'Grid relay state': 'Disconnect', 'Load relay state': 'Connect', 'N_Line relay state': 'Disconnect', 'DC relay state': 'Connect', 'Earth relay state': 'Disconnect', 'Charger workstate': 'Initialization mode', 'Mppt state': 'Stop', 'charging state': 'Stop'},

class InverterParamState(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Часова мітка
    work_state = models.CharField(max_length=50)  # Стан роботи (напр., PowerOn, SelfTest тощо)
    inverter_relay_state = models.CharField(max_length=50)  # Стан реле інвертора
    grid_relay_state = models.CharField(max_length=50)  # Стан реле мережі
    load_relay_state = models.CharField(max_length=50)  # Стан реле навантаження
    n_line_relay_state = models.CharField(max_length=50)  # Стан реле N лінії
    dc_relay_state = models.CharField(max_length=50)  # Стан реле постійного струму
    earth_relay_state = models.CharField(max_length=50)  # Стан реле заземлення
    charger_workstate = models.CharField(max_length=50)  # Стан роботи зарядного пристрою
    mppt_state = models.CharField(max_length=50)  # Стан MPPT (контролер заряду)
    charging_state = models.CharField(max_length=50)  # Стан заряду батареї

    def __str__(self):
        return f"Param State at {self.timestamp}"


#'inverters_errors': {'Error message 1': 0, 'Error message 2': 0, 'Error message 3': 0, 'Warning message 1': 0, 'Warning message 2': 0, 'Error message, Refer to frame Charger Error message 1': 0, 'Warning message, Refer to frame Charger Warning message 1': 0}}

class InverterError(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Часова мітка
    error_message_1 = models.TextField(blank=True, null=True)  # Повідомлення про помилку 1
    error_message_2 = models.TextField(blank=True, null=True)  # Повідомлення про помилку 2
    error_message_3 = models.TextField(blank=True, null=True)  # Повідомлення про помилку 3
    warning_message_1 = models.TextField(blank=True, null=True)  # Попередження 1
    warning_message_2 = models.TextField(blank=True, null=True)  # Попередження 2
    charger_error_message = models.TextField(blank=True, null=True)  # Помилка зарядного пристрою
    charger_warning_message = models.TextField(blank=True, null=True)  # Попередження зарядного пристрою

    def __str__(self):
        return f"Error at {self.timestamp}"