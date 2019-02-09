from tools import escape
from subprocess import Popen, PIPE


class Device(object):

    def __init__(self, name=None, hardware=None):
        self.name = name
        self.hardware = hardware

    # Write memory content using the hex memory file

    def write_to_memory_from_file(self, instance_index=0, path="", memfile_type="hex"):

        print("update_content_to_memory_from_file - instance_index 0 - mem_file_path \"" \
            + path + "\" -mem_file_type hex")
                
        commands = [
            # Initiate a editing sequence
            "begin_memory_edit -hardware_name \"" + str(escape(self.hardware.name)) + "\" -device_name " \
            + str(escape(self.name)),
            "update_content_to_memory_from_file - instance_index 0 - mem_file_path \"" \
            + path + "\" -mem_file_type hex",
            "end_memory_edit"
        ]
        output, error = Popen(commands, shell=True,
                              stdout=PIPE, stderr=PIPE).communicate()
        print(output)
        print(error)
