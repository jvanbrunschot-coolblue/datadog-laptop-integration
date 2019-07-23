import pytest
import mock

@pytest.fixture(scope='session')
def dd_environment():
    yield


@pytest.fixture
def instance():
    return {}


class SensorsBattery(object):
    percent = 20

@pytest.fixture
def psutil_mocks():
    with mock.patch('psutil.sensors_battery', return_value=SensorsBattery()):
        yield
