from django.test import TestCase
from inverter_db.models import InverterData, InverterAccumulatedData, InverterBaseConfig, InverterParamState, InverterErrors

class InverterDataModelTest(TestCase):
    def setUp(self):
        self.inverter_data = InverterData.objects.create(
            timestamp="2024-01-01T12:00:00Z",
            battery_voltage=48.5,
            inverter_voltage=230.0,
            grid_voltage=230.0,
            bus_voltage=48.5,
            control_current=10.0,
            inverter_current=5.0,
            grid_current=2.5,
            load_current=4.0,
            p_inverter=500.0,
            p_grid=100.0,
            p_load=400.0,
            load_percent=80.0,
            s_inverter=550.0,
            s_grid=110.0,
            s_load=450.0,
            q_inverter=50.0,
            q_grid=10.0,
            q_load=40.0,
            inverter_frequency=50.0,
            grid_frequency=50.0,
            ac_radiator_temperature=30.0,
            transformer_temperature=25.0,
            dc_radiator_temperature=28.0,
            pv_voltage=300.0,
            charger_current=12.0,
            charger_power=360.0
        )
    
    def test_inverter_data_creation(self):
        self.assertIsInstance(self.inverter_data, InverterData)
        self.assertIn("Inverter data at 2024-01-01", str(self.inverter_data))

