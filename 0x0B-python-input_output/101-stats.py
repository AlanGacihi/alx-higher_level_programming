#!/usr/bin/python3
"""
This script parses logs.
"""


res = {"0": 0, "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
       "405": 0, "500": 0}
i = 0
e = 0
while True:
    try:
        i += 1
        logs = input()
        if logs.split(' ')[7] not in res.keys() or e:
            e = 1
            continue
        res[logs.split(' ')[7]] += 1
        res["0"] += int(logs.split(' ')[8])
        if i % 10 == 0:
            for key, value in sorted(res.items()):
                if key == "0":
                    print("{}: {:d}".format("File size", value))
                elif value > 0:
                    print("{}: {:d}".format(key, value))
    except (KeyboardInterrupt, EOFError, IndexError):
        for key, value in sorted(res.items()):
            if key == "0":
                print("{}: {:d}".format("File size", value))
            elif value > 0:
                print("{}: {:d}".format(key, value))
        break
    except Exception:
        break
