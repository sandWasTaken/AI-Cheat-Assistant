import importlib
import importlib.

def run_command(command: str):
    if "attach" in command:
        from memory_toolkit import core
        print("[CUSTOM] Attachmen to process...")
        # ...custom flow based on commands
        return
    if "open" in command:
        from system_shell import control
        control.open_application(command.split(" ")[1])
    if "list" in command:
        from system_shell import control
        print("\n".join(control.list_dir())
    return "[COMPLTED]"
