import datetime
from _10gen import db

o = db.data.findOne()

print '<html><body>'
print 'Hello from Python!<br/>'

if not o:
    print 'This is the first visit'
    o = { 'lang': 'python', 'date': str(datetime.datetime.now()), 'count': 1 }
else:
    print 'Last visit was visit %d from language %s on %s' % (o['count'], o['lang'], str(o['date']))
    o['count'] = o['count'] + 1
    o['lang'] = 'python'
    o['date'] = str(datetime.datetime.now())

db.data.save(o);

print '<br/>'
print "<a href='/javascript'>JavaScript</a> &nbsp <a href='/python'>Python</a> &nbsp; <a href='/ruby'>Ruby</a>"

print '</body></html>'


