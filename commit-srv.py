ok = 1
msg = 'done'
sid = 12
freq = 90

#import sys
#  start_response('200 OK', [('Content-type', 'text/html')])
#  result = [ 'YPResponse: ' + ok ] + [ 'YPMessage: ' + msg ] + [ 'SID: ' + sid ] + [ 'TouchFreq: ' + freq ]
#
url = 'http://again.fm/radio/1'
f = open('/tmp/urls', 'w') 
f.write(url)
f.close()

print "\n\nContent-type text/html"
print "\nYPResponse: %s" % ok 
print "\nYPMessage: %s" % msg
print "\nSID: %s " % sid 
print "\nTouchFreq: %s " % freq 
