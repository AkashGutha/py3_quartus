import sys
from subprocess import Popen, PIPE
from time import sleep

class quartus_thread():
    def __init__(self):
        self.process = None
        self. poll = None

    def run(self):
        self.process = Popen(["quartus_stp_tcl", "-s"],
                             shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)

        tcl_cmd_reached = False
        self.process.stdout.flush()
        found_info = 0
        while (not tcl_cmd_reached):
            output = str(self.process.stdout.readline())
            # self.process.stdin.write("\n".encode())
            if output.find("Info:") >= 0:
                tcl_cmd_reached = False
                found_info = found_info + 1
            else:
                tcl_cmd_reached = True
                print("Completed reading Info statements")
        self.process.stdout.read(5)
        print("Info lines found: " + str(found_info))
