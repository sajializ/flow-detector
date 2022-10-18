
from lib import datagram
from lib import flow
import queue as Queue

import signal
import sys
import csv

class Collector:
    QUEUE_TIMEOUT = 2

    def __init__(self):
        self.flows = dict()
        self.running = True


    def signal_handler(self, sig, frame):
        self.running = False

    
    def collect(self, queue):
        while self.running:
            try:
                packet = queue.get(True, Collector().QUEUE_TIMEOUT)
            except Queue.Empty:
                continue

            key = packet.source_ip + packet.destination_ip
            reversed_key = packet.destination_ip + packet.source_ip
            if key in self.flows.keys():
                self.flows[key].add_packet(packet)
            elif reversed_key in self.flows.keys():
                self.flows[reversed_key].add_packet(packet)
            else:
                self.flows[key] = flow.Flow(packet.source_ip, packet.destination_ip)
                self.flows[key].add_packet(packet)

        self.generate_stat()


    def generate_stat(self):
        with open("output.csv", "w") as fp:
            for flow in self.flows.values():
                fp.write(str(flow.get_stat()) + '\n')
