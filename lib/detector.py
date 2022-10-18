
from lib import datagram
from lib import flow

import signal
import sys
import csv

class Detector:

    def __init__(self):
        self.flows = dict()
        self.running = True
        signal.signal(signal.SIGINT, self.signal_handler)


    def signal_handler(self, sig, frame):
        self.running = False

    
    def detect(self, queue):
        while self.running:
            packet = queue.get()
            
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
        with open("output.csv", "a") as fp:
            writer = csv.writer(fp)
            writer.writerow(["SourceIP", "DestinationIP", "SourcePort", "DestinationPort", "Protocol", "Duration", "Sent Bytes", "Recieved Bytes", "Header Bytes"])
            for flow in self.flows.values():
                writer.writerow(flow.get_stat())
