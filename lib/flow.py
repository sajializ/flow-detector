

class Flow:

    def __init__(self, src_ip, dest_ip):
        self.source_ip = src_ip
        self.destination_ip = dest_ip
        self.packets = list()

    
    def add_packet(self, packet):
        self.packets.append(packet)