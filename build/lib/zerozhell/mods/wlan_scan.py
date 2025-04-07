import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base

from wifi import Cell, Scheme

class Main(base.Module):
    """WLAN SCAN Network"""

    def scan_wifi(self, interface):
        networks = Cell.all(interface)
        for network in networks:
            print(f"SSID: {network.ssid} | Signalstärke: {network.signal} dBm")
            
    def do_run(self, line):
        self.scan_wifi("wlan0")

