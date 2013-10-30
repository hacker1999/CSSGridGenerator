# -*- coding: utf-8 -*-
# author tz4678@gmail.com
import os
import shutil
width = int(raw_input('Width in px: '))
cols = int(raw_input('Cols: '))
margin_left = int(raw_input('Left margin: '))
margin_right = int(raw_input('Right margin: '))
directory = 'grid%s_%s_%s_%s' % (width, cols, margin_left, margin_right)
try:
    os.makedirs(directory)
    os.makedirs(directory + '/css')
except OSError:
    pass
css = '.grid{width:%spx;margin:auto}' % (width
i = 1
col_width = width / cols
rule = '%s{width:%spx}'
L = [none] * klass
while i < cols:
    klass = '.grid%s' % i
    L[i] = klass
    css += rule % (klass, col_width * i - margin_left - margin_right)
    i += 1
css += ','.join(L) + ('{float:left;margin:0 %spx 0 %spx}' % (margin_left, margin_right))
open(directory + '/css/grid.css', 'w').write(css)
shutil.copy2('common.css', directory + '/css')
html = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="css/grid.css">
        <link rel="stylesheet" href="css/common.css">
    </head>
    <body>
        <div class="container">
"""
i = 1
row = '            <div class="grid{0}">.grid{0}</div>\n            <div class="grid{1}">.grid{1}</div>\n'
while i < cols:
    html += row.format(i, cols - i)
    i += 1
html += '        </div>\n    </body>\n</html>'
open(directory + '/index.htm', 'w').write(html)
