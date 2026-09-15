#!/usr/bin/env python3
"""Generate color and B&W example images for emoji proposals at 18x18 and 72x72 px."""

from PIL import Image, ImageDraw

TRANSPARENT = (0, 0, 0, 0)


def new_canvas(size):
    return Image.new("RGBA", (size, size), TRANSPARENT)


def draw_nail_biting(size):
    """A face profile with a finger/hand at the mouth, biting a nail."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0  # scale factor

    # Face (yellow circle, left portion visible as profile)
    face_color = (255, 200, 60, 255)
    d.ellipse([8*s, 10*s, 56*s, 64*s], fill=face_color)

    # Hair / top of head
    d.ellipse([8*s, 4*s, 56*s, 30*s], fill=(120, 80, 40, 255))

    # Mouth area (open slightly)
    d.ellipse([30*s, 38*s, 48*s, 48*s], fill=(180, 90, 90, 255))

    # Finger pointing to mouth (skin tone)
    finger_color = (255, 200, 160, 255)
    # finger
    d.rounded_rectangle([40*s, 30*s, 50*s, 60*s], radius=int(4*s), fill=finger_color)
    # fingernail being bitten (small white/cream oval at fingertip near mouth)
    d.ellipse([42*s, 28*s, 50*s, 36*s], fill=(240, 220, 200, 255))

    # Eye
    d.ellipse([22*s, 24*s, 30*s, 32*s], fill=(40, 40, 40, 255))

    return img


def draw_whip(size):
    """A whip with a handle and a curved lash."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0

    # Handle (brown)
    handle_color = (101, 67, 33, 255)
    d.rounded_rectangle([6*s, 50*s, 22*s, 66*s], radius=int(3*s), fill=handle_color)
    # grip pattern
    d.line([10*s, 52*s, 10*s, 64*s], fill=(70, 45, 20, 255), width=max(1, int(2*s)))
    d.line([18*s, 52*s, 18*s, 64*s], fill=(70, 45, 20, 255), width=max(1, int(2*s)))

    # Lash (black/dark curving line from handle)
    lash_color = (40, 40, 40, 255)
    w = max(2, int(4*s))
    # Draw a curved lash using an arc-like polyline
    points = []
    cx, cy = 20*s, 52*s
    # Create a sweeping curve
    import math
    for i in range(0, 60):
        t = i / 59.0
        # parametric curve sweeping up and to the right then curving
        x = cx + t * 46 * s
        y = cy - 40 * s * math.sin(t * math.pi * 0.9) + 8 * s * t
        points.append((x, y))
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=lash_color, width=w)
    # tip cracker (small frayed end)
    tip = points[-1]
    d.line([tip, (tip[0]+6*s, tip[1]-4*s)], fill=lash_color, width=max(1, int(2*s)))
    d.line([tip, (tip[0]+6*s, tip[1]+2*s)], fill=lash_color, width=max(1, int(2*s)))

    return img


def draw_tail(size):
    """A generic mammalian tail curving upward."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0

    # Tail as a thick curved line, brown/tan
    tail_color = (160, 110, 60, 255)
    w = max(3, int(10*s))

    import math
    points = []
    for i in range(0, 50):
        t = i / 49.0
        # S-curve tail starting bottom-left, curving up and to the right
        x = 10*s + t * 50 * s
        y = 60*s - 45 * s * t + 10 * s * math.sin(t * math.pi * 1.5)
        points.append((x, y))

    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=tail_color, width=w)

    # Fluffy tip (slightly wider/fuzzy)
    tip = points[-1]
    r = int(7*s)
    d.ellipse([tip[0]-r, tip[1]-r, tip[0]+r, tip[1]+r], fill=tail_color)

    return img


def draw_sharp_teeth(size):
    """An open mouth showing pointed/sharp teeth."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0

    # Mouth outline (dark red interior)
    d.rounded_rectangle([10*s, 20*s, 62*s, 56*s], radius=int(8*s), fill=(140, 30, 30, 255))

    # Upper teeth (white triangles pointing down)
    teeth_color = (255, 255, 255, 255)
    n_upper = 5
    x_start = 14*s
    x_end = 58*s
    step = (x_end - x_start) / (n_upper - 1)
    tw = 7*s  # tooth width
    for i in range(n_upper):
        cx = x_start + i * step
        d.polygon([(cx-tw/2, 22*s), (cx+tw/2, 22*s), (cx, 36*s)], fill=teeth_color)

    # Lower teeth (white triangles pointing up)
    for i in range(n_upper):
        cx = x_start + i * step + step/2
        d.polygon([(cx-tw/2, 54*s), (cx+tw/2, 54*s), (cx, 42*s)], fill=teeth_color)

    # Lips outline
    d.rounded_rectangle([8*s, 18*s, 64*s, 58*s], radius=int(9*s), outline=(180, 80, 80, 255), width=max(1, int(3*s)))

    return img


