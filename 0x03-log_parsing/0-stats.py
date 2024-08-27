#!/usr/bin/python3
"""
    Log parsing
"""

import sys
def print_status(total_size, status_code_counts):
    print(f"File Size: {total_size}")
    for x in sorted(status_code_counts.keys()):
        if status_code_counts[x] > 0:
            print(f"{x}: {status_code_counts[x]}")
def main():
    total_size = 0
    line_count = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split(" ")
            # check that the line doesnot exced the 10th line
            if line < 9:
                continue
            # Input format
            ip_address = parts[0]
            date = parts[3] + ' ' + parts[4]
            request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
            status_code = parts[8]
            file_size = parts[9]
            # validate the extract format
            if not date.startswith('[') or not date.endswith(']'):
                continue
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            try:
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                continue
            # update the metrics
            total_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
    except KeyboardInterrupt:
        print(total_size, status_code_counts)
        raise
    # starts if the input enter without ctrl + c
    print_status(total_size, status_code_counts)
