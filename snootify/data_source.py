from abc import ABC, abstractmethod
from typing import Dict, Any

class DataSource(ABC):
    @abstractmethod
    def get_current_session(self):
        pass

    @property
    @abstractmethod
    def session(self) -> Dict[str, Any]:
        pass

"""
Example output from the Snoo endpoint for a single session:
{
    'startTime': '2020-05-30T19:59:05.039Z',
    'endTime': '2020-05-30T21:01:11.866Z',
    'levels': [
        {'level': 'BASELINE'},
        {'level': 'LEVEL1'},
        {'level': 'LEVEL2'},
        {'level': 'LEVEL1'},
        {'level': 'BASELINE'},
        {'level': 'LEVEL1'},
        {'level': 'LEVEL2'},
        {'level': 'LEVEL1'},
        {'level': 'ONLINE'}
    ]
}

To convert this to basic tri-state, the Snoo package does this (level is levels[-1])
    if session["end_time"]:
        status = "Awake"
    elif session["level"] in ["BASELINE", "WEANING_BASELINE"]:
        status = "Asleep"
    else:
        status = "Soothing"
"""