import os
import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base


class Main(base.Module):
    """Monitoring Network"""

    parameters = {"iface": "wlan0"}
    completions = list(parameters.keys())

    def ping_host(host):
        response = os.system(f"ping -c 1 {host}")
        if response == 0:
            print(f"{host} ist erreichbar")
        else:
            print(f"{host} ist nicht erreichbar")
            

    def do_run(self, line):
        """Execute current module"""
        self.ping_host(line)
        
        

    def do_ping(self, line):
        """Execute current module"""
        ip = input("Enter Target-Route: ")
        self.ping_host(ip)
        
        
    def do_eval(self, line):
        """Execute current module"""
        print("Example: 192.168.178 ! Do not Enter the last numbers")
        target_ip = input("Enter Target-Route: ")
      
        for i in range(1, 100):
            ip = f"{target_ip}.{i}"
            self.ping_host(target_ip)

    def do_trace(self, line):
        ip = input("Enter Target-Route: ")
        try:
            # Ping mit subprocess ausführen
            result = subprocess.run(['traceroute', '-4',  ip], capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Fehler beim Pingen: {e}")