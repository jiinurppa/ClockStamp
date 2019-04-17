# ClockStamp
Python script to stamp images with a clock face from file creation time

## Sample Image
File created at 19:50
![alt text](https://github.com/jiinurppa/ClockStamp/raw/master/sample.jpg "Sample Image")

## Usage
With default **(15, 15)** clock position:
```bash
ClockStamp.py image.jpg
```
With clock at position **(64, 15)**:
```bash
ClockStamp.py image.jpg 64
```
With clock at position **(96, 32)**:
```bash
ClockStamp.py image.jpg 96 32
```

The script contains an embedded font file for drawing the clock face, which is written to the current folder when the script is executed. This file is named `analogclock.ttf` and it can be safely deleted after the script has finished running.

The font file is from [PE-Analog-Clock-icon-font](https://github.com/jhogue/PE-Analog-Clock-icon-font).

## Stamp Folder Contents
Run `stamp.sh` to stamp all `.jpg` files in current directory. This script deletes the temporary font file automatically.
