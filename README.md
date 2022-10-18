# Flow-Monitoring
Monitors the flow of packets and extracts different things.

**Table of Contents**


* [Overview](#overview)
* [Dependencies](#dependencies)
* [How to Run](#how-to-run)

## Overview
This application captures and reports traffic flow between two nodes based on IP. The structure consists of two main threads. The capturer thread captures network traffic from an interface, and the collector thread collects data and generates a report based on the observed traffic. These two threads are connected through a queue. The result consists of the source address and port, destination address and port, duration of the flow, number of sent and received bytes, sent bytes in the header, and duration of the flow. The result is saved in a CSV file.

## Dependencies
- Python3
- TShark
- pyshark


## How to Run
Run `main.py` file
```bash
python3 main.py
```
After pressing Crtl+C, the output file will generate.