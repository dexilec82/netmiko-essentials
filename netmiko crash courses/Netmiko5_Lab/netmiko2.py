#!/usr/bin/env python

from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'carlo',
    'password': 'cisco',
}

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**iosv_l2_s1)
    output = net_connect.send_command(commands_to_send)
    print(output)