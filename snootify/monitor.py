# Checks the latest Snoo status against the last-known status and determines if we need to notify the user

from typing import Any, Dict, Optional

from snoo.client import Client as Snoo
from pushover import Client as Pushover

from .data_source import DataSource
from .notifier import Notifier
from .session_status import SessionStatus


# Register our external services as conforming to our protocols
DataSource.register(Snoo)
Notifier.register(Pushover)


class Monitor:
    def __init__(self, data_source: DataSource = Snoo(), notifier: Notifier = Pushover()):
        self.data_source = data_source
        self.notifier = notifier
        self.session = data_source.session

    def __str__(self) -> str:
        return f'{str(self.status)} {self.__class__._humanize(self.session["duration"])}'

    def __repr__(self, *args, **kwargs):
        return f'{dict(self.session)}'

    def get_current_session(self) -> Dict[str, Any]:
        session = self.data_source.get_current_session()
        if session is not None:
            return dict(session)
        return None

    def update_session(self):
        session = self.get_current_session()
        print(f"Updating {dict(self.session)} to {dict(session)}")
        self.session = session

    # Borrowed from snoo.client.Client
    @classmethod
    def _humanize(cls, duration) -> str:
        if not duration:
            return "0m"
        if isinstance(duration, str):
            duration = int(duration)
        minutes = int(duration // 60)
        if minutes >= 60:
            hours = minutes // 60
            return f"{hours}h {minutes % 60}m"
        return f"{minutes}m"

    @property
    def status(self) -> SessionStatus:
        status = None
        if self.session["end_time"]:
            status = SessionStatus.AWAKE
        elif self.session["level"] in ["BASELINE", "WEANING_BASELINE"]:
            status = SessionStatus.ASLEEP
        else:
            status = SessionStatus.SOOTHING
        return status

    def message(self, level: SessionStatus = SessionStatus.SOOTHING) -> Optional[str]:
        status = self.status
        if status >= level:
            return f"{self}"
        return None

    def notify(self, level: SessionStatus = SessionStatus.SOOTHING) -> Optional[str]:
        message = self.message(level=level)
        if message is not None:
            self.notifier.send_message(message)

        return message