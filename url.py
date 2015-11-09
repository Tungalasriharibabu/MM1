import urllib2
class lLib:
 data = urllib2.urlopen("http://b5prod1.mentoringmindsonline.com/codes_dev/_design/te_keys/_list/by-id/codes?startkey=[%22te_serial_num%22,1408870571103]&endkey=[%22te_serial_num%22,1408870571103]").read(20000) # read only 20 000 chars
 data = data.split("<br>") # then split it into lines
 for line in data:
    print line
