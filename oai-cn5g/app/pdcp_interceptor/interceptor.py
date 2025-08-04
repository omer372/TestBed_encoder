#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 11:13:58 2025

@author: omer24
"""

import socket

INTERCEPTOR_PORT = 8800

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', INTERCEPTOR_PORT))
    
    print("PDCP Interceptor running...")
    
    while True:
        data, addr = sock.recvfrom(65535)
        print(f"Received PDCP packet of size {len(data)}")
        # Process packet here

if __name__ == "__main__":
    main()