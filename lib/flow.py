

class Flow:

    def __init__(self, src_ip, dest_ip):
        self.source_ip = src_ip
        self.destination_ip = dest_ip
        self.packets = list()

    
    def add_packet(self, packet):
        self.packets.append(packet)

    
    def get_stat(self):
        send_ports = set()
        receive_ports = set()
        protocols = set()
        sent_bytes = 0
        received_bytes = 0
        header_bytes = 0

        for packet in self.packets:
            send_ports.add(packet.source_port)
            receive_ports.add(packet.destination_port)
            protocols.add(packet.protocol)
        
        return [self.source_ip, self.destination_ip, " ".join(send_ports), " ".join(receive_ports), " ".join(protocols), sent_bytes, received_bytes, header_bytes]
