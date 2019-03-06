from .quartus_process import quartus_thread
from .Hardware import Hardware


def get_hardware_names(thread=None):
    if(thread is None):
        thread = quartus_thread()
    if(thread.process is None):
        thread.run()
    thread.process.stdout.flush()
    output, err = thread.process.communicate("get_hardware_names\n".encode())
    output = str(output).replace("tcl> ", "").replace("\\r\\n", "").replace(
        "{", "").replace("}", "").replace("b'", "").replace("'", "").lstrip().rstrip()
    return [output]


def get_device_names(thread=None):
    if(thread is None):
        thread = quartus_thread()
    if(thread.process is None):
        thread.run()
    hardware_name = get_hardware_names(thread)
    print("Hardware detected: " + hardware_name)
    hardware = Hardware(str(hardware_name))
    return hardware.devices


def run_tcl_command(command):
    thread = quartus_thread()
    thread.run()
    output, err = thread.process.communicate(command)
    return (output, err)
