import unittest
from typing import Any, Optional

from snootify.monitor import Monitor
from snootify.monitor import SessionStatus
from snootify.data_source import DataSource
from snootify.notifier import Notifier


class TestDataSource(DataSource):
    def __init__(self, session=None):
        self._session = session or {}

    def get_current_session(self):
        pass

    @property
    def session(self):
        return self._session


class TestNotifier(Notifier):
    def __init__(self):
        self.last_message = None
        super().__init__()

    def send_message(self, message: str, attachment=None, **kwords) -> Any:
        self.last_message = message


class MonitorTestCase(unittest.TestCase):
    def testCreateMonitor(self):
        data_source = TestDataSource(session={'level': 'BASELINE'})
        notifier = TestNotifier()

        monitor = Monitor(data_source=data_source, notifier=notifier)


class SessionStateTestCase(unittest.TestCase):
    def testStringifyEnum(self):
        self.assertEqual("Asleep", f"{str(SessionStatus.ASLEEP)}")
        self.assertEqual("Awake", f"{str(SessionStatus.AWAKE)}")
        self.assertEqual("Soothing", f"{str(SessionStatus.SOOTHING)}")

    def testFromString(self):
        self.assertEqual(SessionStatus.ASLEEP, SessionStatus.from_str('asleep'))
        self.assertEqual(SessionStatus.AWAKE, SessionStatus.from_str('AWAKE'))
        self.assertEqual(SessionStatus.SOOTHING, SessionStatus.from_str('Soothing'))
        self.assertEqual(SessionStatus.ASLEEP, SessionStatus.from_str('2'))
        self.assertEqual(SessionStatus.AWAKE, SessionStatus.from_str('1'))
        self.assertEqual(SessionStatus.SOOTHING, SessionStatus.from_str('3'))

    def testComparison(self):
        self.assertGreater(SessionStatus.SOOTHING, SessionStatus.AWAKE)
        self.assertGreaterEqual(SessionStatus.AWAKE, SessionStatus.AWAKE)
        self.assertGreaterEqual(SessionStatus.ASLEEP, SessionStatus.AWAKE)

class RunTestCase(unittest.TestCase):
    monitor = Monitor(data_source=TestDataSource(), notifier=TestNotifier())

if __name__ == '__main__':
    unittest.main()
