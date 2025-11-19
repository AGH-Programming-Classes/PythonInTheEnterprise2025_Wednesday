from collections import defaultdict
from typing import Any, Callable, Dict, Set

class EventBus:
    def  __init__(self):
        self._events = defaultdict(set)  # type: Dict[Any, Set[Callable]]

    def register_event(self, event_name, handler):
        self._events[event_name].add(handler)

    def subscribe(self, event_name):
        def main_decorator(func):
            self.register_event(event_name, func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return wrapper
        return main_decorator
    
    def emit_event(self, event_name, *args, **kwargs):
        for h in self._events[event_name]:
            h(*args, **kwargs)     
    