import sys
import signal
from queue import Queue
from threading import Thread

from src import sniffer
from src import collector


class FlowDetector:
    def __init__(self, sniffer_instance=None, collector_instance=None, ifname=None):
        self.sniffer = (
            sniffer_instance
            if sniffer_instance is not None
            else sniffer.Sniffer(ifname)
        )
        self.collector = (
            collector_instance
            if collector_instance is not None
            else collector.Collector()
        )

    def run(self):
        shared_queue = Queue()
        signal.signal(signal.SIGINT, self.sniffer.signal_handler)
        signal.signal(signal.SIGINT, self.collector.signal_handler)

        sniffer_thread = Thread(target=self.sniffer.sniff, args=(shared_queue,))
        collector_thread = Thread(target=self.collector.collect, args=(shared_queue,))

        sniffer_thread.start()
        collector_thread.start()

        sniffer_thread.join()
        collector_thread.join()
