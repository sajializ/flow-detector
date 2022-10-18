import pyshark
import signal
import sys
import os

from _thread import interrupt_main
from src import datagram


class Sniffer:
    def __init__(self, if_name):
        self.running = True
        self.capture = pyshark.LiveCapture(interface=if_name)

    def signal_handler(self, sig, frame):
        self.running = False

    def sniff(self, queue):
        try:
            for packet in self.capture.sniff_continuously():
                if not self.running:
                    return

                try:
                    new_packet = datagram.Datagram(
                        protocol=packet.transport_layer,
                        src_ip=packet.ip.src,
                        dest_ip=packet.ip.dst,
                        src_port=packet[packet.transport_layer].srcport,
                        dest_port=packet[packet.transport_layer].dstport,
                        time=packet.sniff_time,
                        size=packet.ip.len,
                        header_size=packet.ip.hdr_len,
                    )

                    queue.put(new_packet)

                except AttributeError as e:
                    # New packet was controlling packet, discarded
                    pass

        except pyshark.capture.live_capture.UnknownInterfaceException as e:
            print(e)
            interrupt_main()
