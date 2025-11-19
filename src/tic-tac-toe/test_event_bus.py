import unittest

from event_bus import EventBus


class TestEventBus(unittest.TestCase):
    def test_registering_event(self):
        bus = EventBus()
        called = []
        @bus.subscribe("test_event")
        def test_func(called):
            called.append(0)
            
        bus.emit_event("test_event", called)
        self.assertEqual(called[0], 0)
        
if __name__ == "__main__":
    unittest.main()
