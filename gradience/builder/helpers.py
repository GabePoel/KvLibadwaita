from builder.settings import BASE16_DIR


def available_color_schemes():
    color_schemes = []
    for p in BASE16_DIR.iterdir():
        if p.is_file():
            color_schemes.append(p.stem)
    return color_schemes
