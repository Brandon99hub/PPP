import os
import shutil
import subprocess
import time
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


def clean_temp():
    """Remove files from system temporary directories."""
    temp_dirs = [Path(os.environ.get('TEMP', '')), Path(os.environ.get('TMP', ''))]
    for d in temp_dirs:
        if d.is_dir():
            for item in d.iterdir():
                try:
                    if item.is_file() or item.is_symlink():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                except Exception as e:
                    print(f"Failed to remove {item}: {e}")


def run_disk_cleanup():
    """Run Windows Disk Cleanup in silent mode if available."""
    try:
        # Configure cleanup settings once with /sageset:1 as needed manually
        subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
    except FileNotFoundError:
        print("Disk Cleanup utility not found.")
    except subprocess.CalledProcessError as e:
        print(f"Disk Cleanup exited with error: {e}")


def defrag_drive(drive="C:"):
    """Run the Windows defragmentation tool on the specified drive."""
    try:
        subprocess.run(["defrag", drive, "/O"], check=True)
    except FileNotFoundError:
        print("Defrag utility not found.")
    except subprocess.CalledProcessError as e:
        print(f"Defrag exited with error: {e}")


def optimize_ram():
    """Placeholder for RAM optimization steps."""
    print("RAM optimization not implemented.")


def optimize_cpu():
    """Placeholder for CPU tuning."""
    print("CPU optimization not implemented.")


def optimize_gpu():
    """Placeholder for GPU tuning."""
    print("GPU optimization not implemented.")


def optimize_windows():
    """Placeholder for general Windows tweaks."""
    print("General Windows optimization not implemented.")


def optimize_antivirus():
    """Placeholder for antivirus updates/optimization."""
    print("Antivirus optimization not implemented.")


def disable_animations():
    """Placeholder for disabling Windows animations."""
    print("Disable animations not implemented.")


def increase_fps():
    """Placeholder for FPS enhancements (e.g., game mode)."""
    print("FPS optimization not implemented.")


def optimize_wifi():
    """Placeholder for WiFi settings adjustment."""
    print("WiFi optimization not implemented.")


def overclock_system():
    """Placeholder for overclocking using vendor tools."""
    print("Overclocking not implemented. Use manufacturer utilities.")


def scan_system_files():
    """Run Windows utilities to check for corrupted system files."""
    try:
        subprocess.run(["sfc", "/scannow"], check=True)
    except FileNotFoundError:
        print("sfc utility not found.")
    except subprocess.CalledProcessError as e:
        print(f"sfc exited with error: {e}")


def cleanup_component_store():
    """Clean obsolete files from the Windows component store."""
    try:
        subprocess.run(["dism", "/online", "/cleanup-image", "/startcomponentcleanup", "/quiet"], check=True)
    except FileNotFoundError:
        print("DISM utility not found.")
    except subprocess.CalledProcessError as e:
        print(f"DISM exited with error: {e}")


def find_unused_files(directory, days=180):
    """Print files in 'directory' not accessed in the given number of days."""
    root = Path(directory)
    if not root.is_dir():
        print(f"Directory {directory} not found")
        return
    cutoff = time.time() - days * 86400
    unused = []
    for path in root.rglob('*'):
        if path.is_file() and path.stat().st_atime < cutoff:
            unused.append(path)
    if unused:
        print("Unused files:")
        for f in unused:
            print(f)
    else:
        print("No unused files found.")


def main():
    """Launch a basic GUI for selecting optimization tasks."""
    root = tk.Tk()
    root.title("Windows Optimizer")
    root.resizable(False, False)

    options = {
        "Clean temporary files": tk.BooleanVar(value=True),
        "Run Disk Cleanup": tk.BooleanVar(value=False),
        "Defragment drive C": tk.BooleanVar(value=False),
        "Scan system files": tk.BooleanVar(value=False),
        "Cleanup old updates": tk.BooleanVar(value=False),
        "Check unused files": tk.BooleanVar(value=False),
        "Optimize RAM": tk.BooleanVar(value=False),
        "Optimize CPU": tk.BooleanVar(value=False),
        "Optimize GPU": tk.BooleanVar(value=False),
        "Optimize Windows": tk.BooleanVar(value=False),
        "Optimize Antivirus": tk.BooleanVar(value=False),
        "Disable animations": tk.BooleanVar(value=False),
        "Increase FPS": tk.BooleanVar(value=False),
        "Optimize WiFi": tk.BooleanVar(value=False),
        "Overclock system": tk.BooleanVar(value=False),
    }

    frame = ttk.Frame(root, padding=10)
    frame.pack()

    for text, var in options.items():
        ttk.Checkbutton(frame, text=text, variable=var).pack(anchor="w")

    def start_optimization():
        if options["Clean temporary files"].get():
            clean_temp()
        if options["Run Disk Cleanup"].get():
            run_disk_cleanup()
        if options["Defragment drive C"].get():
            defrag_drive("C:")
        if options["Scan system files"].get():
            scan_system_files()
        if options["Cleanup old updates"].get():
            cleanup_component_store()
        if options["Check unused files"].get():
            user_dir = os.path.expanduser("~")
            find_unused_files(user_dir)
        if options["Optimize RAM"].get():
            optimize_ram()
        if options["Optimize CPU"].get():
            optimize_cpu()
        if options["Optimize GPU"].get():
            optimize_gpu()
        if options["Optimize Windows"].get():
            optimize_windows()
        if options["Optimize Antivirus"].get():
            optimize_antivirus()
        if options["Disable animations"].get():
            disable_animations()
        if options["Increase FPS"].get():
            increase_fps()
        if options["Optimize WiFi"].get():
            optimize_wifi()
        if options["Overclock system"].get():
            overclock_system()

        messagebox.showinfo("Windows Optimizer", "Selected optimizations complete.")

    ttk.Button(frame, text="Optimize", command=start_optimization).pack(pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
