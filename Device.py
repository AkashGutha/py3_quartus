from tools import escape, write_hex
from subprocess import Popen, PIPE
from quartus_process import quartus_thread
from time import sleep
from queue import Queue, Empty


class Device(object):

    def __init__(self, name=None, hardware=None):
        self.name = name
        self.hardware = hardware

    # Write memory content using the hex memory file
    def write_to_memory_from_file(self, instance_index=0, path="", memfile_type="hex"):

        commands = [
            "quartus_stp_tcl",
            "--tcl_eval",
            # Initiate a editing sequence
            "begin_memory_edit -hardware_name \"{}\" -device_name \"{}\"".format(
                escape(self.hardware.name), escape(self.name)),
            "update_content_to_memory_from_file -instance_index 0 -mem_file_path \"{}\" -mem_file_type hex".format(
                path),
            "end_memory_edit"
        ]

        print(commands)

        output, error = Popen(commands, shell=True,
                              stdout=PIPE, stderr=PIPE).communicate()
        print(output)
        print("error: " + str(error))

    # Write memory content using the hex memory file

    def write_to_memory_from_file_2(self, process=None, instance_index=0, path="", memfile_type="hex"):

        thread = quartus_thread()
        thread.run()
        process = thread.process

        commands = [
            # Initiate a editing sequence
            "begin_memory_edit -hardware_name \"{}\" -device_name \"{}\"".format(
                escape(self.hardware.name), escape(self.name)),
            "update_content_to_memory_from_file -instance_index 0 -mem_file_path \"{}\" -mem_file_type hex".format(
                path),
            "end_memory_edit\r\n"
        ]

        for command in commands:
            process.stdin.write(command.encode())
            sleep(0.1)
            print("command runing: " + command)

        # output = process.stdout.readlines()
        # error = process.stderr.readline()

        # print(output)
        # print("error: " + str(error))
