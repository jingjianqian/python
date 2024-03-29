import socket
import re
import sys

# How-to
# >>  python wol.py ‎00-00-00-00-00-C4

# Get Mac from input
# mac_ext = "‎00-00-00-00-00-C4"   # For mobile
mac_ext = sys.argv[1]
# Support format 00:00:00:00:00:00  or 00-00-00-00-00-00
mac = ''.join(re.findall('[^-:]',mac_ext))  # match character w/o '-' and ':' 

# Transform to magic packet
data = ''.join(['FFFFFFFFFFFF', mac * 16])  # Magic packet string
send_data = bytes.fromhex(data)             # String to bytes

# Broadcast via socket
destination = ('255.255.255.255', 9)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(send_data, destination)

# print("WOL packet %d bytes sent !" % len(send_data))
