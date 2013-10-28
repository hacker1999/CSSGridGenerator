# -*- coding: utf-8 -*-
# author tz4678@gmail.com
import os
width = int(raw_input('Width in px: '))
cols = int(raw_input('Cols: '))
margin_left = int(raw_input('Left margin: '))
margin_right = int(raw_input('Right margin: '))
directory = 'grid%s_%s_%s_%s' % (width, cols, margin_left, margin_right)
try:
    os.makedirs(directory)
    os.makedirs(directory + '/css')
    os.makedirs(directory + '/img')
except OSError:
    pass
css = '.container{width:%spx;margin:auto}.column{float:left;margin-left:%spx;margin-right:%spx}'
css = css % (width, margin_left, margin_right)
i = 1
col_width = width / cols
rule = '.column%s{width:%spx}'
while i < cols:
    css += rule % (i, col_width * i - margin_left - margin_right)
    i += 1
open(directory + '/css/grid.css', 'w').write(css)
open(directory + '/css/common.css', 'w').write("""body {
    margin: 0;
}

img {
    border: 0;  
}

table {
    border-collapse: 0;
    border-spacing: 0;
}

:focus {
    outline: none;
}

.clearfix {
    clear: both;
}""")
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
row = '            <div class="column column{0}">.column{0}</div>\n            <div class="column column{1}">.column{1}</div>\n            <br class="clearfix">\n'
while i < cols:
    html += row.format(i, cols - i)
    i += 1
html += '        </div>\n    </body>\n</html>'
open(directory + '/index.htm', 'w').write(html)