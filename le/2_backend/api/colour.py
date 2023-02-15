def interpolate_linear(start_hex, end_hex, fraction):
    # Convert the hexadecimal colours to RGB values
    start_rgb = tuple(int(start_hex[i : i + 2], 16) for i in (0, 2, 4))
    end_rgb = tuple(int(end_hex[i : i + 2], 16) for i in (0, 2, 4))

    # Interpolate the RGB values using the specified percentage
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * fraction)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * fraction)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * fraction)

    # Convert the interpolated RGB values back to a hexadecimal colour
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