def draw_bull_horns(size):
    """A pair of curved bull horns."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0

    horn_color = (200, 180, 150, 255)
    horn_dark = (150, 130, 100, 255)

    import math

    # Left horn
    left_pts = []
    for i in range(0, 40):
        t = i / 39.0
        # Start near center-bottom, curve up and out to the left
        angle = math.pi * (0.5 + 0.7 * t)
        r = 8*s + 26*s * t
        cx, cy = 30*s, 40*s
        x = cx - r * math.sin(angle - math.pi*0.5) * 0.6
        y = cy - r * math.cos(angle - math.pi*0.5) * 0.8
        left_pts.append((x, y))

    # Right horn (mirror)
    right_pts = []
    for i in range(0, 40):
        t = i / 39.0
        angle = math.pi * (0.5 + 0.7 * t)
        r = 8*s + 26*s * t
        cx, cy = 42*s, 40*s
        x = cx + r * math.sin(angle - math.pi*0.5) * 0.6
        y = cy - r * math.cos(angle - math.pi*0.5) * 0.8
        right_pts.append((x, y))

    w_base = max(3, int(10*s))
    w_tip = max(1, int(2*s))

    def draw_tapered(pts, w_start, w_end):
        for i in range(len(pts) - 1):
            t = i / (len(pts) - 1)
            w = int(w_start + (w_end - w_start) * t)
            d.line([pts[i], pts[i+1]], fill=horn_color, width=w)

    draw_tapered(left_pts, w_base, w_tip)
    draw_tapered(right_pts, w_base, w_tip)

    # Tips (sharper)
    d.ellipse([left_pts[-1][0]-w_tip, left_pts[-1][1]-w_tip, left_pts[-1][0]+w_tip, left_pts[-1][1]+w_tip], fill=horn_dark)
    d.ellipse([right_pts[-1][0]-w_tip, right_pts[-1][1]-w_tip, right_pts[-1][0]+w_tip, right_pts[-1][1]+w_tip], fill=horn_dark)

    # Base plate (small skull/head hint)
    d.ellipse([26*s, 38*s, 46*s, 56*s], fill=(200, 180, 150, 255))

    return img


EMOJIS = {
    "nail-biting": draw_nail_biting,
    "whip": draw_whip,
    "tail": draw_tail,
    "sharp-teeth": draw_sharp_teeth,
    "bull-horns": draw_bull_horns,
}


def to_bw(img):
    """Convert to true black & white (not grayscale) using alpha-weighted luminance threshold."""
    gray = img.convert("LA").convert("RGBA")
    bw = Image.new("RGBA", img.size, TRANSPARENT)
    px = img.load()
    bw_px = bw.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            bw_px[x, y] = (0, 0, 0, 255) if lum < 180 else (255, 255, 255, 255)
    return bw


def main():
    for name, draw_fn in EMOJIS.items():
        for size in (72, 18):
            color = draw_fn(size)
            color.save(f"{name}/images/{name}-color-{size}.png")
            bw = to_bw(draw_fn(size))
            bw.save(f"{name}/images/{name}-bw-{size}.png")
        print(f"Generated images for {name}")


if __name__ == "__main__":
    main()
