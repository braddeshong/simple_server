#!/usr/bin/env python

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

data = "Hello World!"
print "Sending Length..."
s.send(struct.pack("I", len(data)))
print "Sending Data..."
s.send(data)
print "Receivind data..."
recv_data = s.recv(1024)
print "Received: %s" % recv_data
