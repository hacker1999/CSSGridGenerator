# -*- coding: utf-8 -*-
# author tz4678@gmail.com
import time
cols = int(raw_input('Columns: '))
col_width = int(raw_input('Column width, px: '))
gutter = int(raw_input('Gutter, px: '))
total = (col_width + gutter) * cols - gutter
style = '.grid {}\n\n'
style += """.container { 
    width: %spx; 
    margin: auto; 
}
""" % total
style += """
.row { 
    overflow: hidden; 
}

.clear {
    clear: both;
}"""
i = 1
selectors = []
print col_width
while i < cols:
    selector = '.span-%s' % i
    selectors.append(selector)
    style += """

%s { 
    width: %spx; 
}""" % (selector, (col_width + gutter) * i - gutter)
    i += 1
style += """

%s { 
    float: left;
    margin-right: %spx; 
}""" % (',\n'.join(selectors), gutter)
style += """

.row > [class*="span-"]:last-of-type { 
    margin-right: 0; 
}"""
i = 1
while i < cols:
    style += """

.prepend-%s { 
    margin-left: %spx; 
}""" % (i, (col_width + gutter) * i)
    i += 1
i = 1
while i < cols:
    style += """

.append-%s { 
    margin-right: %spx; 
}""" % (i, (col_width + gutter) * i)
    i += 1
open('%s.css' % str(time.time()).split('.')[0], 'w').write(style)