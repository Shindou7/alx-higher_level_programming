#!/usr/bin/python3
"""
Module 101-stats.py
to print status code
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 0
            count += 1

            parts = line.split()
            if len(parts) < 9:
                continue

            try:
                code = parts[-2]
                size += int(parts[-1])

                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1

            except (ValueError, IndexError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
