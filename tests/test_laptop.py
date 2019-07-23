from datadog_checks.laptop import LaptopCheck
import pytest


@pytest.mark.usefixtures('psutil_mocks')
def test_check(aggregator, instance):
    check = LaptopCheck('laptop', {}, {})
    check.check(instance)

    aggregator.assert_metric(
        'laptop.battery_percentage', value=20, tags=[])
    aggregator.assert_service_check('laptop.health', LaptopCheck.OK)

    aggregator.assert_all_metrics_covered()
