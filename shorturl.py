import sys
import string
import math
import hashlib

def getShortUrlFromId(orgUrl):
	base = ['q','w','e','r','t','y','u','i','o','p',
            'M','N','B','V','C','X','Z','a','s','d',
            'f','g','h','j','k','l','L','K','J','H',
            'G','F','D','S','A','z','x','c','v','b',
            'n','m','P','O','I','U','Y','T','R','E',
            'W','Q','q','w','e','r','t','y','u','i',
            'o','p','M','N','B','V','C','X','Z','a',
            's','d','f','g','h','j','k','l','L','K',
            'J','H','G','F','D','S','A','z','x','c']
    #get the media id from url
        orgUrlArr = string.split(orgUrl,'/')
    #extend the media id to 9-bit string
        mediaId = '%09.0f'%string.atoi(orgUrlArr[-1])
        sudoId = ""
        index = 0
        for i in mediaId:
            sudoId += base[index*10+string.atoi(i)]
            index = index+1
    #change media id into sudo id
        orgUrlArr[-1] = sudoId
        sudoUrl = string.join(orgUrlArr,'/')
        print "After encoding, the link changed into "+sudoUrl
        return sudoUrl
	

def getIdFromShortUrl(sudoUrl):
    base = ['q','w','e','r','t','y','u','i','o','p',
            'M','N','B','V','C','X','Z','a','s','d',
            'f','g','h','j','k','l','L','K','J','H',
            'G','F','D','S','A','z','x','c','v','b',
            'n','m','P','O','I','U','Y','T','R','E',
            'W','Q','q','w','e','r','t','y','u','i',
            'o','p','M','N','B','V','C','X','Z','a',
            's','d','f','g','h','j','k','l','L','K',
            'J','H','G','F','D','S','A','z','x','c']
    sudoUrlArr = string.split(sudoUrl,'/')
    sudoId = sudoUrlArr[-1]
    mediaId = ""
    index = 0
    for i in sudoId:
        temBase = base[index*10: (index+1)*10]
        mediaId += '%d'%(temBase.index(i))
        index = index+1
    mediaId = string.atoi(mediaId)
    sudoUrlArr[-1] = "%d"%mediaId
    orgUrl = string.join(sudoUrlArr, '/')
    print "After decoding, the link changed into " + orgUrl
    return orgUrl

if __name__=="__main__":
    if len(sys.argv)>2:
        exit(0)
    getIdFromShortUrl(getShortUrlFromId(sys.argv[1]))
#getIdFromShortUrl(sys.argv[1])