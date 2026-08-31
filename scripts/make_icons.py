#!/usr/bin/env python3
"""Generate the site's home-screen icons. Pure standard library, no Pillow.

Writes, in the repo root:
  apple-touch-icon.png   180x180   referenced by index.html
  icon-192.png           192x192   referenced by manifest.webmanifest
  icon-512.png           512x512   referenced by manifest.webmanifest

The mark is a thermometer on the site's accent teal: climate, on a field that
reads as security. No text, legible at favicon size. Re-run after editing the
geometry or palette, then commit the PNGs.

    python scripts/make_icons.py
"""

import os
import struct
import zlib

# Palette, taken from index.html / manifest.webmanifest.
BG = (0x1E, 0x4A, 0x52)       # --evidence teal, the brand accent
GLASS = (0xEE, 0xF1, 0xF2)    # near-white, ~ --paper
MERCURY = (0xD1, 0x49, 0x5B)  # warm red, so the shape reads as a thermometer

SS = 3  # supersample factor, downsampled for antialiasing

TARGETS = [("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)]


def render(size):
    """Return a size*size*3 RGB buffer for one icon."""
    n = size * SS
    cx = n * 0.5
    bulb_cy = n * 0.775
    bulb_r_out = n * 0.140
    bulb_r_in = n * 0.093
    stem_half_out = n * 0.076
    stem_half_in = n * 0.036
    stem_top = n * 0.135
    mercury_top = n * 0.450

    px = bytearray(bytes(BG) * (n * n))

    # Only the columns/rows the thermometer can touch need testing; the rest is BG.
    x0 = max(0, int(cx - bulb_r_out - 2))
    x1 = min(n, int(cx + bulb_r_out + 2))
    y0 = max(0, int(stem_top - stem_half_out - 2))
    y1 = min(n, int(bulb_cy + bulb_r_out + 2))

    for y in range(y0, y1):
        fy = y + 0.5
        dyb = fy - bulb_cy
        dyt = fy - stem_top
        dym = fy - mercury_top
        row = y * n * 3
        for x in range(x0, x1):
            fx = x + 0.5
            dx = fx - cx
            adx = dx if dx >= 0 else -dx

            in_mercury = (
                dx * dx + dyb * dyb <= bulb_r_in * bulb_r_in
                or (mercury_top <= fy <= bulb_cy and adx <= stem_half_in)
                or (fy < mercury_top and dx * dx + dym * dym <= stem_half_in * stem_half_in)
            )
            if in_mercury:
                c = MERCURY
            else:
                in_glass = (
                    dx * dx + dyb * dyb <= bulb_r_out * bulb_r_out
                    or (stem_top <= fy <= bulb_cy and adx <= stem_half_out)
                    or (fy < stem_top and dx * dx + dyt * dyt <= stem_half_out * stem_half_out)
                )
                if not in_glass:
                    continue  # leave the pre-filled BG
                c = GLASS

            o = row + x * 3
            px[o], px[o + 1], px[o + 2] = c

    # Box downsample SS x SS.
    out = bytearray(size * size * 3)
    area = SS * SS
    for y in range(size):
        for x in range(size):
            r = g = b = 0
            for dy in range(SS):
                base = ((y * SS + dy) * n + x * SS) * 3
                for dx in range(SS):
                    o = base + dx * 3
                    r += px[o]
                    g += px[o + 1]
                    b += px[o + 2]
            o = (y * size + x) * 3
            out[o] = r // area
            out[o + 1] = g // area
            out[o + 2] = b // area
    return bytes(out)


def write_png(path, size, rgb):
    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    stride = size * 3
    raw = bytearray()
    for y in range(size):
        raw.append(0)  # filter: none
        raw.extend(rgb[y * stride:(y + 1) * stride])

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
        f.write(chunk(b"IEND", b""))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for name, size in TARGETS:
        path = os.path.join(root, name)
        write_png(path, size, render(size))
        print(f"wrote {name}  ({size}x{size})")


if __name__ == "__main__":
    main()
