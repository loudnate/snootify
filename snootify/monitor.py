# Checks the latest Snoo status against the last-known status and determines if we need to notify the user

from configparser import SectionProxy
from typing import Any, Dict

from snoo.client import Client as Snoo
from pushover import Client as Pushover

from .data_source import DataSource
from .notifier import Notifier

# Register our external services as conforming to our protocols
DataSource.register(Snoo)
Notifier.register(Pushover)

class Monitor:
    def __init__(self, data_source: DataSource = Snoo(), notifier: Notifier = Pushover()):
        self.data_source = data_source
        self.notifier = notifier
        self.session = data_source.session

    def get_current_session(self) -> Dict[str, Any]:
        session = self.data_source.get_current_session()
        if session is not None:
            return dict(session)
        return None

    def update_session(self, session: Dict[str, Any]):
        print(f"Updating {dict(self.session)} to {session}")
