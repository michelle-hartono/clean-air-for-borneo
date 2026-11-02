"""Prepare a photo for the public tracker.

Re-encodes the image from raw pixels, which drops all EXIF/GPS/camera metadata,
resizes it, and optionally blurs rectangles (addresses, phone numbers, tracking
numbers, faces that shouldn't be public).

Usage:
  python3 scripts/add_photo.py SRC photos/NAME.jpg
  python3 scripts/add_photo.py SRC photos/NAME.jpg --blur 120,340,610,420 --blur 50,900,400,960
Blur boxes are x1,y1,x2,y2 in the ORIGINAL image's pixel coordinates.
"""
import argparse
from PIL import Image, ImageFilter, ImageOps

ap = argparse.ArgumentParser()
ap.add_argument('src')
ap.add_argument('dest')
ap.add_argument('--blur', action='append', default=[], help='x1,y1,x2,y2')
ap.add_argument('--max', type=int, default=1600, help='longest side in px')
a = ap.parse_args()

im = ImageOps.exif_transpose(Image.open(a.src)).convert('RGB')
for box in a.blur:
    x1, y1, x2, y2 = (int(v) for v in box.split(','))
    region = im.crop((x1, y1, x2, y2)).filter(ImageFilter.GaussianBlur(radius=max(12, (x2 - x1) // 12)))
    im.paste(region, (x1, y1))
im.thumbnail((a.max, a.max))
clean = Image.new('RGB', im.size)
clean.putdata(list(im.getdata()))
clean.save(a.dest, 'JPEG', quality=82, optimize=True)
print(f'saved {a.dest} {clean.size[0]}x{clean.size[1]} (metadata stripped)')
