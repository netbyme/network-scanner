# network-scanner

A Python tool that scans a network range and detects which devices are alive.
Built as part of my network automation learning path.

## What it does

- Takes a network range like 192.168.1.0/24
- Pings every IP in the range automatically
- Shows which devices are UP or DOWN
- Saves results to a report file

## Demo

![Scanner output](scan-output.png)

## How to run

```bash
python3 scanner.py
```

## Tools used

- Python 3.12
- subprocess — to run ping commands
- ipaddress — to calculate IP ranges
- Ubuntu WSL

## Author

Mohammed Hammouch — Casablanca, Morocco