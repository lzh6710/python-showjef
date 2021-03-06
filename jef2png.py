#!/usr/bin/env python

"""
jef2png.py - Converts the contents of JEF files to PNG images.

Copyright (C) 2009 David Boddie <david@boddie.org.uk>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, sys
from PyQt4.QtCore import QRect, Qt
from PyQt4.QtGui import *

import jef

class Convertor:

    def __init__(self, path, stitches_only = False):
    
        self.jef = jef.Pattern(path)
        self.stitches_only = stitches_only
        self.rect = QRect()
    
    def bounding_rect(self):
    
        if not self.rect.isNull():
            return self.rect
        
        x, y = [], []
        for coordinates in self.jef.coordinates:
            i = map(lambda (op, i, j): i, coordinates)
            j = map(lambda (op, i, j): j, coordinates)
            x.append(min(i))
            x.append(max(i))
            y.append(min(j))
            y.append(max(j))
        
        return QRect(min(x), -max(y), max(x) - min(x), max(y) - min(y))
    
    def show(self, painter):
    
        painter.save()
        painter.translate(-self.bounding_rect().topLeft())
        
        i = 0
        for i in range(self.jef.threads):
        
            colour = QColor(*self.jef.colour_for_thread(i))
            coordinates = self.jef.coordinates[i]
            
            if not self.stitches_only:
                pen = QPen(QColor(200, 200, 200))
                painter.setPen(pen)
                
                for op, x, y in coordinates:
                    painter.drawEllipse(x - 2, -y - 2, 4, 4)
            
            pen = QPen(colour)
            painter.setPen(pen)
            
            mx, my = 0, 0
            for op, x, y in coordinates:
                if op == "move":
                    mx, my = x, y
                elif op == "stitch":
                    painter.drawLine(mx, -my, x, -y)
                    mx, my = x, y
            
            i += 1
        
        painter.restore()


def read_argument(name, args):

    matching = filter(lambda x: x.startswith(name), args)
    value = False
    
    for item in matching:
        args.remove(item)
        if name.endswith("="):
            value = item[len(name):]
        else:
            value = True
    
    return value


if __name__ == "__main__":

    if not 4 <= len(sys.argv) <= 7:
        sys.stderr.write("Usage: %s [--background=<colour>] [--stitches-only] [--quality=high|low] <dimensions> <JEF file> <PNG file>\n" % sys.argv[0])
        sys.exit(1)
    
    stitches_only = read_argument("--stitches-only", sys.argv)
    
    background = read_argument("--background=", sys.argv)
    if background is False:
        background_colour = qRgba(0, 0, 0, 0)
    else:
        colour = QColor(background)
        background_colour = qRgba(colour.red(), colour.green(), colour.blue(), colour.alpha())
    
    quality = read_argument("--quality=", sys.argv)
    if quality is False:
        quality = "high"
    elif quality != "high" and quality != "low":
        sys.stderr.write("Please specify either low or high quality.\n")
        sys.exit(1)
    
    dimensions = sys.argv[1]
    try:
        width, height = map(int, dimensions.split("x"))
        if width <= 0 or height <= 0:
            raise ValueError
    
    except ValueError:
        sys.stderr.write("Please specify the dimensions of the image as <width>x<height>.\n"
                         "For example: 640x480\n")
        sys.exit(1)
    
    jef_file = sys.argv[2]
    png_file = sys.argv[3]
    
    app = QApplication(sys.argv)
    
    convertor = Convertor(jef_file, stitches_only)
    rect = convertor.bounding_rect()
    
    image = QImage(rect.width(), rect.height(), QImage.Format_ARGB32)
    image.fill(background_colour)
    
    painter = QPainter()
    painter.begin(image)
    if quality == "high":
        painter.setRenderHint(QPainter.Antialiasing)
    convertor.show(painter)
    painter.end()
    
    image = image.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    image.save(png_file)
    sys.exit()
