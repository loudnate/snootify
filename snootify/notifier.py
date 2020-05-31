from abc import ABC, abstractmethod
from typing import Any

class Notifier(ABC):
    @abstractmethod
    def send_message(self, message: str, attachment=None, **kwords) -> Any:
        
        pass

"""
Pushover client call:

Client(args.user_key, None, args.api_token, args.config,
           args.profile).send_message(args.message, title=args.title,
                                      priority=args.priority, url=args.url,
                                      url_title=args.url_title, timestamp=True,
                                      retry=args.retry,expire=args.expire)

"""