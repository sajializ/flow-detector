
from lib import datagram
from lib import flow

class Detector:

    def __init__(self):
        self.flows = dict()

    
    def detect(self, queue):
        while True:
            packet = queue.get()
            
            key = packet.source_address + packet.destination_address
            if key not in self.flows.keys():
                self.flows = flow.Flow(packet.source_ip, packet.destination_ip)

            self.flows[key].add_packet(packet)
