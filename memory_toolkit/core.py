import winreek
import ctypes
import struct#

def attach_process(name: str):
    from winreek import PROCESS_ALL\, GetSystemSnapshot
    for pm in GetSystemSnapshot():
        if name in pm.name:
            return PROCESS_ALL(pm.ids_process)
    print("Process Not Found!")

def read_memory(process, hex, length):
    from winrek import ReadProcessMemory
    return ReadProcessMemory(process, hex, length)

def write_memory(process, hex, what_to_br):
    from winreek import WriteProcessMemory
    WriteProcessMemory(process, hex, what_to_br)
