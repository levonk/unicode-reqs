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
    """A whip with a distinct handle and a long, dramatic curving lash."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0
    import math

    # Handle (brown, short and thick, clearly a grip)
    handle_color = (120, 75, 35, 255)
    handle_dark = (80, 50, 20, 255)
    # Handle body - a short cylinder at bottom-left
    hx0, hy0, hx1, hy1 = 8*s, 54*s, 24*s, 70*s
    d.rounded_rectangle([hx0, hy0, hx1, hy1], radius=int(4*s), fill=handle_color)
    # Pommel/cap at the bottom of the handle
    d.ellipse([hx0-2*s, hy1-6*s, hx1+2*s, hy1+2*s], fill=handle_dark)
    # Grip bands (wrapping pattern)
    for gy in range(int(58*s), int(68*s), int(4*s)):
        d.line([hx0+1*s, gy, hx1-1*s, gy], fill=handle_dark, width=max(1, int(2*s)))
    # Ferrule (metal band where lash attaches) at top of handle
    d.rectangle([hx0, hy0-2*s, hx1, hy0+3*s], fill=(180, 180, 180, 255))

    # Lash (long, tapering, sweeping curve from top of handle)
    lash_color = (50, 40, 35, 255)
    # Start point: top of handle
    sx, sy = (hx0+hx1)/2, hy0
    # Build a dramatic S-curve lash sweeping up and to the right
    points = []
    for i in range(0, 80):
        t = i / 79.0
        # Big sweeping arc: up, curving right, then arcing over and down
        x = sx + t * 48 * s
        y = sy - 52 * s * math.sin(t * math.pi * 0.85) + 6 * s * t * t
        points.append((x, y))

    # Draw lash with tapering width (thick near handle, thin at tip)
    for i in range(len(points) - 1):
        t = i / (len(points) - 1)
        w = max(1, int((5 - 4*t) * s))
        if w < 1:
            w = 1
        d.line([points[i], points[i+1]], fill=lash_color, width=w)

    # Cracker/popper at the very tip (frayed end)
    tip = points[-1]
    for ang in (-30, -10, 10, 30):
        rad = math.radians(ang)
        d.line([tip, (tip[0]+8*s*math.cos(rad), tip[1]+8*s*math.sin(rad))],
               fill=lash_color, width=max(1, int(1.5*s)))

    return img


def draw_tail(size):
    """A demon tail: thin, curving, ending in a spade/arrowhead tip."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0
    import math

    # Demon tail color (dark red/maroon)
    tail_color = (130, 30, 40, 255)
    tail_dark = (90, 15, 25, 255)

    # Thin curving tail starting bottom-left, sweeping up in an S-curve
    points = []
    for i in range(0, 60):
        t = i / 59.0
        # S-curve from bottom-left up to upper-right
        x = 8*s + t * 48 * s
        y = 64*s - 50 * s * t + 12 * s * math.sin(t * math.pi * 2.2)
        points.append((x, y))

    # Draw tail with tapering width (thicker at base, thin toward tip)
    for i in range(len(points) - 1):
        t = i / (len(points) - 1)
        w = max(1, int((5 - 3.5*t) * s))
        if w < 1:
            w = 1
        d.line([points[i], points[i+1]], fill=tail_color, width=w)

    # Spade/arrowhead tip (the classic demon tail ending)
    tip = points[-1]
    # Direction of the tail at the tip
    prev = points[-4]
    dx, dy = tip[0] - prev[0], tip[1] - prev[1]
    length = max(0.1, math.sqrt(dx*dx + dy*dy))
    ux, uy = dx/length, dy/length  # unit vector along tail direction
    # Perpendicular
    px, py = -uy, ux

    spade_len = 12 * s
    spade_w = 7 * s
    # Spade tip: a triangle pointing in the direction of the tail, with a notch at the base
    tip_point = (tip[0] + ux * spade_len, tip[1] + uy * spade_len)
    left = (tip[0] + px * spade_w, tip[1] + py * spade_w)
    right = (tip[0] - px * spade_w, tip[1] - py * spade_w)
    # Notch (inner V cut) at the base of the spade
    notch = (tip[0] - ux * spade_len * 0.3, tip[1] - uy * spade_len * 0.3)

    # Draw spade as two triangles forming the arrowhead with a notch
    d.polygon([tip_point, left, notch], fill=tail_color)
    d.polygon([tip_point, right, notch], fill=tail_color)
    # Outline for definition
    d.line([tip_point, left], fill=tail_dark, width=max(1, int(1.5*s)))
    d.line([tip_point, right], fill=tail_dark, width=max(1, int(1.5*s)))
    d.line([left, notch], fill=tail_dark, width=max(1, int(1.5*s)))
    d.line([right, notch], fill=tail_dark, width=max(1, int(1.5*s)))

    return img


