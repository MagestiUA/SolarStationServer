from django.contrib.admin.sites import site
from django.test import TestCase
from inverter_db.models import (
    InverterData,
    InverterAccumulatedData,
    InverterBaseConfig,
    InverterParamState,
    InverterErrors,
)

class AdminTestCase(TestCase):
    def test_inverter_data_in_admin(self):
        self.assertIn(InverterData, site._registry)

    def test_inverter_accumulated_data_in_admin(self):
        self.assertIn(InverterAccumulatedData, site._registry)

    def test_inverter_base_config_in_admin(self):
        self.assertIn(InverterBaseConfig, site._registry)

    def test_inverter_param_state_in_admin(self):
        self.assertIn(InverterParamState, site._registry)

    def test_inverter_errors_in_admin(self):
        self.assertIn(InverterErrors, site._registry)
