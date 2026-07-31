# Duplicate File Removal Automation

## Overview

**Duplicate File Removal Automation** is a Python-based automation project that periodically scans a specified directory, identifies duplicate files using their checksum, removes duplicate copies while retaining one original file, generates a detailed log report, and emails the log file to the specified recipient.

This project demonstrates file handling, directory traversal, scheduling, logging, checksum generation, email automation, and command-line argument handling in Python.

---

## Features

* Scans an entire directory recursively.
* Identifies duplicate files using checksum comparison.
* Deletes duplicate copies while preserving one original file.
* Generates a timestamped log file after every execution.
* Sends the generated log file as an email attachment.
* Executes automatically at a user-defined time interval.
* Displays execution statistics in the log report.

---

## Project Structure

```
DuplicateFileRemoval/
│
├── DuplicateFileRemoval.py
├── Modules/
│   ├── ChekSumModule.py
│   └── MailModule.py
│
└── README.md
```

---

## Requirements

* Python 3.x

### Required Python Package

Install the scheduler package:

```bash
pip install schedule
```

---

## Command Line Usage

### Display Help

```bash
python DuplicateFileRemoval.py --h
```

### Display Usage

```bash
python DuplicateFileRemoval.py --usage
```

### Execute Automation

```bash
python DuplicateFileRemoval.py <IntervalMinutes> <DirectoryPath> <ReceiverEmail>
```

### Example

```bash
python DuplicateFileRemoval.py 5 E:/Data/Demo abc@gmail.com
```

This command will:

* Scan `E:/Data/Demo`
* Execute every **5 minutes**
* Remove duplicate files
* Generate a log report
* Email the report to **[abc@gmail.com](mailto:abc@gmail.com)**

---

## How It Works

1. Accepts the execution interval, directory path, and receiver email.
2. Schedules the duplicate file removal task.
3. Recursively scans the specified directory.
4. Calculates the checksum of every file.
5. Groups files having identical checksums.
6. Retains one original file and deletes duplicate copies.
7. Generates a detailed log file.
8. Sends the log file as an email attachment.
9. Repeats the process at the specified interval.

---

## Sample Log Report

```
Duplicate File Removal Report
--------------------------------------------------

Starting time of directory scanning : 20 July 2026, 11:15:30 PM
Completion time of scanning         : 20 July 2026, 11:16:02 PM
Directory scanned                   : E:\Data\Demo
Total files scanned                 : 150
Duplicate files found               : 12
Duplicate files deleted             : 11

Deleted Files
-----------------------------------
E:\Data\Demo\Copy1.jpg
E:\Data\Demo\Test\Copy2.jpg

Email delivery status : Success
```

---

## Technologies Used

* Python
* os
* sys
* time
* schedule
* File Handling
* Hashing (Checksum)
* SMTP Email Automation

---

## Future Enhancements

* Use `argparse` for command-line argument parsing.
* Replace manual logging with Python's `logging` module.
* Support SHA-256 and SHA-512 checksum algorithms.
* Generate reports in PDF or HTML format.
* Provide an option to move duplicates to a recycle bin instead of permanently deleting them.
* Add a graphical user interface (GUI).
* Allow users to choose which duplicate file to retain.
* Improve error handling and validation.

---

## Author

**Neha Jayvant Kadam**

Python Automation Project

2026
