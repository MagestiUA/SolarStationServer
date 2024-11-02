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
    pv_voltage = models.FloatField()  # Напруга PV (сонячна батарея)
    charger_current = models.FloatField()  # Струм зарядного пристрою
    charger_power = models.FloatField()  # Потужність зарядного пристрою (W)

    def __str__(self):
        return f"Inverter data at {self.timestamp}"
    
    class Meta:
        verbose_name = "Inverter Current Data"
        verbose_name_plural = "Inverter Current Data History"

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
    
    class Meta:
        verbose_name = "Inverter Accumulated Data"
        verbose_name_plural = "Inverter Accumulated History"


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
    
    class Meta:
        verbose_name = "Inverter Base Config"  # Назва в однині
        verbose_name_plural = "Inverter Base Config History"  # Назва у множині


class InverterParamState(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Часова мітка
    work_state = models.CharField(max_length=50)  # Стан роботи (напр., PowerOn, SelfTest тощо)
    inverter_relay_state = models.CharField(max_length=50)  # Стан реле інвертора
    grid_relay_state = models.CharField(max_length=50)  # Стан реле мережі
    load_relay_state = models.CharField(max_length=50)  # Стан реле навантаження
    n_line_relay_state = models.CharField(max_length=50)  # Стан реле N лінії
    dc_relay_state = models.CharField(max_length=50)  # Стан реле постійного струму
    earth_relay_state = models.CharField(max_length=50)  # Стан реле заземлення
    charger_work_state = models.CharField(max_length=50)  # Стан роботи зарядного пристрою
    mppt_state = models.CharField(max_length=50)  # Стан MPPT (контролер заряду)
    charging_state = models.CharField(max_length=50)  # Стан заряду батареї

    def __str__(self):
        return f"Param State at {self.timestamp}"
    
    class Meta:
        verbose_name = "Inverter Current Systems State"
        verbose_name_plural = "Inverter Current Systems State History"


class InverterErrors(models.Model):
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
    
    class Meta:
        verbose_name = "Inverter Current Errors"
        verbose_name_plural = "Inverter Errors History"
        