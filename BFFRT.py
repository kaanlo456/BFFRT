# Its still in alpha may exprienece issues!!!!!!!
#
#           BFFRT (Basic File Finding and Running Tool) vAlpha1
#

import os
import subprocess # WHAT THE FUCK IS THIS
import platform # WHAT THE FUCK IS THIS

def this_is_a_bucket(path): # dear god ....no
    print(f"\nContents of {path}:\n")
    for i in os.listdir(path):
        full_path = os.path.join(path, i) # LOOK AT THIS SHIT WHAT THE FUCK IS THIS
        if os.path.isdir(full_path):
            print("[DIR] ", i)
        else:
            print("      ", i)

def open_file(path, name):
    target = os.path.join(path, name) # OH MY GOD THEY ARE DUPLICATING
    if not os.path.exists(target): 
        print(f"[!] '{name}' not found.")
        return

    try:
        if platform.system() == "Windows":
            os.startfile(target)
        elif platform.system() == "Darwin":  # Who thought that naming macOS Darwin just say mac or appleOS.
            subprocess.run(["open", target])
        else:  # Linux / Unix
            subprocess.run(["xdg-open", target])
        print(f"[+] Opened: {target}")
    except Exception as e:
        print(f"[!] Error opening file: {e}")

def main():
    cwd = os.getcwd()
    print(r"""
===========================================
   BFFRT (Basic File Finding and Running Tool) vAlpha1
   Commands: ls | cd <folder> | open <file> | quit
===========================================
""")

    while True:
        try:
            cmd = input(f"{cwd}> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n[!] Forced exit. Bye!")
            break

        if cmd == "":
            continue # wait what.... huh

        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "quit":
            print("Exiting... Bye ")
            break
        elif action == "ls":
            this_is_a_bucket(cwd) # dear god ....no
        elif action == "cd":
            if len(parts) == 2:
                new_path = os.path.join(cwd, parts[1]) # Words cant describe my fucking confusion.I hate this!
                if os.path.isdir(new_path):
                    cwd = new_path
                else:
                    print(f"[!] '{parts[1]}' is not a directory.")
            else:
                print("Usage: cd <folder>")
        elif action == "open":
            if len(parts) == 2:
                open_file(cwd, parts[1])
            else:
                print("Usage: open <file>")
        else:
            print(f"[!] Unknown command: {action}")

if __name__ == "__main__":
    main()
# Finally i can go to get some doritos.    