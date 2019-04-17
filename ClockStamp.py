#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import platform
import datetime
import zlib
import sys
import os

# Font file from:
# github.com/jhogue/PE-Analog-Clock-icon-font/blob/master/fonts/analogclock.ttf
clockfont = """
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
""".replace('\n', '');

def HourToChar(h):
    if h > 24: return chr(53);
    if h < 0:  return chr(53);
    if h > 11: h -= 12;
    return chr(53 + h);

def MinutesToChar(m):
    return chr(33 + m / 3);

def DrawClock(d, f, h, m, x, y, c, a):
    # Draw hours
    d.text((x, y), HourToChar(h), font=f, fill=(c, c, c, a));
    # Draw minutes
    d.text((x, y), MinutesToChar(m), font=f, fill=(c, c, c, a));

def DrawOutlinedClock(d, f, h, m, x, y, c, a, ol):
    # Draw outline
    DrawClock(d, f, h, m, x - ol, y - ol, 0, a);
    DrawClock(d, f, h, m, x + ol, y - ol, 0, a);
    DrawClock(d, f, h, m, x + ol, y + ol, 0, a);
    DrawClock(d, f, h, m, x - ol, y + ol, 0, a);
    # Draw clock
    DrawClock(d, f, h, m, x, y, c, a);

def FileCreated(path):
    # http://stackoverflow.com/a/39501288/1709587
    if platform.system() == 'Windows':
        return os.path.getctime(path);
    else:
        stat = os.stat(path);
        try:
            return stat.st_birthtime;
        except AttributeError:
            return stat.st_mtime;

# Check arguments
arguments = len(sys.argv);
usage = """usage:
stamp.py image.jpg
stamp.py image.jpg xoffset
stamp.py image.jpg xoffset yoffset
""";

if arguments < 2:
    print(usage);
    exit();

# Setup
filename = sys.argv[1];
fontname = 'analogclock.ttf';
x = 15;
y = 15;
size = 128;
brightness = 255;
alpha = 128;
outline = 1;

if arguments > 2:
    x = int(sys.argv[2]);

if arguments > 3:
    y = int(sys.argv[3]);

# Get creation time
time = datetime.datetime.fromtimestamp(FileCreated(sys.argv[1]));
hours = time.hour;
minutes = time.minute;

# Load original
base = Image.open(filename).convert('RGBA');

# Create buffer
overlay = Image.new('RGBA', base.size);
draw = ImageDraw.Draw(overlay);

# Write temp font if none exists
if not os.path.isfile(fontname):
    with open(fontname, 'w') as fdesc:
        fdesc.write(zlib.decompress(clockfont.decode('base64')));

# Load font
font = ImageFont.truetype(fontname, size);

DrawOutlinedClock(draw, font, hours, minutes, x, y, brightness, alpha, outline);

# Flatten image
result = Image.alpha_composite(base, overlay).convert('RGB');

# Write file
result.save(filename);
