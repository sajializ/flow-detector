
import pyshark
from lib import datagram

import signal
import sys

class Sniffer:
    
    def __init__(self, if_name):
        self.inteface_name = if_name
        self.capture = pyshark.LiveCapture(interface=self.inteface_name)
        self.running = True
        signal.signal(signal.SIGINT, self.signal_handler)


    def signal_handler(self, sig, frame):
        self.running = False


    def sniff(self, queue):
        for packet in self.capture.sniff_continuously():
            try:
                protocol = packet.transport_layer
                source_address = packet.ip.src
                source_port = packet[packet.transport_layer].srcport
                destination_address = packet.ip.dst
                destination_port = packet[packet.transport_layer].dstport
                packet_time = packet.sniff_time
                
                new_packet = datagram.Datagram(protocol=protocol,
                                    src_ip=source_address,
                                    dest_ip=destination_address,
                                    src_port=source_port,
                                    dest_port=destination_port,
                                    time=packet_time)

                queue.put(new_packet)
            except AttributeError as e:
                # New packet was controlling packet, discarded
                pass

            if not self.running:
                return