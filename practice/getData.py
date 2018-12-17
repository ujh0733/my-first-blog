import urllib.request

class GetData:

    key = 'mykey'
    url =  "http://localhost/php/mapTest/mapsTest.php" % key

    def main(self):

        data = urllib.request.urlopen(self.url).read()
        f = open("sample.xml", "wb")
        f.write(data)
        f.close()

getData = GetData()
getData.main()
