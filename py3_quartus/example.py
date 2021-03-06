__name__ = "py3_quartus"

from .Hardware import Hardware
from .Device import Device
from .tools import write_hex
from .tcl_tools import get_device_names, get_hardware_names

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
connected_device.write_to_memory_from_file(
    path="memfile.hex", instance_index=0)

