# see http://www.loc.gov/marc/specifications/speccharmarc8.html

import unicodedata
import marc8_mapping

from sys import stderr

def marc8_to_unicode(marc8):
  """
  Pass in a string, and get back a Unicode object.

    print marc8_to_unicode(record.title())

  """
  converter = MARC8_to_Unicode()
  return converter.translate(marc8)

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
    def __init__ (self, G0 = basic_latin, G1 = ansel, quiet=False):
        self.g0 = G0
        self.g1 = G1
        self.quiet = quiet

    def is_multibyte (self, charset):
        return charset == 0x31

    g0_set = set(['(', ',', '$'])
    g1_set = set([')', '-', '$'])
        
    def translate (self, s):
        uni_list = []
        combinings = []
        pos = 0
        while pos < len (s):
            # http://www.loc.gov/marc/specifications/speccharmarc8.html
            if s[pos] == '\x1b':
                next = s[pos+1]
                if (next in self.g0_set):
                    if s[pos+2] == ',' and next == '$':
                        pos += 1
                    self.g0 = ord(s[pos+2])
                    pos = pos + 3
                    continue
                elif next in self.g1_set:
                    if s[pos+2] == '-' and next == '$':
                        pos += 1
                    self.g1 = ord(s[pos+2])
                    pos = pos + 3
                    continue
            
            mb_flag = self.is_multibyte(self.g0)
                
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

            try:
                if d > 0x80 and not mb_flag:
                    (uni, cflag) = marc8_mapping.codesets [self.g1] [d]
                else:
                    (uni, cflag) = marc8_mapping.codesets [self.g0] [d]
            except KeyError, e:
                if not self.quiet:
                  stderr.write("couldn't find 0x%x in g0=%s g1=%s\n", 
                      (d, self.g0, self.g1))
                uni = ord(' ')
                cflag = False
                
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
