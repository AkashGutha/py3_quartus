from .tools import escape, write_hex
from subprocess import Popen, PIPE
from .quartus_process import quartus_thread
from time import sleep
from queue import Queue, Empty


class Device(object):

    def __init__(self, name=None, hardware=None):
        self.name = name
        self.hardware = hardware

    # Write memory content using the hex memory file
    def write_to_memory_from_file(self, instance_index=0, path="", memfile_type="hex"):

        tcl_lines = [
            "begin_memory_edit -hardware_name \"{}\" -device_name \"{}\"".format(
                escape(self.hardware.name), escape(self.name)),
            "update_content_to_memory_from_file -instance_index {} -mem_file_path \"{}\" -mem_file_type hex".format(instance_index,
                                                                                                                    path),
            "end_memory_edit"
        ]

        commands = [
            "quartus_stp_tcl",
            "-t",
            "scratch.tmp.tcl"
        ]

        with open("scratch.tmp.tcl", "w") as file:
            txt = ""
            for line in tcl_lines:
                txt += line + "\n"
            file.write(txt)
            file.close()

        output, error = Popen(commands, shell=True,
                              stdout=PIPE, stderr=PIPE).communicate()

        print("info : " + str(output))
        if (str(output).find(" was successful") >= 0):
            print("Write successful")
        print(str(output).find(" was successful"))
        print("error: " + str(error))
