import socket
import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base

class Main(base.Module):
    """Monitoring Network"""

    def scan_ports(self, target_ip, ports):
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports
    
    
    def do_run(self, line):
        open_ports = self.scan_ports("192.168.1.1", [80, 443])
        print(f"Offene Ports: {open_ports}")
    
    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]