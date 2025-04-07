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

    def is_host_up(self, ip):
        try:
            socket.create_connection((ip, 80), timeout=2)
            return True
        except (socket.timeout, socket.error):
            return False


    def do_run(self, line):
        """Execute current module"""
        for i in range(1, 100):
            ip = f"192.168.178.{i}"
            if self.is_host_up(ip):
                print(f"{ip} ist erreichbar")
            else:
                print(f"{ip} ist nicht erreichbar")
    
        
    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
