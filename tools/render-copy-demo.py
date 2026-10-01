"""Render the README's MsQuic buffer-copy illustration (requires Pillow)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1000, 326
FONT_DIR = Path("C:/Windows/Fonts")


def font(size, mono=False, bold=False):
    filename = "consola.ttf" if mono else "segoeuib.ttf" if bold else "segoeui.ttf"
    if (FONT_DIR / filename).exists():
        return ImageFont.truetype(str(FONT_DIR / filename), size)
    for fallback in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf" if mono
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf",
    ):
        if Path(fallback).exists():
            return ImageFont.truetype(fallback, size)
    return ImageFont.load_default(size=size)


BG, LINE = "#101817", "#33433e"
TEXT, MUTED = "#f2f0e8", "#a8b9ad"
GREEN, AMBER = "#a8d5b5", "#d9b477"
OLD = bytes(range(16))
CURRENT = bytes(range(0xA0, 0xB0))


def draw_frame(stage, progress=0):
    frame = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(frame)
    draw.rounded_rectangle((0, 0, WIDTH - 1, HEIGHT - 1), radius=14, outline=LINE)
    draw.text((30, 23), "MsQuic / receive batch split", font=font(19, bold=True), fill=TEXT)
    labels = {
        "before": "01 / sample extracted",
        "wrong": "02 / reversed arguments",
        "lost": "02 / current sample overwritten",
        "right": "03 / corrected arguments",
        "fixed": "03 / current sample at offset 0",
    }
    label = labels[stage]
    label_font = font(15, mono=True)
    draw.text((WIDTH - 30 - draw.textlength(label, font=label_font), 27),
              label, font=label_font, fill=AMBER if stage in ("wrong", "lost") else GREEN)
    draw.line((30, 64, 970, 64), fill=LINE)
    draw.text((242, 77), "16 bytes per header-protection sample", font=font(13), fill=MUTED)

    sample0 = CURRENT if stage == "fixed" else OLD
    sample1 = OLD if stage == "lost" else CURRENT
    for row, (data, offset) in enumerate(((sample0, "0x00"), (sample1, "0x10"))):
        top = 104 + row * 70
        draw.text((30, top + 9), f"Cipher + {offset}", font=font(17, mono=True), fill=MUTED)
        for col, value in enumerate(data):
            left = 242 + col * 45
            is_current = value >= 0xA0
            draw.rounded_rectangle((left, top, left + 39, top + 40), radius=5,
                                   fill="#1f332a" if is_current else "#1a2320",
                                   outline="#5c8068" if is_current else LINE)
            draw.text((left + 8, top + 10), f"{value:02X}", font=font(17, mono=True),
                      fill=GREEN if is_current else MUTED)

    if stage in ("wrong", "right"):
        start_y, end_y = (125, 194) if stage == "wrong" else (194, 125)
        accent = AMBER if stage == "wrong" else GREEN
        draw.line((213, start_y, 213, end_y), fill=LINE, width=2)
        y = start_y + (end_y - start_y) * progress
        draw.line((213, start_y, 213, y), fill=accent, width=3)
        draw.ellipse((209, y - 4, 217, y + 4), fill=accent)
        if progress == 1:
            direction = 1 if end_y > start_y else -1
            draw.line((208, end_y - direction * 6, 213, end_y, 218, end_y - direction * 6),
                      fill=accent, width=2)

    code = {
        "before": "batch_offset = BatchCount * CXPLAT_HP_SAMPLE_LENGTH",
        "wrong": "CxPlatMoveMemory(Cipher + batch_offset, Cipher, 16);",
        "lost": "CxPlatMoveMemory(Cipher + batch_offset, Cipher, 16);",
        "right": "CxPlatMoveMemory(Cipher, Cipher + batch_offset, 16);",
        "fixed": "CxPlatMoveMemory(Cipher, Cipher + batch_offset, 16);",
    }[stage]
    notes = {
        "before": "Illustration: BatchCount = 1. A0-AF is the current packet's sample.",
        "wrong": "The stale sample is copied over the current packet's sample.",
        "lost": "Offset 0 is still stale; the current sample has been lost.",
        "right": "Move the current packet's sample to the start of the next batch.",
        "fixed": "The next batch now starts with the current packet's sample.",
    }
    draw.line((30, 237, 970, 237), fill=LINE)
    draw.text((30, 252), code, font=font(17, mono=True),
              fill=AMBER if stage in ("wrong", "lost") else GREEN)
    draw.text((30, 286), notes[stage], font=font(15), fill=MUTED)
    return frame


def draw_mobile_frame(stage, progress=0):
    frame = Image.new("RGB", (560, 480), BG)
    draw = ImageDraw.Draw(frame)
    draw.rounded_rectangle((0, 0, 559, 479), radius=14, outline=LINE)
    draw.text((24, 20), "MsQuic / receive batch split", font=font(21, bold=True), fill=TEXT)
    captions = {
        "before": "01 / sample extracted",
        "wrong": "02 / reversed copy arguments",
        "lost": "02 / current sample overwritten",
        "right": "03 / corrected copy arguments",
        "fixed": "03 / current sample at offset zero",
    }
    draw.text((24, 55), captions[stage], font=font(17, mono=True),
              fill=AMBER if stage in ("wrong", "lost") else GREEN)
    samples = (CURRENT if stage == "fixed" else OLD, OLD if stage == "lost" else CURRENT)
    for row, data in enumerate(samples):
        top = 94 + row * 126
        draw.text((24, top), f"Cipher + 0x{row * 16:02X}", font=font(18, mono=True), fill=MUTED)
        for index, value in enumerate(data):
            x = 119 + (index % 8) * 49
            y = top + 29 + (index // 8) * 42
            is_current = value >= 0xA0
            draw.rounded_rectangle((x, y, x + 42, y + 35), radius=5,
                                   fill="#1f332a" if is_current else "#1a2320",
                                   outline="#5c8068" if is_current else LINE)
            draw.text((x + 9, y + 7), f"{value:02X}", font=font(19, mono=True),
                      fill=GREEN if is_current else MUTED)
    if stage in ("wrong", "right"):
        start, end = (161, 287) if stage == "wrong" else (287, 161)
        accent = AMBER if stage == "wrong" else GREEN
        draw.line((66, start, 66, end), fill=LINE, width=2)
        marker = start + (end - start) * progress
        draw.line((66, start, 66, marker), fill=accent, width=3)
        draw.ellipse((62, marker - 4, 70, marker + 4), fill=accent)
    draw.line((24, 350, 536, 350), fill=LINE)
    wrong = stage in ("wrong", "lost")
    color = AMBER if wrong else GREEN
    if stage == "before":
        lines = ("BatchCount = 1", "16 bytes per sample")
    else:
        lines = ("CxPlatMoveMemory(",
                 "  Cipher + batch_offset, Cipher, 16);" if wrong else
                 "  Cipher, Cipher + batch_offset, 16);")
    for index, line in enumerate(lines):
        draw.text((24, 365 + index * 27), line, font=font(18, mono=True), fill=color)
    notes = {
        "before": "A0-AF: current packet's sample.",
        "wrong": "Stale bytes overwrite the current sample.",
        "lost": "Offset zero is still stale; A0-AF is lost.",
        "right": "Copy the current sample to offset zero.",
        "fixed": "The next batch starts with A0-AF.",
    }
    draw.text((24, 438), notes[stage], font=font(18), fill=MUTED)
    return frame


def main():
    frames, mobile_frames, durations = [], [], []

    def hold(stage, ms):
        frames.append(draw_frame(stage))
        mobile_frames.append(draw_mobile_frame(stage))
        durations.append(ms)

    def move(stage):
        for index in range(13):
            frames.append(draw_frame(stage, index / 12))
            mobile_frames.append(draw_mobile_frame(stage, index / 12))
            durations.append(80)

    hold("before", 1800)
    move("wrong")
    hold("lost", 2400)
    hold("before", 1200)
    move("right")
    hold("fixed", 3200)
    output = ROOT / "assets" / "sample-copy.gif"
    frames[0].save(output, save_all=True, append_images=frames[1:],
                   duration=durations, loop=0, disposal=1, optimize=True)
    mobile_frames[0].save(ROOT / "assets" / "sample-copy-mobile.gif", save_all=True,
                          append_images=mobile_frames[1:], duration=durations,
                          loop=0, disposal=1, optimize=True)
    draw_frame("fixed").save(ROOT / "assets" / "sample-copy.png")
    print(f"{output.name}: {output.stat().st_size:,} bytes, {sum(durations) / 1000:.2f}s loop")


if __name__ == "__main__":
    main()
