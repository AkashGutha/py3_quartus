import os
import click
from py3_quartus.Hardware import Hardware
from py3_quartus import tcl_tools


@click.command()
@click.option("--hardware", help="Hardware name attached to the system")
@click.option("--device", help="Device to be selected for programming")
def program(hardware, device):
    '''
    run the main program to configure and program the boards
    '''
    selected_hardware = None
    selected_device = None
    selected_sof_file = None

    if(hardware == "" or hardware == None):
        hw_names = tcl_tools.get_hardware_names()
        if(str(hw_names).find("ERROR") >= 0):
            print(hw_names)
            return
        hw_list = []
        for name in hw_names:
            hw_list.append(Hardware(name))
        for hw in hw_list:
            print(hw)
        print("\nPlease select a Hardware from the above list")
        selected_hardware = select_one_from_list(hw_list)
    pass

    if(device == "" or device == None):
        device_names = tcl_tools.get_device_names(hw)
        if(str(device_names).find("ERROR") >= 0):
            print(device_names)
            return
        devices_list = []
        for name in device_names:
            devices_list.append(Hardware(name))
        for dv in devices_list:
            print(dv)
        print("\nPlease select a Device from the above list")
        selected_device = select_one_from_list(devices_list)
    pass


def select_one_from_list(options_list=[]):
    selected_option = None
    if len(options_list) > 0:
        while True:
            print("Select one options form the list:\n")
            for i in range(len(options_list)):
                print(str(i+1)+": " + options_list[i])
            inp = input("Select an option: ")
            if (inp.isnumeric() and int(inp) > 0):
                print("Selected option: " + str(options_list[int(inp)-1]))
                return inp

    return selected_option


if (__name__ == "__main__"):
    # program(None, None)
    select_one_from_list(["asdfsdf", 'adsfsdf', "dfasdfasd"])
