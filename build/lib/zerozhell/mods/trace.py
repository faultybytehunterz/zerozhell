import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base
from scapy.all import traceroute

class Main(base.Module):
    """TRACE Network"""

    def traceroute_scan(self, target_ip):
        ans, unans = traceroute(target_ip, maxttl=30)
        ans.summary()
        
        
    def do_run(self, line):
        """Execute current module"""
        target_ip = input("Enter Target-Route: ")
        self.traceroute_scan(target_ip)