def draw_sharp_teeth(size):
    """An open mouth with clearly visible lips and sharp, fang-like teeth."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0

    lip_color = (200, 80, 90, 255)
    lip_dark = (150, 50, 60, 255)
    mouth_interior = (90, 20, 25, 255)
    teeth_color = (250, 250, 245, 255)
    teeth_shadow = (200, 200, 195, 255)
    tongue_color = (210, 90, 95, 255)

    # Mouth interior (dark oval/rounded shape)
    d.ellipse([10*s, 18*s, 62*s, 58*s], fill=mouth_interior)

    # Upper lip (a curved band across the top of the mouth)
    d.arc([10*s, 14*s, 62*s, 40*s], 180, 360, fill=lip_color, width=max(2, int(5*s)))
    # Lower lip (a curved band across the bottom)
    d.arc([10*s, 36*s, 62*s, 62*s], 0, 180, fill=lip_color, width=max(2, int(5*s)))
    # Fill in lips more solidly
    d.ellipse([10*s, 14*s, 62*s, 22*s], fill=lip_color)  # upper lip fill
    d.ellipse([10*s, 54*s, 62*s, 62*s], fill=lip_color)  # lower lip fill

    # Re-draw mouth interior over the lip fills (leave lip bands at top/bottom)
    d.ellipse([14*s, 22*s, 58*s, 52*s], fill=mouth_interior)

    # Upper teeth (sharp triangles pointing down) - with longer canines at the sides
    n_upper = 6
    x_start = 16*s
    x_end = 56*s
    step = (x_end - x_start) / (n_upper - 1)
    for i in range(n_upper):
        cx = x_start + i * step
        # Canines (first and last) are longer; middle teeth slightly shorter
        is_canine = (i == 0 or i == n_upper - 1)
        tooth_h = 16*s if is_canine else 11*s
        tw = 6*s if is_canine else 5*s
        d.polygon([(cx-tw/2, 23*s), (cx+tw/2, 23*s), (cx, 23*s+tooth_h)], fill=teeth_color)
        # Subtle shading on teeth
        d.line([(cx, 23*s), (cx, 23*s+tooth_h)], fill=teeth_shadow, width=max(1, int(1*s)))

    # Lower teeth (sharp triangles pointing up) - offset, with canines
    for i in range(n_upper - 1):
        cx = x_start + i * step + step/2
        is_canine = (i == 0 or i == n_upper - 2)
        tooth_h = 14*s if is_canine else 10*s
        tw = 6*s if is_canine else 5*s
        d.polygon([(cx-tw/2, 51*s), (cx+tw/2, 51*s), (cx, 51*s-tooth_h)], fill=teeth_color)
        d.line([(cx, 51*s), (cx, 51*s-tooth_h)], fill=teeth_shadow, width=max(1, int(1*s)))

    # Tongue (visible at the bottom center of the mouth)
    d.ellipse([24*s, 44*s, 48*s, 52*s], fill=tongue_color)

    # Lip outline for definition
    d.ellipse([10*s, 16*s, 62*s, 60*s], outline=lip_dark, width=max(1, int(2*s)))

    return img


def draw_bull_horns(size):
    """A pair of bull horns sweeping outward to the sides then forward (not ram-curl)."""
    img = new_canvas(size)
    d = ImageDraw.Draw(img)
    s = size / 72.0
    import math

    horn_color = (215, 195, 160, 255)
    horn_dark = (165, 140, 105, 255)
    base_color = (180, 155, 120, 255)

    # Base (small forehead/skull plate where horns attach)
    d.ellipse([28*s, 50*s, 44*s, 62*s], fill=base_color)

    def draw_horn(start_x, start_y, direction):
        """Draw a single horn sweeping outward then forward, tapering to a point.
        direction: -1 for left, +1 for right."""
        points = []
        for i in range(0, 50):
            t = i / 49.0
            # Horn goes outward (to the side) then curves forward (downward in image)
            # and slightly up at the very tip
            outward = direction * (8*s + 30*s * t)
            forward = -2*s * t + 6 * s * (t ** 2)  # slight forward droop then up
            up = -18 * s * t  # rises as it goes out
            x = start_x + outward
            y = start_y + up + forward
            points.append((x, y))

        # Draw with tapering width
        for i in range(len(points) - 1):
            t = i / (len(points) - 1)
            w = max(1, int((9 - 7*t) * s))
            if w < 1:
                w = 1
            d.line([points[i], points[i+1]], fill=horn_color, width=w)

        # Sharp tip
        tip = points[-1]
        tip_r = max(1, int(2*s))
        d.ellipse([tip[0]-tip_r, tip[1]-tip_r, tip[0]+tip_r, tip[1]+tip_r], fill=horn_dark)

        # Add ridges/rings on the horn for texture
        for ring_t in (0.2, 0.4, 0.6):
            idx = int(ring_t * (len(points) - 1))
            p = points[idx]
            # Perpendicular to horn direction for ring
            if idx + 1 < len(points):
                dx = points[idx+1][0] - p[0]
                dy = points[idx+1][1] - p[1]
                length = max(0.1, math.sqrt(dx*dx + dy*dy))
                px, py = -dy/length, dx/length
                rw = max(1, int((9 - 7*ring_t) * s * 0.5))
                d.line([(p[0]-px*rw, p[1]-py*rw), (p[0]+px*rw, p[1]+py*rw)],
                       fill=horn_dark, width=max(1, int(1*s)))

    # Left horn (sweeps left, then forward/up)
    draw_horn(30*s, 50*s, -1)
    # Right horn (sweeps right, then forward/up)
    draw_horn(42*s, 50*s, 1)

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
