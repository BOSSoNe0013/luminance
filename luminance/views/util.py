import colorsys

import gi
from gi.repository import Gdk

gi.require_version('Gdk', '3.0')


def hsv_to_gdk_rgb(hue, sat, bri):
    rgb = colorsys.hsv_to_rgb(
        hue / 65535,
        sat / 255,
        bri / 255
    )

    return Gdk.RGBA(red=rgb[0], green=rgb[1], blue=rgb[2])


def is_rgb(model):
    try:
        return hasattr(model, 'hue')
    except KeyError:
        return False


def is_dimmable(model):
    try:
        return hasattr(model, 'brightness')
    except KeyError:
        return False

