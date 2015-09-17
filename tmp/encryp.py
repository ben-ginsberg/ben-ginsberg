from Crypto.Cipher import AES
from urllib import quote
import sys
import string

def encrypt(orgUrl):
    # Note that for AES the key length must be either 16, 24, or 32 bytes
    encryption_obj = AES.new('hewillneverguess')
    orgUrlArr = string.split(orgUrl,'/')
    mediaId = orgUrlArr[-1]

    # The plaintext must be a multiple of 16 bytes (for AES), so here we pad it
    # with spaces if necessary.
    mismatch = len(mediaId)%16
    if mismatch != 0:
        padding = (16-mismatch)*' '
        mediaId += padding

    ciph = encryption_obj.encrypt(mediaId)

    # Finally, to make the encrypted string safe to use in a URL we quote it
    quoted_ciph = quote(ciph)
    #print quoted_ciph
    orgUrlArr[-1] = quoted_ciph
    ciphUrl = string.join(orgUrlArr,'/')
    print ciphUrl
    return ciphUrl


if __name__ == "__main__":
    if len(sys.argv)>2:
        exit(0)
    encrypt(sys.argv[1])
