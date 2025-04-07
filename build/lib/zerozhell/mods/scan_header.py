import requests
import cmd
import subprocess
import os
import sys
import socket
from zerozhell.core import base


class Main(base.Module):
    """Monitoring Network"""

    def http_header_scan(self, url):
        try:
            response = requests.head(url)
            print(f"Antwort Header von {url}:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Scannen der URL {url}: {e}")

    def do_run(self, line):
        adresse = input("Enter Target-Route: ")
        self.http_header_scan(adresse)
