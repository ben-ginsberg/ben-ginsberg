from Crypto.Cipher import AES
from urllib import unquote
import sys
import string

# We've already created encryption_object as shown above
def decrypt(ciphUrl):
    encryption_obj = AES.new('hewillneverguess')
    ciphUrlArr = string.split(ciphUrl,'/')
    ciph = unquote(ciphUrlArr[-1])
    mediaId = encryption_obj.decrypt(ciph)
    #print mediaId
    #print len(mediaId)
    mediaId = mediaId.replace(' ','')
    #print mediaId
    #print len(mediaId)
    ciphUrlArr[-1] = mediaId
    orgUrl = string.join(ciphUrlArr,'/')
    print orgUrl
    return orgUrl

if __name__ == "__main__":
    if len(sys.argv)>2:
        exit(0)
    decrypt(sys.argv[1])
