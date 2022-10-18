from src import flow_detector


if __name__ == "__main__":
    interface_name = input("Enter interface name: ")

    detector = flow_detector.FlowDetector(ifname=interface_name)
    detector.run()
