import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base
from scapy.all import ARP, Ether, srp
from zerozhell.configs.colors import *

class Main(base.Module):
    """Monitoring Network"""

    parameters = {"iface": "wlan0"}
    completions = list(parameters.keys())

    def scan_network(self, target_ip):
        # Erstelle ARP-Request Paket
        arp_request = ARP(pdst=target_ip)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request

    # Sende Paket und empfange Antwort
        result = srp(arp_request_broadcast, timeout=3, verbose=False)[0]

        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})

        return devices

    def do_run(self, line):
    # Beispiel: Scanne 192.168.1.1 bis 192.168.1.254
        target_ip = "192.168.178.1/24"
        devices = self.scan_network(target_ip)

        p("r Gefundene Geräte:")
        for device in devices:
            print(f"IP: {device['ip']} | MAC: {device['mac']}")
