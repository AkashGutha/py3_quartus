from .quartus_process import quartus_thread
from time import sleep


def escape(input_string=""):
    escaped = input_string.translate(str.maketrans({
        "\\": r"\\",
        "]":  r"\]",
        "[":  r"\[",
        "^":  r"\^",
        "$":  r"\$",
        "*":  r"\*",
        ".":  r"\."}))
    return escaped


def write_hex(path, data):
    """The Write Hex function.

    This function is for taking ints and writing an appropriately
    formatted hex file to load onto an FPGA's on-board memory.

    This function is a slightly modified version of a file from Intel.

    Args:
        path (str): Path for hex file.
        data (int): Data to write.
    """

    f = open(path, 'w')

    # data length, start address, record type
    f.write(':{:02x}{:04x}{:02x}'.format(32, 0, 0))
    checksum = 32

    # now data
    fmt = '{:0' + str(32 * 2) + 'x}'
    mask = (256 ** 32) - 1
    f.write(fmt.format(data & mask))

    csum = data & mask
    while csum:
        checksum += csum & 0xff
        csum = csum >> 8

    # now a checksum byte
    checksum_byte = checksum & 0xff
    checksum_byte = (~checksum + 1) & 0xff
    assert (checksum_byte + checksum) & 0xff == 0
    f.write('{:02x}\n'.format(checksum_byte))

    # and an end of file marker
    # data length, start address, record type, <data>, checksum
    f.write(':{:02x}{:04x}{:02x}{:02x}\n'.format(0, 0, 1, 0xff))

    f.close()


def write_2_hex_file(input, target):
    pass
