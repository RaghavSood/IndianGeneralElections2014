import urllib2
import os

baseurl = "http://ceodelhi.gov.in/WriteReadData/AssemblyConstituency/AC"

constituencyCount = 1
constituencyTotal = 70 #Delhi has 70 sub sections

while constituencyCount <= constituencyTotal:

    pdfCount = 1

    notDone = True
    constituencyCount = constituencyCount + 1

    while notDone:

        url = baseurl + str(constituencyCount).zfill(2) + "/A" + str(constituencyCount).zfill(3) + str(pdfCount).zfill(4) + ".pdf"

        pdfCount = pdfCount + 1
        try:
            u = urllib2.urlopen(url)
            response_headers = u.info()
            if response_headers.type == 'application/pdf':
                directory = "/Users/vedant/Downloads/Elections/Delhi/" + str(constituencyCount).zfill(3) + "/"
                try:
                    os.makedirs(directory)
                except OSError:
                    pass # already exists
                file_name = directory + url.split('/')[-1]
                u = urllib2.urlopen(url)
                f = open(file_name, 'wb')
                meta = u.info()
                file_size = int(meta.getheaders("Content-Length")[0])
                print "Downloading: %s Bytes: %s" % (file_name, file_size)

                file_size_dl = 0
                block_sz = 8192
                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break

                    file_size_dl += len(buffer)
                    f.write(buffer)
                    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                    status = status + chr(8)*(len(status)+1)
                    print status,

                f.close()
            else:
                notDone = False

        except urllib2.URLError, e:
            if e.code == 404:
                notDone = False
