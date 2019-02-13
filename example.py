from Hardware import Hardware
from Device import Device
from tools import write_hex
from tcl_tools import get_device_names, get_hardware_names

connected_hardware = None
connected_devices = None

hardware_name = get_hardware_names()
connected_hardware = Hardware(hardware_name)
print("hardware connected: " + connected_hardware.name)

connected_devices = connected_hardware.devices
print("connected devices: " +
      ", ".join([str(device) for device in connected_devices]))
connected_device = Device(
    name=connected_devices[1], hardware=connected_hardware)
write_hex("memfile.hex", 32)
connected_device.write_to_memory_from_file_2(
    path="memfile.hex", instance_index=1)


# import sys
# from subprocess import Popen, PIPE

# from time import sleep

# output, err = Popen(["quartus_stp", "-t", "a.tcl"],
#                     shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()

# print(output)
