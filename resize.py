#!/usr/bin/env python
import i3
import sys

pct = float(sys.argv[1])
c = i3.filter(nodes=[], focused=True)[0]

ws = i3.get_workspaces()
for el in ws:
    if el['focused'] and el['visible']:
        cur = el
w = float(cur['rect']['width'])
h = float(cur['rect']['height'])
print "workspace width is {}".format(w)

p = w/100.0
print "p {}".format(p)

cur_pct = (float(c['rect']['width'])/w) * 100.0
diff = pct - cur_pct
print "diff {}".format(diff)
pix = str(int(abs(diff)*p))
diffp = int(abs(pct - cur_pct))

if diff > 0:
    print "ingrandisci di {} px".format(pix)
    i3.resize("grow width " + pix + " px or " + str(diffp) + " ppt" );
else:
    print "rimpicciolisci di {} px".format(pix)
    i3.resize("shrink width " + pix + " px or " + str(diffp) + " ppt" );
