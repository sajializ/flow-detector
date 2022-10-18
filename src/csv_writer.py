import csv


class CSVWriter:
    OUTPUT = "output.csv"
    HEADER = [
        "Source IP",
        "Destination IP",
        "Source Ports",
        "Destination Ports",
        "Protocols",
        "Duration",
        "Sent Bytes",
        "Received Bytes",
        "Header Bytes FWD",
    ]

    def open(self):
        self.fp = open(CSVWriter.OUTPUT, "w")
        self.writer = csv.writer(self.fp)
        self.writer.writerow(CSVWriter.HEADER)

    def write(self, flow_stat):
        row = [
            flow_stat.source_ip,
            flow_stat.destination_ip,
            " ".join(flow_stat.source_ports),
            " ".join(flow_stat.destination_ports),
            " ".join(flow_stat.protocols),
            flow_stat.duration,
            flow_stat.sent_bytes,
            flow_stat.received_bytes,
            flow_stat.sent_header_bytes,
        ]
        self.writer.writerow(row)

    def close(self):
        self.fp.close()
