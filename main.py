from socket import socket
import hdmq
import stun

sip = "0.0.0.0" # interface to listen on (all)
port = 54320 # port to listen on
nat_type, external_ip, external_port = stun.get_ip_info(sip, port)

print(nat_type+external_ip+external_port)