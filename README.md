# PPP Scripts Repository

This repository contains various scripts. The new addition is a Windows optimization script.

## windows_optimizer.py

A simple Python utility to automate common Windows maintenance tasks. A graphical interface allows you to choose which optimizations to perform, including basic clean up actions. Many advanced options such as overclocking or GPU tuning are provided only as placeholders.

Recent updates include commands to check for corrupted system files via *sfc*,
cleanup obsolete Windows updates using *DISM*, and scan your user directory for
unused files that haven't been accessed in months.

### Usage

Run with Python 3 on a Windows machine:
```bash
python windows_optimizer.py
```

Administrator privileges may be required for certain operations.
Some features like overclocking or GPU tuning are represented as placeholders
and will only display a message when selected. Use manufacturer-provided tools
for advanced tuning.
