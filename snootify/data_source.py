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
