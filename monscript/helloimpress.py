# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from com.sun.star.awt import Size
from com.sun.star.awt import Point
from com.sun.star.drawing.FillStyle import SOLID as SOLID_FILLSTYLE
from com.sun.star.drawing.LineStyle import SOLID as SOLID_LINESTYLE

_GREEN, _BLACK, _RED = 0x00ff00, 0x000000, 0xff0000
_VALUES = range(0,256,1)  # 0-255 integer values

def _RGB(red: "# as 0-255", green: int, blue: "one-byte values") -> int:
    """Return a number color value made of red, green, and blue components"""

    if not (red in _VALUES and green in _VALUES and blue in _VALUES):
        raise ValueError
    return (red * 2**16) + (green * 2**8) + (blue * 2**0)

    # note:  ''red'', ''green'' and ''blue'' arguments of RGB function are one byte unsigned integer values.

def BulletprooMusicianPowerpoint():
    """Insert a RectangleShape to the currently selected slide"""

    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
    slide = model.CurrentController.CurrentPage    
    rect = model.createInstance("com.sun.star.drawing.RectangleShape")
    slide.add(rect)  # Create the rectangle

    size = Size()
    size.Width = 5000  # 50 mm
    size.Height = 3000  # 50 mm
    
    position = Point()
    position.X = 0.9*(slide.Width - size.Width)
    position.Y = 0.5*(slide.Width - size.Width)
    
    rect.setSize(size)
    rect.setPosition(position)

    rect.FillStyle = SOLID_FILLSTYLE  # or NONE
    rect.FillColor = _RGB(255, 0, 0)  # _RED
    rect.FillTransparence = 30  # 0-100 from opaque to transparent
    rect.LineStyle = SOLID_LINESTYLE  # or NONE
    rect.LineWidth = 100  # 1 mm
    rect.LineColor = _RGB(0, 0, 0)  # _BLACK
    rect.setName("MyPythonRectangle")
    rect.setString("Bulletproof musician")
    rect.CharFontName ='Lucida Calligraphy'
    rect.CharColor = _RGB(0, 255, 0)  # _GREEN
    rect.ZOrder = 1

    
g_exportedScripts = (InsertRectangleShape,)
