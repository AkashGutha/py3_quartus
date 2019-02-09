from devices import get_hardware_names, get_device_names
from Hardware import Hardware
from Device import Device

connected_hardware = None
connected_devices = None

hardware_name = get_hardware_names()
connected_hardware = Hardware(hardware_name)
print("hardware connected: " + connected_hardware.name)

connected_devices = connected_hardware.devices
print("connected devices: " +
      ", ".join([str(device) for device in connected_devices]))
connected_device = Device(name=connected_devices[1], hardware=connected_hardware)
connected_device.write_to_memory_from_file(path="C:\\Users\\gutha.3\\Desktop\\py3-quartus\\memfile.hex", instance_index=1)


# import sys
# from subprocess import Popen, PIPE

# from time import sleep

# output, err = Popen(["quartus_stp", "-t", "a.tcl"],
#                     shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()

# print(output)
