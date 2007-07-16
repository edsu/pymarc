from PyZ3951 import marc_to_unicode

# see http://www.loc.gov/marc/specifications/speccharmarc8.html

import unicodedata

class MARC8_to_Unicode:
    """Converts MARC-8 to Unicode.  Note that currently, unicode strings
    aren't normalized, and some codecs (e.g. iso8859-1) will fail on
    such strings.  When I can require python 2.3, this will go away.

    Warning: MARC-8 EACC (East Asian characters) makes some
    distinctions which aren't captured in Unicode.  The LC tables give
    the option of mapping such characters either to a Unicode private
    use area, or a substitute character which (usually) gives the
    sense.  I've picked the second, so this means that the MARC data
    should be treated as primary and the Unicode data used for display
    purposes only.  (If you know of either of fonts designed for use
    with LC's private-use Unicode assignments, or of attempts to
    standardize Unicode characters to allow round-trips from EACC,
    or if you need the private-use Unicode character translations,
    please inform me, asl2@pobox.com."""


    
    basic_latin = 0x42
    ansel = 0x45
    def __init__ (self, G0 = basic_latin, G1 = ansel):
        self.g0 = G0
        self.g1 = G1

    def is_multibyte (self, charset):
        return charset == 0x31
        
    def translate (self, s):
        uni_list = []
        combinings = []
        pos = 0
        while pos < len (s):
            if s[pos] == '\x1b':
                if (s[pos +1] == s[pos+2] and
                    (s[pos +1] == '$' or s[pos+1] == '(')):
                    # '$' for multiple bytes/char, '(' for single
                    # XXX note that ',' is also acceptable for single, and
                    # '$' for double.
                    self.g0 = ord (s[pos+3])
                    # XXX or !E two-char seq for ANSEL?
                    # XXX or ')', '-', 1-char or '$)', '$-' for G1
                    pos = pos + 4
                    continue
            mb_flag = self.is_multibyte (self.g0)
                
            if mb_flag:
                d = (ord (s[pos]) * 65536 +
                     ord (s[pos+1]) * 256 +
                     ord (s[pos+2]))
                pos += 3
            else:
                d = ord (s[pos])
                pos += 1
                
            if (d < 0x20 or
                (d > 0x80 and d < 0xa0)):
                uni = unichr (d)
                continue
            
            if d > 0x80 and not mb_flag:
                (uni, cflag) = marc_to_unicode.codesets [self.g1] [d]
            else:
                (uni, cflag) = marc_to_unicode.codesets [self.g0] [d]
                
            if cflag:
                combinings.append (unichr (uni))
            else:
                uni_list.append (unichr (uni))
                if len (combinings) > 0:
                    uni_list += combinings
                    combinings = []
        # what to do if combining chars left over?
        uni_str = u"".join (uni_list)
        
        # unicodedata.normalize not available until Python 2.3        
        if hasattr (unicodedata, 'normalize'):
            uni_str = unicodedata.normalize ('NFC', uni_str)
            
        return uni_str

def test_convert (s, enc):
    conv = MARC8_to_Unicode ()
    converted = conv.translate (s)
    converted = unicodedata.normalize ('NFC', converted)
    print converted.encode (enc)

    print repr (converted)

        

if __name__ == '__main__':
    # My console is usually set to iso-8859-1.  Sorry if yours is different.
    test_convert('''The  oldest cuisine in the world : cooking in
    Mesopotamia  / Jean Bott\xe2ero ; translated by Teresa Lavender Fagan.''',
                 'iso-8859-1')
    
    test_convert (
        """$6 245-02/$1$a \x1b$$1!M>!`o!#!KPa!\\O!#!\x1b((B/$c \x1b$$1!1?!R_!#!-bb!#!!Gm!>`!#!\x1b((B; \x1b$$1!RY!YF!#!9Z6!#!!J(!Yi!#!\x1b((B;\x1b$$1!#!!BX!O>!#!!4`!4)!#!!\\e!#!!Hk!:M!#!\x1b((B... [et al.] ; \x1b$$1!Iq!MH!#!!9%!];!#!!KG!#!\x1b((B= Great garnishes / author, Huang Su-Huei ; translator, Yen-Jen Lai ; collaborators, Cheng-Tzu Chiu ... [et al.] ; photographers, Aki Ohno.""",
        'utf-8')
    

    for f in sys.argv[1:]:
        marc_file = open(f, 'rb')
        marc_text = marc_file.read ()
        while 1:
            marc_data1 = MARC(marc_text)
            print str (marc_data1)
            new = marc_data1.get_MARC ()
            marc_data2 = MARC (marc_text)
            k1 = marc_data1.fields.keys ()
            k2 = marc_data2.fields.keys ()
            assert (k1 == k2)
            for field in k1:
                same = (marc_data1.fields [field] ==
                        marc_data2.fields [field])
                assert (same)
            marc_text = marc_text[marc_data1.reclen:]
            if len (marc_text) == 0:
                break
        marc_file.close ()


