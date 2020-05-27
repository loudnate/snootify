import unittest

from snootify.monitor import Monitor
from snootify.data_source import DataSource

class TestDataSource(DataSource):
    def __init__(self):
        self._session = {}

    def get_current_session(self):
        pass

    @property
    def session(self):
        return self._session


class MonitorTestCase(unittest.TestCase):
    def testCreateMonitor(self):
        monitor = Monitor(data_source=TestDataSource())
        monitor.update_session({"foo": "bar"})
        pass


if __name__ == '__main__':
    unittest.main()
