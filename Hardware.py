from subprocess import PIPE, Popen
from tools import escape
import re


class Hardware():
    """
    All functionality relating to jtag hardware (i.e., a usb-blaster)
    """

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self.name is None:
            return "Hardware chain does not exist"
        else:
            return self.name

    @property
    def devices(self):
        """
        tcl command: get_device_names
        :return: list of quartus.jtag.Device
        """
        command = "quartus_stp_tcl --tcl_eval get_device_names -hardware_name \"{}\"".format(
            escape(self.name))
        output, error = Popen(command, shell=True, stdout=PIPE,
                              stderr=PIPE).communicate()
        _devices = []
        if len(error) > 0:
            print("error: "+str(error.decode()))
            return _devices

        devices = re.findall(r'{(.*?)}', str(output))
        for device in devices:
            print(device)
            _devices.append(device)

        return _devices
