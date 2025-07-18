import os
import shutil
import subprocess
from pathlib import Path


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


def main():
    print("Cleaning temporary files...")
    clean_temp()
    print("Running Disk Cleanup...")
    run_disk_cleanup()
    print("Defragmenting drive C...")
    defrag_drive("C:")
    print("Optimization tasks complete.")


if __name__ == "__main__":
    main()
