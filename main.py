
from queue import Queue
from threading import Thread

from lib import detector
from lib import sniffer


if __name__ == "__main__":
    interface_name = input("Enter interface name: ")

    shared_queue = Queue()
    sniffer = sniffer.Sniffer(interface_name)
    detector = detector.Detector()

    sniffer_thread = Thread(target=sniffer.sniff, args=(shared_queue, ))
    detector_thread = Thread(target=detector.detect, args=(shared_queue, ))

    sniffer_thread.start()
    detector_thread.start()