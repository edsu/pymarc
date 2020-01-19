# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

"""MARC-8 mapping."""

CHARSET_34 = {  # Extended Arabic
    0xA1: (0x6FD, 0),  # DOUBLE ALEF WITH HAMZA ABOVE / ARABIC SIGN SINDHI AMPERSAND
    0xA2: (0x672, 0),  # ARABIC LETTER ALEF WITH WAVY HAMZA ABOVE
    0xA3: (0x673, 0),  # ARABIC LETTER ALEF WITH WAVY HAMZA BELOW
    0xA4: (0x679, 0),  # ARABIC LETTER TTEH
    0xA5: (0x67A, 0),  # ARABIC LETTER TTEHEH
    0xA6: (0x67B, 0),  # ARABIC LETTER BBEH
    0xA7: (0x67C, 0),  # ARABIC LETTER TEH WITH RING
    0xA8: (0x67D, 0),  # ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS
    0xA9: (0x67E, 0),  # ARABIC LETTER PEH
    0xAA: (0x67F, 0),  # ARABIC LETTER TEHEH
    0xAB: (0x680, 0),  # ARABIC LETTER BEHEH
    0xAC: (0x681, 0),  # ARABIC LETTER HAH WITH HAMZA ABOVE
    0xAD: (0x682, 0),  # ARABIC LETTER HAH WITH TWO ABOVE DOTS VERTICAL ABOVE
    0xAE: (0x683, 0),  # ARABIC LETTER NYEH
    0xAF: (0x684, 0),  # ARABIC LETTER DYEH
    0xB0: (0x685, 0),  # ARABIC LETTER HAH WITH THREE DOTS ABOVE
    0xB1: (0x686, 0),  # ARABIC LETTER TCHEH
    0xB2: (0x6BF, 0),  # ARABIC LETTER TCHEH WITH DOT ABOVE
    0xB3: (0x687, 0),  # ARABIC LETTER TCHEHEH
    0xB4: (0x688, 0),  # ARABIC LETTER DDAL
    0xB5: (0x689, 0),  # ARABIC LETTER DAL WITH RING
    0xB6: (0x68A, 0),  # ARABIC LETTER DAL WITH DOT BELOW
    0xB7: (0x68B, 0),  # ARABIC LETTER DAL WITH DOT BELOW AND SMALL TAH
    0xB8: (0x68C, 0),  # ARABIC LETTER DAHAL
    0xB9: (0x68D, 0),  # ARABIC LETTER DDAHAL
    0xBA: (0x68E, 0),  # ARABIC LETTER DUL
    0xBB: (0x68F, 0),  # ARABIC LETTER DAL WITH THREE DOTS ABOVE DOWNWARDS
    0xBC: (0x690, 0),  # ARABIC LETTER DAL WITH FOUR DOTS ABOVE
    0xBD: (0x691, 0),  # ARABIC LETTER RREH
    0xBE: (0x692, 0),  # ARABIC LETTER REH WITH SMALL V
    0xBF: (0x693, 0),  # ARABIC LETTER REH WITH RING
    0xC0: (0x694, 0),  # ARABIC LETTER REH WITH DOT BELOW
    0xC1: (0x695, 0),  # ARABIC LETTER REH WITH SMALL V BELOW
    0xC2: (0x696, 0),  # ARABIC LETTER REH WITH DOT BELOW AND DOT ABOVE
    0xC3: (0x697, 0),  # ARABIC LETTER REH WITH TWO DOTS ABOVE
    0xC4: (0x698, 0),  # ARABIC LETTER JEH
    0xC5: (0x699, 0),  # ARABIC LETTER REH WITH FOUR DOTS ABOVE
    0xC6: (0x69A, 0),  # ARABIC LETTER SEEN WITH DOT BELOW AND DOT ABOVE
    0xC7: (0x69B, 0),  # ARABIC LETTER SEEN WITH THREE DOTS BELOW
    0xC8: (0x69C, 0),  # ARABIC LETTER SEEN WITH THREE DOTS BELOW AND THREE DOTS ABOVE
    0xC9: (0x6FA, 0),  # ARABIC LETTER SHEEN WITH DOT BELOW
    0xCA: (0x69D, 0),  # ARABIC LETTER SAD WITH TWO DOTS BELOW
    0xCB: (0x69E, 0),  # ARABIC LETTER SAD WITH THREE DOTS ABOVE
    0xCC: (0x6FB, 0),  # ARABIC LETTER DAD WITH DOT BELOW
    0xCD: (0x69F, 0),  # ARABIC LETTER TAH WITH THREE DOTS ABOVE
    0xCE: (0x6A0, 0),  # ARABIC LETTER AIN WITH THREE DOTS ABOVE
    0xCF: (0x6FC, 0),  # ARABIC LETTER GHAIN WITH DOT BELOW
    0xD0: (0x6A1, 0),  # ARABIC LETTER DOTLESS FEH
    0xD1: (0x6A2, 0),  # ARABIC LETTER FEH WITH DOT MOVED BELOW
    0xD2: (0x6A3, 0),  # ARABIC LETTER FEH WITH DOT BELOW
    0xD3: (0x6A4, 0),  # ARABIC LETTER VEH
    0xD4: (0x6A5, 0),  # ARABIC LETTER FEH WITH THREE DOTS BELOW
    0xD5: (0x6A6, 0),  # ARABIC LETTER PEHEH
    0xD6: (0x6A7, 0),  # ARABIC LETTER QAF WITH DOT ABOVE
    0xD7: (0x6A8, 0),  # ARABIC LETTER QAF WITH THREE DOTS ABOVE
    0xD8: (0x6A9, 0),  # ARABIC LETTER KEHEH
    0xD9: (0x6AA, 0),  # ARABIC LETTER SWASH KAF
    0xDA: (0x6AB, 0),  # ARABIC LETTER KAF WITH RING
    0xDB: (0x6AC, 0),  # ARABIC LETTER KAF WITH DOT ABOVE
    0xDC: (0x6AD, 0),  # ARABIC LETTER NG
    0xDD: (0x6AE, 0),  # ARABIC LETTER KAF WITH THREE DOTS BELOW
    0xDE: (0x6AF, 0),  # ARABIC LETTER GAF
    0xDF: (0x6B0, 0),  # ARABIC LETTER GAF WITH RING
    0xE0: (0x6B1, 0),  # ARABIC LETTER NGOEH
    0xE1: (0x6B2, 0),  # ARABIC LETTER GAF WITH TWO DOTS BELOW
    0xE2: (0x6B3, 0),  # ARABIC LETTER GUEH
    0xE3: (0x6B4, 0),  # ARABIC LETTER GAF WITH THREE DOTS ABOVE
    0xE4: (0x6B5, 0),  # ARABIC LETTER LAM WITH SMALL V
    0xE5: (0x6B6, 0),  # ARABIC LETTER LAM WITH DOT ABOVE
    0xE6: (0x6B7, 0),  # ARABIC LETTER LAM WITH THREE DOTS ABOVE
    0xE7: (0x6B8, 0),  # ARABIC LETTER LAM WITH THREE DOTS BELOW
    0xE8: (0x6BA, 0),  # ARABIC LETTER NOON GHUNNA
    0xE9: (0x6BB, 0),  # ARABIC LETTER RNOON
    0xEA: (0x6BC, 0),  # ARABIC LETTER NOON WITH RING
    0xEB: (0x6BD, 0),  # ARABIC LETTER NOON WITH THREE DOTS ABOVE
    0xEC: (0x6B9, 0),  # ARABIC LETTER NOON WITH DOT BELOW
    0xED: (0x6BE, 0),  # ARABIC LETTER HEH DOACHASHMEE
    0xEE: (0x6C0, 0),  # HEH WITH HAMZA ABOVE / ARABIC LETTER HEH WITH YEH ABOVE
    0xEF: (0x6C4, 0),  # ARABIC LETTER WAW WITH RING
    0xF0: (0x6C5, 0),  # KYRGHYZ OE / ARABIC LETTER KIRGHIZ OE
    0xF1: (0x6C6, 0),  # ARABIC LETTER OE
    0xF2: (0x6CA, 0),  # ARABIC LETTER WAW WITH TWO DOTS ABOVE
    0xF3: (0x6CB, 0),  # ARABIC LETTER VE
    0xF4: (0x6CD, 0),  # ARABIC LETTER YEH WITH TAIL
    0xF5: (0x6CE, 0),  # ARABIC LETTER YEH WITH SMALL V
    0xF6: (0x6D0, 0),  # ARABIC LETTER E
    0xF7: (0x6D2, 0),  # ARABIC LETTER YEH BARREE
    0xF8: (0x6D3, 0),  # ARABIC LETTER YEH BARREE WITH HAMZA ABOVE
    0xFD: (0x306, 1),  # SHORT E / COMBINING BREVE
    0xFE: (0x30C, 1),  # SHORT U / COMBINING CARON
}
CHARSET_45 = {  # Extended Latin (ANSEL)
    0x88: (0x98, 0),  # NON-SORT BEGIN / START OF STRING
    0x89: (0x9C, 0),  # NON-SORT END / STRING TERMINATOR
    0x8D: (0x200D, 0),  # JOINER / ZERO WIDTH JOINER
    0x8E: (0x200C, 0),  # NON-JOINER / ZERO WIDTH NON-JOINER
    0xA1: (0x141, 0),  # UPPERCASE POLISH L / LATIN CAPITAL LETTER L WITH STROKE
    0xA2: (0xD8, 0),  # UPPERCASE SCANDINAVIAN O / LATIN CAPITAL LETTER O WITH STROKE
    0xA3: (0x110, 0),  # UPPERCASE D WITH CROSSBAR / LATIN CAPITAL LETTER D WITH STROKE
    0xA4: (
        0xDE,
        0,
    ),  # UPPERCASE ICELANDIC THORN / LATIN CAPITAL LETTER THORN (Icelandic)
    0xA5: (0xC6, 0),  # UPPERCASE DIGRAPH AE / LATIN CAPITAL LIGATURE AE
    0xA6: (0x152, 0),  # UPPERCASE DIGRAPH OE / LATIN CAPITAL LIGATURE OE
    0xA7: (0x2B9, 0),  # SOFT SIGN, PRIME / MODIFIER LETTER PRIME
    0xA8: (0xB7, 0),  # MIDDLE DOT
    0xA9: (0x266D, 0),  # MUSIC FLAT SIGN
    0xAA: (0xAE, 0),  # PATENT MARK / REGISTERED SIGN
    0xAB: (0xB1, 0),  # PLUS OR MINUS / PLUS-MINUS SIGN
    0xAC: (0x1A0, 0),  # UPPERCASE O-HOOK / LATIN CAPITAL LETTER O WITH HORN
    0xAD: (0x1AF, 0),  # UPPERCASE U-HOOK / LATIN CAPITAL LETTER U WITH HORN
    0xAE: (0x2BC, 0),  # ALIF / MODIFIER LETTER RIGHT HALF RING
    0xB0: (0x2BB, 0),  # AYN / MODIFIER LETTER TURNED COMMA
    0xB1: (0x142, 0),  # LOWERCASE POLISH L / LATIN SMALL LETTER L WITH STROKE
    0xB2: (0xF8, 0),  # LOWERCASE SCANDINAVIAN O / LATIN SMALL LETTER O WITH STROKE
    0xB3: (0x111, 0),  # LOWERCASE D WITH CROSSBAR / LATIN SMALL LETTER D WITH STROKE
    0xB4: (0xFE, 0),  # LOWERCASE ICELANDIC THORN / LATIN SMALL LETTER THORN (Icelandic)
    0xB5: (0xE6, 0),  # LOWERCASE DIGRAPH AE / LATIN SMALL LIGATURE AE
    0xB6: (0x153, 0),  # LOWERCASE DIGRAPH OE / LATIN SMALL LIGATURE OE
    0xB7: (0x2BA, 0),  # HARD SIGN, DOUBLE PRIME / MODIFIER LETTER DOUBLE PRIME
    0xB8: (0x131, 0),  # LOWERCASE TURKISH I / LATIN SMALL LETTER DOTLESS I
    0xB9: (0xA3, 0),  # BRITISH POUND / POUND SIGN
    0xBA: (0xF0, 0),  # LOWERCASE ETH / LATIN SMALL LETTER ETH (Icelandic)
    0xBC: (0x1A1, 0),  # LOWERCASE O-HOOK / LATIN SMALL LETTER O WITH HORN
    0xBD: (0x1B0, 0),  # LOWERCASE U-HOOK / LATIN SMALL LETTER U WITH HORN
    0xC0: (0xB0, 0),  # DEGREE SIGN
    0xC1: (0x2113, 0),  # SCRIPT SMALL L
    0xC2: (0x2117, 0),  # SOUND RECORDING COPYRIGHT
    0xC3: (0xA9, 0),  # COPYRIGHT SIGN
    0xC4: (0x266F, 0),  # MUSIC SHARP SIGN
    0xC5: (0xBF, 0),  # INVERTED QUESTION MARK
    0xC6: (0xA1, 0),  # INVERTED EXCLAMATION MARK
    0xC7: (0xDF, 0),  # ESZETT SYMBOL
    0xC8: (0x20AC, 0),  # EURO SIGN
    0xE0: (0x309, 1),  # PSEUDO QUESTION MARK / COMBINING HOOK ABOVE
    0xE1: (0x300, 1),  # GRAVE / COMBINING GRAVE ACCENT (Varia)
    0xE2: (0x301, 1),  # ACUTE / COMBINING ACUTE ACCENT (Oxia)
    0xE3: (0x302, 1),  # CIRCUMFLEX / COMBINING CIRCUMFLEX ACCENT
    0xE4: (0x303, 1),  # TILDE / COMBINING TILDE
    0xE5: (0x304, 1),  # MACRON / COMBINING MACRON
    0xE6: (0x306, 1),  # BREVE / COMBINING BREVE (Vrachy)
    0xE7: (0x307, 1),  # SUPERIOR DOT / COMBINING DOT ABOVE
    0xE8: (0x308, 1),  # UMLAUT, DIAERESIS / COMBINING DIAERESIS (Dialytika)
    0xE9: (0x30C, 1),  # HACEK / COMBINING CARON
    0xEA: (0x30A, 1),  # CIRCLE ABOVE, ANGSTROM / COMBINING RING ABOVE
    0xEB: (0xFE20, 1),  # LIGATURE, FIRST HALF / COMBINING LIGATURE LEFT HALF
    0xEC: (0xFE21, 1),  # LIGATURE, SECOND HALF / COMBINING LIGATURE RIGHT HALF
    0xED: (0x315, 1),  # HIGH COMMA, OFF CENTER / COMBINING COMMA ABOVE RIGHT
    0xEE: (0x30B, 1),  # DOUBLE ACUTE / COMBINING DOUBLE ACUTE ACCENT
    0xEF: (0x310, 1),  # CANDRABINDU / COMBINING CANDRABINDU
    0xF0: (0x327, 1),  # CEDILLA / COMBINING CEDILLA
    0xF1: (0x328, 1),  # RIGHT HOOK, OGONEK / COMBINING OGONEK
    0xF2: (0x323, 1),  # DOT BELOW / COMBINING DOT BELOW
    0xF3: (0x324, 1),  # DOUBLE DOT BELOW / COMBINING DIAERESIS BELOW
    0xF4: (0x325, 1),  # CIRCLE BELOW / COMBINING RING BELOW
    0xF5: (0x333, 1),  # DOUBLE UNDERSCORE / COMBINING DOUBLE LOW LINE
    0xF6: (0x332, 1),  # UNDERSCORE / COMBINING LOW LINE
    0xF7: (0x326, 1),  # LEFT HOOK (COMMA BELOW) / COMBINING COMMA BELOW
    0xF8: (0x31C, 1),  # RIGHT CEDILLA / COMBINING LEFT HALF RING BELOW
    0xF9: (0x32E, 1),  # UPADHMANIYA / COMBINING BREVE BELOW
    0xFA: (0xFE22, 1),  # DOUBLE TILDE, FIRST HALF / COMBINING DOUBLE TILDE LEFT HALF
    0xFB: (0xFE23, 1),  # DOUBLE TILDE, SECOND HALF / COMBINING DOUBLE TILDE RIGHT HALF
    0xFE: (0x313, 1),  # HIGH COMMA, CENTERED / COMBINING COMMA ABOVE (Psili)
}
CHARSET_33 = {  # Basic Arabic
    0x21: (0x21, 0),  # EXCLAMATION MARK
    0x22: (0x22, 0),  # QUOTATION MARK
    0x23: (0x23, 0),  # NUMBER SIGN
    0x24: (0x24, 0),  # DOLLAR SIGN
    0x25: (0x66A, 0),  # PERCENT SIGN / ARABIC PERCENT SIGN
    0x26: (0x26, 0),  # AMPERSAND
    0x27: (0x27, 0),  # APOSTROPHE
    0x28: (0x28, 0),  # OPENING PARENTHESIS / LEFT PARENTHESIS
    0x29: (0x29, 0),  # CLOSING PARENTHESIS / RIGHT PARENTHESIS
    0x2A: (0x66D, 0),  # ASTERISK / ARABIC FIVE POINTED STAR
    0x2B: (0x2B, 0),  # PLUS SIGN
    0x2C: (0x60C, 0),  # ARABIC COMMA
    0x2D: (0x2D, 0),  # HYPHEN-MINUS
    0x2E: (0x2E, 0),  # PERIOD, DECIMAL POINT / FULL STOP
    0x2F: (0x2F, 0),  # SLASH / SOLIDUS
    0x30: (0x660, 0),  # ARABIC-INDIC DIGIT ZERO
    0x31: (0x661, 0),  # ARABIC-INDIC DIGIT ONE
    0x32: (0x662, 0),  # ARABIC-INDIC DIGIT TWO
    0x33: (0x663, 0),  # ARABIC-INDIC DIGIT THREE
    0x34: (0x664, 0),  # ARABIC-INDIC DIGIT FOUR
    0x35: (0x665, 0),  # ARABIC-INDIC DIGIT FIVE
    0x36: (0x666, 0),  # ARABIC-INDIC DIGIT SIX
    0x37: (0x667, 0),  # ARABIC-INDIC DIGIT SEVEN
    0x38: (0x668, 0),  # ARABIC-INDIC DIGIT EIGHT
    0x39: (0x669, 0),  # ARABIC-INDIC DIGIT NINE
    0x3A: (0x3A, 0),  # COLON
    0x3B: (0x61B, 0),  # ARABIC SEMICOLON
    0x3C: (0x3C, 0),  # LESS-THAN SIGN
    0x3D: (0x3D, 0),  # EQUALS SIGN
    0x3E: (0x3E, 0),  # GREATER-THAN SIGN
    0x3F: (0x61F, 0),  # ARABIC QUESTION MARK
    0x41: (0x621, 0),  # HAMZAH / ARABIC LETTER HAMZA
    0x42: (0x622, 0),  # ARABIC LETTER ALEF WITH MADDA ABOVE
    0x43: (0x623, 0),  # ARABIC LETTER ALEF WITH HAMZA ABOVE
    0x44: (0x624, 0),  # ARABIC LETTER WAW WITH HAMZA ABOVE
    0x45: (0x625, 0),  # ARABIC LETTER ALEF WITH HAMZA BELOW
    0x46: (0x626, 0),  # ARABIC LETTER YEH WITH HAMZA ABOVE
    0x47: (0x627, 0),  # ARABIC LETTER ALEF
    0x48: (0x628, 0),  # ARABIC LETTER BEH
    0x49: (0x629, 0),  # ARABIC LETTER TEH MARBUTA
    0x4A: (0x62A, 0),  # ARABIC LETTER TEH
    0x4B: (0x62B, 0),  # ARABIC LETTER THEH
    0x4C: (0x62C, 0),  # ARABIC LETTER JEEM
    0x4D: (0x62D, 0),  # ARABIC LETTER HAH
    0x4E: (0x62E, 0),  # ARABIC LETTER KHAH
    0x4F: (0x62F, 0),  # ARABIC LETTER DAL
    0x50: (0x630, 0),  # ARABIC LETTER THAL
    0x51: (0x631, 0),  # ARABIC LETTER REH
    0x52: (0x632, 0),  # ARABIC LETTER ZAIN
    0x53: (0x633, 0),  # ARABIC LETTER SEEN
    0x54: (0x634, 0),  # ARABIC LETTER SHEEN
    0x55: (0x635, 0),  # ARABIC LETTER SAD
    0x56: (0x636, 0),  # ARABIC LETTER DAD
    0x57: (0x637, 0),  # ARABIC LETTER TAH
    0x58: (0x638, 0),  # ARABIC LETTER ZAH
    0x59: (0x639, 0),  # ARABIC LETTER AIN
    0x5A: (0x63A, 0),  # ARABIC LETTER GHAIN
    0x5B: (0x5B, 0),  # OPENING SQUARE BRACKET / LEFT SQUARE BRACKET
    0x5D: (0x5D, 0),  # CLOSING SQUARE BRACKET / RIGHT SQUARE BRACKET
    0x60: (0x640, 0),  # ARABIC TATWEEL
    0x61: (0x641, 0),  # ARABIC LETTER FEH
    0x62: (0x642, 0),  # ARABIC LETTER QAF
    0x63: (0x643, 0),  # ARABIC LETTER KAF
    0x64: (0x644, 0),  # ARABIC LETTER LAM
    0x65: (0x645, 0),  # ARABIC LETTER MEEM
    0x66: (0x646, 0),  # ARABIC LETTER NOON
    0x67: (0x647, 0),  # ARABIC LETTER HEH
    0x68: (0x648, 0),  # ARABIC LETTER WAW
    0x69: (0x649, 0),  # ARABIC LETTER ALEF MAKSURA
    0x6A: (0x64A, 0),  # ARABIC LETTER YEH
    0x6B: (0x64B, 1),  # ARABIC FATHATAN
    0x6C: (0x64C, 1),  # ARABIC DAMMATAN
    0x6D: (0x64D, 1),  # ARABIC KASRATAN
    0x6E: (0x64E, 1),  # ARABIC FATHA
    0x6F: (0x64F, 1),  # ARABIC DAMMA
    0x70: (0x650, 1),  # ARABIC KASRA
    0x71: (0x651, 1),  # ARABIC SHADDA
    0x72: (0x652, 1),  # ARABIC SUKUN
    0x73: (0x671, 0),  # ARABIC LETTER ALEF WASLA
    0x74: (0x670, 0),  # ARABIC LETTER SUPERSCRIPT ALEF
    0x78: (0x66C, 0),  # ARABIC THOUSANDS SEPARATOR
    0x79: (0x201D, 0),  # RIGHT DOUBLE QUOTATION MARK
    0x7A: (0x201C, 0),  # LEFT DOUBLE QUOTATION MARK
}
CHARSET_32 = {  # Basic Hebrew
    0x21: (0x21, 0),  # EXCLAMATION MARK
    0x22: (0x5F4, 0),  # QUOTATION MARK, GERSHAYIM / HEBREW PUNCTUATION GERSHAYIM
    0x23: (0x23, 0),  # NUMBER SIGN
    0x24: (0x24, 0),  # DOLLAR SIGN
    0x25: (0x25, 0),  # PERCENT SIGN
    0x26: (0x26, 0),  # AMPERSAND
    0x27: (0x5F3, 0),  # APOSTROPHE, GERESH / HEBREW PUNCTUATION GERESH
    0x28: (0x28, 0),  # OPENING PARENTHESIS / LEFT PARENTHESIS
    0x29: (0x29, 0),  # CLOSING PARENTHESIS / RIGHT PARENTHESIS
    0x2A: (0x2A, 0),  # ASTERISK
    0x2B: (0x2B, 0),  # PLUS SIGN
    0x2C: (0x2C, 0),  # COMMA
    0x2D: (0x5BE, 0),  # HYPHEN-MINUS, MAKEF / HEBREW PUNCTUATION MAQAF
    0x2E: (0x2E, 0),  # PERIOD, DECIMAL POINT / FULL STOP
    0x2F: (0x2F, 0),  # SLASH / SOLIDUS
    0x30: (0x30, 0),  # DIGIT ZERO
    0x31: (0x31, 0),  # DIGIT ONE
    0x32: (0x32, 0),  # DIGIT TWO
    0x33: (0x33, 0),  # DIGIT THREE
    0x34: (0x34, 0),  # DIGIT FOUR
    0x35: (0x35, 0),  # DIGIT FIVE
    0x36: (0x36, 0),  # DIGIT SIX
    0x37: (0x37, 0),  # DIGIT SEVEN
    0x38: (0x38, 0),  # DIGIT EIGHT
    0x39: (0x39, 0),  # DIGIT NINE
    0x3A: (0x3A, 0),  # COLON
    0x3B: (0x3B, 0),  # SEMICOLON
    0x3C: (0x3C, 0),  # LESS-THAN SIGN
    0x3D: (0x3D, 0),  # EQUALS SIGN
    0x3E: (0x3E, 0),  # GREATER-THAN SIGN
    0x3F: (0x3F, 0),  # QUESTION MARK
    0x40: (0x5B7, 1),  # HEBREW POINT PATAH
    0x41: (0x5B8, 1),  # KAMATS / HEBREW POINT QAMATS
    0x42: (0x5B6, 1),  # HEBREW POINT SEGOL
    0x43: (0x5B5, 1),  # TSEREH / HEBREW POINT TSERE
    0x44: (0x5B4, 1),  # HIRIK / HEBREW POINT HIRIQ
    0x45: (0x5B9, 1),  # HOLAM, LEFT SIN DOT / HEBREW POINT HOLAM
    0x46: (0x5BB, 1),  # KUBUTS / HEBREW POINT QUBUTS
    0x47: (0x5B0, 1),  # HEBREW POINT SHEVA
    0x48: (0x5B2, 1),  # HEBREW POINT HATAF PATAH
    0x49: (0x5B3, 1),  # HATAF KAMATS / HEBREW POINT HATAF QAMATS
    0x4A: (0x5B1, 1),  # HEBREW POINT HATAF SEGOL
    0x4B: (0x5BC, 1),  # HEBREW POINT DAGESH OR MAPIQ
    0x4C: (0x5BF, 1),  # RAFEH / HEBREW POINT RAFE
    0x4D: (0x5C1, 1),  # RIGHT SHIN DOT / HEBREW POINT  SHIN DOT
    0x4E: (0xFB1E, 1),  # VARIKA / HEBREW POINT JUDEO-SPANISH VARIKA
    0x5B: (0x5B, 0),  # OPENING SQUARE BRACKET / LEFT SQUARE BRACKET
    0x5D: (0x5D, 0),  # CLOSING SQUARE BRACKET / RIGHT SQUARE BRACKET
    0x60: (0x5D0, 0),  # HEBREW LETTER ALEF
    0x61: (0x5D1, 0),  # HEBREW LETTER BET
    0x62: (0x5D2, 0),  # HEBREW LETTER GIMEL
    0x63: (0x5D3, 0),  # HEBREW LETTER DALET
    0x64: (0x5D4, 0),  # HEBREW LETTER HE
    0x65: (0x5D5, 0),  # HEBREW LETTER VAV
    0x66: (0x5D6, 0),  # HEBREW LETTER ZAYIN
    0x67: (0x5D7, 0),  # HEBREW LETTER HET
    0x68: (0x5D8, 0),  # HEBREW LETTER TET
    0x69: (0x5D9, 0),  # HEBREW LETTER YOD
    0x6A: (0x5DA, 0),  # HEBREW LETTER FINAL KAF
    0x6B: (0x5DB, 0),  # HEBREW LETTER KAF
    0x6C: (0x5DC, 0),  # HEBREW LETTER LAMED
    0x6D: (0x5DD, 0),  # HEBREW LETTER FINAL MEM
    0x6E: (0x5DE, 0),  # HEBREW LETTER MEM
    0x6F: (0x5DF, 0),  # HEBREW LETTER FINAL NUN
    0x70: (0x5E0, 0),  # HEBREW LETTER NUN
    0x71: (0x5E1, 0),  # HEBREW LETTER SAMEKH
    0x72: (0x5E2, 0),  # HEBREW LETTER AYIN
    0x73: (0x5E3, 0),  # HEBREW LETTER FINAL PE
    0x74: (0x5E4, 0),  # HEBREW LETTER PE
    0x75: (0x5E5, 0),  # HEBREW LETTER FINAL TSADI
    0x76: (0x5E6, 0),  # HEBREW LETTER TSADI
    0x77: (0x5E7, 0),  # HEBREW LETTER QOF / KOF
    0x78: (0x5E8, 0),  # HEBREW LETTER RESH
    0x79: (0x5E9, 0),  # HEBREW LETTER SHIN
    0x7A: (0x5EA, 0),  # HEBREW LETTER TAV
    0x7B: (0x5F0, 0),  # HEBREW LIGATURE YIDDISH DOUBLE VAV / TSVEY VOVN
    0x7C: (0x5F1, 0),  # HEBREW LIGATURE YIDDISH VAV YOD / VOV YUD
    0x7D: (0x5F2, 0),  # HEBREW LIGATURE YIDDISH DOUBLE YOD / TSVEY YUDN
}
CHARSET_31 = {  # Chinese, Japanese, Korean (EACC)
    0x215556: (0x8461, 0),  # East Asian ideograph
    0x6F5557: (0xC5D1, 0),  # Korean hangul
    0x456324: (0x9F61, 0),  # East Asian ideograph
    0x6F5140: (0xBCCF, 0),  # Korean hangul
    0x6F5558: (0xC5D4, 0),  # Korean hangul
    0x213536: (0x53EC, 0),  # East Asian ideograph
    0x6F5D3C: (0xD64B, 0),  # Korean hangul
    0x215559: (0x8438, 0),  # East Asian ideograph
    0x2D555A: (0x8386, 0),  # East Asian ideograph
    0x6F5C7C: (0xD5D0, 0),  # Korean hangul
    0x295B60: (0x9E55, 0),  # East Asian ideograph
    0x2D555B: (0x8385, 0),  # East Asian ideograph
    0x6F555C: (0xC5E3, 0),  # Korean hangul
    0x6F5141: (0xBCD0, 0),  # Korean hangul
    0x27555D: (0x5E2D, 0),  # East Asian ideograph
    0x23555E: (0x9B1F, 0),  # East Asian ideograph
    0x333F24: (0x7718, 0),  # East Asian ideograph
    0x6F555F: (0xC5ED, 0),  # Korean hangul
    0x6F4F5C: (0xB9AC, 0),  # Korean hangul
    0x6F5560: (0xC5EE, 0),  # Korean hangul
    0x6F4E21: (0xB540, 0),  # Korean hangul
    0x4B4146: (0x6362, 0),  # East Asian ideograph
    0x235031: (0x9874, 0),  # East Asian ideograph
    0x225561: (0x7273, 0),  # East Asian ideograph
    0x274257: (0x6BD9, 0),  # East Asian ideograph
    0x295C28: (0x9E58, 0),  # East Asian ideograph
    0x6F5142: (0xBCD1, 0),  # Korean hangul
    0x6F5562: (0xC5F4, 0),  # Korean hangul
    0x213727: (0x5616, 0),  # East Asian ideograph
    0x215563: (0x84C0, 0),  # East Asian ideograph
    0x215564: (0x8499, 0),  # East Asian ideograph
    0x6F562E: (0xC679, 0),  # Korean hangul
    0x2D4674: (0x51B2, 0),  # East Asian ideograph
    0x6F5565: (0xC5FC, 0),  # Korean hangul
    0x4B4147: (0x633F, 0),  # East Asian ideograph
    0x215566: (0x8490, 0),  # East Asian ideograph
    0x6F5143: (0xBCD2, 0),  # Korean hangul
    0x275567: (0x82CD, 0),  # East Asian ideograph
    0x215568: (0x853D, 0),  # East Asian ideograph
    0x6F5569: (0xC600, 0),  # Korean hangul
    0x27314C: (0x6765, 0),  # East Asian ideograph
    0x276071: (0x517B, 0),  # East Asian ideograph
    0x6F556A: (0xC601, 0),  # Korean hangul
    0x33325D: (0x4FA1, 0),  # East Asian ideograph
    0x6F5839: (0xC9DD, 0),  # Korean hangul
    0x2D6B5F: (0x5273, 0),  # East Asian ideograph
    0x21556B: (0x851A, 0),  # East Asian ideograph
    0x6F5144: (0xBCD5, 0),  # Korean hangul
    0x27556C: (0x83B2, 0),  # East Asian ideograph
    0x22556D: (0x727C, 0),  # East Asian ideograph
    0x21556E: (0x852D, 0),  # East Asian ideograph
    0x6F556F: (0xC610, 0),  # Korean hangul
    0x295721: (0x9C86, 0),  # East Asian ideograph
    0x466074: (0x76B2, 0),  # East Asian ideograph
    0x333529: (0x53DC, 0),  # East Asian ideograph
    0x6F5145: (0xBCF4, 0),  # Korean hangul
    0x225571: (0x727F, 0),  # East Asian ideograph
    0x225D42: (0x7521, 0),  # East Asian ideograph
    0x275949: (0x8A89, 0),  # East Asian ideograph
    0x6F5037: (0xBA84, 0),  # Korean hangul
    0x215573: (0x8514, 0),  # East Asian ideograph
    0x215574: (0x84EC, 0),  # East Asian ideograph
    0x4C2330: (0x5C53, 0),  # East Asian ideograph
    0x69656E: (0x7DD5, 0),  # East Asian ideograph
    0x6F5146: (0xBCF5, 0),  # Korean hangul
    0x215576: (0x8569, 0),  # East Asian ideograph
    0x282441: (0x5C98, 0),  # East Asian ideograph
    0x234021: (0x9132, 0),  # East Asian ideograph
    0x4D4176: (0x91DB, 0),  # East Asian ideograph
    0x335577: (0x8602, 0),  # East Asian ideograph
    0x394022: (0x6443, 0),  # East Asian ideograph
    0x6F5578: (0xC634, 0),  # Korean hangul
    0x6F4F5D: (0xB9AD, 0),  # Korean hangul
    0x2D3749: (0x5650, 0),  # East Asian ideograph
    0x287139: (0x7EE8, 0),  # East Asian ideograph
    0x234024: (0x9126, 0),  # East Asian ideograph
    0x6F557A: (0xC637, 0),  # Korean hangul
    0x213C35: (0x5DDE, 0),  # East Asian ideograph
    0x6F5147: (0xBCF6, 0),  # Korean hangul
    0x6F557B: (0xC639, 0),  # Korean hangul
    0x215945: (0x8B66, 0),  # East Asian ideograph
    0x21372C: (
        0x5606,
        0,
    ),  # East Asian ideograph (variant of 4B372C which maps to 5606)
    0x27557C: (0x829C, 0),  # East Asian ideograph
    0x224027: (0x69BF, 0),  # East Asian ideograph
    0x23557D: (0x9B34, 0),  # East Asian ideograph
    0x6F557E: (0xC640, 0),  # Korean hangul
    0x2D4029: (0x5214, 0),  # East Asian ideograph
    0x6F5148: (0xBCF8, 0),  # Korean hangul
    0x23402B: (0x9134, 0),  # East Asian ideograph
    0x21372D: (0x5609, 0),  # East Asian ideograph
    0x23402C: (0x9136, 0),  # East Asian ideograph
    0x6F5876: (0xCC14, 0),  # Korean hangul
    0x22402D: (0x69A3, 0),  # East Asian ideograph
    0x22507C: (0x70DC, 0),  # East Asian ideograph
    0x22402E: (0x69A4, 0),  # East Asian ideograph
    0x6F5149: (0xBCFC, 0),  # Korean hangul
    0x6F575F: (0xC8B0, 0),  # Korean hangul
    0x295A75: (0x9E41, 0),  # East Asian ideograph
    0x4B525A: (0x7FFA, 0),  # East Asian ideograph
    0x234031: (0x913A, 0),  # East Asian ideograph
    0x2D383F: (0x575A, 0),  # East Asian ideograph
    0x294371: (0x94FD, 0),  # East Asian ideograph
    0x234032: (0x913B, 0),  # East Asian ideograph
    0x6F5C27: (0xD38C, 0),  # Korean hangul
    0x224034: (0x69D4, 0),  # East Asian ideograph
    0x6F514A: (0xBD04, 0),  # Korean hangul
    0x335F73: (0x9759, 0),  # East Asian ideograph
    0x6F4C33: (0xB17C, 0),  # Korean hangul
    0x4B525B: (
        0x66DC,
        0,
    ),  # East Asian ideograph (variant of 39525B which maps to 66DC)
    0x2E7C2E: (0x831C, 0),  # East Asian ideograph
    0x224038: (0x69C3, 0),  # East Asian ideograph
    0x6F5B4D: (0xD280, 0),  # Korean hangul
    0x2D4039: (0x67C6, 0),  # East Asian ideograph
    0x6F514B: (0xBD05, 0),  # Korean hangul
    0x276036: (0x54CD, 0),  # East Asian ideograph
    0x395477: (0x85A6, 0),  # East Asian ideograph
    0x213730: (0x5617, 0),  # East Asian ideograph
    0x4B525C: (0x8002, 0),  # East Asian ideograph
    0x23403B: (0x9143, 0),  # East Asian ideograph
    0x295B6B: (0x9E57, 0),  # East Asian ideograph
    0x2D5963: (0x8C98, 0),  # East Asian ideograph
    0x224C3C: (0x6F3B, 0),  # East Asian ideograph
    0x22403E: (0x6A11, 0),  # East Asian ideograph
    0x6F5A73: (0xD0C8, 0),  # Korean hangul
    0x6F514C: (0xBD07, 0),  # Korean hangul
    0x213B74: (0x5CFD, 0),  # East Asian ideograph
    0x23403F: (0x9145, 0),  # East Asian ideograph
    0x21594A: (0x8B80, 0),  # East Asian ideograph
    0x213731: (0x560D, 0),  # East Asian ideograph
    0x225D49: (0x752F, 0),  # East Asian ideograph
    0x234040: (0x9148, 0),  # East Asian ideograph
    0x224041: (0x6A00, 0),  # East Asian ideograph
    0x295B6C: (0x9E4B, 0),  # East Asian ideograph
    0x234042: (0x9150, 0),  # East Asian ideograph
    0x234043: (0x914E, 0),  # East Asian ideograph
    0x6F514D: (0xBD09, 0),  # Korean hangul
    0x213B75: (0x5CED, 0),  # East Asian ideograph
    0x394A60: (0x9AE6, 0),  # East Asian ideograph
    0x213732: (0x562E, 0),  # East Asian ideograph
    0x334045: (0x629B, 0),  # East Asian ideograph
    0x292A34: (0x86AC, 0),  # East Asian ideograph
    0x224046: (0x69E6, 0),  # East Asian ideograph
    0x2F2D79: (0x88B5, 0),  # East Asian ideograph
    0x234048: (0x9159, 0),  # East Asian ideograph
    0x6F514E: (0xBD10, 0),  # Korean hangul
    0x276039: (0x9877, 0),  # East Asian ideograph
    0x234049: (0x915C, 0),  # East Asian ideograph
    0x33494A: (0x70D6, 0),  # East Asian ideograph
    0x294372: (0x9513, 0),  # East Asian ideograph
    0x22404B: (0x6A0B, 0),  # East Asian ideograph
    0x22404C: (0x69E5, 0),  # East Asian ideograph
    0x2E2F7A: (0x6738, 0),  # East Asian ideograph
    0x22404D: (0x69E9, 0),  # East Asian ideograph
    0x6F514F: (0xBD14, 0),  # Korean hangul
    0x27603A: (0x9879, 0),  # East Asian ideograph
    0x2D4F29: (0x9F9D, 0),  # East Asian ideograph
    0x213734: (0x564E, 0),  # East Asian ideograph
    0x2D404F: (0x6294, 0),  # East Asian ideograph
    0x6F5039: (0xBA87, 0),  # Korean hangul
    0x224050: (0x69FC, 0),  # East Asian ideograph
    0x6F5B4E: (0xD284, 0),  # Korean hangul
    0x234052: (0x915A, 0),  # East Asian ideograph
    0x6F5150: (0xBD24, 0),  # Korean hangul
    0x213B78: (0x5CF0, 0),  # East Asian ideograph
    0x234053: (0x9161, 0),  # East Asian ideograph
    0x6F596B: (0xCE6B, 0),  # Korean hangul
    0x225D4D: (0x753A, 0),  # East Asian ideograph
    0x224054: (0x6A17, 0),  # East Asian ideograph
    0x4B4C3C: (0x7573, 0),  # East Asian ideograph
    0x224056: (0x69E7, 0),  # East Asian ideograph
    0x224057: (0x69EB, 0),  # East Asian ideograph
    0x6F5151: (0xBD48, 0),  # Korean hangul
    0x213B79: (0x5CF6, 0),  # East Asian ideograph
    0x294621: (0x9553, 0),  # East Asian ideograph
    0x4B6266: (0x9ED2, 0),  # East Asian ideograph
    0x6F5631: (0xC688, 0),  # Korean hangul
    0x22405B: (0x69F1, 0),  # East Asian ideograph
    0x6F5152: (0xBD49, 0),  # Korean hangul
    0x27603D: (0x9884, 0),  # East Asian ideograph
    0x22405E: (0x6A2B, 0),  # East Asian ideograph
    0x29444D: (0x952B, 0),  # East Asian ideograph
    0x22405F: (0x69FF, 0),  # East Asian ideograph
    0x224060: (0x6A20, 0),  # East Asian ideograph
    0x234061: (0x916F, 0),  # East Asian ideograph
    0x6F5153: (0xBD4C, 0),  # Korean hangul
    0x27603E: (0x987C, 0),  # East Asian ideograph
    0x234062: (0x916E, 0),  # East Asian ideograph
    0x275D60: (0x94E8, 0),  # East Asian ideograph
    0x6F5A71: (0xD0C1, 0),  # Korean hangul
    0x4B4E21: (0x7B36, 0),  # East Asian ideograph
    0x224064: (0x69ED, 0),  # East Asian ideograph
    0x28355B: (0x6484, 0),  # East Asian ideograph
    0x6F547D: (0xC545, 0),  # Korean hangul
    0x234066: (0x917A, 0),  # East Asian ideograph
    0x6F582E: (0xC9CA, 0),  # Korean hangul
    0x6F5154: (0xBD50, 0),  # Korean hangul
    0x27603F: (0x987D, 0),  # East Asian ideograph
    0x224067: (0x6A1B, 0),  # East Asian ideograph
    0x213739: (0x5657, 0),  # East Asian ideograph
    0x2D7143: (0x55E2, 0),  # East Asian ideograph
    0x234068: (0x9172, 0),  # East Asian ideograph
    0x2D5A63: (0x8DE5, 0),  # East Asian ideograph
    0x2D384A: (0x5872, 0),  # East Asian ideograph
    0x234069: (0x9179, 0),  # East Asian ideograph
    0x27632C: (0x9F9A, 0),  # East Asian ideograph
    0x23406A: (0x9176, 0),  # East Asian ideograph
    0x4C233F: (0x5C76, 0),  # East Asian ideograph
    0x23406B: (0x9174, 0),  # East Asian ideograph
    0x6F5155: (0xBD58, 0),  # Korean hangul
    0x213B7D: (0x5D1B, 0),  # East Asian ideograph
    0x276040: (0x987F, 0),  # East Asian ideograph
    0x23406C: (0x9173, 0),  # East Asian ideograph
    0x23406D: (0x9185, 0),  # East Asian ideograph
    0x22406E: (0x6A18, 0),  # East Asian ideograph
    0x23406F: (0x9182, 0),  # East Asian ideograph
    0x4B5F30: (
        0x9686,
        0,
    ),  # East Asian ideograph (variant of 215F30 which maps to 9686)
    0x234070: (0x918A, 0),  # East Asian ideograph
    0x6F5A75: (0xD0D0, 0),  # Korean hangul
    0x213C38: (0x5DE8, 0),  # East Asian ideograph
    0x6F5156: (0xBD59, 0),  # Korean hangul
    0x276041: (0x9881, 0),  # East Asian ideograph
    0x234071: (0x9186, 0),  # East Asian ideograph
    0x21373B: (0x5653, 0),  # East Asian ideograph
    0x234072: (0x918C, 0),  # East Asian ideograph
    0x234073: (0x9181, 0),  # East Asian ideograph
    0x224075: (0x6A0C, 0),  # East Asian ideograph
    0x6F5157: (0xBD64, 0),  # Korean hangul
    0x224076: (0x6A0F, 0),  # East Asian ideograph
    0x21373C: (0x563F, 0),  # East Asian ideograph
    0x4B3F74: (0x623B, 0),  # East Asian ideograph
    0x282F43: (0x6206, 0),  # East Asian ideograph
    0x454738: (0x6CFA, 0),  # East Asian ideograph
    0x275E6A: (0x9610, 0),  # East Asian ideograph
    0x274F36: (0x5E0C, 0),  # East Asian ideograph
    0x6F5E21: (0xD79D, 0),  # Korean hangul
    0x232B24: (0x876A, 0),  # East Asian ideograph
    0x212B25: (0x300C, 0),  # Ideographic left corner bracket
    0x2F5158: (0x7CC7, 0),  # East Asian ideograph
    0x23407B: (0x9191, 0),  # East Asian ideograph
    0x225D55: (0x754A, 0),  # East Asian ideograph
    0x294628: (0x9552, 0),  # East Asian ideograph
    0x4B3050: (0x4E8A, 0),  # East Asian ideograph
    0x22407C: (0x69EE, 0),  # East Asian ideograph
    0x232B27: (0x874E, 0),  # East Asian ideograph
    0x695B37: (0x6737, 0),  # East Asian ideograph
    0x23407D: (0x9190, 0),  # East Asian ideograph
    0x23407E: (0x918E, 0),  # East Asian ideograph
    0x4C6775: (0x7962, 0),  # Unrelated variant of EACC 293032 which maps to 7962
    0x6F5159: (0xBD81, 0),  # Korean hangul
    0x21373E: (0x5637, 0),  # East Asian ideograph
    0x294629: (0x84E5, 0),  # East Asian ideograph
    0x4B3051: (0x5F10, 0),  # East Asian ideograph
    0x6F503B: (0xBAA9, 0),  # Korean hangul
    0x222B2D: (0x602B, 0),  # East Asian ideograph
    0x6F5B50: (0xD290, 0),  # Korean hangul
    0x455847: (
        0x8A25,
        0,
    ),  # East Asian ideograph (variant of 215847 which maps to 8A25)
    0x396B2F: (0x521F, 0),  # East Asian ideograph
    0x6F515A: (0xBD84, 0),  # Korean hangul
    0x6F5861: (0xCAD9, 0),  # Korean hangul
    0x222B30: (0x6019, 0),  # East Asian ideograph
    0x225D57: (0x754E, 0),  # East Asian ideograph
    0x4B3052: (0x6275, 0),  # East Asian ideograph
    0x212B31: (0xFF3B, 0),  # Ideographic left square bracket
    0x4B3749: (
        0x5668,
        0,
    ),  # East Asian ideograph (variant of 213749 which maps to 5668)
    0x3A3B7D: (0x67B1, 0),  # East Asian ideograph
    0x216B33: (0x5231, 0),  # East Asian ideograph
    0x23504A: (0x98BF, 0),  # East Asian ideograph
    0x4B5F35: (0x6B92, 0),  # East Asian ideograph
    0x474270: (0x94BC, 0),  # East Asian ideograph
    0x6F515B: (0xBD87, 0),  # Korean hangul
    0x212B35: (0x3001, 0),  # Ideographic comma
    0x216B36: (0x5235, 0),  # East Asian ideograph
    0x4B6268: (0x9ED9, 0),  # East Asian ideograph
    0x3F404F: (0x638A, 0),  # East Asian ideograph
    0x695B7B: (0x6926, 0),  # East Asian ideograph
    0x222B38: (0x601B, 0),  # East Asian ideograph
    0x216B39: (0x5233, 0),  # East Asian ideograph
    0x6F485F: (0xAC00, 0),  # Korean hangul
    0x276047: (0x988A, 0),  # East Asian ideograph
    0x212B3A: (0xFF1A, 0),  # Ideographic colon
    0x225D59: (0x754B, 0),  # East Asian ideograph
    0x333F3F: (0x51F4, 0),  # East Asian ideograph
    0x212B3B: (0xFF1F, 0),  # Ideographic question mark
    0x2D3852: (0x51A2, 0),  # East Asian ideograph
    0x295739: (0x9C9E, 0),  # East Asian ideograph
    0x222B3D: (0x6033, 0),  # East Asian ideograph
    0x276B3E: (0x522D, 0),  # East Asian ideograph
    0x6F515D: (0xBD89, 0),  # Korean hangul
    0x276048: (0x9888, 0),  # East Asian ideograph
    0x275A28: (0x8D42, 0),  # East Asian ideograph
    0x225D5A: (0x7548, 0),  # East Asian ideograph
    0x29462D: (0x9549, 0),  # East Asian ideograph
    0x6F4B45: (0xB07D, 0),  # Korean hangul
    0x274F3C: (0x79F0, 0),  # East Asian ideograph
    0x706B42: (0x80BC, 0),  # East Asian ideograph
    0x6F515E: (0xBD90, 0),  # Korean hangul
    0x276049: (0x9891, 0),  # East Asian ideograph
    0x217B75: (0x5AA0, 0),  # East Asian ideograph
    0x706B44: (0x80BD, 0),  # East Asian ideograph
    0x33615A: (0x8EB0, 0),  # East Asian ideograph
    0x222B45: (0x600D, 0),  # East Asian ideograph
    0x2D3854: (0x5896, 0),  # East Asian ideograph
    0x274F3D: (0x79CD, 0),  # East Asian ideograph
    0x28533C: (0x709D, 0),  # East Asian ideograph
    0x69573B: (0x5F41, 0),  # East Asian ideograph
    0x216B47: (0x5260, 0),  # East Asian ideograph
    0x6F5B51: (0xD291, 0),  # Korean hangul
    0x6F515F: (0xBD91, 0),  # Korean hangul
    0x27604A: (0x9893, 0),  # East Asian ideograph
    0x213744: (0x5678, 0),  # East Asian ideograph
    0x4B3057: (0x4E99, 0),  # East Asian ideograph
    0x6F2477: (0x3154, 0),  # Korean hangul
    0x2F4053: (0x914F, 0),  # East Asian ideograph
    0x226B4B: (0x7B37, 0),  # East Asian ideograph
    0x29573C: (0x9C91, 0),  # East Asian ideograph
    0x706B4C: (0x80E9, 0),  # East Asian ideograph
    0x4B5F3A: (0x967A, 0),  # East Asian ideograph
    0x216B4D: (0x525E, 0),  # East Asian ideograph
    0x6F5160: (0xBD93, 0),  # Korean hangul
    0x6F5940: (0xCCAD, 0),  # Korean hangul
    0x29573D: (0x9C92, 0),  # East Asian ideograph
    0x6F5161: (0xBD95, 0),  # Korean hangul
    0x216B53: (0x5255, 0),  # East Asian ideograph
    0x705F50: (0x549D, 0),  # East Asian ideograph
    0x2E6B54: (0x7B04, 0),  # East Asian ideograph
    0x292B55: (0x86F3, 0),  # East Asian ideograph
    0x6F555A: (0xC5E0, 0),  # Korean hangul
    0x70622A: (0x7339, 0),  # East Asian ideograph
    0x6F5162: (0xBD99, 0),  # Korean hangul
    0x212B59: (0xFF0F, 0),  # Ideographic solidus
    0x2D562E: (0x8024, 0),  # East Asian ideograph
    0x213563: (0x5439, 0),  # East Asian ideograph
    0x216B5B: (0x526E, 0),  # East Asian ideograph
    0x6F4B67: (0xB0C8, 0),  # Korean hangul
    0x4B3D24: (0x53A6, 0),  # East Asian ideograph
    0x6F5163: (0xBD9C, 0),  # Korean hangul
    0x225D60: (0x755B, 0),  # East Asian ideograph
    0x276B5F: (0x672D, 0),  # East Asian ideograph
    0x2D433E: (0x667B, 0),  # East Asian ideograph
    0x235053: (0x98C6, 0),  # East Asian ideograph
    0x345452: (0x7118, 0),  # East Asian ideograph
    0x6F5B40: (0xD1D8, 0),  # Korean hangul
    0x213569: (0x5462, 0),  # East Asian ideograph
    0x4C6B62: (
        0x7B4C,
        0,
    ),  # East Asian ideograph (variant of 226B62 which maps to 7B4C)
    0x394634: (
        0x6B96,
        0,
    ),  # East Asian ideograph (variant of 214634 which maps to 6B96)
    0x274171: (0x629A, 0),  # East Asian ideograph
    0x6F5165: (0xBDF0, 0),  # Korean hangul
    0x28356D: (0x6512, 0),  # East Asian ideograph
    0x274F44: (0x79EF, 0),  # East Asian ideograph
    0x295742: (0x9C95, 0),  # East Asian ideograph
    0x4B3D27: (0x5EC3, 0),  # East Asian ideograph
    0x6F5166: (0xBE0C, 0),  # Korean hangul
    0x6F4D23: (0xB310, 0),  # Korean hangul
    0x213B61: (
        0x5C64,
        0,
    ),  # East Asian ideograph (variant of 4B3B61 which maps to 5C64)
    0x4B5277: (0x8068, 0),  # East Asian ideograph
    0x336162: (0x9A23, 0),  # East Asian ideograph
    0x705F51: (0x54D0, 0),  # East Asian ideograph
    0x6F4A46: (0xAE50, 0),  # Korean hangul
    0x292B6E: (0x86F0, 0),  # East Asian ideograph
    0x2D4A60: (0x6C02, 0),  # East Asian ideograph
    0x222B6F: (0x604C, 0),  # East Asian ideograph
    0x6F5167: (0xBE0D, 0),  # Korean hangul
    0x276052: (0x989B, 0),  # East Asian ideograph
    0x6F4D24: (0xB311, 0),  # Korean hangul
    0x232B72: (0x87AC, 0),  # East Asian ideograph
    0x6F496C: (0xAD49, 0),  # Korean hangul
    0x216B74: (0x5282, 0),  # East Asian ideograph
    0x2D5F2E: (0x661C, 0),  # East Asian ideograph
    0x216B75: (0x5281, 0),  # East Asian ideograph
    0x6F5168: (0xBE10, 0),  # Korean hangul
    0x215966: (0x8C8C, 0),  # East Asian ideograph
    0x6F5621: (0xC641, 0),  # Korean hangul
    0x33515C: (0x7DAB, 0),  # East Asian ideograph
    0x275622: (0x8427, 0),  # East Asian ideograph
    0x215623: (0x859B, 0),  # East Asian ideograph
    0x226B79: (0x7B72, 0),  # East Asian ideograph
    0x215624: (0x8591, 0),  # East Asian ideograph
    0x2D496B: (0x70DF, 0),  # East Asian ideograph
    0x226B7A: (0x7B78, 0),  # East Asian ideograph
    0x6F5169: (0xBE14, 0),  # Korean hangul
    0x275626: (0x8537, 0),  # East Asian ideograph
    0x23487C: (0x9481, 0),  # East Asian ideograph
    0x226B7C: (0x7B67, 0),  # East Asian ideograph
    0x6F5627: (0xC654, 0),  # Korean hangul
    0x2D5635: (0x846F, 0),  # East Asian ideograph
    0x215628: (0x8587, 0),  # East Asian ideograph
    0x29352D: (0x8C30, 0),  # East Asian ideograph
    0x275629: (0x84DD, 0),  # East Asian ideograph
    0x21562A: (0x85A9, 0),  # East Asian ideograph
    0x276055: (0x613F, 0),  # East Asian ideograph
    0x6F4D27: (0xB315, 0),  # Korean hangul
    0x225D67: (0x7563, 0),  # East Asian ideograph
    0x273D2F: (0x5385, 0),  # East Asian ideograph
    0x335D23: (0x8A76, 0),  # East Asian ideograph
    0x6F562D: (0xC678, 0),  # Korean hangul
    0x2E2968: (0x5F51, 0),  # East Asian ideograph
    0x21562E: (0x85C9, 0),  # East Asian ideograph
    0x4B3D2C: (0x53B0, 0),  # East Asian ideograph
    0x21562F: (0x85B0, 0),  # East Asian ideograph
    0x4B527C: (0x8080, 0),  # East Asian ideograph
    0x233F4E: (0x9100, 0),  # East Asian ideograph
    0x4B4E39: (0x5CFA, 0),  # East Asian ideograph
    0x275631: (0x827A, 0),  # East Asian ideograph
    0x215632: (0x85EA, 0),  # East Asian ideograph
    0x695633: (0x5CBE, 0),  # East Asian ideograph
    0x6F516C: (0xBE1F, 0),  # Korean hangul
    0x21596A: (0x8CA0, 0),  # East Asian ideograph
    0x213751: (0x5687, 0),  # East Asian ideograph
    0x275635: (0x836F, 0),  # East Asian ideograph
    0x6F5529: (0xC558, 0),  # Korean hangul
    0x235636: (0x9B43, 0),  # East Asian ideograph
    0x275637: (0x853C, 0),  # East Asian ideograph
    0x6F5C2E: (0xD39C, 0),  # Korean hangul
    0x4C5638: (0x729F, 0),  # East Asian ideograph
    0x275639: (0x853A, 0),  # East Asian ideograph
    0x21563A: (0x8606, 0),  # East Asian ideograph
    0x233F50: (0x9107, 0),  # East Asian ideograph
    0x225927: (0x73EA, 0),  # East Asian ideograph
    0x21563B: (0x860B, 0),  # East Asian ideograph
    0x6F5A22: (0xCEAC, 0),  # Korean hangul
    0x21563C: (0x8607, 0),  # East Asian ideograph
    0x224C5E: (0x6F36, 0),  # East Asian ideograph
    0x21563D: (0x860A, 0),  # East Asian ideograph
    0x4B3D2F: (0x5EF0, 0),  # East Asian ideograph
    0x696576: (0x7E90, 0),  # East Asian ideograph
    0x21563E: (0x862D, 0),  # East Asian ideograph
    0x276059: (0x9885, 0),  # East Asian ideograph
    0x21596C: (0x8CA1, 0),  # East Asian ideograph
    0x2D563F: (0x6A97, 0),  # East Asian ideograph
    0x276023: (0x5DE9, 0),  # East Asian ideograph
    0x275640: (0x85D3, 0),  # East Asian ideograph
    0x346126: (0x6900, 0),  # East Asian ideograph
    0x2D3421: (0x5294, 0),  # East Asian ideograph
    0x235641: (0x9B4B, 0),  # East Asian ideograph
    0x215642: (0x863F, 0),  # East Asian ideograph
    0x4B5F49: (0x51CB, 0),  # East Asian ideograph
    0x2D4971: (0x70A4, 0),  # East Asian ideograph
    0x395643: (0x4E55, 0),  # East Asian ideograph
    0x6F4D2C: (0xB35C, 0),  # Korean hangul
    0x213754: (0x5695, 0),  # East Asian ideograph
    0x275644: (0x4E47, 0),  # East Asian ideograph
    0x70602D: (0x55B9, 0),  # East Asian ideograph
    0x692426: (0x3046, 0),  # Hiragana letter U
    0x2D5A7E: (0x8E7B, 0),  # East Asian ideograph
    0x6F5645: (0xC6CC, 0),  # Korean hangul
    0x6F5646: (0xC6CD, 0),  # Korean hangul
    0x2D572B: (0x8797, 0),  # East Asian ideograph
    0x275647: (0x5904, 0),  # East Asian ideograph
    0x215648: (0x865C, 0),  # East Asian ideograph
    0x27605B: (0x98CE, 0),  # East Asian ideograph
    0x28645A: (0x7817, 0),  # East Asian ideograph
    0x6F4D2D: (0xB35F, 0),  # Korean hangul
    0x225D6D: (0x7579, 0),  # East Asian ideograph
    0x21564A: (0x865F, 0),  # East Asian ideograph
    0x2D563C: (0x8613, 0),  # East Asian ideograph
    0x45564B: (
        0x865E,
        0,
    ),  # East Asian ideograph (variant of 21564B which maps to 865E)
    0x21564C: (0x8667, 0),  # East Asian ideograph
    0x6F5171: (0xBE4C, 0),  # Korean hangul
    0x27605C: (0x98D2, 0),  # East Asian ideograph
    0x69564E: (0x5D76, 0),  # East Asian ideograph
    0x29302D: (0x88E3, 0),  # East Asian ideograph
    0x22564F: (0x72B4, 0),  # East Asian ideograph
    0x6F496E: (0xAD6C, 0),  # Korean hangul
    0x277169: (0x5522, 0),  # East Asian ideograph
    0x6F5650: (0xC6EC, 0),  # Korean hangul
    0x6F5C2F: (0xD3A0, 0),  # Korean hangul
    0x235061: (0x98E4, 0),  # East Asian ideograph
    0x4B5F4C: (0x9D8F, 0),  # East Asian ideograph
    0x225652: (0x72B5, 0),  # East Asian ideograph
    0x27605D: (0x53F0, 0),  # East Asian ideograph (duplicate simplified)
    0x6F4D2F: (0xB365, 0),  # Korean hangul
    0x6F5653: (0xC704, 0),  # Korean hangul
    0x294642: (0x94E0, 0),  # East Asian ideograph
    0x692429: (0x3049, 0),  # Hiragana letter small O
    0x333F55: (0x5B3E, 0),  # East Asian ideograph
    0x6F5654: (0xC705, 0),  # Korean hangul
    0x6F5655: (0xC708, 0),  # Korean hangul
    0x225656: (0x72BC, 0),  # East Asian ideograph
    0x695657: (0x5D90, 0),  # East Asian ideograph
    0x27605E: (0x522E, 0),  # East Asian ideograph
    0x6F4D30: (0xB367, 0),  # Korean hangul
    0x225658: (0x72C3, 0),  # East Asian ideograph
    0x217747: (0x5853, 0),  # East Asian ideograph
    0x6F5659: (0xC719, 0),  # Korean hangul
    0x21565A: (0x86CB, 0),  # East Asian ideograph
    0x293537: (0x8C20, 0),  # East Asian ideograph
    0x235063: (0x98E5, 0),  # East Asian ideograph
    0x6F5174: (0xBE55, 0),  # Korean hangul
    0x27605F: (0x98D3, 0),  # East Asian ideograph
    0x6F4D31: (0xB368, 0),  # Korean hangul
    0x23565D: (0x9B74, 0),  # East Asian ideograph
    0x6F4B23: (0xAFB9, 0),  # Korean hangul
    0x4B306C: (0x96E0, 0),  # East Asian ideograph
    0x6F565E: (0xC730, 0),  # Korean hangul
    0x6F5638: (0xC6A7, 0),  # Korean hangul
    0x6F565F: (0xC735, 0),  # Korean hangul
    0x4C6074: (0x76B9, 0),  # East Asian ideograph
    0x224C65: (0x6F2D, 0),  # East Asian ideograph
    0x215660: (0x86DF, 0),  # East Asian ideograph
    0x4B5052: (0x7C56, 0),  # East Asian ideograph
    0x6F5175: (0xBE57, 0),  # Korean hangul
    0x6F4D32: (0xB369, 0),  # Korean hangul
    0x213B64: (0x5C6F, 0),  # East Asian ideograph
    0x6F5662: (0xC73D, 0),  # Korean hangul
    0x396223: (0x9BFD, 0),  # East Asian ideograph (variant of 216223)
    0x333F58: (0x61F4, 0),  # East Asian ideograph
    0x235663: (0x9B68, 0),  # East Asian ideograph
    0x2D3428: (0x5226, 0),  # East Asian ideograph
    0x2E5A40: (0x73B3, 0),  # East Asian ideograph
    0x215664: (0x86DB, 0),  # East Asian ideograph
    0x6F583B: (0xC9E2, 0),  # Korean hangul
    0x293539: (0x8C33, 0),  # East Asian ideograph
    0x215665: (0x86E4, 0),  # East Asian ideograph
    0x4B5F50: (0x96E3, 0),  # East Asian ideograph
    0x4B3B37: (0x51A9, 0),  # East Asian ideograph
    0x6F5176: (0xBE59, 0),  # Korean hangul
    0x2F2F5D: (0x7E48, 0),  # East Asian ideograph
    0x276061: (0x98D5, 0),  # East Asian ideograph
    0x286460: (0x7856, 0),  # East Asian ideograph
    0x21375B: (0x56B6, 0),  # East Asian ideograph
    0x215667: (0x86F9, 0),  # East Asian ideograph
    0x225930: (0x73DB, 0),  # East Asian ideograph
    0x6F5668: (0xC751, 0),  # Korean hangul
    0x22403D: (0x6A12, 0),  # East Asian ideograph
    0x6F5669: (0xC758, 0),  # Korean hangul
    0x224C67: (0x6F34, 0),  # East Asian ideograph
    0x4B566A: (
        0x8708,
        0,
    ),  # East Asian ideograph (variant of 21566A which maps to 8708)
    0x21566B: (0x8700, 0),  # East Asian ideograph
    0x276062: (0x98D8, 0),  # East Asian ideograph
    0x285E7A: (0x75D6, 0),  # East Asian ideograph
    0x6F4D34: (0xB36B, 0),  # Korean hangul
    0x22566C: (0x72CC, 0),  # East Asian ideograph
    0x294647: (0x954F, 0),  # East Asian ideograph
    0x6F566D: (0xC77C, 0),  # Korean hangul
    0x334730: (0x6E5F, 0),  # East Asian ideograph
    0x6F5041: (0xBABB, 0),  # Korean hangul
    0x22566E: (0x72DB, 0),  # East Asian ideograph
    0x22566F: (0x72CD, 0),  # East Asian ideograph
    0x21356D: (0x5496, 0),  # East Asian ideograph
    0x276063: (0x98DE, 0),  # East Asian ideograph
    0x6F4D35: (0xB36E, 0),  # Korean hangul
    0x21375D: (0x56C1, 0),  # East Asian ideograph
    0x225D75: (0x7571, 0),  # East Asian ideograph
    0x333F5B: (0x6133, 0),  # East Asian ideograph
    0x235672: (0x9B80, 0),  # East Asian ideograph
    0x235673: (0x9B8C, 0),  # East Asian ideograph
    0x2F5E42: (0x9EC9, 0),  # East Asian ideograph
    0x6F5674: (0xC789, 0),  # Korean hangul
    0x6F543C: (0xC318, 0),  # Korean hangul
    0x2D5675: (0x9F05, 0),  # East Asian ideograph
    0x6F4D36: (0xB370, 0),  # Korean hangul
    0x21375E: (0x56C2, 0),  # East Asian ideograph
    0x275676: (0x8680, 0),  # East Asian ideograph
    0x692430: (0x3050, 0),  # Hiragana letter GU
    0x4D386F: (0x544B, 0),  # East Asian ideograph
    0x2D4122: (0x6485, 0),  # East Asian ideograph
    0x224123: (0x69F0, 0),  # East Asian ideograph
    0x295756: (0x9CA9, 0),  # East Asian ideograph
    0x215679: (0x8774, 0),  # East Asian ideograph
    0x224124: (0x69F2, 0),  # East Asian ideograph
    0x21567A: (0x8766, 0),  # East Asian ideograph
    0x234125: (0x9193, 0),  # East Asian ideograph
    0x6F4D37: (0xB371, 0),  # Korean hangul
    0x23567B: (0x9B7D, 0),  # East Asian ideograph
    0x21774E: (0x5856, 0),  # East Asian ideograph
    0x4B3072: (0x4EED, 0),  # East Asian ideograph
    0x6F4A4A: (0xAE60, 0),  # Korean hangul
    0x33567C: (0x8671, 0),  # East Asian ideograph
    0x6F567D: (0xC798, 0),  # Korean hangul
    0x224128: (0x6A14, 0),  # East Asian ideograph
    0x21567E: (0x8757, 0),  # East Asian ideograph
    0x224129: (0x6A63, 0),  # East Asian ideograph
    0x295030: (0x989E, 0),  # East Asian ideograph
    0x6F517B: (0xBE60, 0),  # Korean hangul
    0x4B412A: (0x6323, 0),  # East Asian ideograph
    0x6F4D38: (0xB374, 0),  # Korean hangul
    0x225742: (0x731E, 0),  # East Asian ideograph
    0x23412B: (0x919D, 0),  # East Asian ideograph
    0x212B33: (0x3002, 0),  # Ideographic full stop
    0x23412C: (0x919A, 0),  # East Asian ideograph
    0x2D342E: (0x8274, 0),  # East Asian ideograph
    0x6F5538: (0xC580, 0),  # Korean hangul
    0x276067: (0x9968, 0),  # East Asian ideograph
    0x6F4D39: (0xB378, 0),  # Korean hangul
    0x234130: (0x91A2, 0),  # East Asian ideograph
    0x3F476F: (0x51C8, 0),  # East Asian ideograph
    0x334131: (0x6425, 0),  # East Asian ideograph
    0x6F5042: (0xBABD, 0),  # Korean hangul
    0x2D4132: (0x642F, 0),  # East Asian ideograph
    0x287130: (0x7EDB, 0),  # East Asian ideograph
    0x234C29: (0x9708, 0),  # East Asian ideograph
    0x6F517D: (0xBE64, 0),  # Korean hangul
    0x234134: (
        0x919B,
        0,
    ),  # East Asian ideograph (variant of 4D4134 which maps to 919B)
    0x6F4D3A: (0xB380, 0),  # Korean hangul
    0x213762: (0x56C8, 0),  # East Asian ideograph
    0x336179: (0x9C7B, 0),  # East Asian ideograph
    0x4C3474: (0x631D, 0),  # East Asian ideograph
    0x235D36: (0x9E15, 0),  # East Asian ideograph
    0x274136: (0x62A1, 0),  # East Asian ideograph
    0x274F5C: (0x6D3C, 0),  # East Asian ideograph
    0x6F4F68: (0xB9CC, 0),  # Korean hangul
    0x224137: (0x6A67, 0),  # East Asian ideograph
    0x344138: (0x8022, 0),  # East Asian ideograph
    0x6F517E: (0xBE68, 0),  # Korean hangul
    0x224139: (0x6A43, 0),  # East Asian ideograph
    0x6F4D3B: (0xB383, 0),  # Korean hangul
    0x22413A: (0x6A33, 0),  # East Asian ideograph
    0x225938: (0x73E3, 0),  # East Asian ideograph
    0x22413B: (0x6A32, 0),  # East Asian ideograph
    0x274F5D: (0x7A9D, 0),  # East Asian ideograph
    0x27413C: (0x62E3, 0),  # East Asian ideograph
    0x706247: (0x9987, 0),  # East Asian ideograph
    0x23413D: (0x91AA, 0),  # East Asian ideograph
    0x27606A: (0x996E, 0),  # East Asian ideograph
    0x6F4D3C: (0xB385, 0),  # Korean hangul
    0x213B66: (0x5C79, 0),  # East Asian ideograph
    0x213764: (0x56D1, 0),  # East Asian ideograph
    0x22413F: (0x6A28, 0),  # East Asian ideograph
    0x213321: (0x5167, 0),  # East Asian ideograph
    0x4C3F68: (0x69C7, 0),  # East Asian ideograph
    0x224140: (0x6A48, 0),  # East Asian ideograph
    0x224141: (0x6A50, 0),  # East Asian ideograph
    0x224142: (0x6A52, 0),  # East Asian ideograph
    0x334C2C: (0x754D, 0),  # East Asian ideograph
    0x336058: (0x9855, 0),  # East Asian ideograph
    0x224143: (0x6A72, 0),  # East Asian ideograph
    0x6F4D3D: (0xB38C, 0),  # Korean hangul
    0x274570: (0x6743, 0),  # East Asian ideograph
    0x285836: (0x7315, 0),  # East Asian ideograph
    0x224145: (0x6A3E, 0),  # East Asian ideograph
    0x224146: (0x6A77, 0),  # East Asian ideograph
    0x287134: (0x7ED7, 0),  # East Asian ideograph
    0x224147: (0x6A5B, 0),  # East Asian ideograph
    0x214148: (0x63EA, 0),  # East Asian ideograph
    0x6F4D3E: (0xB3C4, 0),  # Korean hangul
    0x225D7E: (0x757F, 0),  # East Asian ideograph
    0x217755: (0x589A, 0),  # East Asian ideograph
    0x2D3877: (0x5900, 0),  # East Asian ideograph
    0x22414A: (0x6A5E, 0),  # East Asian ideograph
    0x21414B: (0x643E, 0),  # East Asian ideograph
    0x21414C: (0x6413, 0),  # East Asian ideograph
    0x23414D: (0x91B5, 0),  # East Asian ideograph
    0x3F4A60: (0x7266, 0),  # East Asian ideograph
    0x6F4D3F: (0xB3C5, 0),  # Korean hangul
    0x6F4C78: (0xB2F7, 0),  # Korean hangul
    0x335D3B: (0x57DC, 0),  # East Asian ideograph
    0x22414F: (0x6A51, 0),  # East Asian ideograph
    0x2D4150: (0x6428, 0),  # East Asian ideograph
    0x29575F: (0x9CA0, 0),  # East Asian ideograph
    0x224151: (0x6A56, 0),  # East Asian ideograph
    0x2D4152: (0x6447, 0),  # East Asian ideograph
    0x6F4D40: (0xB3C8, 0),  # Korean hangul
    0x224153: (0x6A36, 0),  # East Asian ideograph
    0x2D4154: (0x635C, 0),  # East Asian ideograph
    0x2D3436: (0x52F3, 0),  # East Asian ideograph
    0x274155: (0x62A2, 0),  # East Asian ideograph
    0x217C30: (0x5A93, 0),  # East Asian ideograph
    0x224156: (0x6A7A, 0),  # East Asian ideograph
    0x234157: (0x91BD, 0),  # East Asian ideograph
    0x6F4D41: (0xB3CB, 0),  # Korean hangul
    0x213769: (0x56E4, 0),  # East Asian ideograph
    0x224158: (0x6A3F, 0),  # East Asian ideograph
    0x4B4F7B: (0x7B7A, 0),  # East Asian ideograph
    0x21623B: (
        0x9D12,
        0,
    ),  # East Asian ideograph (variant of 4B623B which maps to 9D12)
    0x4B523E: (
        0x7F9A,
        0,
    ),  # East Asian ideograph (variant of 21523E which maps to 7F9A)
    0x23415A: (0x91C2, 0),  # East Asian ideograph
    0x293651: (0x8D36, 0),  # East Asian ideograph
    0x23415B: (0x91C4, 0),  # East Asian ideograph
    0x33347D: (0x53C1, 0),  # East Asian ideograph
    0x23415C: (0x91C3, 0),  # East Asian ideograph
    0x275A30: (0x8D24, 0),  # East Asian ideograph
    0x29415D: (0x917D, 0),  # East Asian ideograph
    0x29586A: (0x9CCB, 0),  # East Asian ideograph
    0x274F64: (0x7A83, 0),  # East Asian ideograph
    0x27415F: (0x6402, 0),  # East Asian ideograph
    0x70624E: (0x9995, 0),  # East Asian ideograph
    0x224C76: (0x6EFA, 0),  # East Asian ideograph
    0x224833: (0x6CB4, 0),  # East Asian ideograph
    0x4B5164: (0x770C, 0),  # East Asian ideograph
    0x4C4146: (0x8538, 0),  # East Asian ideograph
    0x234161: (0x91D4, 0),  # East Asian ideograph
    0x284257: (0x68BC, 0),  # East Asian ideograph
    0x294656: (0x955B, 0),  # East Asian ideograph
    0x234162: (0x91D3, 0),  # East Asian ideograph
    0x234163: (0x91D5, 0),  # East Asian ideograph
    0x217639: (0x580E, 0),  # East Asian ideograph
    0x234164: (0x91D9, 0),  # East Asian ideograph
    0x274B22: (0x72EF, 0),  # East Asian ideograph
    0x6F5B59: (0xD2B8, 0),  # Korean hangul
    0x274165: (0x635E, 0),  # East Asian ideograph
    0x286272: (0x770D, 0),  # East Asian ideograph
    0x274166: (0x62E8, 0),  # East Asian ideograph
    0x6F4D44: (0xB3D4, 0),  # Korean hangul
    0x234168: (0x91E2, 0),  # East Asian ideograph
    0x6F534A: (0xC1A9, 0),  # Korean hangul
    0x234169: (0x91ED, 0),  # East Asian ideograph
    0x23416A: (0x91F7, 0),  # East Asian ideograph
    0x333D2F: (0x5E81, 0),  # East Asian ideograph
    0x23416B: (0x91FA, 0),  # East Asian ideograph
    0x6F4D45: (0xB3D5, 0),  # Korean hangul
    0x21775C: (0x5889, 0),  # East Asian ideograph
    0x22416C: (0x69F9, 0),  # East Asian ideograph
    0x215543: (0x83CC, 0),  # East Asian ideograph
    0x4B4E56: (0x78FA, 0),  # East Asian ideograph
    0x22416D: (0x6A64, 0),  # East Asian ideograph
    0x295427: (0x9A85, 0),  # East Asian ideograph
    0x27416E: (0x6251, 0),  # East Asian ideograph
    0x217C31: (0x5AAC, 0),  # East Asian ideograph
    0x23416F: (0x91F2, 0),  # East Asian ideograph
    0x234171: (0x91E8, 0),  # East Asian ideograph
    0x294458: (0x952C, 0),  # East Asian ideograph
    0x4B434D: (0x663F, 0),  # East Asian ideograph
    0x234172: (0x91F6, 0),  # East Asian ideograph
    0x2D343C: (0x52A2, 0),  # East Asian ideograph
    0x334C3E: (0x8E08, 0),  # East Asian ideograph
    0x234173: (0x91EE, 0),  # East Asian ideograph
    0x274174: (0x62E5, 0),  # East Asian ideograph
    0x4B3D4B: (0x5F3E, 0),  # East Asian ideograph
    0x334C36: (
        0x753B,
        0,
    ),  # East Asian ideograph (variant of 274C36 which maps to 753B)
    0x4B4C67: (
        0x761F,
        0,
    ),  # East Asian ideograph (variant of 214C67 which maps to 761F)
    0x224175: (0x6AA8, 0),  # East Asian ideograph
    0x29465A: (0x955F, 0),  # East Asian ideograph
    0x274176: (0x51FB, 0),  # East Asian ideograph
    0x692441: (0x3061, 0),  # Hiragana letter TI
    0x21332C: (0x5178, 0),  # East Asian ideograph
    0x235D43: (0x9E7B, 0),  # East Asian ideograph
    0x224177: (0x6AA5, 0),  # East Asian ideograph
    0x2D343D: (0x52E7, 0),  # East Asian ideograph
    0x224179: (0x6A96, 0),  # East Asian ideograph
    0x4B3D4C: (0x5F25, 0),  # East Asian ideograph (variant of 273D4C)
    0x222C24: (0x608A, 0),  # East Asian ideograph
    0x27417A: (0x6321, 0),  # East Asian ideograph
    0x6F4D48: (0xB3DB, 0),  # Korean hangul
    0x707360: (0x7B7B, 0),  # East Asian ideograph
    0x286032: (0x75AC, 0),  # East Asian ideograph
    0x21332D: (0x517C, 0),  # East Asian ideograph
    0x27417C: (0x636E, 0),  # East Asian ideograph
    0x216C27: (0x5296, 0),  # East Asian ideograph
    0x27417D: (0x63B3, 0),  # East Asian ideograph
    0x284F26: (0x6CF7, 0),  # East Asian ideograph
    0x224A44: (0x6E12, 0),  # East Asian ideograph
    0x22417E: (0x6A7D, 0),  # East Asian ideograph
    0x6F5D6A: (0xD750, 0),  # Korean hangul
    0x226C29: (0x7B73, 0),  # East Asian ideograph
    0x2E2B74: (0x609B, 0),  # East Asian ideograph
    0x276077: (0x997F, 0),  # East Asian ideograph
    0x6F4D49: (0xB3FC, 0),  # Korean hangul
    0x217760: (0x589B, 0),  # East Asian ideograph
    0x223378: (0x647D, 0),  # East Asian ideograph
    0x232C2C: (0x87EE, 0),  # East Asian ideograph
    0x274B28: (0x72DE, 0),  # East Asian ideograph
    0x222C2F: (0x609E, 0),  # East Asian ideograph
    0x6F4B28: (0xAFC9, 0),  # Korean hangul
    0x217761: (0x587C, 0),  # East Asian ideograph
    0x222C30: (0x6083, 0),  # East Asian ideograph
    0x4B4E5B: (0x783F, 0),  # East Asian ideograph
    0x22483B: (0x6D28, 0),  # East Asian ideograph
    0x216C33: (0x52AE, 0),  # East Asian ideograph
    0x4C4345: (0x67A6, 0),  # East Asian ideograph
    0x222C34: (0x60A7, 0),  # East Asian ideograph
    0x6F4D4B: (0xB410, 0),  # Korean hangul
    0x213773: (0x5718, 0),  # East Asian ideograph
    0x233B2E: (0x8EC9, 0),  # East Asian ideograph
    0x216C38: (0x52BC, 0),  # East Asian ideograph
    0x2D454E: (0x697D, 0),  # East Asian ideograph
    0x217763: (0x5888, 0),  # East Asian ideograph
    0x692446: (0x3066, 0),  # Hiragana letter TE
    0x232C3A: (0x87D6, 0),  # East Asian ideograph
    0x235D48: (0x9E83, 0),  # East Asian ideograph
    0x39302D: (0x534B, 0),  # East Asian ideograph
    0x6F4D4D: (0xB41C, 0),  # Korean hangul
    0x213775: (0x571F, 0),  # East Asian ideograph
    0x286037: (0x763F, 0),  # East Asian ideograph
    0x692447: (0x3067, 0),  # Hiragana letter DE
    0x223731: (0x65C6, 0),  # East Asian ideograph
    0x294478: (0x9522, 0),  # East Asian ideograph
    0x274B2C: (0x730E, 0),  # East Asian ideograph
    0x287144: (0x7EE0, 0),  # East Asian ideograph
    0x234C3D: (0x971D, 0),  # East Asian ideograph
    0x706C43: (0x70C0, 0),  # East Asian ideograph
    0x213333: (0x5191, 0),  # East Asian ideograph
    0x333066: (0x5FC8, 0),  # East Asian ideograph
    0x69613A: (0x7549, 0),  # East Asian ideograph
    0x6F4F6C: (0xB9D1, 0),  # Korean hangul
    0x216C46: (0x52D4, 0),  # East Asian ideograph
    0x234C3E: (0x9719, 0),  # East Asian ideograph
    0x453666: (0x5AD0, 0),  # East Asian ideograph
    0x232C48: (0x87D3, 0),  # East Asian ideograph
    0x6F4D4F: (0xB428, 0),  # Korean hangul
    0x6F4B29: (0xAFCB, 0),  # Korean hangul
    0x294662: (0x956A, 0),  # East Asian ideograph
    0x692449: (0x3069, 0),  # Hiragana letter DO
    0x275F50: (0x96BE, 0),  # East Asian ideograph
    0x235D4B: (0x9E88, 0),  # East Asian ideograph
    0x274B2E: (0x732E, 0),  # East Asian ideograph
    0x235A6B: (0x9D3D, 0),  # East Asian ideograph
    0x292C4C: (0x866E, 0),  # East Asian ideograph
    0x4B346B: (0x5DF5, 0),  # East Asian ideograph
    0x69595E: (0x63B5, 0),  # East Asian ideograph
    0x472C4D: (
        0x8801,
        0,
    ),  # East Asian ideograph (variant of 232C4D which maps to 8801)
    0x28603A: (0x75C8, 0),  # East Asian ideograph
    0x454774: (0x6E15, 0),  # East Asian ideograph
    0x6F5564: (0xC5F7, 0),  # Korean hangul
    0x694664: (0x51EA, 0),  # East Asian ideograph
    0x294221: (0x9495, 0),  # East Asian ideograph
    0x6F4975: (0xAD7C, 0),  # Korean hangul
    0x292C55: (0x86CF, 0),  # East Asian ideograph
    0x6F5762: (0xC8C8, 0),  # Korean hangul
    0x4B5F6F: (0x970A, 0),  # East Asian ideograph
    0x2D4F37: (0x7980, 0),  # East Asian ideograph
    0x216C58: (0x52F0, 0),  # East Asian ideograph
    0x294222: (0x9490, 0),  # East Asian ideograph
    0x6F5A48: (0xCF78, 0),  # Korean hangul
    0x216C5A: (0x52F1, 0),  # East Asian ideograph
    0x2D632B: (0x5C28, 0),  # East Asian ideograph
    0x4B4135: (0x6368, 0),  # East Asian ideograph
    0x275C3E: (0x8FC7, 0),  # East Asian ideograph
    0x223B7A: (0x67F6, 0),  # East Asian ideograph
    0x69244D: (0x306D, 0),  # Hiragana letter NE
    0x222C5D: (0x60C4, 0),  # East Asian ideograph
    0x3A284C: (0x53A9, 0),  # East Asian ideograph (variant of 4C284C)
    0x294223: (0x94AD, 0),  # East Asian ideograph
    0x235D4F: (0x9E87, 0),  # East Asian ideograph
    0x3F5E60: (0x9586, 0),  # East Asian ideograph
    0x395773: (0x7DAF, 0),  # East Asian ideograph
    0x4B5F71: (0x9756, 0),  # East Asian ideograph
    0x224844: (0x6D39, 0),  # East Asian ideograph
    0x292C61: (0x86F4, 0),  # East Asian ideograph
    0x6F4D54: (0xB451, 0),  # Korean hangul
    0x6F4B2A: (0xAFCD, 0),  # Korean hangul
    0x69544B: (0x5870, 0),  # East Asian ideograph
    0x213339: (0x51A5, 0),  # East Asian ideograph
    0x294224: (0x94AA, 0),  # East Asian ideograph
    0x6F563F: (0xC6B9, 0),  # Korean hangul
    0x292C64: (0x877E, 0),  # East Asian ideograph
    0x4B5F72: (0x975B, 0),  # East Asian ideograph
    0x4B5365: (0x8133, 0),  # East Asian ideograph
    0x222C66: (0x60E2, 0),  # East Asian ideograph
    0x6F4A50: (0xAE6C, 0),  # Korean hangul
    0x294225: (0x94AB, 0),  # East Asian ideograph
    0x2D5664: (0x9F04, 0),  # East Asian ideograph
    0x6F542A: (0xC2ED, 0),  # Korean hangul
    0x4B5F73: (
        0x975C,
        0,
    ),  # East Asian ideograph (variant of 215F73 which maps to 975C)
    0x335228: (0x94B5, 0),  # East Asian ideograph
    0x336C6B: (0x6031, 0),  # East Asian ideograph
    0x6F4D56: (0xB458, 0),  # Korean hangul
    0x692450: (0x3070, 0),  # Hiragana letter BA
    0x4B4E67: (0x79D8, 0),  # East Asian ideograph
    0x6F5C37: (0xD3BC, 0),  # Korean hangul
    0x28714D: (0x7EE1, 0),  # East Asian ideograph
    0x216C6F: (0x530B, 0),  # East Asian ideograph
    0x6F4D57: (0xB460, 0),  # Korean hangul
    0x222C73: (0x6103, 0),  # East Asian ideograph
    0x6F5A21: (0xCEA5, 0),  # Korean hangul
    0x4B3D5C: (0x5F83, 0),  # East Asian ideograph
    0x6F4D58: (0xB461, 0),  # Korean hangul
    0x6F5425: (0xC2E0, 0),  # Korean hangul
    0x692452: (0x3072, 0),  # Hiragana letter HI
    0x21333D: (0x51B6, 0),  # East Asian ideograph
    0x215721: (0x8759, 0),  # East Asian ideograph
    0x6F4F6E: (0xB9D9, 0),  # Korean hangul
    0x6F5723: (0xC7A4, 0),  # Korean hangul
    0x225724: (0x72F4, 0),  # East Asian ideograph
    0x6F5D74: (0xD769, 0),  # Korean hangul
    0x6F4D59: (0xB463, 0),  # Korean hangul
    0x215725: (0x879E, 0),  # East Asian ideograph
    0x695438: (0x57B3, 0),  # East Asian ideograph
    0x692453: (0x3073, 0),  # Hiragana letter BI
    0x6F5726: (0xC7A7, 0),  # Korean hangul
    0x6F5727: (0xC7AC, 0),  # Korean hangul
    0x2F5E66: (0x9B12, 0),  # East Asian ideograph
    0x4B4B71: (
        0x7F3E,
        0,
    ),  # East Asian ideograph (variant of 2D4B71 which maps to 7F3E)
    0x6F5728: (0xC7AD, 0),  # Korean hangul
    0x225729: (0x7302, 0),  # East Asian ideograph
    0x697323: (0x9D64, 0),  # East Asian ideograph
    0x6F4D5A: (0xB465, 0),  # Korean hangul
    0x6F572A: (0xC7B4, 0),  # Korean hangul
    0x2E4873: (0x6FA3, 0),  # East Asian ideograph
    0x21572B: (0x87B3, 0),  # East Asian ideograph
    0x333330: (0x518A, 0),  # East Asian ideograph
    0x21572C: (0x87BB, 0),  # East Asian ideograph
    0x29577A: (0x9CAD, 0),  # East Asian ideograph
    0x21572D: (0x87C8, 0),  # East Asian ideograph
    0x39563C: (0x56CC, 0),  # East Asian ideograph
    0x222632: (0x5DB8, 0),  # East Asian ideograph
    0x21572E: (0x87D2, 0),  # East Asian ideograph
    0x4B5D58: (0x9234, 0),  # East Asian ideograph
    0x6F4D5B: (0xB46C, 0),  # Korean hangul
    0x21572F: (0x87BA, 0),  # East Asian ideograph
    0x2D5730: (0x87C7, 0),  # East Asian ideograph
    0x235731: (0x9B92, 0),  # East Asian ideograph
    0x6F5C38: (0xD3C4, 0),  # Korean hangul
    0x275732: (0x86F2, 0),  # East Asian ideograph
    0x6F4E75: (0xB7AC, 0),  # Korean hangul
    0x275733: (0x866B, 0),  # East Asian ideograph
    0x6F4D5C: (0xB480, 0),  # Korean hangul
    0x275734: (0x8749, 0),  # East Asian ideograph
    0x215735: (0x87FB, 0),  # East Asian ideograph
    0x215736: (0x8805, 0),  # East Asian ideograph
    0x2D5228: (0x9262, 0),  # East Asian ideograph
    0x29577C: (0x9CB0, 0),  # East Asian ideograph
    0x695737: (0x5F16, 0),  # East Asian ideograph
    0x222634: (0x5DBF, 0),  # East Asian ideograph
    0x213D21: (0x5EBE, 0),  # East Asian ideograph
    0x6F4D5D: (0xB488, 0),  # Korean hangul
    0x235739: (0x9B9D, 0),  # East Asian ideograph
    0x6F573A: (0xC811, 0),  # Korean hangul
    0x2D3453: (0x758B, 0),  # East Asian ideograph
    0x21573B: (0x8822, 0),  # East Asian ideograph
    0x213132: (0x4F5B, 0),  # East Asian ideograph
    0x21573C: (0x8823, 0),  # East Asian ideograph
    0x21573D: (0x8821, 0),  # East Asian ideograph
    0x23417A: (0x91F8, 0),  # East Asian ideograph
    0x6F4D5E: (0xB4A4, 0),  # Korean hangul
    0x21573E: (0x881F, 0),  # East Asian ideograph
    0x275E69: (0x5173, 0),  # East Asian ideograph
    0x6F5B7A: (0xD330, 0),  # Korean hangul
    0x692458: (0x3078, 0),  # Hiragana letter HE
    0x21573F: (0x8831, 0),  # East Asian ideograph
    0x235D5A: (0x9E95, 0),  # East Asian ideograph
    0x4B5740: (0x8827, 0),  # East Asian ideograph
    0x2D572D: (0x8748, 0),  # East Asian ideograph
    0x215741: (0x8836, 0),  # East Asian ideograph
    0x69533B: (0x555D, 0),  # East Asian ideograph
    0x275742: (0x86EE, 0),  # East Asian ideograph
    0x27614F: (0x9A74, 0),  # East Asian ideograph
    0x6F4D5F: (0xB4B7, 0),  # Korean hangul
    0x215743: (0x8840, 0),  # East Asian ideograph
    0x4C5C3A: (0x73F1, 0),  # East Asian ideograph
    0x6F5744: (0xC82D, 0),  # Korean hangul
    0x694823: (0x7872, 0),  # East Asian ideograph
    0x6F5745: (0xC82F, 0),  # Korean hangul
    0x2D522B: (0x9475, 0),  # East Asian ideograph
    0x215746: (
        0x8853,
        0,
    ),  # East Asian ideograph (variant of 4B5746 which maps to 8853)
    0x275747: (0x4E8D, 0),  # East Asian ideograph
    0x2D4562: (0x681D, 0),  # East Asian ideograph
    0x275A36: (0x8D56, 0),  # East Asian ideograph
    0x6F4D60: (0xB4C0, 0),  # Korean hangul
    0x69245A: (0x307A, 0),  # Hiragana letter PE
    0x213345: (0x51DD, 0),  # East Asian ideograph
    0x215749: (0x885B, 0),  # East Asian ideograph
    0x235D5C: (0x9E91, 0),  # East Asian ideograph
    0x2D3164: (0x7AE2, 0),  # East Asian ideograph
    0x4B4A2E: (0x55B6, 0),  # East Asian ideograph
    0x21574A: (0x885D, 0),  # East Asian ideograph
    0x474236: (0x949A, 0),  # East Asian ideograph
    0x2D4425: (0x686E, 0),  # East Asian ideograph
    0x29533D: (0x9A90, 0),  # East Asian ideograph
    0x21574C: (0x8862, 0),  # East Asian ideograph
    0x3B3922: (0x8DB5, 0),  # East Asian ideograph
    0x21574D: (0x8863, 0),  # East Asian ideograph
    0x23574E: (0x9BA0, 0),  # East Asian ideograph
    0x2D3457: (0x62FE, 0),  # East Asian ideograph
    0x21574F: (0x8868, 0),  # East Asian ideograph
    0x6F5750: (0xC885, 0),  # Korean hangul
    0x213D22: (0x5ECA, 0),  # East Asian ideograph
    0x2D4564: (0x68B9, 0),  # East Asian ideograph
    0x215752: (0x8881, 0),  # East Asian ideograph
    0x27602E: (0x97E9, 0),  # East Asian ideograph
    0x6F5753: (0xC88B, 0),  # Korean hangul
    0x69613E: (0x7569, 0),  # East Asian ideograph
    0x6F5754: (0xC88C, 0),  # Korean hangul
    0x215755: (0x8888, 0),  # East Asian ideograph
    0x4B3D67: (0x5F84, 0),  # East Asian ideograph (variant of 273D67)
    0x215756: (0x88AB, 0),  # East Asian ideograph
    0x6F4D63: (0xB4DD, 0),  # Korean hangul
    0x29367E: (0x8D59, 0),  # East Asian ideograph
    0x217337: (0x568A, 0),  # East Asian ideograph
    0x215759: (0x888D, 0),  # East Asian ideograph
    0x6F5967: (0xCE60, 0),  # Korean hangul
    0x21575A: (0x888B, 0),  # East Asian ideograph
    0x21575B: (0x889E, 0),  # East Asian ideograph
    0x4D3C6C: (0x8FB6, 0),  # East Asian ideograph
    0x21575C: (0x88C1, 0),  # East Asian ideograph
    0x273A36: (0x5988, 0),  # East Asian ideograph
    0x6F4921: (0xAC70, 0),  # Korean hangul
    0x23575D: (0x9BC6, 0),  # East Asian ideograph
    0x23575E: (0x9BBF, 0),  # East Asian ideograph
    0x22575F: (0x733B, 0),  # East Asian ideograph
    0x2D5760: (0x5E2C, 0),  # East Asian ideograph
    0x6F4D65: (0xB4E3, 0),  # Korean hangul
    0x4C7265: (0x7DFC, 0),  # East Asian ideograph
    0x69245F: (0x307F, 0),  # Hiragana letter MI
    0x6F4922: (0xAC71, 0),  # Korean hangul
    0x225762: (0x733A, 0),  # East Asian ideograph
    0x6F5125: (0xBC45, 0),  # Korean hangul
    0x2E4670: (0x6CD0, 0),  # East Asian ideograph
    0x284539: (0x6B9A, 0),  # East Asian ideograph
    0x2D345B: (0x6607, 0),  # East Asian ideograph
    0x275763: (0x91CC, 0),  # East Asian ideograph
    0x393054: (0x4F0D, 0),  # East Asian ideograph
    0x226260: (0x777A, 0),  # East Asian ideograph
    0x6F5764: (0xC8D4, 0),  # Korean hangul
    0x232739: (0x85DA, 0),  # East Asian ideograph
    0x215765: (0x88DD, 0),  # East Asian ideograph
    0x395564: (0x6726, 0),  # East Asian ideograph
    0x235766: (0x9BB9, 0),  # East Asian ideograph
    0x6F4E2E: (0xB560, 0),  # Korean hangul
    0x6F5767: (0xC8E0, 0),  # Korean hangul
    0x6F504B: (0xBB3B, 0),  # Korean hangul
    0x6F2469: (0x3138, 0),  # Korean hangul
    0x215768: (0x88F3, 0),  # East Asian ideograph
    0x2D5232: (0x8FA0, 0),  # East Asian ideograph
    0x6F5769: (0xC8F0, 0),  # Korean hangul
    0x6F5B60: (0xD2CB, 0),  # Korean hangul
    0x69576A: (0x603A, 0),  # East Asian ideograph
    0x22576B: (0x7352, 0),  # East Asian ideograph
    0x21334C: (0x51F9, 0),  # East Asian ideograph
    0x27576C: (0x5236, 0),  # East Asian ideograph
    0x225521: (0x721D, 0),  # East Asian ideograph
    0x2D345D: (0x5349, 0),  # East Asian ideograph
    0x6F576D: (0xC8FD, 0),  # Korean hangul
    0x2D5233: (0x7F78, 0),  # East Asian ideograph
    0x23576E: (0x9BC0, 0),  # East Asian ideograph
    0x29312B: (0x89D1, 0),  # East Asian ideograph
    0x2D5361: (0x811A, 0),  # East Asian ideograph
    0x4B576F: (
        0x8910,
        0,
    ),  # East Asian ideograph (variant of 21576F which maps to 8910)
    0x6F4D68: (0xB4ED, 0),  # Korean hangul
    0x6F4B2E: (0xAFE9, 0),  # Korean hangul
    0x6F4925: (0xAC77, 0),  # Korean hangul
    0x275771: (0x8934, 0),  # East Asian ideograph
    0x215772: (0x8912, 0),  # East Asian ideograph
    0x294164: (0x948B, 0),  # East Asian ideograph
    0x275773: (0x88E4, 0),  # East Asian ideograph
    0x215774: (0x892A, 0),  # East Asian ideograph
    0x6F4D69: (0xB4EF, 0),  # Korean hangul
    0x29467C: (0x9546, 0),  # East Asian ideograph
    0x3F4926: (0x6E08, 0),  # East Asian ideograph
    0x21334E: (0x51FD, 0),  # East Asian ideograph
    0x6F5776: (0xC92C, 0),  # Korean hangul
    0x234221: (0x91F9, 0),  # East Asian ideograph
    0x215777: (0x893B, 0),  # East Asian ideograph
    0x224222: (0x6A7F, 0),  # East Asian ideograph
    0x6F5A33: (0xCF11, 0),  # Korean hangul
    0x234223: (0x9204, 0),  # East Asian ideograph
    0x216231: (0x9CF6, 0),  # East Asian ideograph
    0x215779: (0x8938, 0),  # East Asian ideograph
    0x224224: (0x6A91, 0),  # East Asian ideograph
    0x21577A: (0x8944, 0),  # East Asian ideograph
    0x214225: (0x64E0, 0),  # East Asian ideograph
    0x6F4927: (0xAC79, 0),  # Korean hangul
    0x22577B: (0x7358, 0),  # East Asian ideograph
    0x224226: (0x6A9F, 0),  # East Asian ideograph
    0x4B4A38: (0x71D7, 0),  # East Asian ideograph
    0x21577C: (0x8960, 0),  # East Asian ideograph
    0x234227: (0x920A, 0),  # East Asian ideograph
    0x27577D: (0x8884, 0),  # East Asian ideograph
    0x234228: (0x9225, 0),  # East Asian ideograph
    0x295347: (0x9A93, 0),  # East Asian ideograph
    0x216232: (0x9CF4, 0),  # East Asian ideograph
    0x21577E: (0x8964, 0),  # East Asian ideograph
    0x274229: (0x6401, 0),  # East Asian ideograph
    0x22422A: (0x6A92, 0),  # East Asian ideograph
    0x692465: (0x3085, 0),  # Hiragana letter small YU
    0x22422B: (0x6AA3, 0),  # East Asian ideograph
    0x6F504C: (0xBB3C, 0),  # Korean hangul
    0x6F545B: (0xC42C, 0),  # Korean hangul
    0x23422C: (0x9228, 0),  # East Asian ideograph
    0x6F5A35: (0xCF15, 0),  # Korean hangul
    0x6F5B61: (0xD2D4, 0),  # Korean hangul
    0x29556C: (0x960B, 0),  # East Asian ideograph
    0x4B5B46: (0x8F0C, 0),  # East Asian ideograph
    0x21422E: (0x64FE, 0),  # East Asian ideograph
    0x456260: (0x5E7A, 0),  # East Asian ideograph
    0x275C57: (0x8FD8, 0),  # East Asian ideograph
    0x23422F: (0x9203, 0),  # East Asian ideograph
    0x276030: (0x827D, 0),  # East Asian ideograph
    0x692466: (0x3086, 0),  # Hiragana letter YU
    0x274230: (0x6446, 0),  # East Asian ideograph
    0x2D567B: (0x8717, 0),  # East Asian ideograph
    0x234231: (0x9200, 0),  # East Asian ideograph
    0x393573: (0x5611, 0),  # East Asian ideograph
    0x234232: (0x9218, 0),  # East Asian ideograph
    0x295C3E: (0x9E37, 0),  # East Asian ideograph
    0x274233: (0x62E6, 0),  # East Asian ideograph
    0x6F4D6D: (0xB518, 0),  # Korean hangul
    0x6F4B2F: (0xAFF0, 0),  # Korean hangul
    0x274234: (0x6400, 0),  # East Asian ideograph
    0x274235: (0x6444, 0),  # East Asian ideograph
    0x234236: (0x9208, 0),  # East Asian ideograph
    0x6F5A37: (0xCF20, 0),  # Korean hangul
    0x224237: (0x6A9B, 0),  # East Asian ideograph
    0x234238: (0x921C, 0),  # East Asian ideograph
    0x2D6079: (0x8218, 0),  # East Asian ideograph
    0x6F492B: (0xAC83, 0),  # Korean hangul
    0x213353: (0x5206, 0),  # East Asian ideograph
    0x27423A: (0x6405, 0),  # East Asian ideograph
    0x287349: (0x7F30, 0),  # East Asian ideograph
    0x2D3464: (0x613D, 0),  # East Asian ideograph
    0x23423B: (0x9224, 0),  # East Asian ideograph
    0x2D3021: (0x5F0C, 0),  # East Asian ideograph
    0x6F5A38: (0xCF24, 0),  # Korean hangul
    0x335772: (0x8943, 0),  # East Asian ideograph
    0x293132: (0x89CC, 0),  # East Asian ideograph
    0x226635: (0x7911, 0),  # East Asian ideograph
    0x33423D: (0x53CE, 0),  # East Asian ideograph
    0x284D2B: (0x6D54, 0),  # East Asian ideograph
    0x2D486B: (0x6F82, 0),  # East Asian ideograph
    0x692469: (0x3089, 0),  # Hiragana letter RA
    0x6F576B: (0xC8F5, 0),  # Korean hangul
    0x2D3C7C: (0x83F4, 0),  # East Asian ideograph
    0x4B516D: (0x7DCF, 0),  # East Asian ideograph
    0x216237: (0x9D23, 0),  # East Asian ideograph
    0x224242: (0x6AA0, 0),  # East Asian ideograph
    0x6F4D70: (0xB524, 0),  # Korean hangul
    0x234243: (0x9212, 0),  # East Asian ideograph
    0x69246A: (0x308A, 0),  # Hiragana letter RI
    0x334244: (0x6559, 0),  # East Asian ideograph
    0x4B4A3E: (0x7235, 0),  # East Asian ideograph
    0x2F5E7D: (0x6641, 0),  # East Asian ideograph
    0x393577: (0x9FA2, 0),  # East Asian ideograph
    0x6F5B62: (0xD1F8, 0),  # Korean hangul
    0x214247: (0x6557, 0),  # East Asian ideograph
    0x6F4D71: (0xB525, 0),  # Korean hangul
    0x6F4C7A: (0xB2FA, 0),  # Korean hangul
    0x234248: (0x91FF, 0),  # East Asian ideograph
    0x285323: (0x8367, 0),  # East Asian ideograph
    0x69246B: (0x308B, 0),  # Hiragana letter RU
    0x217345: (0x5699, 0),  # East Asian ideograph
    0x224249: (0x6A9E, 0),  # East Asian ideograph
    0x22424A: (0x6A87, 0),  # East Asian ideograph
    0x6F5A3B: (0xCF2F, 0),  # Korean hangul
    0x22424B: (0x6A8E, 0),  # East Asian ideograph
    0x23424E: (0x9206, 0),  # East Asian ideograph
    0x27424F: (0x542F, 0),  # East Asian ideograph
    0x6F5A3C: (0xCF30, 0),  # Korean hangul
    0x21623A: (0x9D1B, 0),  # East Asian ideograph
    0x224251: (0x6AAB, 0),  # East Asian ideograph
    0x6F4D73: (0xB528, 0),  # Korean hangul
    0x234252: (0x9249, 0),  # East Asian ideograph
    0x6F4930: (0xAC89, 0),  # Korean hangul
    0x394243: (0x4FF2, 0),  # East Asian ideograph
    0x705F61: (0x54DA, 0),  # East Asian ideograph
    0x234254: (0x924D, 0),  # East Asian ideograph
    0x6F556B: (0xC606, 0),  # Korean hangul
    0x224255: (0x6AC8, 0),  # East Asian ideograph
    0x224864: (0x6D19, 0),  # East Asian ideograph
    0x4C4177: (0x8223, 0),  # East Asian ideograph
    0x274256: (0x655B, 0),  # East Asian ideograph
    0x6F4D74: (0xB529, 0),  # Korean hangul
    0x224257: (0x6AAE, 0),  # East Asian ideograph
    0x6F4931: (0xAC8A, 0),  # Korean hangul
    0x6F497C: (0xAD90, 0),  # Korean hangul
    0x234258: (0x923A, 0),  # East Asian ideograph
    0x2D346A: (0x5918, 0),  # East Asian ideograph
    0x6F4879: (0xAC30, 0),  # Korean hangul
    0x2D3C7D: (0x53A2, 0),  # East Asian ideograph
    0x2D4F3E: (0x7A3E, 0),  # East Asian ideograph
    0x4D4134: (0x919B, 0),  # East Asian ideograph
    0x23425C: (0x922E, 0),  # East Asian ideograph
    0x6F4932: (0xAC8B, 0),  # Korean hangul
    0x22425D: (0x6ABF, 0),  # East Asian ideograph
    0x2D5241: (0x7FA3, 0),  # East Asian ideograph
    0x6F5A3F: (0xCF58, 0),  # Korean hangul
    0x23425F: (0x9233, 0),  # East Asian ideograph
    0x294260: (0x94B7, 0),  # East Asian ideograph
    0x234261: (0x9266, 0),  # East Asian ideograph
    0x6F4933: (0xAC8C, 0),  # Korean hangul
    0x214263: (0x65AC, 0),  # East Asian ideograph
    0x29446D: (0x951B, 0),  # East Asian ideograph
    0x6F5A40: (0xCF5C, 0),  # Korean hangul
    0x224264: (0x6ACA, 0),  # East Asian ideograph
    0x224867: (0x6D0E, 0),  # East Asian ideograph
    0x4B3938: (0x5942, 0),  # East Asian ideograph
    0x214266: (0x65B7, 0),  # East Asian ideograph
    0x6F4934: (0xAC90, 0),  # Korean hangul
    0x22375B: (0x65FB, 0),  # East Asian ideograph
    0x4B4A45: (0x5C13, 0),  # East Asian ideograph
    0x234268: (0x9235, 0),  # East Asian ideograph
    0x4B4B77: (0x4EC0, 0),  # East Asian ideograph
    0x6F5A41: (0xCF64, 0),  # Korean hangul
    0x4B5B52: (0x8F42, 0),  # East Asian ideograph
    0x6F4D78: (0xB530, 0),  # Korean hangul
    0x23426B: (0x9250, 0),  # East Asian ideograph
    0x692472: (0x3092, 0),  # Hiragana letter WO
    0x21335D: (0x5228, 0),  # East Asian ideograph
    0x22375C: (0x65FC, 0),  # East Asian ideograph
    0x23426C: (0x926B, 0),  # East Asian ideograph
    0x23426D: (0x9239, 0),  # East Asian ideograph
    0x6F556C: (0xC607, 0),  # Korean hangul
    0x6F5A42: (0xCF65, 0),  # Korean hangul
    0x6F4B6C: (0xB0E5, 0),  # Korean hangul
    0x23426F: (0x926D, 0),  # East Asian ideograph
    0x234270: (0x926C, 0),  # East Asian ideograph
    0x6F4936: (0xAC9C, 0),  # Korean hangul
    0x234271: (0x924F, 0),  # East Asian ideograph
    0x2D4272: (0x65E3, 0),  # East Asian ideograph
    0x6F5C3E: (0xD3ED, 0),  # Korean hangul
    0x2D3C7E: (0x53A0, 0),  # East Asian ideograph
    0x6F5A43: (0xCF67, 0),  # Korean hangul
    0x294274: (0x94BF, 0),  # East Asian ideograph
    0x6F4D7A: (0xB532, 0),  # Korean hangul
    0x6F4937: (0xAC9F, 0),  # Korean hangul
    0x234277: (0x9260, 0),  # East Asian ideograph
    0x2D302D: (0x4E17, 0),  # East Asian ideograph
    0x6F4D62: (0xB4DC, 0),  # Korean hangul
    0x6F5A44: (0xCF69, 0),  # Korean hangul
    0x234C6A: (0x9741, 0),  # East Asian ideograph
    0x4B5B55: (0x8EE2, 0),  # East Asian ideograph
    0x224279: (0x6AE6, 0),  # East Asian ideograph
    0x216D24: (0x531C, 0),  # East Asian ideograph
    0x6F4D7B: (0xB534, 0),  # Korean hangul
    0x69562E: (0x5CBB, 0),  # East Asian ideograph
    0x6F4938: (0xACA0, 0),  # Korean hangul
    0x6F5B3A: (0xD1A4, 0),  # Korean hangul
    0x275823: (0x88AD, 0),  # East Asian ideograph
    0x29424B: (0x94A3, 0),  # East Asian ideograph
    0x235D77: (0x9EAD, 0),  # East Asian ideograph
    0x6F4F75: (0xB9E5, 0),  # Korean hangul
    0x213D6A: (0x5F97, 0),  # East Asian ideograph
    0x2E3870: (0x714A, 0),  # East Asian ideograph
    0x6F5A45: (0xCF70, 0),  # Korean hangul
    0x22486C: (0x6D00, 0),  # East Asian ideograph
    0x234C6B: (0x9747, 0),  # East Asian ideograph
    0x23427E: (0x9236, 0),  # East Asian ideograph
    0x6F4D7C: (0xB537, 0),  # Korean hangul
    0x6F4B32: (0xB00C, 0),  # Korean hangul
    0x222D2A: (0x610A, 0),  # East Asian ideograph
    0x22442A: (0x6B35, 0),  # East Asian ideograph
    0x216D2E: (0x532D, 0),  # East Asian ideograph
    0x6F4D7D: (0xB538, 0),  # Korean hangul
    0x6F493A: (0xACA8, 0),  # Korean hangul
    0x213362: (0x5230, 0),  # East Asian ideograph
    0x276822: (0x507B, 0),  # East Asian ideograph
    0x2D3473: (0x5374, 0),  # East Asian ideograph
    0x6F5A47: (0xCF74, 0),  # Korean hangul
    0x4C3F7A: (0x6922, 0),  # East Asian ideograph
    0x29535A: (0x9A9F, 0),  # East Asian ideograph
    0x222D32: (0x6112, 0),  # East Asian ideograph
    0x4B5B58: (0x8EE3, 0),  # East Asian ideograph
    0x4B393F: (0x5333, 0),  # East Asian ideograph
    0x216D33: (0x5330, 0),  # East Asian ideograph
    0x2D486E: (0x6F97, 0),  # East Asian ideograph (not in Unicode)
    0x282D34: (0x607D, 0),  # East Asian ideograph
    0x6F497E: (0xADA4, 0),  # Korean hangul
    0x224E32: (0x6FCA, 0),  # East Asian ideograph
    0x6F5C3F: (0xD3F0, 0),  # Korean hangul
    0x2F5A48: (0x9D44, 0),  # East Asian ideograph
    0x22486F: (0x6D33, 0),  # East Asian ideograph
    0x4C5F58: (0x7640, 0),  # East Asian ideograph
    0x6F4E2F: (0xB561, 0),  # Korean hangul
    0x6F493C: (0xACAA, 0),  # Korean hangul
    0x39424F: (0x5554, 0),  # East Asian ideograph
    0x2D3032: (0x7ADD, 0),  # East Asian ideograph
    0x33392F: (0x9029, 0),  # East Asian ideograph
    0x284F5D: (0x6CA3, 0),  # East Asian ideograph
    0x22442D: (0x6B3B, 0),  # East Asian ideograph
    0x216D3E: (0x533D, 0),  # East Asian ideograph
    0x51513B: (0x7E9F, 0),  # East Asian ideograph
    0x222D3F: (0x6121, 0),  # East Asian ideograph
    0x6F4F76: (0xB9E8, 0),  # Korean hangul
    0x292768: (0x8572, 0),  # East Asian ideograph
    0x274B5F: (0x7410, 0),  # East Asian ideograph
    0x6F5A4A: (0xCF85, 0),  # Korean hangul
    0x232D41: (0x8841, 0),  # East Asian ideograph
    0x2D4277: (0x65EE, 0),  # East Asian ideograph
    0x293A6B: (0x8E7F, 0),  # East Asian ideograph
    0x232A57: (0x873E, 0),  # East Asian ideograph
    0x6F4B33: (0xB00D, 0),  # Korean hangul
    0x222D43: (0x6106, 0),  # East Asian ideograph
    0x294251: (0x94C8, 0),  # East Asian ideograph
    0x3B2D44: (0x8842, 0),  # East Asian ideograph
    0x295053: (0x98D9, 0),  # East Asian ideograph
    0x287178: (0x7EF6, 0),  # East Asian ideograph
    0x226D47: (0x7C00, 0),  # East Asian ideograph
    0x2D4141: (0x63B2, 0),  # East Asian ideograph
    0x6F493F: (0xACB0, 0),  # Korean hangul
    0x6F547E: (0xC548, 0),  # Korean hangul
    0x294252: (0x94C9, 0),  # East Asian ideograph
    0x296028: (0x9F86, 0),  # East Asian ideograph
    0x2F3833: (0x8D91, 0),  # East Asian ideograph
    0x216D4B: (0x535D, 0),  # East Asian ideograph
    0x6F4940: (0xACB8, 0),  # Korean hangul
    0x284F61: (0x6EE0, 0),  # East Asian ideograph
    0x6F5C40: (0xD3F4, 0),  # Korean hangul
    0x295360: (0x9A98, 0),  # East Asian ideograph
    0x4B5B5E: (0x5F01, 0),  # East Asian ideograph
    0x232D51: (0x884A, 0),  # East Asian ideograph
    0x6F4941: (0xACB9, 0),  # Korean hangul
    0x294254: (0x94CB, 0),  # East Asian ideograph
    0x286D54: (0x7B5A, 0),  # East Asian ideograph
    0x222D56: (0x53AF, 0),  # East Asian ideograph
    0x232D57: (0x8850, 0),  # East Asian ideograph
    0x21336A: (0x524C, 0),  # East Asian ideograph
    0x294255: (0x94CA, 0),  # East Asian ideograph
    0x29602B: (0x9F85, 0),  # East Asian ideograph
    0x6F4F77: (0xB9EC, 0),  # Korean hangul
    0x21313A: (0x4F38, 0),  # East Asian ideograph
    0x3F462B: (0x5E30, 0),  # East Asian ideograph
    0x274B64: (0x7391, 0),  # East Asian ideograph
    0x6F5A4F: (0xCFB0, 0),  # Korean hangul
    0x696D5A: (0x8F4C, 0),  # East Asian ideograph
    0x29327E: (0x8C07, 0),  # East Asian ideograph
    0x6F4B34: (0xB010, 0),  # Korean hangul
    0x6F4943: (0xACBC, 0),  # Korean hangul
    0x21336B: (0x524B, 0),  # East Asian ideograph
    0x4D4862: (0x9229, 0),  # East Asian ideograph
    0x222D5E: (0x6137, 0),  # East Asian ideograph
    0x28717D: (0x7EFA, 0),  # East Asian ideograph
    0x6F5A50: (0xCFC4, 0),  # Korean hangul
    0x6F4B75: (0xB113, 0),  # Korean hangul
    0x6F4A5A: (0xAEBD, 0),  # Korean hangul
    0x6F4944: (0xACBD, 0),  # Korean hangul
    0x21735B: (0x56C3, 0),  # East Asian ideograph
    0x225541: (0x723F, 0),  # East Asian ideograph
    0x226D63: (0x7C20, 0),  # East Asian ideograph
    0x2D4147: (0x6271, 0),  # East Asian ideograph
    0x216D66: (0x5393, 0),  # East Asian ideograph
    0x6F4945: (0xACC1, 0),  # Korean hangul
    0x21336D: (0x5247, 0),  # East Asian ideograph
    0x294258: (0x94B0, 0),  # East Asian ideograph
    0x6F4B22: (0xAFB8, 0),  # Korean hangul
    0x335941: (0x54D7, 0),  # East Asian ideograph
    0x274B67: (0x73AF, 0),  # East Asian ideograph
    0x234C78: (0x975D, 0),  # East Asian ideograph
    0x234835: (0x942B, 0),  # East Asian ideograph
    0x6F5052: (0xBB4F, 0),  # Korean hangul
    0x276D6D: (0x538D, 0),  # East Asian ideograph
    0x274B68: (0x7477, 0),  # East Asian ideograph
    0x6F5A53: (0xCFE4, 0),  # Korean hangul
    0x225235: (0x712F, 0),  # East Asian ideograph
    0x294F23: (0x9880, 0),  # East Asian ideograph
    0x4B546D: (
        0x82D3,
        0,
    ),  # East Asian ideograph (variant of 21546D which maps to 82D3)
    0x6F4C7B: (0xB2FB, 0),  # Korean hangul
    0x6F4947: (0xACC4, 0),  # Korean hangul
    0x21336F: (0x5256, 0),  # East Asian ideograph
    0x225544: (0x7242, 0),  # East Asian ideograph
    0x6F5724: (0xC7A5, 0),  # Korean hangul
    0x274932: (0x6CFB, 0),  # East Asian ideograph
    0x4B682E: (0x4EC2, 0),  # East Asian ideograph
    0x274B69: (0x73BA, 0),  # East Asian ideograph
    0x6F5A54: (0xCFE8, 0),  # Korean hangul
    0x234837: (0x9441, 0),  # East Asian ideograph
    0x213D3F: (0x5F17, 0),  # East Asian ideograph
    0x4D2D75: (
        0x8872,
        0,
    ),  # East Asian ideograph (variant of 232D75 which maps to 8872)
    0x213370: (0x525B, 0),  # East Asian ideograph
    0x69252C: (0x30AC, 0),  # Katakana letter GA
    0x225821: (0x734B, 0),  # East Asian ideograph
    0x282D77: (0x60AD, 0),  # East Asian ideograph
    0x215822: (0x896F, 0),  # East Asian ideograph
    0x6F5A55: (0xCFF0, 0),  # Korean hangul
    0x6F557D: (0xC63B, 0),  # Korean hangul
    0x234C7B: (0x975F, 0),  # East Asian ideograph
    0x222D79: (0x6164, 0),  # East Asian ideograph
    0x4B5824: (0x897E, 0),  # East Asian ideograph
    0x696D7A: (0x9027, 0),  # East Asian ideograph
    0x6F4949: (0xACD7, 0),  # Korean hangul
    0x215825: (0x8981, 0),  # East Asian ideograph
    0x29425C: (0x94CC, 0),  # East Asian ideograph
    0x695C29: (0x6925, 0),  # East Asian ideograph
    0x4B5826: (
        0x8983,
        0,
    ),  # East Asian ideograph (variant of 215826 which maps to 8983)
    0x232D7C: (0x8879, 0),  # East Asian ideograph
    0x295827: (0x9CB2, 0),  # East Asian ideograph
    0x6F5A56: (0xCFF3, 0),  # Korean hangul
    0x295369: (0x9A7A, 0),  # East Asian ideograph
    0x215828: (0x898B, 0),  # East Asian ideograph
    0x225829: (0x736C, 0),  # East Asian ideograph
    0x6F494A: (0xACE0, 0),  # Korean hangul
    0x21582A: (0x8993, 0),  # East Asian ideograph
    0x21582B: (0x8996, 0),  # East Asian ideograph
    0x2D5259: (0x98DC, 0),  # East Asian ideograph
    0x21582C: (0x89AA, 0),  # East Asian ideograph
    0x284F6B: (0x6F13, 0),  # East Asian ideograph
    0x29536A: (0x9A9D, 0),  # East Asian ideograph
    0x21582D: (0x89A6, 0),  # East Asian ideograph
    0x27582E: (0x89CA, 0),  # East Asian ideograph
    0x6F494B: (0xACE1, 0),  # Korean hangul
    0x22582F: (0x736F, 0),  # East Asian ideograph
    0x275830: (0x89C9, 0),  # East Asian ideograph
    0x215831: (0x89BD, 0),  # East Asian ideograph
    0x6F5A58: (0xCFFC, 0),  # Korean hangul
    0x275832: (0x89C2, 0),  # East Asian ideograph
    0x222871: (0x5EE8, 0),  # East Asian ideograph
    0x22443C: (0x6B43, 0),  # East Asian ideograph
    0x33483B: (0x6CDD, 0),  # East Asian ideograph
    0x2D5833: (0x752A, 0),  # East Asian ideograph
    0x276037: (0x9875, 0),  # East Asian ideograph
    0x6F494C: (0xACE4, 0),  # Korean hangul
    0x215834: (0x89E3, 0),  # East Asian ideograph
    0x29425F: (0x94B6, 0),  # East Asian ideograph
    0x275835: (0x89DE, 0),  # East Asian ideograph
    0x274933: (0x6E0E, 0),  # East Asian ideograph
    0x235B52: (0x9D6F, 0),  # East Asian ideograph
    0x215836: (0x89F8, 0),  # East Asian ideograph
    0x455837: (0x8BA0, 0),  # East Asian ideograph
    0x4C5F69: (0x75EB, 0),  # East Asian ideograph
    0x275838: (0x8BA1, 0),  # East Asian ideograph
    0x6F4B36: (0xB01C, 0),  # Korean hangul
    0x6F494D: (0xACE7, 0),  # Korean hangul
    0x275839: (0x8BA2, 0),  # East Asian ideograph
    0x4D2962: (
        0x86C9,
        0,
    ),  # East Asian ideograph (variant of 232962 which maps to 86C9)
    0x223331: (0x640C, 0),  # East Asian ideograph
    0x22583B: (0x7381, 0),  # East Asian ideograph
    0x6F5A5A: (0xD018, 0),  # Korean hangul
    0x2E7431: (0x7F48, 0),  # East Asian ideograph
    0x4B625C: (
        0x9EB8,
        0,
    ),  # East Asian ideograph (variant of 27625C which maps to 9EB8)
    0x27583C: (0x8BB0, 0),  # East Asian ideograph
    0x22443E: (0x6B48, 0),  # East Asian ideograph
    0x23483D: (0x9467, 0),  # East Asian ideograph
    0x27583D: (0x8BA8, 0),  # East Asian ideograph
    0x273A63: (0x5B6A, 0),  # East Asian ideograph
    0x6F494E: (0xACE8, 0),  # Korean hangul
    0x27583E: (0x8BA7, 0),  # East Asian ideograph
    0x294261: (0x94B2, 0),  # East Asian ideograph
    0x22583F: (0x7388, 0),  # East Asian ideograph
    0x2D525D: (0x6537, 0),  # East Asian ideograph
    0x224C3F: (0x6F26, 0),  # East Asian ideograph
    0x6F5A5B: (0xD02D, 0),  # Korean hangul
    0x215841: (0x8A16, 0),  # East Asian ideograph
    0x215842: (0x8A17, 0),  # East Asian ideograph
    0x6F494F: (0xACEA, 0),  # Korean hangul
    0x275843: (0x8BAD, 0),  # East Asian ideograph
    0x275844: (0x8BBF, 0),  # East Asian ideograph
    0x233732: (0x8D0C, 0),  # East Asian ideograph
    0x2D3045: (0x4E57, 0),  # East Asian ideograph
    0x275845: (0x8BC0, 0),  # East Asian ideograph
    0x6F5A5C: (0xD034, 0),  # Korean hangul
    0x225846: (0x7395, 0),  # East Asian ideograph
    0x294F2C: (0x988F, 0),  # East Asian ideograph
    0x215847: (0x8A25, 0),  # East Asian ideograph
    0x6F4950: (0xACEC, 0),  # Korean hangul
    0x225848: (0x7397, 0),  # East Asian ideograph
    0x6F5739: (0xC810, 0),  # Korean hangul
    0x285C3A: (0x748E, 0),  # East Asian ideograph
    0x6F5054: (0xBB54, 0),  # Korean hangul
    0x215849: (0x8A2D, 0),  # East Asian ideograph
    0x21584A: (0x8A1B, 0),  # East Asian ideograph
    0x6F5A5D: (0xD035, 0),  # Korean hangul
    0x295370: (0x9A9C, 0),  # East Asian ideograph
    0x286D47: (0x7BA6, 0),  # East Asian ideograph
    0x21584B: (0x8A1F, 0),  # East Asian ideograph
    0x21584C: (0x8A3B, 0),  # East Asian ideograph
    0x2D4153: (0x64E3, 0),  # East Asian ideograph
    0x276038: (0x9876, 0),  # East Asian ideograph
    0x6F4951: (0xACEF, 0),  # Korean hangul
    0x22584D: (0x7394, 0),  # East Asian ideograph
    0x294264: (0x94BA, 0),  # East Asian ideograph
    0x21584E: (0x8A55, 0),  # East Asian ideograph
    0x21584F: (0x8A5E, 0),  # East Asian ideograph
    0x4B576C: (0x523E, 0),  # East Asian ideograph
    0x27486D: (0x6DA6, 0),  # East Asian ideograph
    0x275851: (0x8BC2, 0),  # East Asian ideograph
    0x6F4B37: (0xB01D, 0),  # Korean hangul
    0x6F4952: (0xACF0, 0),  # Korean hangul
    0x225852: (0x73A6, 0),  # East Asian ideograph
    0x227768: (0x80B8, 0),  # East Asian ideograph
    0x223336: (0x6415, 0),  # East Asian ideograph
    0x275854: (0x8BC8, 0),  # East Asian ideograph
    0x6F5A5F: (0xD050, 0),  # Korean hangul
    0x275855: (0x8BCB, 0),  # East Asian ideograph
    0x275856: (0x8BC9, 0),  # East Asian ideograph
    0x6F4A5D: (0xAEC4, 0),  # Korean hangul
    0x215857: (0x8A3A, 0),  # East Asian ideograph
    0x21736A: (0x56D4, 0),  # East Asian ideograph
    0x33333C: (0x6C37, 0),  # East Asian ideograph
    0x215858: (0x8A6B, 0),  # East Asian ideograph
    0x4B4621: (0x6B53, 0),  # East Asian ideograph
    0x235859: (0x9C12, 0),  # East Asian ideograph
    0x6F5A60: (0xD06C, 0),  # Korean hangul
    0x27585A: (0x8BE6, 0),  # East Asian ideograph
    0x27585B: (0x8BD5, 0),  # East Asian ideograph
    0x45456D: (0x6A10, 0),  # East Asian ideograph
    0x2D5F2C: (0x5826, 0),  # East Asian ideograph
    0x6F4954: (0xACF3, 0),  # Korean hangul
    0x21585C: (0x8A69, 0),  # East Asian ideograph
    0x6F4B4A: (0xB08F, 0),  # Korean hangul
    0x225551: (0x724F, 0),  # East Asian ideograph
    0x21585D: (0x8A70, 0),  # East Asian ideograph
    0x29443E: (0x94E4, 0),  # East Asian ideograph
    0x21585E: (0x8A63, 0),  # East Asian ideograph
    0x6F5A61: (0xD070, 0),  # Korean hangul
    0x21625F: (0x9EBB, 0),  # East Asian ideograph
    0x21585F: (0x8A7C, 0),  # East Asian ideograph
    0x215860: (0x8AA0, 0),  # East Asian ideograph
    0x6F4E30: (0xB5A0, 0),  # Korean hangul
    0x2D5F2D: (0x964F, 0),  # East Asian ideograph
    0x275861: (0x5938, 0),  # East Asian ideograph
    0x275840: (0x8BAF, 0),  # East Asian ideograph
    0x6F5055: (0xBB58, 0),  # Korean hangul
    0x215862: (0x8A85, 0),  # East Asian ideograph
    0x6F5441: (0xC329, 0),  # Korean hangul
    0x225863: (0x73A0, 0),  # East Asian ideograph
    0x6F5A62: (0xD074, 0),  # Korean hangul
    0x695375: (0x56CE, 0),  # East Asian ideograph
    0x6F5864: (0xCB18, 0),  # Korean hangul
    0x215865: (0x8A62, 0),  # East Asian ideograph
    0x2D575B: (0x886E, 0),  # East Asian ideograph
    0x3F4956: (0x7832, 0),  # East Asian ideograph
    0x215866: (0x8A71, 0),  # East Asian ideograph
    0x285C40: (0x74D2, 0),  # East Asian ideograph
    0x215867: (0x8A6E, 0),  # East Asian ideograph
    0x295132: (0x997D, 0),  # East Asian ideograph
    0x233739: (0x8D11, 0),  # East Asian ideograph
    0x2D5265: (0x79D0, 0),  # East Asian ideograph
    0x225868: (0x73CF, 0),  # East Asian ideograph
    0x6F5A63: (0xD07C, 0),  # Korean hangul
    0x282D5E: (0x607A, 0),  # East Asian ideograph
    0x6F4A25: (0xADD0, 0),  # Korean hangul
    0x275869: (0x8BF4, 0),  # East Asian ideograph
    0x21586A: (0x8AA6, 0),  # East Asian ideograph
    0x6F4B38: (0xB028, 0),  # Korean hangul
    0x21586B: (0x8AA1, 0),  # East Asian ideograph
    0x215155: (0x7DD6, 0),  # East Asian ideograph
    0x22333B: (0x6422, 0),  # East Asian ideograph
    0x27586D: (0x5FD7, 0),  # East Asian ideograph
    0x22456F: (0x6BE7, 0),  # East Asian ideograph
    0x23586E: (0x9C23, 0),  # East Asian ideograph
    0x27586F: (0x8BEC, 0),  # East Asian ideograph
    0x6F4F36: (0xB839, 0),  # Korean hangul
    0x6F4A5E: (0xAECC, 0),  # Korean hangul
    0x215870: (0x8A8D, 0),  # East Asian ideograph
    0x21736F: (0x56E1, 0),  # East Asian ideograph
    0x294469: (0x94FC, 0),  # East Asian ideograph
    0x215871: (
        0x8AA4,
        0,
    ),  # East Asian ideograph (variant of 4B5871 which maps to 8AA4)
    0x23373B: (0x8D12, 0),  # East Asian ideograph
    0x2D5267: (0x79CF, 0),  # East Asian ideograph
    0x215872: (0x8AA8, 0),  # East Asian ideograph
    0x2D4E24: (0x6998, 0),  # East Asian ideograph
    0x215873: (0x8AA5, 0),  # East Asian ideograph
    0x217E60: (0x5BC9, 0),  # East Asian ideograph
    0x215874: (0x8A98, 0),  # East Asian ideograph
    0x4B5D65: (0x8217, 0),  # East Asian ideograph
    0x6F4959: (0xACFD, 0),  # Korean hangul
    0x215875: (0x8A91, 0),  # East Asian ideograph
    0x6F5130: (0xBC9A, 0),  # Korean hangul
    0x275876: (0x8C0A, 0),  # East Asian ideograph
    0x6F4B68: (0xB0C9, 0),  # Korean hangul
    0x215877: (0x8AC4, 0),  # East Asian ideograph
    0x6F5A66: (0xD0A4, 0),  # Korean hangul
    0x4B5176: (0x7E04, 0),  # East Asian ideograph
    0x295379: (0x9A96, 0),  # East Asian ideograph
    0x235878: (0x9C21, 0),  # East Asian ideograph
    0x234323: (0x924E, 0),  # East Asian ideograph
    0x275879: (0x8C08, 0),  # East Asian ideograph
    0x6F495A: (0xAD00, 0),  # Korean hangul
    0x27587A: (0x8BF7, 0),  # East Asian ideograph
    0x224325: (0x6ACC, 0),  # East Asian ideograph
    0x21587B: (0x8AF8, 0),  # East Asian ideograph
    0x23373D: (0x8D14, 0),  # East Asian ideograph
    0x21587C: (0x8AB2, 0),  # East Asian ideograph
    0x234327: (0x9256, 0),  # East Asian ideograph
    0x29537A: (0x9AA2, 0),  # East Asian ideograph
    0x21587D: (0x8ABF, 0),  # East Asian ideograph
    0x224328: (0x6AD1, 0),  # East Asian ideograph
    0x21587E: (0x8AC9, 0),  # East Asian ideograph
    0x4C7D4D: (0x8343, 0),  # East Asian ideograph
    0x2D4329: (0x668E, 0),  # East Asian ideograph
    0x6F495B: (0xAD04, 0),  # Korean hangul
    0x6F5D31: (0xD611, 0),  # Korean hangul
    0x6F4F7C: (0xB9F9, 0),  # Korean hangul
    0x23432B: (0x925A, 0),  # East Asian ideograph
    0x2D3051: (0x5F0D, 0),  # East Asian ideograph
    0x6F5A68: (0xD0A8, 0),  # Korean hangul
    0x216266: (0x9ED1, 0),  # East Asian ideograph
    0x27432D: (0x65F6, 0),  # East Asian ideograph
    0x4B5736: (0x877F, 0),  # East Asian ideograph
    0x23432E: (0x9241, 0),  # East Asian ideograph
    0x6F495C: (0xAD0C, 0),  # Korean hangul
    0x285252: (0x709C, 0),  # East Asian ideograph
    0x275847: (0x8BB7, 0),  # East Asian ideograph
    0x23432F: (0x9283, 0),  # East Asian ideograph
    0x335958: (0x8C4A, 0),  # East Asian ideograph
    0x394330: (0x6644, 0),  # East Asian ideograph
    0x2D526B: (0x7085, 0),  # East Asian ideograph
    0x234331: (0x92A5, 0),  # East Asian ideograph
    0x213065: (0x4ECA, 0),  # East Asian ideograph
    0x6F5626: (0xC653, 0),  # Korean hangul
    0x274332: (0x663C, 0),  # East Asian ideograph
    0x234333: (0x9282, 0),  # East Asian ideograph
    0x2D5F35: (0x78D2, 0),  # East Asian ideograph
    0x6F495D: (0xAD0D, 0),  # Korean hangul
    0x275848: (0x8BB8, 0),  # East Asian ideograph
    0x224334: (0x6ACD, 0),  # East Asian ideograph
    0x234335: (0x92A8, 0),  # East Asian ideograph
    0x2D3053: (0x4E3C, 0),  # East Asian ideograph
    0x29572B: (0x9C90, 0),  # East Asian ideograph
    0x6F5A6A: (0xD0B4, 0),  # Korean hangul
    0x224337: (0x6AEC, 0),  # East Asian ideograph
    0x215E25: (0x938A, 0),  # East Asian ideograph
    0x234338: (0x92A4, 0),  # East Asian ideograph
    0x6F495E: (0xAD0F, 0),  # Korean hangul
    0x224339: (0x6AF3, 0),  # East Asian ideograph
    0x22433A: (0x6AE7, 0),  # East Asian ideograph
    0x2D433B: (0x6662, 0),  # East Asian ideograph
    0x226225: (0x7735, 0),  # East Asian ideograph
    0x4B5B29: (0x8E8D, 0),  # East Asian ideograph
    0x6F495F: (0xAD11, 0),  # Korean hangul
    0x23433E: (0x9276, 0),  # East Asian ideograph
    0x227775: (0x6711, 0),  # East Asian ideograph
    0x22433F: (0x6AEB, 0),  # East Asian ideograph
    0x224340: (0x6AEA, 0),  # East Asian ideograph
    0x21626A: (0x9EDE, 0),  # East Asian ideograph
    0x274341: (0x6655, 0),  # East Asian ideograph
    0x6F5428: (0xC2EB, 0),  # Korean hangul
    0x234342: (0x9288, 0),  # East Asian ideograph
    0x27603B: (0x987A, 0),  # East Asian ideograph
    0x6F4960: (0xAD18, 0),  # Korean hangul
    0x274343: (0x7545, 0),  # East Asian ideograph
    0x6F4F7D: (0xB9FA, 0),  # Korean hangul
    0x223344: (0x6430, 0),  # East Asian ideograph
    0x224344: (0x6AF1, 0),  # East Asian ideograph
    0x4C6C46: (0x7B9F, 0),  # East Asian ideograph
    0x234345: (0x928E, 0),  # East Asian ideograph
    0x6F562A: (0xC65D, 0),  # Korean hangul
    0x234346: (0x92A0, 0),  # East Asian ideograph
    0x4B7954: (0x5968, 0),  # East Asian ideograph
    0x6F4B3A: (0xB045, 0),  # Korean hangul
    0x234347: (0x9277, 0),  # East Asian ideograph
    0x6F4961: (0xAD19, 0),  # Korean hangul
    0x274348: (0x6653, 0),  # East Asian ideograph
    0x274349: (0x5386, 0),  # East Asian ideograph (duplicate simplified)
    0x6F564F: (0xC6E9, 0),  # Korean hangul
    0x224571: (0x6BE8, 0),  # East Asian ideograph
    0x213066: (0x4EC1, 0),  # East Asian ideograph
    0x6F562B: (0xC660, 0),  # Korean hangul
    0x27434B: (0x66A7, 0),  # East Asian ideograph
    0x6F4962: (0xAD1C, 0),  # Korean hangul
    0x27434D: (0x65F7, 0),  # East Asian ideograph
    0x6F4A60: (0xAECF, 0),  # Korean hangul
    0x4B335B: (0x522B, 0),  # East Asian ideograph
    0x23595E: (0x9C6E, 0),  # East Asian ideograph
    0x22434E: (0x6AFD, 0),  # East Asian ideograph
    0x2D3058: (0x4E9C, 0),  # East Asian ideograph
    0x29434F: (0x94DE, 0),  # East Asian ideograph
    0x6F562C: (0xC671, 0),  # Korean hangul
    0x224350: (0x6AFA, 0),  # East Asian ideograph
    0x347D24: (0x83C7, 0),  # East Asian ideograph
    0x6F552E: (0xC561, 0),  # Korean hangul
    0x2D5F3B: (0x96A0, 0),  # East Asian ideograph
    0x6F4963: (0xAD20, 0),  # Korean hangul
    0x6F5132: (0xBCA1, 0),  # Korean hangul
    0x224352: (0x6B01, 0),  # East Asian ideograph
    0x4B4A74: (
        0x731C,
        0,
    ),  # East Asian ideograph (variant of 214A74 which maps to 731C)
    0x234354: (0x927E, 0),  # East Asian ideograph
    0x6F5C47: (0xD45C, 0),  # Korean hangul
    0x274355: (0x4E66, 0),  # East Asian ideograph
    0x6F4964: (0xAD28, 0),  # Korean hangul
    0x334357: (0x6702, 0),  # East Asian ideograph
    0x223348: (0x6435, 0),  # East Asian ideograph
    0x224358: (0x6B03, 0),  # East Asian ideograph
    0x224359: (0x6AF8, 0),  # East Asian ideograph
    0x21605F: (0x98B6, 0),  # East Asian ideograph
    0x4D6047: (0x816D, 0),  # East Asian ideograph
    0x27435A: (0x4F1A, 0),  # East Asian ideograph
    0x23435B: (0x9291, 0),  # East Asian ideograph
    0x27603C: (0x987B, 0),  # East Asian ideograph
    0x6F4965: (0xAD29, 0),  # Korean hangul
    0x6F4F7E: (0xBA00, 0),  # Korean hangul
    0x23435D: (0x929B, 0),  # East Asian ideograph
    0x233748: (0x8D6C, 0),  # East Asian ideograph
    0x2D305B: (0x4EBE, 0),  # East Asian ideograph
    0x217573: (0x57D5, 0),  # East Asian ideograph
    0x6F562F: (0xC67C, 0),  # Korean hangul
    0x284B43: (0x8365, 0),  # East Asian ideograph
    0x22435F: (0x6B0D, 0),  # East Asian ideograph
    0x6F4B3B: (0xB048, 0),  # Korean hangul
    0x224360: (0x6B09, 0),  # East Asian ideograph
    0x355053: (0x98C8, 0),  # East Asian ideograph
    0x6F4966: (0xAD2D, 0),  # Korean hangul
    0x224361: (0x6B0E, 0),  # East Asian ideograph
    0x225563: (0x726E, 0),  # East Asian ideograph
    0x234362: (0x927F, 0),  # East Asian ideograph
    0x69243C: (0x305C, 0),  # Hiragana letter ZE
    0x6F5630: (0xC680, 0),  # Korean hangul
    0x234364: (0x92A3, 0),  # East Asian ideograph
    0x6F4967: (0xAD34, 0),  # Korean hangul
    0x275852: (0x8BCF, 0),  # East Asian ideograph
    0x214366: (0x6727, 0),  # East Asian ideograph
    0x224367: (0x6B11, 0),  # East Asian ideograph
    0x2D4E33: (0x78AA, 0),  # East Asian ideograph
    0x3F5631: (0x517F, 0),  # East Asian ideograph
    0x334369: (0x5932, 0),  # East Asian ideograph
    0x234857: (0x9464, 0),  # East Asian ideograph
    0x21436A: (0x672B, 0),  # East Asian ideograph
    0x293032: (0x7962, 0),  # East Asian ideograph
    0x6F4968: (0xAD38, 0),  # Korean hangul
    0x275853: (0x8BC5, 0),  # East Asian ideograph
    0x33496A: (0x934A, 0),  # East Asian ideograph
    0x22436D: (0x6B19, 0),  # East Asian ideograph
    0x4B5179: (0x7F0B, 0),  # East Asian ideograph
    0x6F5632: (0xC68B, 0),  # Korean hangul
    0x23436F: (0x92D0, 0),  # East Asian ideograph
    0x6F4969: (0xAD3C, 0),  # Korean hangul
    0x2D4370: (0x6736, 0),  # East Asian ideograph
    0x215167: (0x7E46, 0),  # East Asian ideograph
    0x234371: (0x92F1, 0),  # East Asian ideograph
    0x234372: (0x92DF, 0),  # East Asian ideograph
    0x275528: (0x835A, 0),  # East Asian ideograph
    0x215E31: (0x93C8, 0),  # East Asian ideograph
    0x6F496A: (0xAD44, 0),  # Korean hangul
    0x214375: (0x6750, 0),  # East Asian ideograph
    0x215168: (0x7E37, 0),  # East Asian ideograph
    0x6F572B: (0xC7BC, 0),  # Korean hangul
    0x234376: (0x92B6, 0),  # East Asian ideograph
    0x4B4638: (0x6BB1, 0),  # East Asian ideograph
    0x234377: (0x92C0, 0),  # East Asian ideograph
    0x6F5634: (0xC694, 0),  # Korean hangul
    0x6F4D2B: (0xB35B, 0),  # Korean hangul
    0x6F4B3C: (0xB04A, 0),  # Korean hangul
    0x234379: (0x92BE, 0),  # East Asian ideograph
    0x6F572E: (0xC7C0, 0),  # Korean hangul
    0x2D3061: (0x4EB0, 0),  # East Asian ideograph
    0x6F5A78: (0xD0D4, 0),  # Korean hangul
    0x6F5635: (0xC695, 0),  # Korean hangul
    0x29437D: (0x94D8, 0),  # East Asian ideograph
    0x696E28: (0x9056, 0),  # East Asian ideograph
    0x4B5746: (0x8853, 0),  # East Asian ideograph
    0x23437E: (0x92D5, 0),  # East Asian ideograph
    0x2D3D2B: (0x5EBF, 0),  # East Asian ideograph
    0x6F4A62: (0xAED1, 0),  # Korean hangul
    0x276E2A: (0x53A3, 0),  # East Asian ideograph
    0x2D527B: (0x8074, 0),  # East Asian ideograph
    0x6F5A79: (0xD0D5, 0),  # Korean hangul
    0x282D74: (0x6004, 0),  # East Asian ideograph
    0x6F5636: (0xC698, 0),  # Korean hangul
    0x23485C: (0x9465, 0),  # East Asian ideograph
    0x226233: (0x774A, 0),  # East Asian ideograph
    0x6F496D: (0xAD50, 0),  # Korean hangul
    0x6F5C49: (0xD478, 0),  # Korean hangul
    0x6F5840: (0xC9ED, 0),  # Korean hangul
    0x222E2F: (0x615C, 0),  # East Asian ideograph
    0x223351: (0x640A, 0),  # East Asian ideograph
    0x21317D: (0x501A, 0),  # East Asian ideograph
    0x6F5A7A: (0xD0DC, 0),  # Korean hangul
    0x2E7451: (0x7F58, 0),  # East Asian ideograph
    0x6F5637: (0xC6A5, 0),  # Korean hangul
    0x215E35: (0x93DD, 0),  # East Asian ideograph
    0x23485D: (0x9455, 0),  # East Asian ideograph
    0x6F4E31: (0xB5A1, 0),  # Korean hangul
    0x225E2C: (0x7590, 0),  # East Asian ideograph
    0x2D3D2D: (0x5396, 0),  # East Asian ideograph
    0x275859: (0x8BE5, 0),  # East Asian ideograph
    0x21516C: (0x7E2B, 0),  # East Asian ideograph
    0x225128: (0x70E0, 0),  # East Asian ideograph
    0x6F5A7B: (0xD0DD, 0),  # Korean hangul
    0x275529: (0x830E, 0),  # East Asian ideograph
    0x22445F: (0x6B6E, 0),  # East Asian ideograph
    0x33485E: (0x67D2, 0),  # East Asian ideograph
    0x226235: (0x7743, 0),  # East Asian ideograph
    0x2D4171: (0x62CA, 0),  # East Asian ideograph
    0x6F496F: (0xAD6D, 0),  # Korean hangul
    0x6F572C: (0xC7BD, 0),  # Korean hangul
    0x27493A: (0x6FD1, 0),  # East Asian ideograph
    0x23596B: (0x9C7A, 0),  # East Asian ideograph
    0x235B59: (0x9DA9, 0),  # East Asian ideograph
    0x27474E: (0x6CFE, 0),  # East Asian ideograph
    0x6F5639: (0xC6A9, 0),  # Korean hangul
    0x215E37: (0x93D8, 0),  # East Asian ideograph
    0x222E3D: (0x61A2, 0),  # East Asian ideograph
    0x2D3D2F: (0x539B, 0),  # East Asian ideograph
    0x6F5946: (0xCCD0, 0),  # Korean hangul
    0x345D6B: (0x756D, 0),  # East Asian ideograph
    0x285D6B: (0x7572, 0),  # East Asian ideograph
    0x222E40: (0x61A8, 0),  # East Asian ideograph
    0x6F563A: (0xC6B0, 0),  # Korean hangul
    0x4B3C2B: (0x67C3, 0),  # East Asian ideograph (Version J extension)
    0x6F4F37: (0xB840, 0),  # Korean hangul
    0x6F4971: (0xAD73, 0),  # Korean hangul
    0x6F4A63: (0xAED8, 0),  # Korean hangul
    0x22512B: (0x70D4, 0),  # East Asian ideograph
    0x23552A: (0x9AEF, 0),  # East Asian ideograph
    0x6F5A7E: (0xD0EC, 0),  # Korean hangul
    0x222E45: (0x6196, 0),  # East Asian ideograph
    0x6F563B: (0xC6B1, 0),  # Korean hangul
    0x6F4972: (0xAD74, 0),  # Korean hangul
    0x6F563C: (0xC6B4, 0),  # Korean hangul
    0x234862: (0x946A, 0),  # East Asian ideograph
    0x282E4C: (0x6126, 0),  # East Asian ideograph
    0x2D5F4B: (0x96D1, 0),  # East Asian ideograph
    0x6F4973: (0xAD75, 0),  # Korean hangul
    0x215171: (0x7E54, 0),  # East Asian ideograph
    0x6F563D: (0xC6B7, 0),  # Korean hangul
    0x215E3B: (0x93FD, 0),  # East Asian ideograph
    0x2D4176: (0x6483, 0),  # East Asian ideograph
    0x2D5F4C: (0x9DC4, 0),  # East Asian ideograph
    0x6F4974: (0xAD76, 0),  # Korean hangul
    0x6F5D32: (0xD613, 0),  # Korean hangul
    0x282E52: (0x6003, 0),  # East Asian ideograph
    0x27493B: (0x6CA5, 0),  # East Asian ideograph
    0x233941: (0x8DFD, 0),  # East Asian ideograph
    0x6F563E: (0xC6B8, 0),  # Korean hangul
    0x4B5773: (0x7ED4, 0),  # East Asian ideograph
    0x213C23: (0x5D22, 0),  # East Asian ideograph
    0x286E56: (0x7BA8, 0),  # East Asian ideograph
    0x2D3D34: (0x5EFE, 0),  # East Asian ideograph
    0x215173: (0x7E5E, 0),  # East Asian ideograph
    0x223359: (0x6407, 0),  # East Asian ideograph
    0x216E58: (0x535F, 0),  # East Asian ideograph
    0x707523: (0x9170, 0),  # East Asian ideograph
    0x6F4B77: (0xB119, 0),  # Korean hangul
    0x222E5A: (0x61CB, 0),  # East Asian ideograph
    0x213C24: (0x5D29, 0),  # East Asian ideograph
    0x33355C: (0x5449, 0),  # East Asian ideograph
    0x273648: (0x95EE, 0),  # East Asian ideograph
    0x282E5C: (0x603F, 0),  # East Asian ideograph
    0x27514C: (0x7EFF, 0),  # East Asian ideograph
    0x6F5579: (0xC635, 0),  # Korean hangul
    0x6F5640: (0xC6BA, 0),  # Korean hangul
    0x6F5951: (0xCD5C, 0),  # Korean hangul
    0x4B397B: (0x5A2F, 0),  # East Asian ideograph
    0x29402C: (0x90D0, 0),  # East Asian ideograph
    0x22623D: (0x7760, 0),  # East Asian ideograph
    0x6F4977: (0xAD7F, 0),  # Korean hangul
    0x6F5136: (0xBCB0, 0),  # Korean hangul
    0x216E61: (0x5414, 0),  # East Asian ideograph
    0x22335B: (0x643B, 0),  # East Asian ideograph
    0x6F4A2E: (0xADFC, 0),  # Korean hangul
    0x6F5641: (0xC6C0, 0),  # Korean hangul
    0x213C26: (0x5D19, 0),  # East Asian ideograph
    0x275863: (0x8BE1, 0),  # East Asian ideograph
    0x695A7E: (0x66BC, 0),  # East Asian ideograph
    0x287E61: (0x82CC, 0),  # East Asian ideograph
    0x232E68: (0x88D2, 0),  # East Asian ideograph
    0x6F5642: (0xC6C1, 0),  # Korean hangul
    0x234868: (0x946B, 0),  # East Asian ideograph
    0x6F5429: (0xC2EC, 0),  # Korean hangul
    0x334425: (0x76C3, 0),  # East Asian ideograph
    0x6F4979: (0xAD82, 0),  # Korean hangul
    0x296062: (0x9F9B, 0),  # East Asian ideograph
    0x22335D: (0x643F, 0),  # East Asian ideograph
    0x23375C: (0x8D7A, 0),  # East Asian ideograph
    0x6F5643: (0xC6C3, 0),  # Korean hangul
    0x213C28: (0x5D50, 0),  # East Asian ideograph
    0x216E6F: (0x541A, 0),  # East Asian ideograph
    0x6F497A: (0xAD88, 0),  # Korean hangul
    0x275422: (0x810F, 0),  # East Asian ideograph (duplicate simplified)
    0x222E71: (0x61E0, 0),  # East Asian ideograph
    0x2D3E40: (0x6052, 0),  # East Asian ideograph
    0x6F5644: (0xC6C5, 0),  # Korean hangul
    0x28702E: (0x56E2, 0),  # East Asian ideograph (duplicate simplified)
    0x6F497B: (0xAD8C, 0),  # Korean hangul
    0x6F4A65: (0xAEF4, 0),  # Korean hangul
    0x455164: (0x53BF, 0),  # East Asian ideograph
    0x215921: (0x8AC2, 0),  # East Asian ideograph
    0x222E77: (0x61E5, 0),  # East Asian ideograph
    0x275922: (0x8C01, 0),  # East Asian ideograph
    0x275923: (0x8BDE, 0),  # East Asian ideograph
    0x232652: (0x85A2, 0),  # East Asian ideograph
    0x6F552F: (0xC564, 0),  # Korean hangul
    0x216E79: (0x5454, 0),  # East Asian ideograph
    0x275924: (0x8BBA, 0),  # East Asian ideograph
    0x235925: (0x9C32, 0),  # East Asian ideograph
    0x215926: (0x8AFA, 0),  # East Asian ideograph
    0x275927: (0x8C0F, 0),  # East Asian ideograph
    0x216E7D: (0x543D, 0),  # East Asian ideograph
    0x235928: (0x9C48, 0),  # East Asian ideograph
    0x282E7E: (0x603C, 0),  # East Asian ideograph
    0x215929: (0x8AE7, 0),  # East Asian ideograph
    0x275868: (0x8BDF, 0),  # East Asian ideograph
    0x6F505D: (0xBBC8, 0),  # Korean hangul
    0x23592A: (0x9C33, 0),  # East Asian ideograph
    0x21592B: (0x8B00, 0),  # East Asian ideograph
    0x6F5B72: (0xD31D, 0),  # Korean hangul
    0x27592C: (0x8C12, 0),  # East Asian ideograph
    0x6F5647: (0xC6D0, 0),  # Korean hangul
    0x29416B: (0x948E, 0),  # East Asian ideograph
    0x213E47: (0x6064, 0),  # East Asian ideograph
    0x23486D: (0x9471, 0),  # East Asian ideograph
    0x27592E: (0x8BFA, 0),  # East Asian ideograph
    0x22592F: (0x73D4, 0),  # East Asian ideograph
    0x27493D: (0x6F47, 0),  # East Asian ideograph
    0x233761: (0x8D84, 0),  # East Asian ideograph
    0x215930: (0x8AED, 0),  # East Asian ideograph
    0x335A7B: (0x8E28, 0),  # East Asian ideograph
    0x275931: (0x8C24, 0),  # East Asian ideograph
    0x6F5648: (0xC6D4, 0),  # Korean hangul
    0x697174: (0x9ADE, 0),  # East Asian ideograph
    0x235932: (0x9C35, 0),  # East Asian ideograph
    0x275933: (0x8C1C, 0),  # East Asian ideograph
    0x27586A: (0x8BF5, 0),  # East Asian ideograph
    0x215934: (0x8B1B, 0),  # East Asian ideograph
    0x215935: (0x8B0A, 0),  # East Asian ideograph
    0x225936: (0x73E7, 0),  # East Asian ideograph
    0x6F5649: (0xC6DC, 0),  # Korean hangul
    0x275937: (0x8A8A, 0),  # East Asian ideograph
    0x215938: (0x8B1D, 0),  # East Asian ideograph
    0x27586B: (0x8BEB, 0),  # East Asian ideograph
    0x6F4A66: (0xAF0D, 0),  # Korean hangul
    0x282F66: (0x6217, 0),  # East Asian ideograph
    0x215939: (0x8B39, 0),  # East Asian ideograph
    0x22513A: (0x70D0, 0),  # East Asian ideograph
    0x21593A: (0x8B2C, 0),  # East Asian ideograph
    0x21593B: (0x8B28, 0),  # East Asian ideograph
    0x6F564A: (0xC6DD, 0),  # Korean hangul
    0x224471: (0x6B82, 0),  # East Asian ideograph
    0x21593C: (0x8B58, 0),  # East Asian ideograph
    0x27593D: (0x8C31, 0),  # East Asian ideograph
    0x6F5138: (0xBCB3, 0),  # Korean hangul
    0x27586C: (0x8BED, 0),  # East Asian ideograph
    0x27593E: (0x8C32, 0),  # East Asian ideograph
    0x22513B: (0x70C7, 0),  # East Asian ideograph
    0x22593F: (0x73E9, 0),  # East Asian ideograph
    0x274E5B: (0x77FF, 0),  # East Asian ideograph
    0x215940: (0x8B5A, 0),  # East Asian ideograph
    0x6F564B: (0xC6DF, 0),  # Korean hangul
    0x395577: (0x854B, 0),  # East Asian ideograph
    0x213C30: (0x5DCD, 0),  # East Asian ideograph
    0x215942: (0x8B4F, 0),  # East Asian ideograph
    0x6F573B: (0xC813, 0),  # Korean hangul
    0x275943: (0x8BAE, 0),  # East Asian ideograph
    0x22472C: (0x6C54, 0),  # East Asian ideograph
    0x22513C: (0x70DA, 0),  # East Asian ideograph
    0x6F5944: (0xCCBC, 0),  # Korean hangul
    0x2D435F: (0x6716, 0),  # East Asian ideograph
    0x6F5B73: (0xD31F, 0),  # Korean hangul
    0x235945: (0x9C51, 0),  # East Asian ideograph
    0x6F564C: (0xC6E0, 0),  # Korean hangul
    0x69255A: (0x30DA, 0),  # Katakana letter PE
    0x213C31: (0x5DD2, 0),  # East Asian ideograph
    0x215947: (0x8B74, 0),  # East Asian ideograph
    0x215948: (0x8B77, 0),  # East Asian ideograph
    0x2E4C7B: (0x6E86, 0),  # East Asian ideograph
    0x22513D: (0x70C6, 0),  # East Asian ideograph
    0x235949: (0x9C63, 0),  # East Asian ideograph
    0x333323: (0x4E21, 0),  # East Asian ideograph
    0x22594A: (0x73F8, 0),  # East Asian ideograph
    0x6F564D: (0xC6E1, 0),  # Korean hangul
    0x6F5275: (0xC0DB, 0),  # Korean hangul
    0x27594B: (0x53D8, 0),  # East Asian ideograph
    0x21594C: (0x8B93, 0),  # East Asian ideograph
    0x27594D: (0x8C36, 0),  # East Asian ideograph
    0x28582B: (0x7303, 0),  # East Asian ideograph
    0x27594E: (0x8C17, 0),  # East Asian ideograph
    0x21594F: (0x8B9A, 0),  # East Asian ideograph
    0x6F564E: (0xC6E8, 0),  # Korean hangul
    0x4B3C2F: (0x5DBA, 0),  # East Asian ideograph
    0x287030: (0x7C9D, 0),  # East Asian ideograph
    0x213C33: (0x5DD6, 0),  # East Asian ideograph
    0x6F5A2C: (0xCEF9, 0),  # Korean hangul
    0x2D3253: (0x50E3, 0),  # East Asian ideograph
    0x6F4A67: (0xAF2C, 0),  # Korean hangul
    0x6F5952: (0xCD78, 0),  # Korean hangul
    0x333768: (0x8FF4, 0),  # East Asian ideograph
    0x21373F: (0x5659, 0),  # East Asian ideograph
    0x393439: (0x61C3, 0),  # East Asian ideograph
    0x215954: (0x8C48, 0),  # East Asian ideograph
    0x395652: (0x87A1, 0),  # East Asian ideograph
    0x215955: (0x8C49, 0),  # East Asian ideograph
    0x215956: (0x8C4C, 0),  # East Asian ideograph
    0x396167: (0x9B2A, 0),  # East Asian ideograph
    0x706B5B: (0x810E, 0),  # East Asian ideograph
    0x275957: (0x7AD6, 0),  # East Asian ideograph
    0x215958: (0x8C50, 0),  # East Asian ideograph
    0x474931: (0x95F6, 0),  # East Asian ideograph
    0x2D5959: (0x8277, 0),  # East Asian ideograph
    0x213665: (0x558A, 0),  # East Asian ideograph
    0x22595A: (0x73FD, 0),  # East Asian ideograph
    0x6F4E32: (0xB5A4, 0),  # Korean hangul
    0x217C24: (0x5AA7, 0),  # East Asian ideograph
    0x2F5973: (0x9CEC, 0),  # East Asian ideograph
    0x6F595B: (0xCDB0, 0),  # Korean hangul
    0x21595C: (0x8C62, 0),  # East Asian ideograph
    0x4B4655: (0x6C17, 0),  # East Asian ideograph
    0x6F595D: (0xCDCC, 0),  # Korean hangul
    0x455D3E: (0x9485, 0),  # East Asian ideograph
    0x6F5B74: (0xD320, 0),  # Korean hangul
    0x21595E: (0x8C6B, 0),  # East Asian ideograph
    0x6F5651: (0xC6F0, 0),  # Korean hangul
    0x69717D: (0x9AF1, 0),  # East Asian ideograph
    0x2D595F: (0x732A, 0),  # East Asian ideograph
    0x2D5960: (0x72B2, 0),  # East Asian ideograph
    0x6F5731: (0xC7C9, 0),  # Korean hangul
    0x513A47: (0x8885, 0),  # East Asian ideograph
    0x6F5962: (0xCE30, 0),  # Korean hangul
    0x39505B: (0x9B3B, 0),  # East Asian ideograph
    0x215963: (0x8C8A, 0),  # East Asian ideograph
    0x6F5652: (0xC6F8, 0),  # Korean hangul
    0x224479: (0x6B8D, 0),  # East Asian ideograph
    0x4B5964: (0x72E2, 0),  # East Asian ideograph
    0x234435: (0x92DD, 0),  # East Asian ideograph
    0x2D5965: (0x72F8, 0),  # East Asian ideograph
    0x2D3D48: (0x5F4A, 0),  # East Asian ideograph
    0x275966: (0x7683, 0),  # East Asian ideograph
    0x213F79: (0x6249, 0),  # East Asian ideograph
    0x215967: (0x8C93, 0),  # East Asian ideograph
    0x215968: (0x8C9D, 0),  # East Asian ideograph
    0x295B77: (0x9E63, 0),  # East Asian ideograph
    0x215969: (0x8C9E, 0),  # East Asian ideograph
    0x217C27: (0x5A9C, 0),  # East Asian ideograph
    0x6F5C2D: (0xD399, 0),  # Korean hangul
    0x27596A: (0x8D1F, 0),  # East Asian ideograph
    0x6F4A68: (0xAF2D, 0),  # Korean hangul
    0x706B5F: (0x8112, 0),  # East Asian ideograph
    0x21596B: (0x8CA2, 0),  # East Asian ideograph
    0x52735D: (
        0x7E8A,
        0,
    ),  # East Asian ideograph (variant of 22735D which maps to 7E8A)
    0x695C30: (0x6923, 0),  # East Asian ideograph
    0x225144: (0x7104, 0),  # East Asian ideograph
    0x22596C: (0x7430, 0),  # East Asian ideograph
    0x33332A: (0x4E93, 0),  # East Asian ideograph
    0x21596D: (0x8CAC, 0),  # East Asian ideograph
    0x21596E: (0x8CAB, 0),  # East Asian ideograph
    0x217C28: (0x5A7C, 0),  # East Asian ideograph
    0x697260: (0x9C30, 0),  # East Asian ideograph
    0x27596F: (0x8D27, 0),  # East Asian ideograph
    0x215970: (0x8CAA, 0),  # East Asian ideograph
    0x695C31: (0x6921, 0),  # East Asian ideograph
    0x215971: (0x8CA7, 0),  # East Asian ideograph
    0x6F5C4F: (0xD48B, 0),  # Korean hangul
    0x275E46: (0x9576, 0),  # East Asian ideograph
    0x215972: (0x8CA9, 0),  # East Asian ideograph
    0x215973: (0x8CAF, 0),  # East Asian ideograph
    0x217C29: (0x5A96, 0),  # East Asian ideograph
    0x6F5974: (0xCE85, 0),  # Korean hangul
    0x275975: (0x8D39, 0),  # East Asian ideograph
    0x6F5060: (0xBBF9, 0),  # Korean hangul
    0x4B465A: (0x6C32, 0),  # East Asian ideograph
    0x275976: (0x8D32, 0),  # East Asian ideograph
    0x234421: (0x92C6, 0),  # East Asian ideograph
    0x215977: (0x8CC0, 0),  # East Asian ideograph
    0x6F5656: (0xC70C, 0),  # Korean hangul
    0x277748: (0x57B2, 0),  # East Asian ideograph
    0x215978: (0x8CB4, 0),  # East Asian ideograph
    0x275979: (0x8D34, 0),  # East Asian ideograph
    0x295B2A: (0x9E46, 0),  # East Asian ideograph
    0x6F503E: (0xBAB0, 0),  # Korean hangul
    0x21597A: (0x8CB7, 0),  # East Asian ideograph
    0x234425: (0x92F4, 0),  # East Asian ideograph
    0x27597B: (0x8D2C, 0),  # East Asian ideograph
    0x274426: (0x4E1C, 0),  # East Asian ideograph
    0x27597C: (0x8D3B, 0),  # East Asian ideograph
    0x6F5657: (0xC714, 0),  # Korean hangul
    0x234427: (0x92CF, 0),  # East Asian ideograph
    0x292D51: (0x8511, 0),  # East Asian ideograph
    0x21597D: (0x8CB8, 0),  # East Asian ideograph
    0x23443A: (0x92CA, 0),  # East Asian ideograph
    0x27597E: (0x8D38, 0),  # East Asian ideograph
    0x23442A: (0x92B2, 0),  # East Asian ideograph
    0x225148: (0x70F3, 0),  # East Asian ideograph
    0x29442B: (0x9503, 0),  # East Asian ideograph
    0x6F5324: (0xC120, 0),  # Korean hangul
    0x6F5658: (0xC717, 0),  # Korean hangul
    0x23442C: (0x92E7, 0),  # East Asian ideograph
    0x294F6B: (0x98A1, 0),  # East Asian ideograph
    0x696D41: (0x8EC8, 0),  # East Asian ideograph
    0x23442D: (0x92C7, 0),  # East Asian ideograph
    0x277D40: (0x5AF1, 0),  # East Asian ideograph
    0x2D3D4E: (0x7BF2, 0),  # East Asian ideograph
    0x23442E: (0x92F0, 0),  # East Asian ideograph
    0x6F4A69: (0xAF30, 0),  # Korean hangul
    0x23442F: (0x92DB, 0),  # East Asian ideograph
    0x6F4E5E: (0xB768, 0),  # Korean hangul
    0x234430: (0x92DC, 0),  # East Asian ideograph
    0x2D4E5B: (0x945B, 0),  # East Asian ideograph
    0x234431: (0x92D8, 0),  # East Asian ideograph
    0x224432: (0x6B39, 0),  # East Asian ideograph
    0x234433: (0x92E9, 0),  # East Asian ideograph
    0x224435: (0x6B3F, 0),  # East Asian ideograph
    0x274E5E: (0x783E, 0),  # East Asian ideograph
    0x6F565A: (0xC720, 0),  # Korean hangul
    0x27375A: (0x4E25, 0),  # East Asian ideograph
    0x224437: (0x6B46, 0),  # East Asian ideograph
    0x2D3D50: (0x5F5C, 0),  # East Asian ideograph
    0x224438: (0x6B41, 0),  # East Asian ideograph
    0x234439: (0x92D1, 0),  # East Asian ideograph
    0x6F5061: (0xBBFC, 0),  # Korean hangul
    0x283561: (0x64BA, 0),  # East Asian ideograph
    0x22443A: (0x6B40, 0),  # East Asian ideograph
    0x6F565B: (0xC721, 0),  # Korean hangul
    0x22443B: (0x6B42, 0),  # East Asian ideograph
    0x6F5973: (0xCE84, 0),  # Korean hangul
    0x6F4C7E: (0xB301, 0),  # Korean hangul
    0x23443C: (0x92C2, 0),  # East Asian ideograph
    0x6F4F29: (0xB810, 0),  # Korean hangul
    0x454C3C: (0x7589, 0),  # East Asian ideograph
    0x6F5733: (0xC7D8, 0),  # Korean hangul
    0x23443E: (0x92CC, 0),  # East Asian ideograph
    0x22443F: (0x6B4A, 0),  # East Asian ideograph
    0x235B60: (0x9D98, 0),  # East Asian ideograph
    0x2E525D: (0x715B, 0),  # East Asian ideograph
    0x6F565C: (0xC724, 0),  # Korean hangul
    0x234440: (0x92EF, 0),  # East Asian ideograph
    0x213C41: (0x5DF7, 0),  # East Asian ideograph
    0x234441: (0x92E8, 0),  # East Asian ideograph
    0x6F5D35: (0xD61C, 0),  # Korean hangul
    0x287739: (0x8069, 0),  # East Asian ideograph
    0x27587E: (0x8BFF, 0),  # East Asian ideograph
    0x234443: (0x92EB, 0),  # East Asian ideograph
    0x695C39: (0x697E, 0),  # East Asian ideograph
    0x295D36: (0x9E2C, 0),  # East Asian ideograph
    0x2D4444: (0x69C5, 0),  # East Asian ideograph
    0x6F565D: (0xC728, 0),  # Korean hangul
    0x234445: (0x92F5, 0),  # East Asian ideograph
    0x224446: (
        0x6B4E,
        0,
    ),  # East Asian ideograph (variant of 4C4446 which maps to 6B4E)
    0x6F4A6A: (0xAF34, 0),  # Korean hangul
    0x234448: (0x92F2, 0),  # East Asian ideograph
    0x28422B: (0x6A2F, 0),  # East Asian ideograph
    0x334449: (0x6144, 0),  # East Asian ideograph
    0x22444A: (0x6B57, 0),  # East Asian ideograph
    0x2D444B: (0x6852, 0),  # East Asian ideograph
    0x6F5530: (0xC568, 0),  # Korean hangul
    0x6F513C: (0xBCC0, 0),  # Korean hangul
    0x22444C: (0x6B54, 0),  # East Asian ideograph
    0x23444D: (0x9307, 0),  # East Asian ideograph
    0x22444E: (0x6B55, 0),  # East Asian ideograph
    0x6F5C51: (0xD4CC, 0),  # Korean hangul
    0x515E5D: (0x9616, 0),  # East Asian ideograph
    0x2D4450: (0x8308, 0),  # East Asian ideograph
    0x224451: (0x6B5C, 0),  # East Asian ideograph
    0x287A56: (0x8114, 0),  # East Asian ideograph
    0x6F5062: (0xBBFF, 0),  # Korean hangul
    0x212B38: (0xFF0C, 0),  # Ideographic variant comma
    0x225150: (0x70F4, 0),  # East Asian ideograph
    0x23554F: (0x9B10, 0),  # East Asian ideograph
    0x224453: (0x6B5E, 0),  # East Asian ideograph
    0x6F5B77: (0xD328, 0),  # Korean hangul
    0x224454: (0x6B60, 0),  # East Asian ideograph
    0x22625D: (0x777E, 0),  # East Asian ideograph
    0x217C34: (0x5AAE, 0),  # East Asian ideograph
    0x4B4456: (0x6813, 0),  # East Asian ideograph
    0x6F5734: (0xC800, 0),  # Korean hangul
    0x294457: (0x9529, 0),  # East Asian ideograph
    0x212B39: (0xFF1B, 0),  # Ideographic semicolon
    0x234458: (0x931F, 0),  # East Asian ideograph
    0x6F5661: (0xC73C, 0),  # Korean hangul
    0x23445A: (0x9331, 0),  # East Asian ideograph
    0x4D5F70: (0x9F44, 0),  # East Asian ideograph
    0x22445B: (0x6B6B, 0),  # East Asian ideograph
    0x22736B: (0x7E95, 0),  # East Asian ideograph
    0x22445D: (0x6B6C, 0),  # East Asian ideograph
    0x4C284C: (0x53A9, 0),  # East Asian ideograph
    0x4B3C33: (0x5DCC, 0),  # East Asian ideograph
    0x215E60: (0x95BB, 0),  # East Asian ideograph
    0x23445F: (0x930F, 0),  # East Asian ideograph
    0x6F4A6B: (0xAF3C, 0),  # Korean hangul
    0x224461: (0x6B71, 0),  # East Asian ideograph
    0x6F5D2C: (0xD600, 0),  # Korean hangul
    0x234462: (0x9302, 0),  # East Asian ideograph
    0x6F5170: (0xBE4B, 0),  # Korean hangul
    0x274463: (0x6761, 0),  # East Asian ideograph
    0x234464: (0x9324, 0),  # East Asian ideograph
    0x2D5B2F: (0x8EB1, 0),  # East Asian ideograph
    0x214466: (0x6885, 0),  # East Asian ideograph
    0x274468: (0x67AD, 0),  # East Asian ideograph
    0x294F77: (0x989F, 0),  # East Asian ideograph
    0x6F5221: (0xBE70, 0),  # Korean hangul
    0x6F4B7A: (0xB11D, 0),  # Korean hangul
    0x274469: (0x6800, 0),  # East Asian ideograph
    0x2D5F73: (0x975A, 0),  # Unrelated variant of EACC 234C76 which maps to 975A
    0x23446A: (0x9323, 0),  # East Asian ideograph
    0x22446B: (0x6B7E, 0),  # East Asian ideograph
    0x212B3D: (0xFF01, 0),  # Ideographic exclamation point
    0x225155: (0x7111, 0),  # East Asian ideograph
    0x23446C: (0x9321, 0),  # East Asian ideograph
    0x4C683E: (0x79EB, 0),  # East Asian ideograph
    0x27446D: (0x5F03, 0),  # East Asian ideograph
    0x6F5222: (0xBE71, 0),  # Korean hangul
    0x27446E: (0x6816, 0),  # East Asian ideograph
    0x2D4E79: (0x5FA1, 0),  # East Asian ideograph
    0x6F5735: (0xC801, 0),  # Korean hangul
    0x2D4B43: (0x746F, 0),  # East Asian ideograph
    0x274471: (0x680B, 0),  # East Asian ideograph
    0x4B5A68: (
        0x8DF5,
        0,
    ),  # East Asian ideograph (variant of 275A68 which maps to 8DF5)
    0x234472: (0x9301, 0),  # East Asian ideograph
    0x6F5223: (0xBE73, 0),  # Korean hangul
    0x6F5326: (0xC124, 0),  # Korean hangul
    0x224473: (0x6B84, 0),  # East Asian ideograph
    0x2D3332: (0x5190, 0),  # East Asian ideograph
    0x234474: (0x9315, 0),  # East Asian ideograph
    0x47366F: (0x8D4D, 0),  # East Asian ideograph
    0x294475: (0x9494, 0),  # East Asian ideograph
    0x235556: (0x9B1D, 0),  # East Asian ideograph
    0x234476: (0x9329, 0),  # East Asian ideograph
    0x23386F: (0x8DBA, 0),  # East Asian ideograph
    0x232F21: (0x88FC, 0),  # East Asian ideograph
    0x2D4A26: (0x713C, 0),  # East Asian ideograph
    0x287035: (0x7C74, 0),  # East Asian ideograph
    0x6F5224: (0xBE74, 0),  # Korean hangul
    0x234478: (0x932E, 0),  # East Asian ideograph
    0x234479: (0x932A, 0),  # East Asian ideograph
    0x6F4A6C: (0xAF3D, 0),  # Korean hangul
    0x27447A: (0x67A3, 0),  # East Asian ideograph
    0x6F5D2D: (0xD601, 0),  # Korean hangul
    0x22447B: (0x6B95, 0),  # East Asian ideograph
    0x21447C: (0x6912, 0),  # East Asian ideograph
    0x216F27: (0x5423, 0),  # East Asian ideograph
    0x213C4D: (0x5E11, 0),  # East Asian ideograph
    0x2D447D: (0x684C, 0),  # East Asian ideograph
    0x2D3D5E: (0x9AF4, 0),  # East Asian ideograph
    0x23447E: (0x9335, 0),  # East Asian ideograph
    0x706058: (0x562D, 0),  # East Asian ideograph
    0x273671: (0x54DF, 0),  # East Asian ideograph
    0x6F5226: (0xBE7B, 0),  # Korean hangul
    0x232F2D: (0x8909, 0),  # East Asian ideograph
    0x23444C: (0x9303, 0),  # East Asian ideograph
    0x4D5B35: (0x9DAB, 0),  # East Asian ideograph
    0x232F2F: (0x8918, 0),  # East Asian ideograph
    0x6F5B79: (0xD32C, 0),  # Korean hangul
    0x213D3C: (0x5F15, 0),  # East Asian ideograph
    0x6F566A: (0xC774, 0),  # Korean hangul
    0x6F5227: (0xBE7C, 0),  # Korean hangul
    0x213C4F: (0x5E25, 0),  # East Asian ideograph
    0x2D3632: (0x8A7B, 0),  # East Asian ideograph
    0x346622: (0x589D, 0),  # East Asian ideograph
    0x295C47: (0x9E68, 0),  # East Asian ideograph
    0x293A2E: (0x8DC4, 0),  # East Asian ideograph
    0x2E6F35: (0x6CD4, 0),  # East Asian ideograph
    0x6F566B: (0xC775, 0),  # Korean hangul
    0x6F5228: (0xBE7D, 0),  # Korean hangul
    0x22516D: (0x7134, 0),  # East Asian ideograph
    0x23444E: (0x931E, 0),  # East Asian ideograph
    0x2F5D49: (0x9EA4, 0),  # East Asian ideograph
    0x2E313A: (0x6332, 0),  # East Asian ideograph
    0x216F3A: (0x546D, 0),  # East Asian ideograph
    0x6F566C: (0xC778, 0),  # Korean hangul
    0x282458: (0x5D03, 0),  # East Asian ideograph
    0x216F3B: (0x5491, 0),  # East Asian ideograph
    0x6F5229: (0xBE80, 0),  # Korean hangul
    0x4D5F7B: (0x97F2, 0),  # East Asian ideograph
    0x222F3D: (0x6201, 0),  # East Asian ideograph
    0x295C49: (0x9E47, 0),  # East Asian ideograph
    0x4B577E: (0x7E7F, 0),  # East Asian ideograph
    0x217C41: (0x5AC4, 0),  # East Asian ideograph
    0x215A28: (0x8CC2, 0),  # East Asian ideograph
    0x697265: (0x9C5A, 0),  # East Asian ideograph
    0x216F42: (0x5494, 0),  # East Asian ideograph
    0x232F43: (0x8915, 0),  # East Asian ideograph
    0x333344: (0x51DB, 0),  # East Asian ideograph
    0x6F566E: (0xC77D, 0),  # Korean hangul
    0x274340: (0x6656, 0),  # East Asian ideograph
    0x6F522B: (0xBE8C, 0),  # Korean hangul
    0x213C53: (0x5E36, 0),  # East Asian ideograph
    0x4C5175: (0x8315, 0),  # East Asian ideograph
    0x225E37: (0x75A2, 0),  # East Asian ideograph
    0x222F47: (0x6214, 0),  # East Asian ideograph
    0x2D3921: (0x591F, 0),  # East Asian ideograph
    0x233345: (0x8AE2, 0),  # East Asian ideograph
    0x216F49: (0x548D, 0),  # East Asian ideograph
    0x355D5C: (0x8C8E, 0),  # East Asian ideograph
    0x6F566F: (0xC783, 0),  # Korean hangul
    0x216F4A: (0x5463, 0),  # East Asian ideograph
    0x6F522C: (0xBE8F, 0),  # Korean hangul
    0x6F5737: (0xC808, 0),  # Korean hangul
    0x225160: (0x70F6, 0),  # East Asian ideograph
    0x6F5670: (0xC784, 0),  # Korean hangul
    0x234453: (0x931D, 0),  # East Asian ideograph
    0x216F7B: (0x551A, 0),  # East Asian ideograph
    0x6F5D68: (0xD744, 0),  # Korean hangul
    0x6F5671: (0xC785, 0),  # Korean hangul
    0x6F522E: (0xBE91, 0),  # Korean hangul
    0x294427: (0x94D7, 0),  # East Asian ideograph
    0x234454: (0x92FA, 0),  # East Asian ideograph
    0x2D3D67: (0x9015, 0),  # East Asian ideograph
    0x6F4A6E: (0xAF41, 0),  # Korean hangul
    0x222F56: (0x6223, 0),  # East Asian ideograph
    0x6F4F43: (0xB8E8, 0),  # Korean hangul
    0x6F5D2F: (0xD608, 0),  # Korean hangul
    0x335561: (0x8462, 0),  # East Asian ideograph
    0x216F58: (0x54A1, 0),  # East Asian ideograph
    0x6F5672: (0xC787, 0),  # Korean hangul
    0x274344: (0x6682, 0),  # East Asian ideograph
    0x6F522F: (0xBE98, 0),  # Korean hangul
    0x213C57: (0x5E3D, 0),  # East Asian ideograph
    0x4B356A: (0x55EC, 0),  # East Asian ideograph
    0x23223C: (0x83F3, 0),  # East Asian ideograph
    0x696F5B: (0x958A, 0),  # East Asian ideograph
    0x273238: (0x4FA6, 0),  # East Asian ideograph
    0x695C4F: (0x69DD, 0),  # East Asian ideograph
    0x222F5D: (0x6224, 0),  # East Asian ideograph
    0x6F5673: (0xC788, 0),  # Korean hangul
    0x216F5E: (0x54BE, 0),  # East Asian ideograph
    0x6F5230: (0xBEA8, 0),  # Korean hangul
    0x213C58: (0x5E40, 0),  # East Asian ideograph
    0x692433: (0x3053, 0),  # Hiragana letter KO
    0x292F60: (0x88E2, 0),  # East Asian ideograph
    0x6F5066: (0xBC0B, 0),  # Korean hangul
    0x4C2F61: (0x622C, 0),  # East Asian ideograph
    0x4B4235: (0x6442, 0),  # East Asian ideograph
    0x6F5B7B: (0xD338, 0),  # Korean hangul
    0x6F5C32: (0xD3AB, 0),  # Korean hangul
    0x6F5231: (0xBED0, 0),  # Korean hangul
    0x213C59: (0x5E4C, 0),  # East Asian ideograph
    0x216F64: (0x54B5, 0),  # East Asian ideograph
    0x225E2E: (0x7594, 0),  # East Asian ideograph
    0x6F5738: (0xC80A, 0),  # Korean hangul
    0x2D3F24: (0x661A, 0),  # East Asian ideograph
    0x226F66: (0x7CCE, 0),  # East Asian ideograph
    0x4B4236: (0x643A, 0),  # East Asian ideograph
    0x6F5A30: (0xCF04, 0),  # Korean hangul
    0x2D4A34: (0x718F, 0),  # East Asian ideograph
    0x226F68: (0x7CC8, 0),  # East Asian ideograph
    0x6F5A28: (0xCEF4, 0),  # Korean hangul
    0x6F5232: (0xBED1, 0),  # Korean hangul
    0x222F69: (0x97EF, 0),  # East Asian ideograph
    0x333428: (0x523C, 0),  # East Asian ideograph
    0x6F5676: (0xC78E, 0),  # Korean hangul
    0x216F6D: (0x54AE, 0),  # East Asian ideograph
    0x6F5233: (0xBED4, 0),  # Korean hangul
    0x2D3D6C: (0x5F93, 0),  # East Asian ideograph
    0x6F4A6F: (0xAF42, 0),  # Korean hangul
    0x232F6F: (0x894F, 0),  # East Asian ideograph
    0x2D5B42: (0x8F19, 0),  # East Asian ideograph
    0x393E7D: (0x7609, 0),  # East Asian ideograph
    0x695C53: (0x6A2E, 0),  # East Asian ideograph
    0x225167: (0x70EF, 0),  # East Asian ideograph
    0x235566: (0x9B23, 0),  # East Asian ideograph
    0x216F71: (0x54BF, 0),  # East Asian ideograph
    0x6F5677: (0xC655, 0),  # Korean hangul
    0x292F72: (0x88E5, 0),  # East Asian ideograph
    0x6F5234: (0xBED7, 0),  # Korean hangul
    0x213C5C: (0x5E57, 0),  # East Asian ideograph
    0x4D2F73: (0x7E5D, 0),  # East Asian ideograph
    0x6F4F4C: (0xB93C, 0),  # Korean hangul
    0x2D5B43: (0x8EFD, 0),  # East Asian ideograph
    0x226F75: (0x7CD7, 0),  # East Asian ideograph
    0x225168: (0x7100, 0),  # East Asian ideograph
    0x33334E: (0x51FE, 0),  # East Asian ideograph
    0x225A21: (0x7428, 0),  # East Asian ideograph
    0x215A22: (0x8CC7, 0),  # East Asian ideograph
    0x23445B: (0x9306, 0),  # East Asian ideograph
    0x215A23: (0x8CCA, 0),  # East Asian ideograph
    0x6F536C: (0xC274, 0),  # Korean hangul
    0x4B312D: (0x4F2B, 0),  # East Asian ideograph
    0x235A24: (0x9D04, 0),  # East Asian ideograph
    0x21322A: (0x5003, 0),  # East Asian ideograph
    0x222F7A: (0x6250, 0),  # East Asian ideograph
    0x215A25: (0x8CC4, 0),  # East Asian ideograph
    0x6F5D60: (0xD71C, 0),  # Korean hangul
    0x335568: (0x8406, 0),  # East Asian ideograph
    0x226F7B: (
        0x7CE8,
        0,
    ),  # East Asian ideograph (variant of 4C6F7B which maps to 7CE8)
    0x6F5B7C: (0xD339, 0),  # Korean hangul
    0x275A26: (0x8D40, 0),  # East Asian ideograph
    0x6F5679: (0xC790, 0),  # Korean hangul
    0x2E2F7C: (0x634D, 0),  # East Asian ideograph
    0x215A27: (0x8CC3, 0),  # East Asian ideograph
    0x213C5E: (0x5E63, 0),  # East Asian ideograph
    0x276121: (0x998A, 0),  # East Asian ideograph
    0x2D6F7D: (0x8123, 0),  # East Asian ideograph
    0x235A28: (0x9D07, 0),  # East Asian ideograph
    0x2D4472: (0x68CA, 0),  # East Asian ideograph
    0x215A29: (0x8CD3, 0),  # East Asian ideograph
    0x215A2A: (0x8CD1, 0),  # East Asian ideograph
    0x217D2E: (0x5B0D, 0),  # East Asian ideograph
    0x215A2B: (0x8CD2, 0),  # East Asian ideograph
    0x395063: (0x9939, 0),  # East Asian ideograph
    0x6F567A: (0xC791, 0),  # Korean hangul
    0x275A2C: (0x8D54, 0),  # East Asian ideograph
    0x23445D: (0x92F9, 0),  # East Asian ideograph
    0x215A2D: (0x8CE6, 0),  # East Asian ideograph
    0x295C57: (0x9E6B, 0),  # East Asian ideograph
    0x215A2F: (0x8CE3, 0),  # East Asian ideograph
    0x213076: (0x4ED9, 0),  # East Asian ideograph
    0x215A30: (0x8CE2, 0),  # East Asian ideograph
    0x4B3C38: (0x949C, 0),  # East Asian ideograph
    0x275A31: (0x8D31, 0),  # East Asian ideograph
    0x276123: (0x9992, 0),  # East Asian ideograph
    0x225A32: (0x743B, 0),  # East Asian ideograph
    0x4B3130: (0x4FAB, 0),  # East Asian ideograph
    0x6F4A70: (0xAF43, 0),  # Korean hangul
    0x215A33: (0x8CDC, 0),  # East Asian ideograph
    0x275A34: (0x8D28, 0),  # East Asian ideograph
    0x215A35: (0x8CED, 0),  # East Asian ideograph
    0x2D4A3B: (0x4E89, 0),  # East Asian ideograph
    0x225A36: (0x7444, 0),  # East Asian ideograph
    0x275A37: (0x8D5B, 0),  # East Asian ideograph
    0x215A38: (0x8CFA, 0),  # East Asian ideograph
    0x215A39: (0x8D05, 0),  # East Asian ideograph
    0x293A40: (0x8DF8, 0),  # East Asian ideograph
    0x23556C: (0x9B29, 0),  # East Asian ideograph
    0x215A3A: (0x8CFC, 0),  # East Asian ideograph
    0x215A3B: (
        0x8D08,
        0,
    ),  # East Asian ideograph (variant of 4B5A3B which maps to 8D08)
    0x6F5352: (0xC1F0, 0),  # Korean hangul
    0x215A3C: (0x8D0B, 0),  # East Asian ideograph
    0x215A3D: (0x8D0A, 0),  # East Asian ideograph
    0x215A3E: (0x8D0F, 0),  # East Asian ideograph
    0x6F5B7D: (0xD33B, 0),  # Korean hangul
    0x215A3F: (0x8D0D, 0),  # East Asian ideograph
    0x6F567E: (0xC7A0, 0),  # Korean hangul
    0x213D40: (0x5F1B, 0),  # East Asian ideograph
    0x215A40: (0x8D13, 0),  # East Asian ideograph
    0x276126: (0x990D, 0),  # East Asian ideograph
    0x215A41: (0x8D16, 0),  # East Asian ideograph
    0x215A42: (0x8D1B, 0),  # East Asian ideograph
    0x295C5B: (0x9E6C, 0),  # East Asian ideograph
    0x225A43: (0x7458, 0),  # East Asian ideograph
    0x235A44: (0x9D1D, 0),  # East Asian ideograph
    0x225A45: (0x7442, 0),  # East Asian ideograph
    0x6F5A46: (0xCF71, 0),  # Korean hangul
    0x2D3D75: (0x60EA, 0),  # East Asian ideograph
    0x2E4174: (0x6AA9, 0),  # East Asian ideograph
    0x225A47: (0x744B, 0),  # East Asian ideograph
    0x215A48: (0x8D70, 0),  # East Asian ideograph
    0x6F5660: (0xC737, 0),  # Korean hangul
    0x337345: (0x9F67, 0),  # East Asian ideograph
    0x6F5A49: (0xCF80, 0),  # Korean hangul
    0x225A4A: (0x744A, 0),  # East Asian ideograph
    0x213C65: (0x5E74, 0),  # East Asian ideograph
    0x6F5A4B: (0xCF8C, 0),  # Korean hangul
    0x6F5938: (0xCC71, 0),  # Korean hangul
    0x2D3D76: (0x5FB4, 0),  # East Asian ideograph
    0x2D5476: (0x8318, 0),  # East Asian ideograph
    0x6F5A4C: (0xCF8D, 0),  # Korean hangul
    0x6F5573: (0xC628, 0),  # Korean hangul
    0x6F5A4D: (0xCFA1, 0),  # Korean hangul
    0x2D5A4E: (0x8D82, 0),  # East Asian ideograph
    0x215A4F: (0x8D99, 0),  # East Asian ideograph
    0x4B3864: (0x58C7, 0),  # East Asian ideograph
    0x275A50: (0x8D76, 0),  # East Asian ideograph
    0x2D392F: (0x7287, 0),  # East Asian ideograph
    0x6F5A51: (0xCFE0, 0),  # Korean hangul
    0x704C2A: (0x915E, 0),  # East Asian ideograph
    0x224E37: (0x6FAF, 0),  # East Asian ideograph
    0x6F5A52: (0xCFE1, 0),  # Korean hangul
    0x6F5C58: (0xD515, 0),  # Korean hangul
    0x215A53: (0x8DA8, 0),  # East Asian ideograph
    0x6F492E: (0xAC86, 0),  # Korean hangul
    0x6F537D: (0xC2B4, 0),  # Korean hangul
    0x6F523F: (0xBF40, 0),  # Korean hangul
    0x225A55: (0x7457, 0),  # East Asian ideograph
    0x225A56: (0x7451, 0),  # East Asian ideograph
    0x6F5069: (0xBC0F, 0),  # Korean hangul
    0x6F5A57: (0xCFF5, 0),  # Korean hangul
    0x293A46: (0x8E70, 0),  # East Asian ideograph
    0x23512F: (0x9916, 0),  # East Asian ideograph
    0x4B3642: (0x8BF6, 0),  # East Asian ideograph
    0x2E4E41: (0x7032, 0),  # East Asian ideograph
    0x215A59: (0x8DDB, 0),  # East Asian ideograph
    0x6F5240: (0xBF41, 0),  # Korean hangul
    0x706131: (0x5C9C, 0),  # East Asian ideograph
    0x4B357B: (0x54CC, 0),  # East Asian ideograph
    0x225A5A: (0x745D, 0),  # East Asian ideograph
    0x225A5B: (0x7454, 0),  # East Asian ideograph
    0x225174: (0x7131, 0),  # East Asian ideograph
    0x235573: (0x9B2D, 0),  # East Asian ideograph
    0x235130: (0x9914, 0),  # East Asian ideograph
    0x33386E: (0x576F, 0),  # East Asian ideograph
    0x6F5A5E: (0xD038, 0),  # Korean hangul
    0x6F5241: (0xBF44, 0),  # Korean hangul
    0x2D5A5F: (0x8E5F, 0),  # East Asian ideograph
    0x6F5949: (0xCD09, 0),  # Korean hangul
    0x225A60: (0x746D, 0),  # East Asian ideograph
    0x277239: (0x54D4, 0),  # East Asian ideograph
    0x225A61: (0x7462, 0),  # East Asian ideograph
    0x235574: (0x9B2E, 0),  # East Asian ideograph (not in Unicode)
    0x29506C: (0x996B, 0),  # East Asian ideograph
    0x6F532F: (0xC131, 0),  # Korean hangul
    0x215A62: (0x8DF3, 0),  # East Asian ideograph
    0x215A63: (0x8DFA, 0),  # East Asian ideograph
    0x6F5242: (0xBF48, 0),  # Korean hangul
    0x27612D: (0x51AF, 0),  # East Asian ideograph
    0x6F5A64: (0xD07D, 0),  # Korean hangul
    0x4C796B: (0x815F, 0),  # East Asian ideograph
    0x235A65: (0x9D30, 0),  # East Asian ideograph
    0x275021: (0x7B0B, 0),  # East Asian ideograph
    0x235132: (0x9911, 0),  # East Asian ideograph
    0x2F3B63: (0x5E32, 0),  # East Asian ideograph (not in Unicode)
    0x2D4A45: (0x5C12, 0),  # East Asian ideograph
    0x275A68: (0x8DF5, 0),  # East Asian ideograph
    0x6F5243: (0xBF50, 0),  # Korean hangul
    0x213C6B: (0x5E7E, 0),  # East Asian ideograph
    0x215A69: (0x8E22, 0),  # East Asian ideograph
    0x225A6A: (0x7471, 0),  # East Asian ideograph
    0x225A6B: (0x7468, 0),  # East Asian ideograph
    0x4B5936: (0x8B20, 0),  # East Asian ideograph
    0x4D5A6C: (0x9D46, 0),  # East Asian ideograph
    0x216035: (0x97FB, 0),  # East Asian ideograph
    0x2D4A46: (0x58BB, 0),  # East Asian ideograph
    0x6F5A6D: (0xD0B9, 0),  # Korean hangul
    0x4B4857: (0x6F22, 0),  # East Asian ideograph
    0x235A70: (0x9D5C, 0),  # East Asian ideograph
    0x224D35: (0x6F90, 0),  # East Asian ideograph
    0x282951: (0x5F2A, 0),  # East Asian ideograph
    0x275A71: (0x8E0A, 0),  # East Asian ideograph
    0x6F5A72: (0xD0C4, 0),  # Korean hangul
    0x6F5245: (0xBF55, 0),  # Korean hangul
    0x276130: (0x9A6E, 0),  # East Asian ideograph
    0x6F4C27: (0xB141, 0),  # Korean hangul
    0x695A73: (0x6683, 0),  # East Asian ideograph
    0x454B7A: (0x7523, 0),  # East Asian ideograph
    0x6F5A74: (0xD0C9, 0),  # Korean hangul
    0x2D377C: (0x962C, 0),  # East Asian ideograph
    0x215A75: (0x8E4B, 0),  # East Asian ideograph
    0x295822: (0x9CAE, 0),  # East Asian ideograph
    0x6F5A76: (0xD0D1, 0),  # Korean hangul
    0x6F5A77: (0xD0D3, 0),  # Korean hangul
    0x6F5246: (0xBFB0, 0),  # Korean hangul
    0x234522: (0x9314, 0),  # East Asian ideograph
    0x225A78: (0x7460, 0),  # East Asian ideograph
    0x225A79: (0x7472, 0),  # East Asian ideograph
    0x225A7A: (0x7484, 0),  # East Asian ideograph
    0x224525: (0x6B99, 0),  # East Asian ideograph
    0x224D37: (0x6F8D, 0),  # East Asian ideograph
    0x225A7B: (0x7487, 0),  # East Asian ideograph
    0x274526: (0x6781, 0),  # East Asian ideograph
    0x6F5A7C: (0xD0E0, 0),  # Korean hangul
    0x6F5247: (0xBFC0, 0),  # Korean hangul
    0x276132: (0x9A73, 0),  # East Asian ideograph
    0x6F5A7D: (0xD0E4, 0),  # Korean hangul
    0x234528: (0x92FE, 0),  # East Asian ideograph
    0x215A7E: (0x8E7A, 0),  # East Asian ideograph
    0x224529: (0x6B9B, 0),  # East Asian ideograph
    0x27452A: (0x6768, 0),  # East Asian ideograph
    0x3F4C3C: (0x7582, 0),  # East Asian ideograph
    0x27452B: (0x6862, 0),  # East Asian ideograph
    0x2E7062: (0x7D4F, 0),  # East Asian ideograph
    0x6F5248: (0xBFC5, 0),  # Korean hangul
    0x276133: (0x9A7B, 0),  # East Asian ideograph
    0x4B3B61: (0x5C64, 0),  # East Asian ideograph
    0x69242B: (0x304B, 0),  # Hiragana letter KA
    0x27452D: (0x4E1A, 0),  # East Asian ideograph
    0x2D3931: (0x67F0, 0),  # East Asian ideograph
    0x2D7E6A: (0x51A4, 0),  # East Asian ideograph
    0x27452F: (0x67AB, 0),  # East Asian ideograph
    0x6F5C5A: (0xD53D, 0),  # Korean hangul
    0x224D39: (0x6F92, 0),  # East Asian ideograph
    0x692434: (0x3054, 0),  # Hiragana letter GO
    0x6F5249: (0xBFCC, 0),  # Korean hangul
    0x234531: (0x9341, 0),  # East Asian ideograph
    0x217C60: (0x5ADC, 0),  # East Asian ideograph
    0x273764: (0x5631, 0),  # East Asian ideograph
    0x234532: (0x9319, 0),  # East Asian ideograph
    0x6F506B: (0xBBB4, 0),  # Korean hangul
    0x4B4534: (0x6994, 0),  # East Asian ideograph (variant of 214534)
    0x224D3A: (0x6F89, 0),  # East Asian ideograph
    0x234535: (0x934C, 0),  # East Asian ideograph
    0x6F524A: (0xBFCD, 0),  # Korean hangul
    0x224536: (0x6BA2, 0),  # East Asian ideograph
    0x6F4C28: (0xB144, 0),  # Korean hangul
    0x21382F: (0x577C, 0),  # East Asian ideograph
    0x274537: (0x8363, 0),  # East Asian ideograph
    0x224538: (0x6BAA, 0),  # East Asian ideograph
    0x274539: (0x6784, 0),  # East Asian ideograph
    0x235B6A: (0x9DA1, 0),  # East Asian ideograph
    0x2D453A: (0x6760, 0),  # East Asian ideograph
    0x22453B: (0x6BAD, 0),  # East Asian ideograph
    0x234471: (0x9340, 0),  # East Asian ideograph
    0x692531: (0x30B1, 0),  # Katakana letter KE
    0x22453D: (0x6BB0, 0),  # East Asian ideograph
    0x6F4F66: (0xB9C8, 0),  # Korean hangul
    0x6F5663: (0xC740, 0),  # Korean hangul
    0x274871: (0x6D47, 0),  # East Asian ideograph
    0x224D3C: (0x6F8C, 0),  # East Asian ideograph
    0x22453F: (0x6BB3, 0),  # East Asian ideograph
    0x274540: (0x67AA, 0),  # East Asian ideograph
    0x234541: (0x9379, 0),  # East Asian ideograph
    0x4B3144: (
        0x4F36,
        0,
    ),  # East Asian ideograph (variant of 213144 which maps to 4F36)
    0x295C6C: (0x9E6A, 0),  # East Asian ideograph
    0x2D4543: (0x6901, 0),  # East Asian ideograph
    0x224D3D: (
        0x6F62,
        0,
    ),  # East Asian ideograph (variant of 4C4D3D which maps to 6F62)
    0x33513C: (0x7D4C, 0),  # East Asian ideograph
    0x214544: (0x6A23, 0),  # East Asian ideograph
    0x2D5036: (0x84D1, 0),  # East Asian ideograph
    0x6F524D: (0xBFDC, 0),  # Korean hangul
    0x234A5E: (0x967F, 0),  # East Asian ideograph
    0x223553: (0x6509, 0),  # East Asian ideograph
    0x4B7577: (0x57D3, 0),  # East Asian ideograph
    0x225E4A: (0x75C2, 0),  # East Asian ideograph
    0x214546: (0x6A01, 0),  # East Asian ideograph
    0x2D3932: (0x7AD2, 0),  # East Asian ideograph
    0x274547: (0x6807, 0),  # East Asian ideograph
    0x234548: (0x935C, 0),  # East Asian ideograph
    0x6F5C5B: (0xD540, 0),  # Korean hangul
    0x216037: (0x9801, 0),  # East Asian ideograph
    0x274549: (0x67A2, 0),  # East Asian ideograph
    0x6F524E: (0xBFDD, 0),  # Korean hangul
    0x27454A: (0x697C, 0),  # East Asian ideograph
    0x213833: (0x57AE, 0),  # East Asian ideograph
    0x4B602D: (0x9771, 0),  # East Asian ideograph
    0x2D5B5D: (0x8FA2, 0),  # East Asian ideograph
    0x2D3944: (0x511E, 0),  # East Asian ideograph
    0x27454C: (0x6868, 0),  # East Asian ideograph
    0x23454D: (0x9347, 0),  # East Asian ideograph
    0x293373: (0x8C21, 0),  # East Asian ideograph
    0x27454E: (0x4E50, 0),  # East Asian ideograph
    0x6F524F: (0xBFE1, 0),  # Korean hangul
    0x27454F: (0x679E, 0),  # East Asian ideograph
    0x2D3F2A: (0x5ABF, 0),  # East Asian ideograph
    0x2D4550: (0x58AB, 0),  # East Asian ideograph
    0x2D5B5E: (0x8FA7, 0),  # East Asian ideograph
    0x234551: (0x937A, 0),  # East Asian ideograph
    0x29582C: (0x9CB1, 0),  # East Asian ideograph
    0x274553: (0x692D, 0),  # East Asian ideograph
    0x27767A: (0x57DA, 0),  # East Asian ideograph
    0x224554: (0x6BC8, 0),  # East Asian ideograph
    0x274555: (0x6811, 0),  # East Asian ideograph
    0x234556: (0x937C, 0),  # East Asian ideograph
    0x293A57: (0x8DFB, 0),  # East Asian ideograph
    0x274557: (0x6866, 0),  # East Asian ideograph
    0x29582D: (0x9CB7, 0),  # East Asian ideograph
    0x235140: (0x991C, 0),  # East Asian ideograph
    0x274558: (0x6734, 0),  # East Asian ideograph
    0x474E5C: (
        0x97DE,
        0,
    ),  # East Asian ideograph (variant of 234E5C which maps to 97DE)
    0x274366: (0x80E7, 0),  # East Asian ideograph
    0x6F5251: (0xC059, 0),  # Korean hangul
    0x27613C: (0x9A86, 0),  # East Asian ideograph
    0x2D3261: (0x5039, 0),  # East Asian ideograph
    0x27455B: (0x6865, 0),  # East Asian ideograph
    0x275030: (0x8303, 0),  # East Asian ideograph
    0x23455C: (0x9377, 0),  # East Asian ideograph
    0x6F5172: (0xBE4E, 0),  # Korean hangul
    0x27455D: (0x673A, 0),  # East Asian ideograph
    0x213F50: (0x61CA, 0),  # East Asian ideograph
    0x6F5252: (0xC05C, 0),  # Korean hangul
    0x23455E: (0x9358, 0),  # East Asian ideograph
    0x2D5F63: (0x873A, 0),  # East Asian ideograph
    0x27455F: (0x6863, 0),  # East Asian ideograph
    0x224560: (0x6BDA, 0),  # East Asian ideograph
    0x33327A: (0x5150, 0),  # East Asian ideograph
    0x274561: (0x68C0, 0),  # East Asian ideograph
    0x29582F: (0x9CB5, 0),  # East Asian ideograph
    0x274562: (0x6867, 0),  # East Asian ideograph
    0x3F347D: (0x84E1, 0),  # East Asian ideograph
    0x6F5253: (0xC060, 0),  # Korean hangul
    0x274563: (0x67E0, 0),  # East Asian ideograph
    0x235131: (0x9917, 0),  # East Asian ideograph
    0x234564: (0x9376, 0),  # East Asian ideograph
    0x274565: (0x67DC, 0),  # East Asian ideograph
    0x213230: (0x5065, 0),  # East Asian ideograph
    0x224A4C: (0x6E1F, 0),  # East Asian ideograph
    0x274566: (0x69DB, 0),  # East Asian ideograph
    0x294567: (0x9537, 0),  # East Asian ideograph
    0x6F5254: (0xC068, 0),  # Korean hangul
    0x27613F: (0x9A88, 0),  # East Asian ideograph
    0x6F4C2A: (0xB151, 0),  # Korean hangul
    0x2D4569: (0x6AC9, 0),  # East Asian ideograph
    0x4B314C: (0x5F95, 0),  # East Asian ideograph
    0x6F573F: (0xC81C, 0),  # Korean hangul
    0x23456A: (0x9348, 0),  # East Asian ideograph
    0x27325D: (0x4EF7, 0),  # East Asian ideograph
    0x27456B: (0x691F, 0),  # East Asian ideograph
    0x213F3B: (0x616B, 0),  # East Asian ideograph
    0x295831: (0x9CB6, 0),  # East Asian ideograph
    0x27456C: (0x6809, 0),  # East Asian ideograph
    0x2E4E56: (0x9800, 0),  # East Asian ideograph
    0x6F5255: (0xC069, 0),  # Korean hangul
    0x27456D: (0x6A79, 0),  # East Asian ideograph
    0x276140: (0x9A91, 0),  # East Asian ideograph
    0x23447B: (0x933F, 0),  # East Asian ideograph
    0x27456E: (0x680F, 0),  # East Asian ideograph
    0x27456F: (0x6A31, 0),  # East Asian ideograph
    0x224570: (0x6BEA, 0),  # East Asian ideograph
    0x3F456D: (0x8263, 0),  # East Asian ideograph
    0x235145: (0x9927, 0),  # East Asian ideograph
    0x274571: (0x6984, 0),  # East Asian ideograph
    0x2D4A58: (0x7F9D, 0),  # East Asian ideograph
    0x6F5256: (0xC090, 0),  # Korean hangul
    0x217C6D: (0x5AE5, 0),  # East Asian ideograph
    0x286540: (0x7800, 0),  # East Asian ideograph
    0x23447C: (0x933A, 0),  # East Asian ideograph
    0x234573: (0x9360, 0),  # East Asian ideograph
    0x2D4574: (0x5FFB, 0),  # East Asian ideograph
    0x6F5D37: (0xD639, 0),  # Korean hangul
    0x233021: (0x894D, 0),  # East Asian ideograph
    0x6F5257: (0xC091, 0),  # Korean hangul
    0x234577: (0x936E, 0),  # East Asian ideograph
    0x287022: (0x7CC1, 0),  # East Asian ideograph
    0x274578: (0x94A6, 0),  # East Asian ideograph
    0x6F5844: (0xC9F8, 0),  # Korean hangul
    0x213023: (0x4E03, 0),  # East Asian ideograph
    0x225B2D: (0x7486, 0),  # East Asian ideograph
    0x234579: (0x938F, 0),  # East Asian ideograph
    0x233024: (0x895A, 0),  # East Asian ideograph
    0x293A5E: (0x8DF9, 0),  # East Asian ideograph
    0x23457A: (0x93AC, 0),  # East Asian ideograph
    0x6F5C5D: (0xD54C, 0),  # Korean hangul
    0x233025: (0x895E, 0),  # East Asian ideograph
    0x335147: (0x7EEE, 0),  # East Asian ideograph
    0x23457B: (0x9395, 0),  # East Asian ideograph
    0x213026: (0x4E0A, 0),  # East Asian ideograph
    0x4B4E7B: (
        0x7985,
        0,
    ),  # East Asian ideograph (variant of 274E7B which maps to 7985)
    0x6F5258: (0xC094, 0),  # Korean hangul
    0x27457C: (0x6B27, 0),  # East Asian ideograph
    0x295175: (0x9993, 0),  # East Asian ideograph
    0x21383D: (0x57DF, 0),  # East Asian ideograph
    0x2E3028: (0x640B, 0),  # East Asian ideograph
    0x27457E: (0x6B24, 0),  # East Asian ideograph
    0x213029: (0x4E10, 0),  # East Asian ideograph
    0x293A5F: (0x8DDE, 0),  # East Asian ideograph
    0x2D4A5B: (0x7282, 0),  # East Asian ideograph
    0x22302B: (0x625A, 0),  # East Asian ideograph
    0x6F5259: (0xC098, 0),  # Korean hangul
    0x276144: (0x817E, 0),  # East Asian ideograph
    0x21302C: (0x4E19, 0),  # East Asian ideograph
    0x21383E: (0x580A, 0),  # East Asian ideograph
    0x22302D: (0x6266, 0),  # East Asian ideograph
    0x22702E: (0x7CF0, 0),  # East Asian ideograph
    0x6F5664: (0xC744, 0),  # Korean hangul
    0x293A60: (0x8E2C, 0),  # East Asian ideograph
    0x21302F: (0x4E18, 0),  # East Asian ideograph
    0x217030: (0x5504, 0),  # East Asian ideograph
    0x6F525A: (0xC0A0, 0),  # Korean hangul
    0x234469: (0x9338, 0),  # East Asian ideograph
    0x692126: (0x30FB, 0),  # Ideographic centered point
    0x223031: (0x6286, 0),  # East Asian ideograph
    0x21383F: (0x5805, 0),  # East Asian ideograph
    0x273032: (0x5E76, 0),  # East Asian ideograph
    0x6F594A: (0xCD0C, 0),  # Korean hangul
    0x2D5B69: (0x5EF5, 0),  # East Asian ideograph
    0x6F4C55: (0xB284, 0),  # Korean hangul
    0x275039: (0x7B03, 0),  # East Asian ideograph
    0x6F5666: (0xC74C, 0),  # Korean hangul
    0x692139: (0x3005, 0),  # Ideographic iteration mark
    0x69213C: (0x30FC, 0),  # Vowel elongation mark for kana
    0x213035: (0x4E32, 0),  # East Asian ideograph
    0x695130: (0x5116, 0),  # East Asian ideograph
    0x6F525B: (0xC0A3, 0),  # Korean hangul
    0x276146: (0x9AA0, 0),  # East Asian ideograph
    0x217C72: (0x5AEA, 0),  # East Asian ideograph
    0x6F4A77: (0xAF64, 0),  # Korean hangul
    0x23403E: (0x9146, 0),  # East Asian ideograph
    0x2D3263: (0x4FAD, 0),  # East Asian ideograph
    0x4B4F29: (0x7A50, 0),  # East Asian ideograph
    0x692152: (0x3008, 0),  # Ideographic less than sign
    0x27503A: (0x7B51, 0),  # East Asian ideograph
    0x692154: (0x300A, 0),  # Ideographic left double angle bracket
    0x692155: (0x300B, 0),  # Ideographic right double angle bracket
    0x217039: (0x54F7, 0),  # East Asian ideograph
    0x21303A: (0x4E43, 0),  # East Asian ideograph
    0x2E4E5D: (0x6DE0, 0),  # East Asian ideograph
    0x6F525C: (0xC0A5, 0),  # Korean hangul
    0x21303B: (0x4E45, 0),  # East Asian ideograph
    0x213841: (0x5806, 0),  # East Asian ideograph
    0x217830: (0x58A3, 0),  # East Asian ideograph
    0x6F576A: (0xC8F1, 0),  # Korean hangul
    0x233376: (0x8B1F, 0),  # East Asian ideograph
    0x33514C: (0x7DD1, 0),  # East Asian ideograph
    0x213E21: (0x5FCD, 0),  # East Asian ideograph
    0x276148: (0x84E6, 0),  # East Asian ideograph
    0x2D4B71: (0x7F3E, 0),  # East Asian ideograph
    0x223041: (0x62A3, 0),  # East Asian ideograph
    0x213042: (0x4E52, 0),  # East Asian ideograph
    0x277255: (0x54D3, 0),  # East Asian ideograph
    0x213043: (0x4E53, 0),  # East Asian ideograph
    0x227044: (0x7D03, 0),  # East Asian ideograph
    0x234544: (0x9386, 0),  # East Asian ideograph
    0x287045: (0x7EA8, 0),  # East Asian ideograph
    0x227C31: (0x82AF, 0),  # East Asian ideograph
    0x234041: (0x9147, 0),  # East Asian ideograph
    0x2D3954: (0x7385, 0),  # East Asian ideograph
    0x213047: (0x4E5D, 0),  # East Asian ideograph
    0x213049: (0x4E5E, 0),  # East Asian ideograph
    0x6F525F: (0xC0AC, 0),  # Korean hangul
    0x28255A: (0x5D5D, 0),  # East Asian ideograph
    0x273F31: (0x60ED, 0),  # East Asian ideograph
    0x225E5C: (0x75CF, 0),  # East Asian ideograph
    0x29472F: (0x94E9, 0),  # East Asian ideograph
    0x21304B: (0x4E73, 0),  # East Asian ideograph
    0x21304C: (0x4E7E, 0),  # East Asian ideograph
    0x27503E: (0x7BD3, 0),  # East Asian ideograph
    0x6F5667: (0xC74D, 0),  # Korean hangul
    0x27304D: (0x4E71, 0),  # East Asian ideograph
    0x23514F: (0x992E, 0),  # East Asian ideograph
    0x6F5870: (0xCBD4, 0),  # Korean hangul
    0x275B36: (0x8F69, 0),  # East Asian ideograph
    0x6F5260: (0xC0AD, 0),  # Korean hangul
    0x27614B: (0x60CA, 0),  # East Asian ideograph
    0x6F4A78: (0xAF65, 0),  # Korean hangul
    0x227050: (0x7D18, 0),  # East Asian ideograph
    0x227051: (0x7D1E, 0),  # East Asian ideograph
    0x277258: (0x6076, 0),  # East Asian ideograph (duplicate simplified)
    0x393052: (0x65BC, 0),  # East Asian ideograph
    0x235150: (0x992C, 0),  # East Asian ideograph
    0x213053: (0x4E95, 0),  # East Asian ideograph
    0x6F5261: (0xC0AE, 0),  # Korean hangul
    0x294040: (0x90E6, 0),  # East Asian ideograph
    0x213055: (0x4E92, 0),  # East Asian ideograph
    0x2E5F6F: (0x75B8, 0),  # East Asian ideograph
    0x27326A: (0x4FEA, 0),  # East Asian ideograph
    0x223057: (0x62D1, 0),  # East Asian ideograph
    0x235151: (0x992A, 0),  # East Asian ideograph
    0x213058: (0x4E9E, 0),  # East Asian ideograph
    0x2D4621: (0x61FD, 0),  # East Asian ideograph
    0x213059: (0x4E9B, 0),  # East Asian ideograph
    0x284333: (0x680E, 0),  # East Asian ideograph
    0x294732: (0x94F4, 0),  # East Asian ideograph
    0x33625E: (0x9EAA, 0),  # East Asian ideograph
    0x22705A: (0x7D3D, 0),  # East Asian ideograph
    0x6F5070: (0xBC18, 0),  # Korean hangul
    0x232223: (0x83FD, 0),  # East Asian ideograph
    0x222224: (0x5BF0, 0),  # East Asian ideograph
    0x232225: (0x841E, 0),  # East Asian ideograph
    0x693C36: (0x96EB, 0),  # East Asian ideograph
    0x232229: (0x83C9, 0),  # East Asian ideograph
    0x23222A: (0x83DF, 0),  # East Asian ideograph
    0x23222C: (0x841F, 0),  # East Asian ideograph
    0x23222E: (0x840F, 0),  # East Asian ideograph
    0x69705D: (0x9786, 0),  # East Asian ideograph
    0x232230: (0x8411, 0),  # East Asian ideograph
    0x222233: (0x5C00, 0),  # East Asian ideograph
    0x222235: (0x5C57, 0),  # East Asian ideograph
    0x232236: (0x839A, 0),  # East Asian ideograph
    0x707438: (0x823E, 0),  # East Asian ideograph
    0x33625F: (0x8534, 0),  # East Asian ideograph
    0x21305F: (0x4EA8, 0),  # East Asian ideograph
    0x22223C: (0x5C15, 0),  # East Asian ideograph
    0x333060: (0x4EAF, 0),  # East Asian ideograph
    0x6F5742: (0xC824, 0),  # Korean hangul
    0x232243: (0x83D1, 0),  # East Asian ideograph
    0x275042: (0x7BAB, 0),  # East Asian ideograph
    0x222246: (0x5C22, 0),  # East Asian ideograph
    0x223061: (0x62E4, 0),  # East Asian ideograph
    0x222248: (0x5C25, 0),  # East Asian ideograph
    0x23224A: (0x848E, 0),  # East Asian ideograph
    0x22224B: (0x5C2A, 0),  # East Asian ideograph
    0x23224C: (0x8439, 0),  # East Asian ideograph
    0x23224D: (0x8476, 0),  # East Asian ideograph
    0x23224E: (0x8479, 0),  # East Asian ideograph
    0x213C6E: (0x5E8A, 0),  # East Asian ideograph
    0x222252: (0x5C2F, 0),  # East Asian ideograph
    0x217C7B: (0x5ADA, 0),  # East Asian ideograph
    0x284335: (0x6A7C, 0),  # East Asian ideograph
    0x4C3B22: (0x6860, 0),  # East Asian ideograph
    0x294734: (0x9566, 0),  # East Asian ideograph
    0x213064: (0x4EBA, 0),  # East Asian ideograph
    0x22225B: (0x5C32, 0),  # East Asian ideograph
    0x23225C: (0x8451, 0),  # East Asian ideograph
    0x23225F: (0x847D, 0),  # East Asian ideograph
    0x232262: (0x845A, 0),  # East Asian ideograph
    0x222263: (0x5C3B, 0),  # East Asian ideograph
    0x222265: (0x5C44, 0),  # East Asian ideograph
    0x232266: (0x8459, 0),  # East Asian ideograph
    0x222267: (0x5C49, 0),  # East Asian ideograph
    0x232269: (0x8473, 0),  # East Asian ideograph
    0x23226E: (0x843E, 0),  # East Asian ideograph
    0x6F5265: (0xC0B4, 0),  # Korean hangul
    0x276150: (0x9AA5, 0),  # East Asian ideograph
    0x232271: (0x846D, 0),  # East Asian ideograph
    0x394735: (0x6C3E, 0),  # East Asian ideograph
    0x223069: (0x62B6, 0),  # East Asian ideograph
    0x232278: (0x847A, 0),  # East Asian ideograph
    0x222279: (0x5C59, 0),  # East Asian ideograph
    0x22227B: (0x5C5D, 0),  # East Asian ideograph
    0x22227C: (0x5C5F, 0),  # East Asian ideograph
    0x22706A: (0x7D3F, 0),  # East Asian ideograph
    0x21306B: (0x4ECD, 0),  # East Asian ideograph
    0x2D306C: (0x8B8E, 0),  # East Asian ideograph
    0x6F5266: (0xC0B5, 0),  # Korean hangul
    0x276151: (0x9A8A, 0),  # East Asian ideograph
    0x284337: (0x6987, 0),  # East Asian ideograph
    0x225E63: (0x75E7, 0),  # East Asian ideograph
    0x33512E: (0x7E8D, 0),  # East Asian ideograph
    0x4B306E: (
        0x4EE4,
        0,
    ),  # East Asian ideograph (variant of 21306E which maps to 4EE4)
    0x21306F: (0x4ED8, 0),  # East Asian ideograph
    0x235156: (0x992B, 0),  # East Asian ideograph
    0x454146: (0x63DB, 0),  # East Asian ideograph
    0x213071: (0x4ED6, 0),  # East Asian ideograph
    0x6F5267: (0xC0B6, 0),  # Korean hangul
    0x213072: (0x4EDE, 0),  # East Asian ideograph
    0x6F4E24: (0xB544, 0),  # Korean hangul
    0x6F5A24: (0xCEE4, 0),  # Korean hangul
    0x225254: (0x714F, 0),  # East Asian ideograph
    0x215B21: (0x8E76, 0),  # East Asian ideograph
    0x6F5268: (0xC0BC, 0),  # Korean hangul
    0x276153: (0x80AE, 0),  # East Asian ideograph
    0x213077: (0x4EE5, 0),  # East Asian ideograph
    0x215B22: (0x8E7C, 0),  # East Asian ideograph
    0x21384D: (0x5857, 0),  # East Asian ideograph
    0x333078: (0x5F77, 0),  # East Asian ideograph
    0x225D69: (0x756F, 0),  # East Asian ideograph
    0x335E21: (0x9221, 0),  # East Asian ideograph
    0x213079: (0x4F09, 0),  # East Asian ideograph
    0x6F5B24: (0xD0F1, 0),  # Korean hangul
    0x6F5B25: (0xD130, 0),  # Korean hangul
    0x235158: (0x9931, 0),  # East Asian ideograph
    0x4B3E2A: (0x6035, 0),  # East Asian ideograph
    0x275B26: (0x8DB8, 0),  # East Asian ideograph
    0x6F5269: (0xC0BD, 0),  # Korean hangul
    0x6F4B2C: (0xAFD4, 0),  # Korean hangul
    0x225B27: (0x7482, 0),  # East Asian ideograph
    0x21384E: (0x5858, 0),  # East Asian ideograph
    0x21307D: (0x4F0A, 0),  # East Asian ideograph
    0x215B28: (0x8E8A, 0),  # East Asian ideograph
    0x215B29: (
        0x8E8D,
        0,
    ),  # East Asian ideograph (variant of 4B5B29 which maps to 8E8D)
    0x275048: (0x5E18, 0),  # East Asian ideograph
    0x275B2A: (0x8E2F, 0),  # East Asian ideograph
    0x4B6044: (0x9818, 0),  # East Asian ideograph
    0x4D4A6C: (0x9667, 0),  # East Asian ideograph
    0x275B2B: (0x8E51, 0),  # East Asian ideograph
    0x6F526A: (0xC0BF, 0),  # Korean hangul
    0x293B7A: (0x8F8F, 0),  # East Asian ideograph
    0x215A68: (0x8E10, 0),  # East Asian ideograph
    0x23404D: (0x9156, 0),  # East Asian ideograph
    0x215B2D: (0x8EAB, 0),  # East Asian ideograph
    0x235B2E: (0x9D8A, 0),  # East Asian ideograph
    0x3F5F34: (0x9699, 0),  # East Asian ideograph (not in Unicode)
    0x274224: (0x6361, 0),  # East Asian ideograph
    0x212320: (0x3000, 0),  # Ideographic space in some implementations
    0x215B30: (0x8EBA, 0),  # East Asian ideograph
    0x222323: (0x5C63, 0),  # East Asian ideograph
    0x232324: (0x8432, 0),  # East Asian ideograph
    0x225772: (0x735E, 0),  # East Asian ideograph
    0x212328: (0xFF08, 0),  # Ideographic left parenthesis
    0x222329: (0x5C67, 0),  # East Asian ideograph
    0x22232B: (0x5C68, 0),  # East Asian ideograph
    0x23232D: (0x842A, 0),  # East Asian ideograph
    0x23232E: (0x8429, 0),  # East Asian ideograph
    0x222330: (0x5C6D, 0),  # East Asian ideograph
    0x222331: (0x5C6E, 0),  # East Asian ideograph
    0x232332: (0x8471, 0),  # East Asian ideograph
    0x215B33: (0x8ECB, 0),  # East Asian ideograph
    0x232335: (0x845F, 0),  # East Asian ideograph
    0x232336: (0x8460, 0),  # East Asian ideograph
    0x222337: (0x5C74, 0),  # East Asian ideograph
    0x222339: (0x5C73, 0),  # East Asian ideograph
    0x23233A: (0x8446, 0),  # East Asian ideograph
    0x22233B: (0x5C77, 0),  # East Asian ideograph
    0x22233C: (0x5C7A, 0),  # East Asian ideograph
    0x29233D: (0x836E, 0),  # East Asian ideograph
    0x235B35: (0x9D87, 0),  # East Asian ideograph
    0x222340: (0x5C7C, 0),  # East Asian ideograph
    0x6F526C: (0xC0C1, 0),  # Korean hangul
    0x232345: (0x844E, 0),  # East Asian ideograph
    0x222346: (0x5C8F, 0),  # East Asian ideograph
    0x29473C: (0x9568, 0),  # East Asian ideograph
    0x222349: (0x5C88, 0),  # East Asian ideograph
    0x275B37: (0x8F6B, 0),  # East Asian ideograph
    0x22234D: (0x5C99, 0),  # East Asian ideograph
    0x232350: (0x84A1, 0),  # East Asian ideograph
    0x225B38: (0x7480, 0),  # East Asian ideograph
    0x232353: (0x849F, 0),  # East Asian ideograph
    0x222355: (0x5CA6, 0),  # East Asian ideograph
    0x232356: (0x84BA, 0),  # East Asian ideograph
    0x222357: (0x5CA0, 0),  # East Asian ideograph
    0x23515C: (0x993B, 0),  # East Asian ideograph
    0x69255E: (0x30DE, 0),  # Katakana letter MA
    0x22235C: (0x5CA2, 0),  # East Asian ideograph
    0x275B3A: (0x8F72, 0),  # East Asian ideograph
    0x23235E: (0x84C1, 0),  # East Asian ideograph
    0x23235F: (0x84BB, 0),  # East Asian ideograph
    0x222360: (0x5CB5, 0),  # East Asian ideograph
    0x222361: (0x5CA7, 0),  # East Asian ideograph
    0x215B3B: (0x8EF8, 0),  # East Asian ideograph
    0x222366: (0x5CA8, 0),  # East Asian ideograph
    0x222367: (0x5CAC, 0),  # East Asian ideograph
    0x234050: (0x9158, 0),  # East Asian ideograph
    0x225B3C: (0x7481, 0),  # East Asian ideograph
    0x22236B: (0x5CA3, 0),  # East Asian ideograph
    0x22236C: (0x5CB6, 0),  # East Asian ideograph
    0x22236D: (0x5CC1, 0),  # East Asian ideograph
    0x23456E: (0x9351, 0),  # East Asian ideograph
    0x22236F: (0x5CAD, 0),  # East Asian ideograph
    0x232370: (0x84B1, 0),  # East Asian ideograph
    0x232371: (0x849D, 0),  # East Asian ideograph
    0x232372: (0x84D0, 0),  # East Asian ideograph
    0x224666: (0x6C2D, 0),  # East Asian ideograph
    0x232375: (0x8494, 0),  # East Asian ideograph
    0x222378: (0x5CD3, 0),  # East Asian ideograph
    0x232379: (0x84C7, 0),  # East Asian ideograph
    0x23237A: (0x84BD, 0),  # East Asian ideograph
    0x215B3F: (0x8F09, 0),  # East Asian ideograph
    0x23237C: (0x84C2, 0),  # East Asian ideograph
    0x6F526E: (0xC0C8, 0),  # Korean hangul
    0x282569: (0x5D02, 0),  # East Asian ideograph
    0x225B40: (0x7497, 0),  # East Asian ideograph
    0x29473E: (0x94F9, 0),  # East Asian ideograph
    0x23572E: (0x9B93, 0),  # East Asian ideograph
    0x275B41: (0x8F85, 0),  # East Asian ideograph
    0x215B42: (0x8F12, 0),  # East Asian ideograph
    0x27504D: (0x7B79, 0),  # East Asian ideograph
    0x224D5F: (0x6F72, 0),  # East Asian ideograph
    0x225B43: (0x7498, 0),  # East Asian ideograph
    0x6F5B44: (0xD22D, 0),  # Korean hangul
    0x6F526F: (0xC0C9, 0),  # Korean hangul
    0x2E6C46: (0x7BE6, 0),  # East Asian ideograph
    0x225B45: (0x749A, 0),  # East Asian ideograph
    0x284340: (0x67A5, 0),  # East Asian ideograph
    0x692526: (0x30A6, 0),  # Katakana letter U
    0x275B46: (0x8F86, 0),  # East Asian ideograph
    0x2D573B: (0x60F7, 0),  # East Asian ideograph
    0x215B47: (0x8F1F, 0),  # East Asian ideograph
    0x275B48: (0x8F89, 0),  # East Asian ideograph
    0x275B49: (0x8F88, 0),  # East Asian ideograph
    0x6F5270: (0xC0CC, 0),  # Korean hangul
    0x27615B: (0x810F, 0),  # East Asian ideograph
    0x275B4A: (0x8F6E, 0),  # East Asian ideograph
    0x234A65: (0x9688, 0),  # East Asian ideograph
    0x6F5845: (0xC9F9, 0),  # Korean hangul
    0x215B4B: (0x8F1C, 0),  # East Asian ideograph
    0x33422A: (0x62E1, 0),  # East Asian ideograph
    0x275B4C: (0x8F90, 0),  # East Asian ideograph
    0x225B4D: (0x74A4, 0),  # East Asian ideograph
    0x235160: (0x993A, 0),  # East Asian ideograph
    0x275B4E: (0x8F93, 0),  # East Asian ideograph
    0x6F516B: (0xBE1D, 0),  # Korean hangul
    0x276131: (0x9A6F, 0),  # East Asian ideograph
    0x215B4F: (0x8F44, 0),  # East Asian ideograph
    0x225A2B: (0x7424, 0),  # East Asian ideograph
    0x2D3B40: (
        0x5C06,
        0,
    ),  # East Asian ideograph (variant of 273B40 which maps to 5C06)
    0x275B51: (0x8F95, 0),  # East Asian ideograph
    0x28544F: (0x70EC, 0),  # East Asian ideograph
    0x224D62: (0x6F57, 0),  # East Asian ideograph
    0x29337A: (0x8BCC, 0),  # East Asian ideograph
    0x235161: (0x9941, 0),  # East Asian ideograph
    0x275B53: (0x8206, 0),  # East Asian ideograph
    0x215B54: (0x8F4D, 0),  # East Asian ideograph
    0x692533: (0x30B3, 0),  # Katakana letter KO
    0x4B316A: (0x723C, 0),  # East Asian ideograph
    0x215B55: (0x8F49, 0),  # East Asian ideograph
    0x2D3F31: (0x6159, 0),  # East Asian ideograph
    0x6F5665: (0xC74A, 0),  # Korean hangul
    0x225B56: (0x748D, 0),  # East Asian ideograph
    0x224667: (0x6C30, 0),  # East Asian ideograph
    0x215B57: (0x8F4E, 0),  # East Asian ideograph
    0x275B58: (0x8F70, 0),  # East Asian ideograph
    0x213C71: (0x5E96, 0),  # East Asian ideograph
    0x275B59: (0x8F94, 0),  # East Asian ideograph
    0x234056: (0x9164, 0),  # East Asian ideograph
    0x225A2D: (0x742D, 0),  # East Asian ideograph
    0x6F4C56: (0xB289, 0),  # Korean hangul
    0x232421: (0x8495, 0),  # East Asian ideograph
    0x692422: (0x3042, 0),  # Hiragana letter A
    0x692423: (0x3043, 0),  # Hiragana letter small I
    0x692424: (0x3044, 0),  # Hiragana letter I
    0x692425: (0x3045, 0),  # Hiragana letter small U
    0x222426: (0x5CE0, 0),  # East Asian ideograph
    0x232427: (0x84AF, 0),  # East Asian ideograph
    0x222428: (0x5CD2, 0),  # East Asian ideograph
    0x232429: (0x84AD, 0),  # East Asian ideograph
    0x69242A: (0x304A, 0),  # Hiragana letter O
    0x22242B: (0x5CCB, 0),  # East Asian ideograph
    0x69242C: (0x304C, 0),  # Hiragana letter GA
    0x69242D: (0x304D, 0),  # Hiragana letter KI
    0x69242E: (0x304E, 0),  # Hiragana letter GI
    0x215B5D: (0x8FA3, 0),  # East Asian ideograph
    0x222430: (0x5CC7, 0),  # East Asian ideograph
    0x222431: (0x5CDC, 0),  # East Asian ideograph
    0x232432: (0x84A8, 0),  # East Asian ideograph
    0x232433: (0x84D6, 0),  # East Asian ideograph
    0x222434: (0x5D00, 0),  # East Asian ideograph
    0x215B5E: (0x8FA8, 0),  # East Asian ideograph
    0x213859: (0x5875, 0),  # East Asian ideograph
    0x692437: (0x3057, 0),  # Hiragana letter SI
    0x692438: (0x3058, 0),  # Hiragana letter ZI
    0x692439: (0x3059, 0),  # Hiragana letter SU
    0x23243A: (0x8493, 0),  # East Asian ideograph
    0x22243B: (0x5CFF, 0),  # East Asian ideograph
    0x22243C: (0x5CEB, 0),  # East Asian ideograph
    0x69243D: (0x305D, 0),  # Hiragana letter SO
    0x69243E: (0x305E, 0),  # Hiragana letter ZO
    0x23243F: (0x84CF, 0),  # East Asian ideograph
    0x692440: (0x3060, 0),  # Hiragana letter DA
    0x232441: (0x84CA, 0),  # East Asian ideograph
    0x692442: (0x3062, 0),  # Hiragana letter DI
    0x692443: (0x3063, 0),  # Hiragana letter small TU
    0x692444: (0x3064, 0),  # Hiragana letter TU
    0x692445: (0x3065, 0),  # Hiragana letter DU
    0x232446: (0x8506, 0),  # East Asian ideograph
    0x232447: (0x850B, 0),  # East Asian ideograph
    0x692448: (0x3068, 0),  # Hiragana letter TO
    0x222449: (0x5D1E, 0),  # East Asian ideograph
    0x22244A: (0x5D12, 0),  # East Asian ideograph
    0x69244B: (0x306B, 0),  # Hiragana letter NI
    0x69244C: (0x306C, 0),  # Hiragana letter NU
    0x23244D: (0x8500, 0),  # East Asian ideograph
    0x69244E: (0x306E, 0),  # Hiragana letter NO
    0x69244F: (0x306F, 0),  # Hiragana letter HA
    0x222450: (0x5D1A, 0),  # East Asian ideograph
    0x692451: (0x3071, 0),  # Hiragana letter PA
    0x222452: (0x5D0C, 0),  # East Asian ideograph
    0x222453: (0x5D20, 0),  # East Asian ideograph
    0x222454: (0x5D21, 0),  # East Asian ideograph
    0x692455: (0x3075, 0),  # Hiragana letter HU
    0x692456: (0x3076, 0),  # Hiragana letter BU
    0x222457: (0x5D27, 0),  # East Asian ideograph
    0x222458: (0x5D0D, 0),  # East Asian ideograph
    0x232459: (0x851F, 0),  # East Asian ideograph
    0x22245A: (0x5D26, 0),  # East Asian ideograph
    0x69245B: (0x307B, 0),  # Hiragana letter HO
    0x23245C: (0x853B, 0),  # East Asian ideograph
    0x22245D: (0x5D2E, 0),  # East Asian ideograph
    0x69245E: (0x307E, 0),  # Hiragana letter MA
    0x23245F: (0x84EA, 0),  # East Asian ideograph
    0x692460: (0x3080, 0),  # Hiragana letter MU
    0x692461: (0x3081, 0),  # Hiragana letter ME
    0x692462: (0x3082, 0),  # Hiragana letter MO
    0x692463: (0x3083, 0),  # Hiragana letter small YA
    0x692464: (0x3084, 0),  # Hiragana letter YA
    0x235B66: (0x9DA4, 0),  # East Asian ideograph
    0x232466: (0x84F4, 0),  # East Asian ideograph
    0x692467: (0x3087, 0),  # Hiragana letter small YO
    0x692468: (0x3088, 0),  # Hiragana letter YO
    0x222469: (0x5D24, 0),  # East Asian ideograph
    0x23246A: (0x850C, 0),  # East Asian ideograph
    0x215B67: (0x8FC5, 0),  # East Asian ideograph
    0x69246C: (0x308C, 0),  # Hiragana letter RE
    0x69246D: (0x308D, 0),  # Hiragana letter RO
    0x69246E: (0x308E, 0),  # Hiragana letter small WA
    0x69246F: (0x308F, 0),  # Hiragana letter WA
    0x692470: (0x3090, 0),  # Hiragana letter WI
    0x222471: (0x5D36, 0),  # East Asian ideograph
    0x222472: (0x5D3E, 0),  # East Asian ideograph
    0x692473: (0x3093, 0),  # Hiragana letter N
    0x222474: (0x5D4B, 0),  # East Asian ideograph
    0x232475: (0x8515, 0),  # East Asian ideograph
    0x222476: (0x5D57, 0),  # East Asian ideograph
    0x222477: (0x5D34, 0),  # East Asian ideograph
    0x6F2478: (0x3155, 0),  # Korean hangul
    0x335E2F: (0x5257, 0),  # East Asian ideograph
    0x23247A: (0x84FC, 0),  # East Asian ideograph
    0x6F247B: (0x3158, 0),  # Korean hangul
    0x23247C: (0x84EB, 0),  # East Asian ideograph
    0x23247D: (0x84FD, 0),  # East Asian ideograph
    0x6F247E: (0x315B, 0),  # Korean hangul
    0x235B6B: (0x9D9A, 0),  # East Asian ideograph
    0x235166: (0x993C, 0),  # East Asian ideograph
    0x225B6C: (0x74A5, 0),  # East Asian ideograph
    0x6F5277: (0xC0DD, 0),  # Korean hangul
    0x6F4C31: (0xB179, 0),  # Korean hangul
    0x215B6D: (
        0x8FF0,
        0,
    ),  # East Asian ideograph (variant of 275B6D which maps to 8FF0)
    0x21385C: (0x5885, 0),  # East Asian ideograph
    0x69252E: (0x30AE, 0),  # Katakana letter GI
    0x225B6E: (0x74A8, 0),  # East Asian ideograph
    0x235E30: (0x9EC1, 0),  # East Asian ideograph
    0x295921: (0x9CD9, 0),  # East Asian ideograph
    0x6F5B6F: (0xD310, 0),  # Korean hangul
    0x295854: (0x9CC4, 0),  # East Asian ideograph
    0x215B70: (0x8FEA, 0),  # East Asian ideograph
    0x705B71: (0x57B4, 0),  # East Asian ideograph
    0x6F5278: (0xC0E4, 0),  # Korean hangul
    0x276163: (0x677E, 0),  # East Asian ideograph (duplicate simplified)
    0x6F4E35: (0xB5B0, 0),  # Korean hangul
    0x69252F: (0x30AF, 0),  # Katakana letter KU
    0x234B66: (0x96D8, 0),  # East Asian ideograph
    0x235B74: (0x9DB1, 0),  # East Asian ideograph
    0x6F4B7C: (0xB123, 0),  # Korean hangul
    0x4B6053: (0x985E, 0),  # East Asian ideograph
    0x224926: (0x6D6F, 0),  # East Asian ideograph
    0x235B76: (0x9DB6, 0),  # East Asian ideograph
    0x234621: (0x93B5, 0),  # East Asian ideograph
    0x276164: (0x80E1, 0),  # East Asian ideograph (duplicate simplified)
    0x235B77: (0x9DBC, 0),  # East Asian ideograph
    0x336275: (0x76BC, 0),  # East Asian ideograph
    0x234623: (0x9388, 0),  # East Asian ideograph
    0x295B79: (0x9E5A, 0),  # East Asian ideograph
    0x51496B: (0x852B, 0),  # East Asian ideograph
    0x215B7A: (0x9003, 0),  # East Asian ideograph
    0x234625: (0x93B9, 0),  # East Asian ideograph
    0x215B7B: (0x8FFD, 0),  # East Asian ideograph
    0x6F5173: (0xBE54, 0),  # Korean hangul
    0x6F527A: (0xC0E8, 0),  # Korean hangul
    0x276165: (0x987B, 0),  # East Asian ideograph (duplicate simplified)
    0x235B7C: (0x9DBA, 0),  # East Asian ideograph
    0x21385F: (0x5880, 0),  # East Asian ideograph
    0x234627: (0x93A1, 0),  # East Asian ideograph
    0x215635: (0x85E5, 0),  # East Asian ideograph
    0x275B7D: (0x8FD9, 0),  # East Asian ideograph
    0x234628: (0x93B0, 0),  # East Asian ideograph
    0x235B7E: (0x9DCF, 0),  # East Asian ideograph
    0x234629: (0x93A3, 0),  # East Asian ideograph
    0x21462A: (0x6B77, 0),  # East Asian ideograph
    0x224928: (0x6D61, 0),  # East Asian ideograph
    0x23462B: (0x939B, 0),  # East Asian ideograph
    0x276166: (0x9B13, 0),  # East Asian ideograph
    0x4B3F50: (0x61CA, 0),  # East Asian ideograph (variant of 213F50)
    0x22462C: (0x6BF3, 0),  # East Asian ideograph
    0x692532: (0x30B2, 0),  # Katakana letter GE
    0x23462D: (0x9398, 0),  # East Asian ideograph
    0x213238: (0x5075, 0),  # East Asian ideograph
    0x282626: (0x5CC4, 0),  # East Asian ideograph
    0x4B462E: (0x6B81, 0),  # East Asian ideograph
    0x2F5F45: (0x86A1, 0),  # East Asian ideograph
    0x2D4B22: (0x736A, 0),  # East Asian ideograph
    0x29576E: (0x9CA7, 0),  # East Asian ideograph
    0x692521: (0x30A1, 0),  # Katakana letter small A
    0x692522: (0x30A2, 0),  # Katakana letter A
    0x276167: (0x6597, 0),  # East Asian ideograph
    0x232524: (0x851E, 0),  # East Asian ideograph
    0x222525: (0x5D3F, 0),  # East Asian ideograph
    0x222526: (0x5D52, 0),  # East Asian ideograph
    0x222527: (0x5D3D, 0),  # East Asian ideograph
    0x222528: (0x5D4E, 0),  # East Asian ideograph
    0x692529: (0x30A9, 0),  # Katakana letter small O
    0x23252A: (0x8518, 0),  # East Asian ideograph
    0x69252B: (0x30AB, 0),  # Katakana letter KA
    0x22252C: (0x5D59, 0),  # East Asian ideograph
    0x23252D: (0x8526, 0),  # East Asian ideograph
    0x23252E: (
        0x8507,
        0,
    ),  # East Asian ideograph (variant of 2F252E which maps to 8507)
    0x22252F: (0x5D32, 0),  # East Asian ideograph
    0x692530: (0x30B0, 0),  # Katakana letter GU
    0x222531: (0x5D42, 0),  # East Asian ideograph
    0x4C2532: (0x5D5B, 0),  # East Asian ideograph
    0x224633: (0x6BF8, 0),  # East Asian ideograph
    0x232534: (0x84F0, 0),  # East Asian ideograph
    0x232535: (0x84EF, 0),  # East Asian ideograph
    0x232536: (0x8556, 0),  # East Asian ideograph
    0x692537: (0x30B7, 0),  # Katakana letter SI
    0x692538: (0x30B8, 0),  # Katakana letter ZI
    0x222539: (0x5D6F, 0),  # East Asian ideograph
    0x22253A: (0x5D6B, 0),  # East Asian ideograph
    0x696136: (0x753C, 0),  # East Asian ideograph
    0x69253C: (0x30BC, 0),  # Katakana letter ZE
    0x69253D: (0x30BD, 0),  # Katakana letter SO
    0x69253E: (0x30BE, 0),  # Katakana letter ZO
    0x274635: (0x6B87, 0),  # East Asian ideograph
    0x692540: (0x30C0, 0),  # Katakana letter DA
    0x276168: (0x95F9, 0),  # East Asian ideograph
    0x692542: (0x30C2, 0),  # Katakana letter DI
    0x692543: (0x30C3, 0),  # Katakana letter small TU
    0x222544: (0x5D4A, 0),  # East Asian ideograph
    0x225E7A: (0x7602, 0),  # East Asian ideograph
    0x232546: (0x8541, 0),  # East Asian ideograph
    0x692534: (0x30B4, 0),  # Katakana letter GO
    0x692548: (0x30C8, 0),  # Katakana letter TO
    0x222549: (0x5D6C, 0),  # East Asian ideograph
    0x22254A: (0x5D62, 0),  # East Asian ideograph
    0x23254B: (0x8558, 0),  # East Asian ideograph
    0x69254C: (0x30CC, 0),  # Katakana letter NU
    0x22254D: (0x5D82, 0),  # East Asian ideograph
    0x23254E: (0x8561, 0),  # East Asian ideograph
    0x23254F: (0x8540, 0),  # East Asian ideograph
    0x222550: (0x5D79, 0),  # East Asian ideograph
    0x224638: (0x6BF9, 0),  # East Asian ideograph
    0x692552: (0x30D2, 0),  # Katakana letter HI
    0x692553: (0x30D3, 0),  # Katakana letter BI
    0x692554: (0x30D4, 0),  # Katakana letter PI
    0x287231: (0x7F03, 0),  # East Asian ideograph
    0x692556: (0x30D6, 0),  # Katakana letter BU
    0x33516D: (0x6374, 0),  # East Asian ideograph
    0x4D222A: (0x83B5, 0),  # East Asian ideograph
    0x692559: (0x30D9, 0),  # Katakana letter BE
    0x22255A: (0x5D81, 0),  # East Asian ideograph
    0x69255B: (0x30DB, 0),  # Katakana letter HO
    0x23255C: (0x8564, 0),  # East Asian ideograph
    0x23255D: (0x855E, 0),  # East Asian ideograph
    0x23255E: (0x8573, 0),  # East Asian ideograph
    0x23255F: (0x8551, 0),  # East Asian ideograph
    0x222560: (0x5D7E, 0),  # East Asian ideograph
    0x692561: (0x30E1, 0),  # Katakana letter ME
    0x692562: (0x30E2, 0),  # Katakana letter MO
    0x27463B: (0x6740, 0),  # East Asian ideograph
    0x232564: (0x8562, 0),  # East Asian ideograph
    0x292535: (0x82C1, 0),  # East Asian ideograph
    0x222566: (0x5D92, 0),  # East Asian ideograph
    0x292567: (0x836C, 0),  # East Asian ideograph
    0x222568: (0x5D99, 0),  # East Asian ideograph
    0x27463C: (0x58F3, 0),  # East Asian ideograph
    0x22256A: (0x5DA2, 0),  # East Asian ideograph
    0x23256B: (0x8563, 0),  # East Asian ideograph
    0x23256C: (0x848D, 0),  # East Asian ideograph
    0x23256D: (0x8542, 0),  # East Asian ideograph
    0x69256E: (0x30EE, 0),  # Katakana letter small WA
    0x23463D: (0x93A4, 0),  # East Asian ideograph
    0x692570: (0x30F0, 0),  # Katakana letter WI
    0x232571: (0x854E, 0),  # East Asian ideograph
    0x692572: (0x30F2, 0),  # Katakana letter WO
    0x222573: (0x5DA1, 0),  # East Asian ideograph
    0x232574: (0x8555, 0),  # East Asian ideograph
    0x222575: (0x5D93, 0),  # East Asian ideograph
    0x232576: (0x855D, 0),  # East Asian ideograph
    0x222577: (0x5DA0, 0),  # East Asian ideograph
    0x4B3E40: (0x6046, 0),  # East Asian ideograph
    0x22257B: (0x5D94, 0),  # East Asian ideograph
    0x27616A: (0x90C1, 0),  # East Asian ideograph
    0x22257E: (0x5DAC, 0),  # East Asian ideograph
    0x6F4E3C: (0xB5C0, 0),  # Korean hangul
    0x284350: (0x68C2, 0),  # East Asian ideograph
    0x234640: (0x93BC, 0),  # East Asian ideograph
    0x692536: (0x30B6, 0),  # Katakana letter ZA
    0x513421: (0x91D6, 0),  # East Asian ideograph
    0x224642: (0x6BFF, 0),  # East Asian ideograph
    0x3F5F49: (0x7431, 0),  # East Asian ideograph
    0x29585C: (0x9CC7, 0),  # East Asian ideograph
    0x6F5C65: (0xD55C, 0),  # Korean hangul
    0x224644: (0x6C06, 0),  # East Asian ideograph
    0x276134: (0x9A7C, 0),  # East Asian ideograph
    0x28656A: (0x789B, 0),  # East Asian ideograph
    0x213865: (0x58C5, 0),  # East Asian ideograph
    0x294750: (0x950E, 0),  # East Asian ideograph
    0x4B3178: (
        0x5029,
        0,
    ),  # East Asian ideograph (variant of 213178 which maps to 5029)
    0x234647: (0x93A6, 0),  # East Asian ideograph
    0x29337D: (0x8C27, 0),  # East Asian ideograph
    0x224648: (0x6C04, 0),  # East Asian ideograph
    0x22492E: (0x6D8A, 0),  # East Asian ideograph
    0x453755: (0x56AE, 0),  # East Asian ideograph
    0x2D516A: (0x7DB3, 0),  # East Asian ideograph
    0x6F4E3E: (0xB5CC, 0),  # Korean hangul
    0x23464A: (0x93AA, 0),  # East Asian ideograph
    0x294751: (0x950F, 0),  # East Asian ideograph
    0x33627D: (0x6589, 0),  # East Asian ideograph
    0x213423: (0x5291, 0),  # East Asian ideograph
    0x235060: (0x98E3, 0),  # East Asian ideograph
    0x333C21: (0x7895, 0),  # East Asian ideograph
    0x6F5748: (0xC84C, 0),  # Korean hangul
    0x295153: (0x9967, 0),  # East Asian ideograph
    0x22464C: (0x6C08, 0),  # East Asian ideograph
    0x23464D: (0x939E, 0),  # East Asian ideograph
    0x213C74: (0x5EA0, 0),  # East Asian ideograph
    0x6F4E3F: (0xB5CF, 0),  # Korean hangul
    0x23464F: (0x9397, 0),  # East Asian ideograph
    0x692539: (0x30B9, 0),  # Katakana letter SU
    0x27727A: (0x54D5, 0),  # East Asian ideograph
    0x234651: (0x93BB, 0),  # East Asian ideograph
    0x295825: (0x9CBA, 0),  # East Asian ideograph
    0x224D73: (0x6FB6, 0),  # East Asian ideograph
    0x224652: (0x6C0D, 0),  # East Asian ideograph
    0x234653: (0x93F1, 0),  # East Asian ideograph
    0x225851: (0x739E, 0),  # East Asian ideograph
    0x6F4E40: (0xB5D1, 0),  # Korean hangul
    0x213868: (0x58D5, 0),  # East Asian ideograph
    0x69253A: (0x30BA, 0),  # Katakana letter ZU
    0x274655: (0x6C14, 0),  # East Asian ideograph
    0x234656: (0x93DE, 0),  # East Asian ideograph
    0x234657: (0x93EE, 0),  # East Asian ideograph
    0x234D30: (0x976E, 0),  # East Asian ideograph
    0x274658: (0x6C22, 0),  # East Asian ideograph
    0x27384A: (0x573A, 0),  # East Asian ideograph
    0x223244: (0x63E5, 0),  # East Asian ideograph
    0x224659: (0x6C15, 0),  # East Asian ideograph
    0x51563F: (0x8616, 0),  # East Asian ideograph
    0x23465A: (0x93C7, 0),  # East Asian ideograph
    0x23465B: (0x93F2, 0),  # East Asian ideograph
    0x232625: (0x8580, 0),  # East Asian ideograph
    0x222626: (0x5DA7, 0),  # East Asian ideograph
    0x232628: (0x858F, 0),  # East Asian ideograph
    0x22465C: (0x6C1A, 0),  # East Asian ideograph
    0x22262A: (0x5DB0, 0),  # East Asian ideograph
    0x23262D: (0x8579, 0),  # East Asian ideograph
    0x22262E: (0x5DB4, 0),  # East Asian ideograph
    0x23465D: (0x93D4, 0),  # East Asian ideograph
    0x222630: (0x5DB6, 0),  # East Asian ideograph
    0x232632: (0x857F, 0),  # East Asian ideograph
    0x232633: (0x8577, 0),  # East Asian ideograph
    0x232634: (0x8578, 0),  # East Asian ideograph
    0x22465E: (0x6C1D, 0),  # East Asian ideograph
    0x222636: (0x5DB7, 0),  # East Asian ideograph
    0x6F4C37: (0xB18B, 0),  # Korean hangul
    0x2D6132: (0x99EE, 0),  # East Asian ideograph
    0x23263D: (0x85A4, 0),  # East Asian ideograph
    0x22263E: (0x5DC3, 0),  # East Asian ideograph
    0x224660: (0x6C20, 0),  # East Asian ideograph
    0x232642: (0x857A, 0),  # East Asian ideograph
    0x222644: (0x5DC7, 0),  # East Asian ideograph
    0x232645: (0x8557, 0),  # East Asian ideograph
    0x222646: (0x5DC9, 0),  # East Asian ideograph
    0x222647: (0x5DCB, 0),  # East Asian ideograph
    0x232649: (0x85A8, 0),  # East Asian ideograph
    0x213D4F: (0x5F59, 0),  # East Asian ideograph
    0x234D32: (0x9778, 0),  # East Asian ideograph
    0x224662: (0x6C21, 0),  # East Asian ideograph
    0x22264E: (0x5DD8, 0),  # East Asian ideograph
    0x232650: (0x8599, 0),  # East Asian ideograph
    0x232651: (0x858A, 0),  # East Asian ideograph
    0x222652: (0x5DDC, 0),  # East Asian ideograph
    0x234663: (0x93CA, 0),  # East Asian ideograph
    0x232654: (0x8590, 0),  # East Asian ideograph
    0x232656: (0x8585, 0),  # East Asian ideograph
    0x232657: (0x8588, 0),  # East Asian ideograph
    0x225A40: (0x7447, 0),  # East Asian ideograph
    0x224664: (0x6C2A, 0),  # East Asian ideograph
    0x23265A: (0x85B8, 0),  # East Asian ideograph
    0x6F5749: (0xC870, 0),  # Korean hangul
    0x23265D: (0x85C1, 0),  # East Asian ideograph
    0x334665: (0x6C61, 0),  # East Asian ideograph
    0x232661: (0x85BA, 0),  # East Asian ideograph
    0x222662: (0x5E00, 0),  # East Asian ideograph
    0x222664: (0x51E7, 0),  # East Asian ideograph
    0x234666: (0x93E8, 0),  # East Asian ideograph
    0x224934: (0x6D79, 0),  # East Asian ideograph
    0x232668: (0x85CE, 0),  # East Asian ideograph
    0x23266A: (0x85C2, 0),  # East Asian ideograph
    0x23266B: (0x85B7, 0),  # East Asian ideograph
    0x23266C: (0x85B9, 0),  # East Asian ideograph
    0x23266E: (0x85B3, 0),  # East Asian ideograph
    0x23266F: (0x85BD, 0),  # East Asian ideograph
    0x232670: (0x85C4, 0),  # East Asian ideograph
    0x224668: (0x6C2C, 0),  # East Asian ideograph
    0x222672: (0x5E14, 0),  # East Asian ideograph
    0x222673: (0x5E17, 0),  # East Asian ideograph
    0x232675: (0x85BE, 0),  # East Asian ideograph
    0x222676: (0x5E19, 0),  # East Asian ideograph
    0x224669: (0x6C31, 0),  # East Asian ideograph (not in Unicode)
    0x222678: (0x5E1F, 0),  # East Asian ideograph
    0x22267A: (0x5E23, 0),  # East Asian ideograph
    0x22267B: (0x5E21, 0),  # East Asian ideograph
    0x23267E: (0x85B6, 0),  # East Asian ideograph
    0x295421: (0x9AA3, 0),  # East Asian ideograph
    0x2D4647: (0x6BD8, 0),  # East Asian ideograph
    0x284359: (0x6989, 0),  # East Asian ideograph
    0x2D466D: (0x51B3, 0),  # East Asian ideograph
    0x294758: (0x9561, 0),  # East Asian ideograph
    0x69253F: (0x30BF, 0),  # Katakana letter TA
    0x227C5B: (0x82D0, 0),  # East Asian ideograph
    0x28723C: (0x7F08, 0),  # East Asian ideograph
    0x224670: (0x6C3B, 0),  # East Asian ideograph
    0x295422: (0x9A81, 0),  # East Asian ideograph
    0x234D35: (0x9773, 0),  # East Asian ideograph
    0x276174: (0x9C7C, 0),  # East Asian ideograph
    0x234672: (0x93DA, 0),  # East Asian ideograph
    0x234673: (0x93D0, 0),  # East Asian ideograph
    0x335E42: (0x9452, 0),  # East Asian ideograph
    0x2D353C: (0x6B62, 0),  # East Asian ideograph
    0x234674: (0x93EF, 0),  # East Asian ideograph
    0x6F4E37: (0xB5B3, 0),  # Korean hangul
    0x4B4676: (0x6C89, 0),  # East Asian ideograph
    0x213121: (0x4F11, 0),  # East Asian ideograph
    0x276136: (0x9A77, 0),  # East Asian ideograph
    0x21386F: (0x58E2, 0),  # East Asian ideograph
    0x223C6E: (0x68B2, 0),  # East Asian ideograph
    0x6F2472: (0x314F, 0),  # Korean hangul
    0x224678: (0x6C46, 0),  # East Asian ideograph
    0x6F5078: (0xBC29, 0),  # Korean hangul
    0x28723E: (0x7F0C, 0),  # East Asian ideograph
    0x29364E: (0x8D33, 0),  # East Asian ideograph
    0x22467A: (0x6C52, 0),  # East Asian ideograph
    0x213125: (0x4F01, 0),  # East Asian ideograph
    0x234D37: (0x9783, 0),  # East Asian ideograph
    0x215F69: (0x9739, 0),  # East Asian ideograph
    0x276176: (0x9C81, 0),  # East Asian ideograph
    0x6F4E48: (0xB69D, 0),  # Korean hangul
    0x23467C: (0x93CC, 0),  # East Asian ideograph
    0x6F574A: (0xC871, 0),  # Korean hangul
    0x224D7C: (0x6FC6, 0),  # East Asian ideograph
    0x23517B: (0x9954, 0),  # East Asian ideograph
    0x21312A: (0x4F4F, 0),  # East Asian ideograph
    0x234D38: (0x977A, 0),  # East Asian ideograph
    0x213C76: (0x5EAB, 0),  # East Asian ideograph
    0x21312B: (0x4F4D, 0),  # East Asian ideograph
    0x6F4E49: (0xB6A4, 0),  # Korean hangul
    0x213871: (0x58E9, 0),  # East Asian ideograph
    0x21312C: (0x4F34, 0),  # East Asian ideograph
    0x6F594C: (0xCD18, 0),  # Korean hangul
    0x21342E: (0x52C3, 0),  # East Asian ideograph
    0x21312D: (0x4F47, 0),  # East Asian ideograph
    0x2D5758: (0x890E, 0),  # East Asian ideograph
    0x21312F: (0x4F3A, 0),  # East Asian ideograph
    0x275B3F: (0x8F7D, 0),  # East Asian ideograph
    0x6F4F3D: (0xB86D, 0),  # Korean hangul
    0x28704A: (0x7EBE, 0),  # East Asian ideograph
    0x222722: (0x5E22, 0),  # East Asian ideograph
    0x286577: (0x789C, 0),  # East Asian ideograph
    0x222724: (0x5E28, 0),  # East Asian ideograph
    0x213872: (0x58EB, 0),  # East Asian ideograph
    0x232728: (0x85F7, 0),  # East Asian ideograph
    0x6F5424: (0xC2DD, 0),  # Korean hangul
    0x23272C: (0x85E6, 0),  # East Asian ideograph
    0x223132: (0x6360, 0),  # East Asian ideograph
    0x23272E: (0x85D4, 0),  # East Asian ideograph
    0x232731: (0x85ED, 0),  # East Asian ideograph
    0x6F5D42: (0xD65C, 0),  # Korean hangul
    0x222735: (0x5E44, 0),  # East Asian ideograph
    0x222736: (0x5E43, 0),  # East Asian ideograph
    0x222739: (0x5E42, 0),  # East Asian ideograph
    0x22273F: (0x5E4E, 0),  # East Asian ideograph
    0x6F4E4B: (0xB6AC, 0),  # Korean hangul
    0x232743: (0x85DF, 0),  # East Asian ideograph
    0x232745: (0x85D8, 0),  # East Asian ideograph
    0x692545: (0x30C5, 0),  # Katakana letter DU
    0x222747: (0x5E58, 0),  # East Asian ideograph
    0x222748: (0x5E48, 0),  # East Asian ideograph
    0x513B52: (0x6C3D, 0),  # East Asian ideograph
    0x213137: (0x4F3D, 0),  # East Asian ideograph
    0x23274C: (0x85DC, 0),  # East Asian ideograph
    0x23274E: (0x85F5, 0),  # East Asian ideograph
    0x273138: (0x5E03, 0),  # East Asian ideograph
    0x232752: (0x8622, 0),  # East Asian ideograph
    0x232754: (0x8610, 0),  # East Asian ideograph
    0x285029: (0x6EDF, 0),  # East Asian ideograph
    0x232757: (0x85FC, 0),  # East Asian ideograph
    0x222758: (0x5E61, 0),  # East Asian ideograph
    0x23275B: (0x85FF, 0),  # East Asian ideograph
    0x23313A: (0x89D6, 0),  # East Asian ideograph
    0x23275E: (0x85FE, 0),  # East Asian ideograph
    0x22275F: (0x5E6C, 0),  # East Asian ideograph
    0x222760: (0x5E6A, 0),  # East Asian ideograph
    0x222763: (0x5E6E, 0),  # East Asian ideograph
    0x222764: (0x5E6D, 0),  # East Asian ideograph
    0x222765: (0x5E70, 0),  # East Asian ideograph
    0x232768: (0x8604, 0),  # East Asian ideograph
    0x27313C: (0x5360, 0),  # East Asian ideograph
    0x227C6E: (0x8314, 0),  # East Asian ideograph
    0x22276D: (0x5E75, 0),  # East Asian ideograph
    0x232771: (0x8605, 0),  # East Asian ideograph
    0x216757: (0x50A3, 0),  # East Asian ideograph
    0x232775: (0x862B, 0),  # East Asian ideograph
    0x213D51: (0x5F62, 0),  # East Asian ideograph
    0x222777: (0x5E80, 0),  # East Asian ideograph
    0x21313F: (0x4F5C, 0),  # East Asian ideograph
    0x22277E: (0x5E8B, 0),  # East Asian ideograph
    0x275D38: (0x91CA, 0),  # East Asian ideograph
    0x294760: (0x9563, 0),  # East Asian ideograph
    0x213432: (0x52D2, 0),  # East Asian ideograph
    0x33572E: (0x880E, 0),  # East Asian ideograph
    0x2D3543: (0x4EDD, 0),  # East Asian ideograph
    0x27506F: (0x7EA0, 0),  # East Asian ideograph
    0x215B27: (0x8E85, 0),  # East Asian ideograph
    0x213142: (0x4F4E, 0),  # East Asian ideograph
    0x217D40: (0x5B19, 0),  # East Asian ideograph
    0x213143: (0x4F5D, 0),  # East Asian ideograph
    0x213C77: (0x5EA7, 0),  # East Asian ideograph
    0x213144: (0x4F36, 0),  # East Asian ideograph
    0x6F4B5C: (0xB0AF, 0),  # Korean hangul
    0x6F4E4E: (0xB6F4, 0),  # Korean hangul
    0x213876: (0x58FA, 0),  # East Asian ideograph
    0x223145: (0x6335, 0),  # East Asian ideograph
    0x706067: (0x567B, 0),  # East Asian ideograph
    0x223832: (0x665F, 0),  # East Asian ideograph
    0x295828: (0x9CB4, 0),  # East Asian ideograph
    0x233147: (0x89E1, 0),  # East Asian ideograph
    0x29586E: (0x9CA5, 0),  # East Asian ideograph
    0x213148: (0x4F8D, 0),  # East Asian ideograph
    0x275B40: (0x8F7E, 0),  # East Asian ideograph
    0x6F4E4F: (0xB6F8, 0),  # Korean hangul
    0x275736: (0x8747, 0),  # East Asian ideograph
    0x21314A: (0x4F7F, 0),  # East Asian ideograph
    0x692549: (0x30C9, 0),  # Katakana letter DO
    0x2F5476: (0x9AE1, 0),  # East Asian ideograph
    0x21314B: (0x4F9B, 0),  # East Asian ideograph
    0x275071: (0x7EA3, 0),  # East Asian ideograph
    0x21314C: (0x4F86, 0),  # East Asian ideograph
    0x2D3730: (0x751E, 0),  # East Asian ideograph
    0x21314D: (0x4F6C, 0),  # East Asian ideograph
    0x6F4E50: (0xB700, 0),  # Korean hangul
    0x21314F: (0x4F96, 0),  # East Asian ideograph
    0x213435: (0x52DE, 0),  # East Asian ideograph
    0x233C33: (0x8F47, 0),  # East Asian ideograph
    0x213151: (0x4F83, 0),  # East Asian ideograph
    0x287247: (0x7F11, 0),  # East Asian ideograph
    0x697152: (0x99F2, 0),  # East Asian ideograph
    0x453768: (0x5EFB, 0),  # East Asian ideograph
    0x213153: (0x4F88, 0),  # East Asian ideograph
    0x276138: (0x9A79, 0),  # East Asian ideograph
    0x4B3F51: (0x61D1, 0),  # East Asian ideograph
    0x6F4E51: (0xB701, 0),  # Korean hangul
    0x213154: (0x4F69, 0),  # East Asian ideograph
    0x69254B: (0x30CB, 0),  # Katakana letter NI
    0x213436: (0x52DB, 0),  # East Asian ideograph
    0x6F5826: (0xC998, 0),  # Korean hangul
    0x275073: (0x7EAB, 0),  # East Asian ideograph
    0x354156: (0x91BE, 0),  # East Asian ideograph
    0x295871: (0x9CCE, 0),  # East Asian ideograph
    0x287248: (0x7F0F, 0),  # East Asian ideograph
    0x4B606F: (0x991D, 0),  # East Asian ideograph
    0x233158: (0x89F1, 0),  # East Asian ideograph
    0x294531: (0x9528, 0),  # East Asian ideograph
    0x6F4E52: (0xB728, 0),  # Korean hangul
    0x284366: (0x6924, 0),  # East Asian ideograph
    0x217159: (0x55D0, 0),  # East Asian ideograph
    0x225A4F: (0x7452, 0),  # East Asian ideograph
    0x21315A: (0x4FAF, 0),  # East Asian ideograph
    0x232822: (0x8627, 0),  # East Asian ideograph
    0x21715B: (0x55CD, 0),  # East Asian ideograph
    0x274C31: (0x7544, 0),  # East Asian ideograph
    0x232826: (0x8629, 0),  # East Asian ideograph
    0x23315C: (0x89F3, 0),  # East Asian ideograph
    0x224943: (0x6D94, 0),  # East Asian ideograph
    0x213A61: (0x5B7A, 0),  # East Asian ideograph
    0x21315D: (0x4FE0, 0),  # East Asian ideograph
    0x6F4B5D: (0xB0B1, 0),  # Korean hangul
    0x232832: (0x8637, 0),  # East Asian ideograph
    0x395230: (0x5BD8, 0),  # East Asian ideograph
    0x222835: (0x5EA5, 0),  # East Asian ideograph
    0x222836: (0x5EAF, 0),  # East Asian ideograph
    0x213438: (0x52E2, 0),  # East Asian ideograph
    0x232838: (0x8636, 0),  # East Asian ideograph
    0x21315F: (0x4FB6, 0),  # East Asian ideograph
    0x23283E: (0x863C, 0),  # East Asian ideograph
    0x23283F: (0x8640, 0),  # East Asian ideograph
    0x232840: (0x863A, 0),  # East Asian ideograph
    0x233160: (0x89F6, 0),  # East Asian ideograph
    0x222842: (0x5EB9, 0),  # East Asian ideograph
    0x39365A: (0x8AE0, 0),  # East Asian ideograph
    0x227161: (0x7DA3, 0),  # East Asian ideograph
    0x22284B: (0x5EB3, 0),  # East Asian ideograph
    0x22284C: (0x5EC4, 0),  # East Asian ideograph
    0x217162: (0x55DD, 0),  # East Asian ideograph
    0x6F4E54: (0xB72C, 0),  # Korean hangul
    0x275D3F: (0x9488, 0),  # East Asian ideograph
    0x294767: (0x94E7, 0),  # East Asian ideograph
    0x69254E: (0x30CE, 0),  # Katakana letter NO
    0x222855: (0x5ECB, 0),  # East Asian ideograph
    0x222857: (0x5ECD, 0),  # East Asian ideograph
    0x213164: (0x4FDF, 0),  # East Asian ideograph
    0x22285A: (0x5ED2, 0),  # East Asian ideograph
    0x22285B: (0x5ED1, 0),  # East Asian ideograph
    0x22285C: (0x5ED5, 0),  # East Asian ideograph
    0x23285E: (0x8659, 0),  # East Asian ideograph
    0x22285F: (0x5ED4, 0),  # East Asian ideograph
    0x222860: (0x5ED9, 0),  # East Asian ideograph
    0x222861: (0x5ECE, 0),  # East Asian ideograph
    0x21232D: (0xFF0D, 0),  # Ideographic hyphen minus
    0x232866: (0x8661, 0),  # East Asian ideograph
    0x4C2867: (0x5EDB, 0),  # East Asian ideograph
    0x222868: (0x5EE1, 0),  # East Asian ideograph
    0x232869: (0x8662, 0),  # East Asian ideograph
    0x23286A: (0x8663, 0),  # East Asian ideograph
    0x287167: (0x7EEF, 0),  # East Asian ideograph
    0x22286D: (0x5EE7, 0),  # East Asian ideograph
    0x232871: (0x8669, 0),  # East Asian ideograph
    0x69254F: (0x30CF, 0),  # Katakana letter HA
    0x2D5B7A: (0x8FEF, 0),  # East Asian ideograph
    0x217169: (0x55E9, 0),  # East Asian ideograph
    0x232878: (0x866C, 0),  # East Asian ideograph
    0x23287B: (0x8672, 0),  # East Asian ideograph
    0x22287C: (0x5EED, 0),  # East Asian ideograph
    0x21316A: (0x4FCE, 0),  # East Asian ideograph
    0x23287E: (0x867B, 0),  # East Asian ideograph
    0x274C34: (0x5F02, 0),  # East Asian ideograph
    0x23462A: (0x93B7, 0),  # East Asian ideograph
    0x21316B: (0x4FD7, 0),  # East Asian ideograph
    0x23316C: (0x8A06, 0),  # East Asian ideograph
    0x276139: (0x9A78, 0),  # East Asian ideograph
    0x6F4E56: (0xB730, 0),  # Korean hangul
    0x294769: (0x9564, 0),  # East Asian ideograph
    0x6F507B: (0xBC31, 0),  # Korean hangul
    0x21316E: (0x500D, 0),  # East Asian ideograph
    0x4B5861: (0x4F89, 0),  # East Asian ideograph
    0x21716F: (0x55CF, 0),  # East Asian ideograph
    0x213170: (0x5026, 0),  # East Asian ideograph
    0x4B3E5B: (0x60C5, 0),  # East Asian ideograph
    0x213171: (0x500C, 0),  # East Asian ideograph
    0x6F4E57: (0xB738, 0),  # Korean hangul
    0x223172: (0x639E, 0),  # East Asian ideograph
    0x692551: (0x30D1, 0),  # Katakana letter PA
    0x21343C: (0x52F5, 0),  # East Asian ideograph
    0x273173: (0x4EEC, 0),  # East Asian ideograph
    0x4C4F24: (0x6F46, 0),  # East Asian ideograph
    0x235B7A: (0x9DC1, 0),  # East Asian ideograph
    0x287174: (0x7EF2, 0),  # East Asian ideograph
    0x274C36: (0x753B, 0),  # East Asian ideograph
    0x39365E: (0x559E, 0),  # East Asian ideograph
    0x6F5B21: (0xD0ED, 0),  # Korean hangul
    0x4B5C32: (0x9038, 0),  # East Asian ideograph
    0x6F4B5E: (0xB0B3, 0),  # Korean hangul
    0x6F4E58: (0xB739, 0),  # Korean hangul
    0x2D3177: (0x5E78, 0),  # East Asian ideograph
    0x21343D: (0x52F8, 0),  # East Asian ideograph
    0x217178: (0x55C1, 0),  # East Asian ideograph
    0x6F5C23: (0xD37C, 0),  # Korean hangul
    0x273179: (0x4FE9, 0),  # East Asian ideograph
    0x6F5C24: (0xD37D, 0),  # Korean hangul
    0x29365F: (0x8D47, 0),  # East Asian ideograph
    0x6F5B22: (0xD0EF, 0),  # Korean hangul
    0x6F5C25: (0xD380, 0),  # Korean hangul
    0x21317B: (0x5012, 0),  # East Asian ideograph
    0x6F5C26: (0xD384, 0),  # Korean hangul
    0x6F4E59: (0xB73B, 0),  # Korean hangul
    0x4B317C: (0x5024, 0),  # East Asian ideograph
    0x235C27: (0x9DC3, 0),  # East Asian ideograph
    0x22317D: (0x63AB, 0),  # East Asian ideograph
    0x215C28: (0x901A, 0),  # East Asian ideograph
    0x4C4F26: (0x6EDD, 0),  # East Asian ideograph
    0x69717E: (0x9AF7, 0),  # East Asian ideograph
    0x215C29: (0x9020, 0),  # East Asian ideograph
    0x216764: (0x5095, 0),  # East Asian ideograph
    0x6F5C2A: (0xD390, 0),  # Korean hangul
    0x6F5C2B: (0xD391, 0),  # Korean hangul
    0x6F4E5A: (0xB744, 0),  # Korean hangul
    0x6F5C2C: (0xD398, 0),  # Korean hangul
    0x695C2D: (0x6928, 0),  # East Asian ideograph
    0x4B372F: (0x5C1C, 0),  # East Asian ideograph
    0x274C39: (0x5F53, 0),  # East Asian ideograph
    0x287251: (0x7F1F, 0),  # East Asian ideograph
    0x6F5C6B: (0xD56C, 0),  # Korean hangul
    0x215C2F: (0x902E, 0),  # East Asian ideograph
    0x27613A: (0x9A7D, 0),  # East Asian ideograph
    0x225C30: (0x74C8, 0),  # East Asian ideograph
    0x6F4E5B: (0xB748, 0),  # Korean hangul
    0x222923: (0x5EF4, 0),  # East Asian ideograph
    0x232925: (0x867A, 0),  # East Asian ideograph
    0x232926: (0x8673, 0),  # East Asian ideograph
    0x225C31: (0x74C5, 0),  # East Asian ideograph
    0x29432B: (0x94C6, 0),  # East Asian ideograph
    0x6F5828: (0xC99D, 0),  # Korean hangul
    0x215C32: (0xFA25, 0),  # East Asian ideograph
    0x23292E: (0x8696, 0),  # East Asian ideograph
    0x27507D: (0x7EAF, 0),  # East Asian ideograph
    0x217671: (0x5827, 0),  # East Asian ideograph
    0x29333B: (0x8C00, 0),  # East Asian ideograph
    0x215C33: (0x9032, 0),  # East Asian ideograph
    0x222935: (0x5F07, 0),  # East Asian ideograph
    0x232936: (0x8691, 0),  # East Asian ideograph
    0x232937: (0x869C, 0),  # East Asian ideograph
    0x235C34: (0x9DAC, 0),  # East Asian ideograph
    0x22293A: (0x5F0B, 0),  # East Asian ideograph
    0x23293C: (0x868D, 0),  # East Asian ideograph
    0x23293D: (0x868B, 0),  # East Asian ideograph
    0x6F5C35: (0xD3B5, 0),  # Korean hangul
    0x232940: (0x86A6, 0),  # East Asian ideograph
    0x232942: (0x869D, 0),  # East Asian ideograph
    0x39476F: (0x51C0, 0),  # East Asian ideograph
    0x235C36: (0x9DB2, 0),  # East Asian ideograph
    0x232946: (0x86A0, 0),  # East Asian ideograph
    0x2D3F3A: (0x6185, 0),  # East Asian ideograph
    0x232948: (0x86A7, 0),  # East Asian ideograph
    0x22294A: (0x5F28, 0),  # East Asian ideograph
    0x22294B: (0x5F22, 0),  # East Asian ideograph
    0x22294C: (0x5F23, 0),  # East Asian ideograph
    0x22294D: (0x5F24, 0),  # East Asian ideograph
    0x235B7B: (0x9DB8, 0),  # East Asian ideograph
    0x225C38: (0x74D6, 0),  # East Asian ideograph
    0x222952: (0x5F30, 0),  # East Asian ideograph
    0x6F5A27: (0xCEEC, 0),  # Korean hangul
    0x215C39: (0x9054, 0),  # East Asian ideograph
    0x232958: (0x86BA, 0),  # East Asian ideograph
    0x232959: (0x86B0, 0),  # East Asian ideograph
    0x22295C: (0x5F40, 0),  # East Asian ideograph
    0x215C3A: (0x9055, 0),  # East Asian ideograph
    0x6F4E5D: (0xB764, 0),  # Korean hangul
    0x22295F: (0x5F44, 0),  # East Asian ideograph
    0x232960: (0x86B3, 0),  # East Asian ideograph
    0x232962: (0x86C9, 0),  # East Asian ideograph
    0x215C3B: (0x903C, 0),  # East Asian ideograph
    0x232967: (0x86D8, 0),  # East Asian ideograph
    0x222968: (0x5F50, 0),  # East Asian ideograph
    0x215C3C: (0x9047, 0),  # East Asian ideograph
    0x22296A: (0x5F56, 0),  # East Asian ideograph
    0x22296C: (0x5F58, 0),  # East Asian ideograph
    0x2D3E60: (0x6075, 0),  # East Asian ideograph
    0x23296E: (0x86E3, 0),  # East Asian ideograph
    0x225C3D: (0x74D8, 0),  # East Asian ideograph
    0x222970: (0x5F60, 0),  # East Asian ideograph
    0x232971: (0x86EC, 0),  # East Asian ideograph
    0x222972: (0x5F63, 0),  # East Asian ideograph
    0x222973: (0x809C, 0),  # East Asian ideograph
    0x222974: (0x5F67, 0),  # East Asian ideograph
    0x215C3E: (0x904E, 0),  # East Asian ideograph
    0x232977: (0x86D0, 0),  # East Asian ideograph
    0x222978: (0x5F72, 0),  # East Asian ideograph
    0x222979: (0x5F73, 0),  # East Asian ideograph
    0x23297A: (0x86D1, 0),  # East Asian ideograph
    0x2D5C3F: (0x5FA7, 0),  # East Asian ideograph
    0x22297C: (0x5F74, 0),  # East Asian ideograph
    0x23297E: (0x86DE, 0),  # East Asian ideograph
    0x225C40: (0x74DA, 0),  # East Asian ideograph
    0x213443: (0x5308, 0),  # East Asian ideograph
    0x215C41: (0x9041, 0),  # East Asian ideograph
    0x4C4F2B: (0x701E, 0),  # East Asian ideograph
    0x6F5C42: (0xD3FD, 0),  # Korean hangul
    0x333251: (0x5FBA, 0),  # East Asian ideograph
    0x6F5B28: (0xD138, 0),  # Korean hangul
    0x22494F: (0x6D96, 0),  # East Asian ideograph
    0x695C43: (0x6981, 0),  # East Asian ideograph
    0x4B5C39: (0x9039, 0),  # East Asian ideograph
    0x215C44: (0x9060, 0),  # East Asian ideograph
    0x6F4E5F: (0xB770, 0),  # Korean hangul
    0x273B31: (0x5B9E, 0),  # East Asian ideograph
    0x215C45: (0x905C, 0),  # East Asian ideograph
    0x29432F: (0x94F3, 0),  # East Asian ideograph
    0x696325: (0x7907, 0),  # East Asian ideograph
    0x235C46: (0x9DDE, 0),  # East Asian ideograph
    0x215C47: (0x9065, 0),  # East Asian ideograph
    0x6F5B29: (0xD140, 0),  # Korean hangul
    0x215C48: (0x905E, 0),  # East Asian ideograph
    0x6F4E38: (0xB5B4, 0),  # Korean hangul
    0x27613B: (0x9A87, 0),  # East Asian ideograph
    0x275C49: (0x9002, 0),  # East Asian ideograph
    0x6F4E60: (0xB771, 0),  # Korean hangul
    0x273B32: (0x5B81, 0),  # East Asian ideograph
    0x29255A: (0x8487, 0),  # East Asian ideograph
    0x6F5C4A: (0xD479, 0),  # Korean hangul
    0x225A5D: (0x7440, 0),  # East Asian ideograph
    0x235E5C: (0x9EE7, 0),  # East Asian ideograph
    0x6F5C4B: (0xD47C, 0),  # Korean hangul
    0x2D3556: (0x7343, 0),  # East Asian ideograph
    0x2D532C: (0x6BD3, 0),  # East Asian ideograph
    0x6F5C4C: (0xD480, 0),  # Korean hangul
    0x336321: (0x6B6F, 0),  # East Asian ideograph
    0x6F5B2A: (0xD141, 0),  # Korean hangul
    0x215C4D: (0x9075, 0),  # East Asian ideograph
    0x6F4C3A: (0xB193, 0),  # Korean hangul
    0x6F5C4E: (0xD489, 0),  # Korean hangul
    0x6F4E61: (0xB775, 0),  # Korean hangul
    0x294774: (0x9571, 0),  # East Asian ideograph
    0x215C4F: (0x9078, 0),  # East Asian ideograph
    0x217435: (0x571A, 0),  # East Asian ideograph
    0x215C50: (0x9072, 0),  # East Asian ideograph
    0x4B3231: (0x4EEE, 0),  # East Asian ideograph
    0x275C51: (0x8FC1, 0),  # East Asian ideograph
    0x6F5B2B: (0xD143, 0),  # Korean hangul
    0x275C52: (0x8FBD, 0),  # East Asian ideograph
    0x215C53: (0x907A, 0),  # East Asian ideograph
    0x4D503A: (0x98D1, 0),  # East Asian ideograph
    0x69255C: (0x30DC, 0),  # Katakana letter BO
    0x225C54: (0x74E9, 0),  # East Asian ideograph
    0x217436: (0x571B, 0),  # East Asian ideograph
    0x6F5C55: (0xD508, 0),  # Korean hangul
    0x213A36: (0x5ABD, 0),  # East Asian ideograph
    0x215C56: (0x9081, 0),  # East Asian ideograph
    0x6F5B2C: (0xD144, 0),  # Korean hangul
    0x455F35: (0x9668, 0),  # East Asian ideograph (Version J extension)
    0x215C57: (0x9084, 0),  # East Asian ideograph
    0x6F4F3E: (0xB86F, 0),  # Korean hangul
    0x6F5C33: (0xD3AD, 0),  # Korean hangul
    0x225C58: (0x74F1, 0),  # East Asian ideograph
    0x69255D: (0x30DD, 0),  # Katakana letter PO
    0x6F5C59: (0xD53C, 0),  # Korean hangul
    0x215C5A: (0x9087, 0),  # East Asian ideograph
    0x212A21: (0xE8D0, 0),  # EACC component character
    0x212A22: (0xE8D1, 0),  # EACC component character
    0x215C5B: (0x908A, 0),  # East Asian ideograph
    0x212A24: (0xE8D3, 0),  # EACC component character
    0x232A25: (0x870B, 0),  # East Asian ideograph
    0x212A26: (0xE8D5, 0),  # EACC component character
    0x222A27: (0x5F89, 0),  # East Asian ideograph
    0x212A28: (0xE8D6, 0),  # EACC component character
    0x215C5C: (0x9090, 0),  # East Asian ideograph
    0x212A2A: (0xE8D8, 0),  # EACC component character
    0x222A2B: (0x5F94, 0),  # East Asian ideograph
    0x212A2C: (0xE8DA, 0),  # EACC component character
    0x212A2D: (0xE8DB, 0),  # EACC component character
    0x69727E: (0x9D48, 0),  # East Asian ideograph
    0x215C5D: (0x908F, 0),  # East Asian ideograph
    0x2E284C: (0x5ECF, 0),  # East Asian ideograph
    0x6F4E64: (0xB77C, 0),  # Korean hangul
    0x275D4F: (0x94B4, 0),  # East Asian ideograph
    0x232A33: (0x86F8, 0),  # East Asian ideograph
    0x232A34: (0x8706, 0),  # East Asian ideograph
    0x4B5C5E: (0x961D, 0),  # East Asian ideograph
    0x232A36: (0x870E, 0),  # East Asian ideograph
    0x212A37: (0xE8E4, 0),  # EACC component character
    0x232A38: (0x8709, 0),  # East Asian ideograph
    0x222A39: (0x5F9C, 0),  # East Asian ideograph
    0x232A3A: (0x870A, 0),  # East Asian ideograph
    0x235C5F: (0x9DEB, 0),  # East Asian ideograph
    0x212A3C: (0xE8E9, 0),  # EACC component character
    0x222A3D: (0x5F9A, 0),  # East Asian ideograph
    0x232A3E: (0x870D, 0),  # East Asian ideograph
    0x212A3F: (0xE8EC, 0),  # EACC component character
    0x212A40: (0xE8ED, 0),  # EACC component character
    0x6F5C60: (0xD551, 0),  # Korean hangul
    0x232A42: (0x874A, 0),  # East Asian ideograph
    0x232A43: (0x8723, 0),  # East Asian ideograph
    0x232A44: (0x8737, 0),  # East Asian ideograph
    0x232A45: (0x8728, 0),  # East Asian ideograph
    0x222A46: (0x5FAF, 0),  # East Asian ideograph
    0x225C61: (0x74F4, 0),  # East Asian ideograph
    0x232A49: (0x8740, 0),  # East Asian ideograph
    0x232A4B: (0x872E, 0),  # East Asian ideograph
    0x232A4C: (0x873D, 0),  # East Asian ideograph
    0x232A4E: (0x871E, 0),  # East Asian ideograph
    0x6F4E65: (0xB77D, 0),  # Korean hangul
    0x222A50: (0x5FBC, 0),  # East Asian ideograph
    0x69255F: (0x30DF, 0),  # Katakana letter MI
    0x232A53: (0x8743, 0),  # East Asian ideograph
    0x232A55: (0x8744, 0),  # East Asian ideograph
    0x6F507E: (0xBC38, 0),  # Korean hangul
    0x222A57: (0x5FC9, 0),  # East Asian ideograph
    0x232A59: (0x8729, 0),  # East Asian ideograph
    0x232A5A: (0x8739, 0),  # East Asian ideograph
    0x213241: (0x5091, 0),  # East Asian ideograph
    0x232A5F: (0x871A, 0),  # East Asian ideograph
    0x222A61: (0x5FD2, 0),  # East Asian ideograph
    0x222A63: (0x5FD0, 0),  # East Asian ideograph
    0x232A64: (0x8731, 0),  # East Asian ideograph
    0x232A65: (0x8711, 0),  # East Asian ideograph
    0x232A66: (0x8712, 0),  # East Asian ideograph
    0x222A67: (0x5FCE, 0),  # East Asian ideograph
    0x222A68: (0x5FED, 0),  # East Asian ideograph
    0x6F4C3B: (0xB194, 0),  # Korean hangul
    0x232A6B: (0x874F, 0),  # East Asian ideograph
    0x232A6C: (0x8771, 0),  # East Asian ideograph
    0x232A6D: (0x8763, 0),  # East Asian ideograph
    0x275D51: (0x94B8, 0),  # East Asian ideograph
    0x232A71: (0x8764, 0),  # East Asian ideograph
    0x222A72: (0x5FEE, 0),  # East Asian ideograph
    0x232A73: (0x8765, 0),  # East Asian ideograph
    0x232A74: (0x877D, 0),  # East Asian ideograph
    0x6F5C69: (0xD569, 0),  # Korean hangul
    0x222A78: (0x5FE1, 0),  # East Asian ideograph
    0x232A79: (0x8758, 0),  # East Asian ideograph
    0x222A7B: (0x5FE4, 0),  # East Asian ideograph
    0x215C6A: (0x90E1, 0),  # East Asian ideograph
    0x28725D: (0x7F1C, 0),  # East Asian ideograph
    0x6F5B30: (0xD150, 0),  # Korean hangul
    0x275C6B: (0x5369, 0),  # East Asian ideograph
    0x3F516D: (0x6403, 0),  # East Asian ideograph
    0x235C6C: (0x9DE6, 0),  # East Asian ideograph
    0x6F4E67: (0xB784, 0),  # Korean hangul
    0x275D52: (0x94C0, 0),  # East Asian ideograph
    0x215C6D: (0x90F5, 0),  # East Asian ideograph
    0x33303A: (0x8FFA, 0),  # East Asian ideograph
    0x6F5C6E: (0xD574, 0),  # Korean hangul
    0x6F5C6F: (0xD575, 0),  # Korean hangul
    0x28725E: (0x7F19, 0),  # East Asian ideograph
    0x6F5873: (0xCC0C, 0),  # Korean hangul
    0x705F30: (0x7519, 0),  # East Asian ideograph
    0x215C70: (0x9109, 0),  # East Asian ideograph
    0x215C71: (0x9112, 0),  # East Asian ideograph
    0x6F4E68: (0xB78C, 0),  # Korean hangul
    0x275E68: (0x9617, 0),  # East Asian ideograph
    0x4B5C72: (
        0x9119,
        0,
    ),  # East Asian ideograph (variant of 215C72 which maps to 9119)
    0x275153: (0x7EAC, 0),  # East Asian ideograph
    0x215C73: (0x912D, 0),  # East Asian ideograph
    0x235A21: (0x9D02, 0),  # East Asian ideograph
    0x215C74: (0x9130, 0),  # East Asian ideograph
    0x28725F: (0x7F1B, 0),  # East Asian ideograph
    0x6F5B32: (0xD15C, 0),  # Korean hangul
    0x224959: (0x6DAB, 0),  # East Asian ideograph
    0x215C75: (0x9127, 0),  # East Asian ideograph
    0x6F5C76: (0xD589, 0),  # Korean hangul
    0x2D4228: (0x5117, 0),  # East Asian ideograph
    0x215C77: (
        0x9139,
        0,
    ),  # East Asian ideograph (variant of 4B5C77 which maps to 9139)
    0x455E60: (0x95EB, 0),  # East Asian ideograph (Version J extension)
    0x6F5C78: (0xD5A5, 0),  # Korean hangul
    0x235A22: (0x9D03, 0),  # East Asian ideograph
    0x2F3D5D: (0x900E, 0),  # East Asian ideograph
    0x6F5C79: (0xD5C8, 0),  # Korean hangul
    0x224724: (0x6C5C, 0),  # East Asian ideograph
    0x6F5C7A: (0xD5C9, 0),  # Korean hangul
    0x27613D: (0x9A8B, 0),  # East Asian ideograph
    0x2E4A6B: (0x6EA6, 0),  # East Asian ideograph
    0x224726: (0x6C5B, 0),  # East Asian ideograph
    0x275D55: (0x94C5, 0),  # East Asian ideograph
    0x292564: (0x8489, 0),  # East Asian ideograph
    0x224727: (0x6C4D, 0),  # East Asian ideograph
    0x225C7D: (0x7507, 0),  # East Asian ideograph
    0x22474D: (0x6C93, 0),  # East Asian ideograph
    0x235A23: (0x9CF7, 0),  # East Asian ideograph
    0x235C7E: (0x9DFD, 0),  # East Asian ideograph
    0x2D4729: (0x6D29, 0),  # East Asian ideograph
    0x213D57: (0x5F6D, 0),  # East Asian ideograph
    0x234D5A: (0x979F, 0),  # East Asian ideograph
    0x6F4C3C: (0xB1A8, 0),  # Korean hangul
    0x294532: (0x9531, 0),  # East Asian ideograph
    0x22472B: (0x6C4B, 0),  # East Asian ideograph
    0x3F4A28: (0x9DF0, 0),  # East Asian ideograph
    0x225A68: (0x7474, 0),  # East Asian ideograph
    0x6F7649: (0xE8BB, 0),  # Korean hangul
    0x6F5751: (0xC886, 0),  # Korean hangul
    0x22472D: (0x6C63, 0),  # East Asian ideograph
    0x6F5B35: (0xD160, 0),  # Korean hangul
    0x4B3D2A: (0x5EE3, 0),  # East Asian ideograph
    0x23472F: (0x93A9, 0),  # East Asian ideograph
    0x28773F: (0x804D, 0),  # East Asian ideograph
    0x232B21: (0x8761, 0),  # East Asian ideograph
    0x692535: (0x30B5, 0),  # Katakana letter SA
    0x222B24: (0x5FEA, 0),  # East Asian ideograph
    0x692566: (0x30E6, 0),  # Katakana letter YU
    0x212B26: (0x300D, 0),  # Ideographic right corner bracket
    0x225A69: (0x746E, 0),  # East Asian ideograph
    0x232B28: (0x875F, 0),  # East Asian ideograph
    0x222B2A: (0x6026, 0),  # East Asian ideograph
    0x222B2C: (0x6029, 0),  # East Asian ideograph
    0x232B2D: (0x876F, 0),  # East Asian ideograph
    0x232B2E: (0x875D, 0),  # East Asian ideograph
    0x232B30: (0x876E, 0),  # East Asian ideograph
    0x222B31: (0x6008, 0),  # East Asian ideograph
    0x212B32: (0xFF3D, 0),  # Ideographic right square bracket
    0x224733: (0x6C76, 0),  # East Asian ideograph
    0x212B34: (0xFF0E, 0),  # Ideographic variant full stop
    0x232B35: (0x8753, 0),  # East Asian ideograph
    0x222B36: (0x600A, 0),  # East Asian ideograph
    0x222B37: (0x600C, 0),  # East Asian ideograph
    0x234D5C: (0x979A, 0),  # East Asian ideograph
    0x214734: (0x6CBB, 0),  # East Asian ideograph
    0x232B3A: (0x87A3, 0),  # East Asian ideograph
    0x4B5E69: (0x95A2, 0),  # East Asian ideograph
    0x222B3C: (0x6017, 0),  # East Asian ideograph
    0x232B3D: (0x8793, 0),  # East Asian ideograph
    0x6F245F: (0x3148, 0),  # Korean hangul
    0x2D4735: (0x6C4E, 0),  # East Asian ideograph
    0x275D58: (0x94C3, 0),  # East Asian ideograph
    0x273B3F: (0x4E13, 0),  # East Asian ideograph
    0x692567: (0x30E7, 0),  # Katakana letter small YO
    0x213452: (0x5331, 0),  # East Asian ideograph
    0x232B45: (0x8799, 0),  # East Asian ideograph
    0x222B46: (0x6010, 0),  # East Asian ideograph
    0x232B48: (0x8788, 0),  # East Asian ideograph
    0x222B4B: (0x6039, 0),  # East Asian ideograph
    0x232B4C: (0x8798, 0),  # East Asian ideograph
    0x222B50: (0x6013, 0),  # East Asian ideograph
    0x224738: (0x6C6C, 0),  # East Asian ideograph
    0x222B53: (0x6054, 0),  # East Asian ideograph
    0x232B54: (0x878B, 0),  # East Asian ideograph
    0x232B55: (0x8784, 0),  # East Asian ideograph
    0x222B57: (0x605D, 0),  # East Asian ideograph
    0x232B58: (0x87A9, 0),  # East Asian ideograph
    0x336B33: (0x524F, 0),  # East Asian ideograph
    0x222B5A: (0x6047, 0),  # East Asian ideograph
    0x2E2B5B: (0x605A, 0),  # East Asian ideograph
    0x232B5D: (0x8789, 0),  # East Asian ideograph
    0x222B5E: (0x6049, 0),  # East Asian ideograph
    0x222B5F: (0x6053, 0),  # East Asian ideograph
    0x232B60: (0x87AD, 0),  # East Asian ideograph
    0x4B4E37: (0x7814, 0),  # East Asian ideograph
    0x23473B: (0x940F, 0),  # East Asian ideograph
    0x232B66: (0x87BE, 0),  # East Asian ideograph
    0x222B68: (0x6067, 0),  # East Asian ideograph
    0x23473C: (0x9420, 0),  # East Asian ideograph (not in Unicode)
    0x232B6E: (0x87C4, 0),  # East Asian ideograph
    0x232B6F: (0x87AF, 0),  # East Asian ideograph
    0x222B71: (0x6041, 0),  # East Asian ideograph
    0x222B72: (0x6077, 0),  # East Asian ideograph
    0x222B74: (0x6042, 0),  # East Asian ideograph
    0x22473E: (0x6C94, 0),  # East Asian ideograph
    0x222B76: (0x605F, 0),  # East Asian ideograph
    0x232B78: (0x87AE, 0),  # East Asian ideograph
    0x2E6C27: (0x7B2E, 0),  # East Asian ideograph
    0x222B7A: (0x6061, 0),  # East Asian ideograph
    0x6F4E6F: (0xB799, 0),  # Korean hangul
    0x232B7E: (0x87BF, 0),  # East Asian ideograph
    0x692569: (0x30E9, 0),  # Katakana letter RA
    0x224740: (0x6C8F, 0),  # East Asian ideograph
    0x333C52: (0x8CEC, 0),  # East Asian ideograph
    0x4B4741: (0x51BD, 0),  # East Asian ideograph
    0x23233C: (0x8452, 0),  # East Asian ideograph
    0x224742: (0x6C65, 0),  # East Asian ideograph
    0x213D58: (0x5F70, 0),  # East Asian ideograph
    0x2D5E61: (0x6FF6, 0),  # East Asian ideograph
    0x6F4C3D: (0xB1CC, 0),  # Korean hangul
    0x69256A: (0x30EA, 0),  # Katakana letter RI
    0x294340: (0x94D6, 0),  # East Asian ideograph
    0x6F5752: (0xC887, 0),  # Korean hangul
    0x4B4B3E: (0xF9AD, 0),  # East Asian ideograph
    0x2D4746: (0x6C79, 0),  # East Asian ideograph
    0x2D6147: (0x99C8, 0),  # East Asian ideograph
    0x224747: (0x6C6F, 0),  # East Asian ideograph
    0x705F39: (0x5416, 0),  # East Asian ideograph
    0x224749: (0x6C9D, 0),  # East Asian ideograph
    0x275D5C: (0x94DC, 0),  # East Asian ideograph
    0x295433: (0x9AA7, 0),  # East Asian ideograph
    0x2F4A2E: (0x90B4, 0),  # East Asian ideograph
    0x22474A: (0x6C69, 0),  # East Asian ideograph
    0x22474B: (0x6C9A, 0),  # East Asian ideograph
    0x21383B: (0x57F7, 0),  # East Asian ideograph
    0x22474C: (0x6C6D, 0),  # East Asian ideograph
    0x23474D: (0x9419, 0),  # East Asian ideograph
    0x275B47: (0x8F8D, 0),  # East Asian ideograph
    0x23474E: (0x940D, 0),  # East Asian ideograph
    0x275D5D: (0x94ED, 0),  # East Asian ideograph
    0x6F4A2F: (0xADFF, 0),  # Korean hangul
    0x234750: (0x9426, 0),  # East Asian ideograph
    0x6F5D4A: (0xD68C, 0),  # Korean hangul
    0x224751: (0x6C87, 0),  # East Asian ideograph
    0x39345B: (0x965E, 0),  # East Asian ideograph
    0x224752: (0x6C6E, 0),  # East Asian ideograph
    0x6F4E73: (0xB7A9, 0),  # Korean hangul
    0x69256D: (0x30ED, 0),  # Katakana letter RO
    0x4D4754: (0x9544, 0),  # East Asian ideograph
    0x294343: (0x94D2, 0),  # East Asian ideograph
    0x276D2E: (0x5326, 0),  # East Asian ideograph
    0x235A2C: (0x9CF8, 0),  # East Asian ideograph
    0x224756: (0x6C95, 0),  # East Asian ideograph
    0x234758: (0x9414, 0),  # East Asian ideograph
    0x275D5F: (0x94EC, 0),  # East Asian ideograph
    0x6F4A31: (0xAE01, 0),  # Korean hangul
    0x274759: (0x6CEA, 0),  # East Asian ideograph
    0x6F582D: (0xC9C8, 0),  # Korean hangul
    0x4C715A: (0x7EE6, 0),  # East Asian ideograph
    0x22475A: (0x6C82, 0),  # East Asian ideograph
    0x2D5340: (0x812C, 0),  # East Asian ideograph
    0x2D3B6E: (0x5D17, 0),  # East Asian ideograph
    0x232C24: (0x87BD, 0),  # East Asian ideograph
    0x23475C: (0x9422, 0),  # East Asian ideograph
    0x222C2B: (0x6092, 0),  # East Asian ideograph
    0x222C2C: (0x609D, 0),  # East Asian ideograph
    0x222C2D: (0x6081, 0),  # East Asian ideograph
    0x23475D: (0x9406, 0),  # East Asian ideograph
    0x232C30: (0x87F3, 0),  # East Asian ideograph
    0x232C31: (0x87F0, 0),  # East Asian ideograph
    0x222C32: (0x6097, 0),  # East Asian ideograph
    0x215673: (0x8725, 0),  # East Asian ideograph
    0x232C34: (0x87EA, 0),  # East Asian ideograph
    0x29475E: (0x9562, 0),  # East Asian ideograph
    0x232C36: (0x87DB, 0),  # East Asian ideograph
    0x232C37: (0x87E2, 0),  # East Asian ideograph
    0x232C39: (0x87EB, 0),  # East Asian ideograph
    0x222C3A: (0x6095, 0),  # East Asian ideograph
    0x2D475F: (0x51C4, 0),  # East Asian ideograph
    0x4D2C3C: (0x87E5, 0),  # East Asian ideograph
    0x222C3E: (0x60C7, 0),  # East Asian ideograph
    0x232C3F: (0x87F5, 0),  # East Asian ideograph
    0x217D48: (0x5B21, 0),  # East Asian ideograph
    0x234760: (0x9410, 0),  # East Asian ideograph
    0x222C42: (0x60B0, 0),  # East Asian ideograph
    0x6F4D33: (0xB36A, 0),  # Korean hangul
    0x222C46: (0x60BE, 0),  # East Asian ideograph
    0x232C47: (0x87E0, 0),  # East Asian ideograph
    0x222C48: (0x60D4, 0),  # East Asian ideograph
    0x232C49: (0x87DC, 0),  # East Asian ideograph
    0x232C4C: (0x87E3, 0),  # East Asian ideograph
    0x232C4D: (0x8801, 0),  # East Asian ideograph
    0x222C4E: (0x60CE, 0),  # East Asian ideograph
    0x232C4F: (0x8803, 0),  # East Asian ideograph
    0x232C50: (0x880A, 0),  # East Asian ideograph
    0x222C51: (0x60CF, 0),  # East Asian ideograph
    0x222C53: (0x60D9, 0),  # East Asian ideograph
    0x222C54: (0x60B3, 0),  # East Asian ideograph
    0x232C55: (0x87F6, 0),  # East Asian ideograph
    0x222C56: (0x60DD, 0),  # East Asian ideograph
    0x232C57: (0x87F7, 0),  # East Asian ideograph
    0x235A2F: (0x9D2A, 0),  # East Asian ideograph
    0x232C5C: (0x880B, 0),  # East Asian ideograph
    0x232C5D: (0x8806, 0),  # East Asian ideograph
    0x232C5F: (0x87FE, 0),  # East Asian ideograph
    0x222C60: (0x60B1, 0),  # East Asian ideograph
    0x232C61: (0x8810, 0),  # East Asian ideograph
    0x222C62: (0x60E3, 0),  # East Asian ideograph
    0x232C63: (0x8819, 0),  # East Asian ideograph
    0x232C64: (0x8811, 0),  # East Asian ideograph
    0x224766: (0x6CEF, 0),  # East Asian ideograph
    0x232C66: (0x8818, 0),  # East Asian ideograph
    0x222C67: (0x60E5, 0),  # East Asian ideograph
    0x222C69: (0x60DB, 0),  # East Asian ideograph
    0x232C6A: (0x8813, 0),  # East Asian ideograph
    0x232C6B: (0x8816, 0),  # East Asian ideograph
    0x6F5236: (0xBEE0, 0),  # Korean hangul
    0x275D62: (0x950C, 0),  # East Asian ideograph
    0x222C6E: (0x60E9, 0),  # East Asian ideograph
    0x692571: (0x30F1, 0),  # Katakana letter WE
    0x222C70: (0x6114, 0),  # East Asian ideograph
    0x274768: (0x6D45, 0),  # East Asian ideograph
    0x232C72: (0x8834, 0),  # East Asian ideograph
    0x232C73: (0x881C, 0),  # East Asian ideograph
    0x222C75: (0x6119, 0),  # East Asian ideograph
    0x234769: (0x93F7, 0),  # East Asian ideograph
    0x232C7A: (0x881B, 0),  # East Asian ideograph
    0x222C7C: (0x60FD, 0),  # East Asian ideograph
    0x222C7D: (0x610D, 0),  # East Asian ideograph
    0x6F5B41: (0xD1F4, 0),  # Korean hangul
    0x29323B: (0x8BCE, 0),  # East Asian ideograph
    0x287042: (0x7EA1, 0),  # East Asian ideograph
    0x4B476C: (0x51C5, 0),  # East Asian ideograph
    0x275D63: (0x9511, 0),  # East Asian ideograph
    0x6F4A35: (0xAE0D, 0),  # Korean hangul
    0x223E61: (0x6971, 0),  # East Asian ideograph
    0x22476E: (
        0x6CAD,
        0,
    ),  # East Asian ideograph (variant of 4C476E which maps to 6CAD)
    0x2D5344: (0x8107, 0),  # East Asian ideograph
    0x23476F: (0x940E, 0),  # East Asian ideograph
    0x6F5B2E: (0xD14C, 0),  # Korean hangul
    0x29323C: (0x8BD2, 0),  # East Asian ideograph
    0x6F4E39: (0xB5B5, 0),  # Korean hangul
    0x224770: (0x6CAF, 0),  # East Asian ideograph
    0x295925: (0x9CCC, 0),  # East Asian ideograph
    0x234771: (0x9411, 0),  # East Asian ideograph
    0x692573: (0x30F3, 0),  # Katakana letter N
    0x275921: (0x8C04, 0),  # East Asian ideograph
    0x294349: (0x94D5, 0),  # East Asian ideograph
    0x2D386E: (0x58CA, 0),  # East Asian ideograph
    0x217E23: (0x5B62, 0),  # East Asian ideograph
    0x274774: (0x6E0A, 0),  # East Asian ideograph
    0x6F5B43: (0xD22C, 0),  # Korean hangul
    0x275551: (0x80E1, 0),  # East Asian ideograph (duplicate simplified)
    0x22496A: (0x6DAC, 0),  # East Asian ideograph
    0x6F5B3E: (0xD1B3, 0),  # Korean hangul
    0x225265: (0x7168, 0),  # East Asian ideograph
    0x2D467C: (0x6CB2, 0),  # East Asian ideograph
    0x29464A: (0x953C, 0),  # East Asian ideograph
    0x3F3E47: (0x5379, 0),  # East Asian ideograph
    0x21345F: (0x5352, 0),  # East Asian ideograph
    0x274777: (0x6CA6, 0),  # East Asian ideograph
    0x2D6159: (0x9AC4, 0),  # East Asian ideograph
    0x213223: (0x5021, 0),  # East Asian ideograph
    0x234779: (0x9429, 0),  # East Asian ideograph
    0x213224: (0x500B, 0),  # East Asian ideograph
    0x695457: (0x58B8, 0),  # East Asian ideograph
    0x22477A: (0x6CBA, 0),  # East Asian ideograph
    0x223225: (0x6387, 0),  # East Asian ideograph
    0x22477B: (0x7553, 0),  # East Asian ideograph
    0x223226: (0x637A, 0),  # East Asian ideograph
    0x6F4B65: (0xB0C5, 0),  # Korean hangul
    0x6F4A38: (0xAE34, 0),  # Korean hangul
    0x213460: (0x5354, 0),  # East Asian ideograph
    0x233227: (0x8A51, 0),  # East Asian ideograph
    0x27477D: (0x6D8C, 0),  # East Asian ideograph
    0x213228: (0x4FF3, 0),  # East Asian ideograph
    0x6F5330: (0xC136, 0),  # Korean hangul
    0x3F3D6F: (0x8986, 0),  # East Asian ideograph
    0x287272: (0x7F21, 0),  # East Asian ideograph
    0x6F4C44: (0xB205, 0),  # Korean hangul
    0x213229: (0x502D, 0),  # East Asian ideograph
    0x28742E: (0x7F42, 0),  # East Asian ideograph
    0x6F4F3F: (0xB871, 0),  # Korean hangul
    0x22322A: (0x6386, 0),  # East Asian ideograph
    0x4C5C61: (
        0x74F4,
        0,
    ),  # East Asian ideograph (variant of 225C61 which maps to 74F4)
    0x6F4E7C: (0xB7F0, 0),  # Korean hangul
    0x6F5237: (0xBEE3, 0),  # Korean hangul
    0x21722B: (0x55F9, 0),  # East Asian ideograph
    0x692576: (0x30F6, 0),  # Katakana letter small KE
    0x223860: (0x6673, 0),  # East Asian ideograph
    0x21322D: (0x502B, 0),  # East Asian ideograph
    0x6F5D4C: (0xD69F, 0),  # Korean hangul
    0x6F5B46: (0xD234, 0),  # Korean hangul
    0x21322E: (0x505C, 0),  # East Asian ideograph
    0x22496D: (0x6DD5, 0),  # East Asian ideograph
    0x232B53: (0x8785, 0),  # East Asian ideograph
    0x21322F: (0x504F, 0),  # East Asian ideograph
    0x225F2F: (0x760F, 0),  # East Asian ideograph
    0x292657: (0x835F, 0),  # East Asian ideograph
    0x233230: (0x8A56, 0),  # East Asian ideograph
    0x232D23: (0x8828, 0),  # East Asian ideograph
    0x217231: (0x560C, 0),  # East Asian ideograph
    0x232D2A: (0x8832, 0),  # East Asian ideograph
    0x222D2C: (0x6110, 0),  # East Asian ideograph
    0x232D2E: (0x882E, 0),  # East Asian ideograph
    0x213E35: (0x600E, 0),  # East Asian ideograph
    0x232D32: (0x882D, 0),  # East Asian ideograph
    0x213233: (0x5049, 0),  # East Asian ideograph
    0x222D34: (0x60F2, 0),  # East Asian ideograph
    0x222D37: (0x6125, 0),  # East Asian ideograph
    0x277234: (0x551B, 0),  # East Asian ideograph
    0x222D3B: (0x60F8, 0),  # East Asian ideograph
    0x232D3C: (0x883C, 0),  # East Asian ideograph
    0x6F4E7E: (0xB7FC, 0),  # Korean hangul
    0x273235: (0x4FA7, 0),  # East Asian ideograph
    0x222D41: (0x60FC, 0),  # East Asian ideograph
    0x232D42: (0x4610, 0),  # East Asian ideograph (not in Unicode)
    0x275926: (0x8C1A, 0),  # East Asian ideograph
    0x232D44: (0x8844, 0),  # East Asian ideograph
    0x227236: (0x7DF9, 0),  # East Asian ideograph
    0x222D48: (0x6149, 0),  # East Asian ideograph
    0x222D4A: (0x614A, 0),  # East Asian ideograph
    0x232D4B: (0x8847, 0),  # East Asian ideograph
    0x222D4E: (0x612B, 0),  # East Asian ideograph
    0x287275: (0x7D77, 0),  # East Asian ideograph
    0x222D50: (0x6129, 0),  # East Asian ideograph
    0x222D51: (0x6150, 0),  # East Asian ideograph
    0x232D53: (0x884E, 0),  # East Asian ideograph
    0x232D56: (0x8852, 0),  # East Asian ideograph
    0x233239: (0x8A48, 0),  # East Asian ideograph
    0x222D58: (0x6130, 0),  # East Asian ideograph
    0x232D59: (0x8856, 0),  # East Asian ideograph
    0x232D5A: (0x8855, 0),  # East Asian ideograph
    0x222D5B: (0x6141, 0),  # East Asian ideograph
    0x21323A: (0x5055, 0),  # East Asian ideograph
    0x232D5E: (0x885C, 0),  # East Asian ideograph
    0x232D5F: (0x885A, 0),  # East Asian ideograph
    0x222D61: (0x6146, 0),  # East Asian ideograph
    0x22323B: (0x6390, 0),  # East Asian ideograph
    0x222D66: (0x615E, 0),  # East Asian ideograph
    0x222D67: (0x6175, 0),  # East Asian ideograph
    0x222D68: (0x6174, 0),  # East Asian ideograph
    0x232D69: (0x8869, 0),  # East Asian ideograph
    0x21316C: (0x5009, 0),  # East Asian ideograph
    0x222D6B: (0x6183, 0),  # East Asian ideograph
    0x232D6D: (0x886D, 0),  # East Asian ideograph
    0x232D6E: (0x887A, 0),  # East Asian ideograph
    0x21323D: (0x508D, 0),  # East Asian ideograph
    0x222D70: (0x6171, 0),  # East Asian ideograph
    0x232D71: (0x8875, 0),  # East Asian ideograph
    0x222757: (0x5E5E, 0),  # East Asian ideograph
    0x222D74: (0x616A, 0),  # East Asian ideograph
    0x232D75: (0x8872, 0),  # East Asian ideograph
    0x6F5045: (0xBB0F, 0),  # Korean hangul
    0x222D77: (0x6173, 0),  # East Asian ideograph
    0x232D79: (0x887D, 0),  # East Asian ideograph
    0x455564: (0x6FDB, 0),  # East Asian ideograph (Version J extension)
    0x222D7B: (0x6153, 0),  # East Asian ideograph
    0x224234: (0x6A99, 0),  # East Asian ideograph
    0x232D7D: (0x887F, 0),  # East Asian ideograph
    0x232D7E: (0x887E, 0),  # East Asian ideograph
    0x275928: (0x8BB3, 0),  # East Asian ideograph
    0x294350: (0x94DF, 0),  # East Asian ideograph
    0x233240: (0x8A3D, 0),  # East Asian ideograph
    0x696126: (0x74F2, 0),  # East Asian ideograph
    0x6F567B: (0xC794, 0),  # Korean hangul
    0x273241: (0x6770, 0),  # East Asian ideograph
    0x6F5874: (0xCC0D, 0),  # Korean hangul
    0x6F5B4A: (0xD241, 0),  # Korean hangul
    0x213242: (0x5080, 0),  # East Asian ideograph
    0x4B5C5B: (0x8FBA, 0),  # East Asian ideograph
    0x223243: (0x63DE, 0),  # East Asian ideograph
    0x6F5238: (0xBEE4, 0),  # Korean hangul
    0x213244: (0x5098, 0),  # East Asian ideograph
    0x6F4A3E: (0xAE44, 0),  # Korean hangul
    0x275929: (0x8C10, 0),  # East Asian ideograph
    0x2D4539: (0x6406, 0),  # East Asian ideograph
    0x213246: (0x50B3, 0),  # East Asian ideograph
    0x274C60: (0x75A1, 0),  # East Asian ideograph
    0x6F5B4B: (0xD264, 0),  # Korean hangul
    0x273247: (0x503A, 0),  # East Asian ideograph
    0x227248: (0x7DF6, 0),  # East Asian ideograph
    0x23492E: (0x9585, 0),  # East Asian ideograph
    0x213249: (0x50C5, 0),  # East Asian ideograph
    0x6F4A3F: (0xAE45, 0),  # Korean hangul
    0x27592A: (0x8C0D, 0),  # East Asian ideograph
    0x223866: (0x666D, 0),  # East Asian ideograph
    0x21724B: (0x564B, 0),  # East Asian ideograph
    0x274C61: (0x759F, 0),  # East Asian ideograph
    0x6F5B4C: (0xD277, 0),  # Korean hangul
    0x21324C: (0x50B7, 0),  # East Asian ideograph
    0x393246: (0x4F1D, 0),  # East Asian ideograph
    0x21324D: (0x50AF, 0),  # East Asian ideograph
    0x275D6E: (0x9530, 0),  # East Asian ideograph
    0x6F4A40: (0xAE4A, 0),  # Korean hangul
    0x27592B: (0x8C0B, 0),  # East Asian ideograph
    0x6F5830: (0xC9D1, 0),  # Korean hangul
    0x21324F: (0x50EE, 0),  # East Asian ideograph
    0x213250: (0x50F1, 0),  # East Asian ideograph
    0x274C62: (0x75EA, 0),  # East Asian ideograph
    0x333963: (0x59C9, 0),  # East Asian ideograph
    0x213251: (0x50E5, 0),  # East Asian ideograph
    0x217252: (0x5640, 0),  # East Asian ideograph
    0x292433: (0x8298, 0),  # East Asian ideograph (duplicate simplified)
    0x69515E: (0x51E9, 0),  # East Asian ideograph
    0x287253: (0x7F12, 0),  # East Asian ideograph
    0x6F575A: (0xC89F, 0),  # Korean hangul
    0x223B63: (0x67D8, 0),  # East Asian ideograph
    0x213255: (0x50D5, 0),  # East Asian ideograph
    0x274C63: (0x75AF, 0),  # East Asian ideograph
    0x4C523A: (0x717A, 0),  # East Asian ideograph
    0x213256: (0x507D, 0),  # East Asian ideograph
    0x234D74: (0x97AB, 0),  # East Asian ideograph
    0x22674B: (0x798A, 0),  # East Asian ideograph
    0x213257: (0x50CF, 0),  # East Asian ideograph
    0x234931: (0x958C, 0),  # East Asian ideograph
    0x213258: (0x50D1, 0),  # East Asian ideograph
    0x224235: (0x6A9D, 0),  # East Asian ideograph
    0x27592D: (0x8C13, 0),  # East Asian ideograph
    0x294355: (0x94EB, 0),  # East Asian ideograph
    0x273259: (0x4EEA, 0),  # East Asian ideograph
    0x6F567C: (0xC796, 0),  # Korean hangul
    0x21325A: (0x5104, 0),  # East Asian ideograph
    0x6F5B4F: (0xD288, 0),  # Korean hangul
    0x222E23: (0x618B, 0),  # East Asian ideograph
    0x2D5129: (0x7D25, 0),  # East Asian ideograph
    0x232E28: (0x88A2, 0),  # East Asian ideograph
    0x21325C: (0x50F5, 0),  # East Asian ideograph
    0x232E2A: (0x88A4, 0),  # East Asian ideograph
    0x222E2C: (0x616F, 0),  # East Asian ideograph
    0x222E2D: (0x6165, 0),  # East Asian ideograph
    0x6F5239: (0xBEE5, 0),  # Korean hangul
    0x232E2F: (0x88AA, 0),  # East Asian ideograph
    0x276135: (0x9A7E, 0),  # East Asian ideograph
    0x222E32: (0x619D, 0),  # East Asian ideograph
    0x222E33: (0x61A6, 0),  # East Asian ideograph
    0x232E34: (0x889A, 0),  # East Asian ideograph
    0x27325E: (0x4FAC, 0),  # East Asian ideograph
    0x235A3F: (0x9D1E, 0),  # East Asian ideograph
    0x232E3A: (0x8890, 0),  # East Asian ideograph
    0x232E3B: (0x888C, 0),  # East Asian ideograph
    0x232E3D: (0x88A0, 0),  # East Asian ideograph
    0x232E40: (0x8899, 0),  # East Asian ideograph
    0x213260: (0x5108, 0),  # East Asian ideograph
    0x222E42: (0x619C, 0),  # East Asian ideograph
    0x222E43: (0x61AF, 0),  # East Asian ideograph
    0x232E45: (0x8897, 0),  # East Asian ideograph
    0x222E46: (0x6197, 0),  # East Asian ideograph
    0x222E47: (0x61AD, 0),  # East Asian ideograph
    0x232E48: (0x88C9, 0),  # East Asian ideograph
    0x232E49: (0x88BF, 0),  # East Asian ideograph
    0x232E4A: (0x88BA, 0),  # East Asian ideograph
    0x222E4C: (0x6192, 0),  # East Asian ideograph
    0x213262: (0x5110, 0),  # East Asian ideograph
    0x232E4F: (0x88C0, 0),  # East Asian ideograph
    0x6F4A44: (0xAE4D, 0),  # Korean hangul
    0x232E51: (0x88B2, 0),  # East Asian ideograph
    0x222E52: (0x61AE, 0),  # East Asian ideograph
    0x213263: (0x5118, 0),  # East Asian ideograph
    0x232E54: (0x88BC, 0),  # East Asian ideograph
    0x222E55: (0x618D, 0),  # East Asian ideograph
    0x232E57: (0x88B7, 0),  # East Asian ideograph
    0x232E59: (0x88BD, 0),  # East Asian ideograph
    0x232E5A: (0x88C4, 0),  # East Asian ideograph
    0x2D313A: (0x62BB, 0),  # East Asian ideograph
    0x222E5C: (0x61CC, 0),  # East Asian ideograph
    0x222E5D: (0x61C6, 0),  # East Asian ideograph
    0x232E5E: (0x88CB, 0),  # East Asian ideograph
    0x213265: (0x5114, 0),  # East Asian ideograph
    0x232E60: (0x88CC, 0),  # East Asian ideograph
    0x232E62: (0x88DB, 0),  # East Asian ideograph
    0x232E64: (0x88CE, 0),  # East Asian ideograph
    0x224535: (0x6BA3, 0),  # East Asian ideograph
    0x234934: (0x9597, 0),  # East Asian ideograph
    0x222E68: (0x61BA, 0),  # East Asian ideograph
    0x222E6A: (0x61B8, 0),  # East Asian ideograph
    0x273267: (0x507F, 0),  # East Asian ideograph
    0x6F4A45: (0xAE4E, 0),  # Korean hangul
    0x275930: (0x8C15, 0),  # East Asian ideograph
    0x294358: (0x94EF, 0),  # East Asian ideograph
    0x232E71: (0x88F1, 0),  # East Asian ideograph
    0x232E72: (0x88FE, 0),  # East Asian ideograph
    0x6F5D66: (0xD734, 0),  # Korean hangul
    0x232E75: (0x88F2, 0),  # East Asian ideograph
    0x233269: (0x8A8F, 0),  # East Asian ideograph
    0x232E78: (0x8900, 0),  # East Asian ideograph
    0x213F2E: (0x6176, 0),  # East Asian ideograph
    0x232E7A: (0x88F0, 0),  # East Asian ideograph
    0x6F5B52: (0xD293, 0),  # Korean hangul
    0x222E7D: (0x61DC, 0),  # East Asian ideograph
    0x222E7E: (0x61DF, 0),  # East Asian ideograph
    0x69723B: (0x9B96, 0),  # East Asian ideograph
    0x21326B: (0x513C, 0),  # East Asian ideograph
    0x276069: (0x996A, 0),  # East Asian ideograph
    0x294359: (0x94E5, 0),  # East Asian ideograph
    0x4B5434: (0x6319, 0),  # East Asian ideograph
    0x6F5B53: (0xD295, 0),  # Korean hangul
    0x21326F: (0x5145, 0),  # East Asian ideograph
    0x223270: (0x63BE, 0),  # East Asian ideograph
    0x234936: (0x958E, 0),  # East Asian ideograph
    0x2D4249: (0x53D9, 0),  # East Asian ideograph
    0x213271: (0x5146, 0),  # East Asian ideograph
    0x224236: (0x6A7E, 0),  # East Asian ideograph
    0x6F4A47: (0xAE54, 0),  # Korean hangul
    0x275932: (0x8C26, 0),  # East Asian ideograph
    0x217272: (0x5660, 0),  # East Asian ideograph
    0x295834: (0x9CBB, 0),  # East Asian ideograph
    0x223273: (0x63DD, 0),  # East Asian ideograph
    0x6F5B54: (0xD29C, 0),  # Korean hangul
    0x22497B: (0x6DBF, 0),  # East Asian ideograph
    0x213275: (0x514C, 0),  # East Asian ideograph
    0x6F523A: (0xBEEC, 0),  # Korean hangul
    0x2D3A26: (0x5A3F, 0),  # East Asian ideograph
    0x6F5D21: (0xD5D9, 0),  # Korean hangul
    0x283F5C: (0x6769, 0),  # East Asian ideograph
    0x29435B: (0x94E3, 0),  # East Asian ideograph
    0x213277: (0x514D, 0),  # East Asian ideograph
    0x6F5D22: (0xD5DB, 0),  # Korean hangul
    0x2D5D23: (0x9167, 0),  # East Asian ideograph
    0x274C6A: (0x75AE, 0),  # East Asian ideograph
    0x6F4C2E: (0xB158, 0),  # Korean hangul
    0x213279: (0x5154, 0),  # East Asian ideograph
    0x705F54: (0x54B4, 0),  # East Asian ideograph
    0x6F5D24: (0xD5E4, 0),  # Korean hangul
    0x29324F: (0x8BD6, 0),  # East Asian ideograph
    0x393460: (0x604A, 0),  # East Asian ideograph
    0x273859: (0x5C18, 0),  # East Asian ideograph
    0x225D25: (0x750E, 0),  # East Asian ideograph
    0x21327B: (0x5157, 0),  # East Asian ideograph
    0x6F5D26: (0xD5E8, 0),  # Korean hangul
    0x275934: (0x8BB2, 0),  # East Asian ideograph
    0x223870: (0x6684, 0),  # East Asian ideograph
    0x235D27: (0x9E0E, 0),  # East Asian ideograph
    0x6F577C: (0xC961, 0),  # Korean hangul
    0x21327D: (0x5162, 0),  # East Asian ideograph
    0x225D28: (0x750D, 0),  # East Asian ideograph
    0x213E38: (0x6059, 0),  # East Asian ideograph
    0x23327E: (0x8AB6, 0),  # East Asian ideograph
    0x295D29: (0x9E71, 0),  # East Asian ideograph
    0x293250: (0x8BD3, 0),  # East Asian ideograph
    0x275D2A: (0x9154, 0),  # East Asian ideograph
    0x235D2B: (0x9E11, 0),  # East Asian ideograph
    0x2F4A4A: (0x5F8F, 0),  # East Asian ideograph
    0x275935: (0x8C0E, 0),  # East Asian ideograph
    0x225D2C: (0x7511, 0),  # East Asian ideograph
    0x225D2D: (0x750F, 0),  # East Asian ideograph
    0x2D3140: (0x4F32, 0),  # East Asian ideograph
    0x6F5B57: (0xD2AC, 0),  # Korean hangul
    0x6F5D2E: (0xD604, 0),  # Korean hangul
    0x215D2F: (0x919E, 0),  # East Asian ideograph
    0x275D79: (0x952E, 0),  # East Asian ideograph
    0x275D30: (0x4E11, 0),  # East Asian ideograph
    0x6F4A4B: (0xAE61, 0),  # Korean hangul
    0x232F23: (0x88EF, 0),  # East Asian ideograph
    0x232F24: (0x8903, 0),  # East Asian ideograph
    0x39456D: (0x826B, 0),  # East Asian ideograph
    0x6F5758: (0xC89C, 0),  # Korean hangul
    0x215D31: (0x91AB, 0),  # East Asian ideograph
    0x225648: (0x72A8, 0),  # East Asian ideograph
    0x222F29: (0x61F3, 0),  # East Asian ideograph
    0x275D32: (0x9171, 0),  # East Asian ideograph
    0x274C6D: (0x75E8, 0),  # East Asian ideograph
    0x212F30: (0x3007, 0),  # East Asian ideograph (number zero)
    0x225D33: (0x7513, 0),  # East Asian ideograph
    0x232F35: (0x8906, 0),  # East Asian ideograph
    0x232F36: (0x890C, 0),  # East Asian ideograph
    0x232F37: (0x8919, 0),  # East Asian ideograph
    0x215D34: (0x91C0, 0),  # East Asian ideograph
    0x232F3D: (0x890A, 0),  # East Asian ideograph
    0x6F4B69: (0xB0D0, 0),  # Korean hangul
    0x215D35: (0x91C1, 0),  # East Asian ideograph
    0x6F4A4C: (0xAE62, 0),  # Korean hangul
    0x222F41: (0x6204, 0),  # East Asian ideograph
    0x235742: (0x9B9E, 0),  # East Asian ideograph
    0x222F43: (0x6207, 0),  # East Asian ideograph
    0x222F44: (0x6209, 0),  # East Asian ideograph
    0x232F45: (0x892F, 0),  # East Asian ideograph
    0x232F47: (0x8930, 0),  # East Asian ideograph
    0x345E47: (0x75FE, 0),  # East Asian ideograph
    0x235D37: (0x9E18, 0),  # East Asian ideograph
    0x274C6E: (0x7597, 0),  # East Asian ideograph
    0x232F4E: (0x8921, 0),  # East Asian ideograph
    0x232F4F: (0x8927, 0),  # East Asian ideograph
    0x232F51: (0x891F, 0),  # East Asian ideograph
    0x232F53: (0x8931, 0),  # East Asian ideograph
    0x232F54: (0x891E, 0),  # East Asian ideograph
    0x295029: (0x98A5, 0),  # East Asian ideograph
    0x232F56: (0x8926, 0),  # East Asian ideograph
    0x232F57: (0x8922, 0),  # East Asian ideograph
    0x232F5A: (0x8935, 0),  # East Asian ideograph
    0x222F5B: (0x6225, 0),  # East Asian ideograph
    0x232F5D: (0x8941, 0),  # East Asian ideograph
    0x275938: (0x8C22, 0),  # East Asian ideograph
    0x232F60: (0x8933, 0),  # East Asian ideograph
    0x222F61: (0x6229, 0),  # East Asian ideograph
    0x235D3B: (0x9E1D, 0),  # East Asian ideograph
    0x232F66: (0x8954, 0),  # East Asian ideograph
    0x222F67: (0x622D, 0),  # East Asian ideograph
    0x6F5D50: (0xD6C5, 0),  # Korean hangul
    0x215D3C: (0x91CF, 0),  # East Asian ideograph
    0x6F5B5A: (0xD2B9, 0),  # Korean hangul
    0x222F6E: (0x6239, 0),  # East Asian ideograph
    0x222F6F: (0x623A, 0),  # East Asian ideograph
    0x222F70: (0x623D, 0),  # East Asian ideograph
    0x232F72: (0x8947, 0),  # East Asian ideograph
    0x27385A: (0x57AB, 0),  # East Asian ideograph
    0x222F75: (0x6243, 0),  # East Asian ideograph
    0x222F77: (0x6246, 0),  # East Asian ideograph
    0x222F78: (0x6245, 0),  # East Asian ideograph
    0x222F79: (0x624A, 0),  # East Asian ideograph
    0x232F7A: (0x894C, 0),  # East Asian ideograph
    0x232F7B: (0x8946, 0),  # East Asian ideograph
    0x222F7C: (0x625E, 0),  # East Asian ideograph
    0x295859: (0x9CC6, 0),  # East Asian ideograph
    0x275D40: (0x9489, 0),  # East Asian ideograph
    0x275D41: (0x948A, 0),  # East Asian ideograph
    0x6F5B5B: (0xD2BC, 0),  # Korean hangul
    0x215D42: (0x91DC, 0),  # East Asian ideograph
    0x6F4E3A: (0xB5BB, 0),  # Korean hangul
    0x275D43: (0x9497, 0),  # East Asian ideograph
    0x45604E: (0x984F, 0),  # East Asian ideograph
    0x215D44: (0x91E6, 0),  # East Asian ideograph
    0x6F4A4F: (0xAE69, 0),  # Korean hangul
    0x27593A: (0x8C2C, 0),  # East Asian ideograph
    0x273721: (0x545C, 0),  # East Asian ideograph
    0x275D45: (0x9493, 0),  # East Asian ideograph
    0x2D535E: (0x8193, 0),  # East Asian ideograph
    0x275D46: (0x948F, 0),  # East Asian ideograph
    0x33632B: (0x7ADC, 0),  # East Asian ideograph
    0x6F5B5C: (0xD2BF, 0),  # Korean hangul
    0x705F5B: (0x54A3, 0),  # East Asian ideograph
    0x215D47: (0x9223, 0),  # East Asian ideograph
    0x293256: (0x8BE9, 0),  # East Asian ideograph
    0x2E493B: (0x6E7C, 0),  # East Asian ideograph
    0x275D48: (0x949D, 0),  # East Asian ideograph
    0x4B4921: (0x6CA2, 0),  # East Asian ideograph
    0x235D49: (0x9E84, 0),  # East Asian ideograph
    0x27606B: (0x996D, 0),  # East Asian ideograph
    0x27593B: (0x8C1F, 0),  # East Asian ideograph
    0x6F5759: (0xC89D, 0),  # Korean hangul
    0x275D4A: (0x94A0, 0),  # East Asian ideograph
    0x215D4B: (0x9214, 0),  # East Asian ideograph
    0x6F5B5D: (0xD2C0, 0),  # Korean hangul
    0x275D4C: (0x94A7, 0),  # East Asian ideograph
    0x284C2E: (0x6D52, 0),  # East Asian ideograph
    0x697246: (0x9BD1, 0),  # East Asian ideograph
    0x275D4D: (0x94A4, 0),  # East Asian ideograph
    0x2D3356: (0x5211, 0),  # East Asian ideograph (not in Unicode)
    0x6F4B6A: (0xB0D1, 0),  # Korean hangul
    0x6F5D4E: (0xD6A8, 0),  # Korean hangul
    0x6F4A51: (0xAE70, 0),  # Korean hangul
    0x27593C: (0x8BC6, 0),  # East Asian ideograph
    0x294364: (0x94F7, 0),  # East Asian ideograph
    0x233C77: (0x8FCB, 0),  # East Asian ideograph
    0x213A38: (0x5AC2, 0),  # East Asian ideograph
    0x275D50: (0x94B9, 0),  # East Asian ideograph
    0x2D3147: (0x5002, 0),  # East Asian ideograph
    0x6F5B5E: (0xD2C8, 0),  # Korean hangul
    0x215D51: (0x923D, 0),  # East Asian ideograph
    0x396074: (0x55B0, 0),  # East Asian ideograph
    0x215D52: (0x923E, 0),  # East Asian ideograph
    0x6F523C: (0xBF09, 0),  # Korean hangul
    0x275D53: (0x94BE, 0),  # East Asian ideograph
    0x21347A: (0x53AD, 0),  # East Asian ideograph
    0x213037: (0x4E38, 0),  # East Asian ideograph
    0x4B4B63: (0x749C, 0),  # East Asian ideograph
    0x215D55: (0x925B, 0),  # East Asian ideograph
    0x6F5B5F: (0xD2C9, 0),  # Korean hangul
    0x275D56: (0x94A9, 0),  # East Asian ideograph
    0x22675C: (0x799A, 0),  # East Asian ideograph
    0x275D57: (0x94C2, 0),  # East Asian ideograph
    0x234942: (0x95AC, 0),  # East Asian ideograph
    0x225D58: (0x7547, 0),  # East Asian ideograph
    0x6F4A53: (0xAE79, 0),  # Korean hangul
    0x224830: (0x6CD1, 0),  # East Asian ideograph
    0x275D59: (0x94F0, 0),  # East Asian ideograph
    0x235A4F: (0x9D41, 0),  # East Asian ideograph
    0x275D5A: (0x94F6, 0),  # East Asian ideograph
    0x274C75: (0x765E, 0),  # East Asian ideograph
    0x213021: (0x4E00, 0),  # East Asian ideograph
    0x213022: (0x4E01, 0),  # East Asian ideograph
    0x215D5B: (0x92AC, 0),  # East Asian ideograph
    0x213024: (0x4E09, 0),  # East Asian ideograph
    0x213025: (0x4E0B, 0),  # East Asian ideograph
    0x223026: (0x6268, 0),  # East Asian ideograph
    0x213027: (0x4E08, 0),  # East Asian ideograph
    0x223028: (0x6260, 0),  # East Asian ideograph
    0x233029: (0x895B, 0),  # East Asian ideograph
    0x21302A: (0x4E0D, 0),  # East Asian ideograph
    0x21302B: (0x4E14, 0),  # East Asian ideograph
    0x22302C: (0x6262, 0),  # East Asian ideograph
    0x21302D: (0x4E16, 0),  # East Asian ideograph
    0x21302E: (0x4E15, 0),  # East Asian ideograph
    0x215D5D: (0x9298, 0),  # East Asian ideograph
    0x213030: (0x4E22, 0),  # East Asian ideograph
    0x233031: (0x8966, 0),  # East Asian ideograph
    0x223032: (0x628E, 0),  # East Asian ideograph
    0x213034: (0x4E2D, 0),  # East Asian ideograph
    0x275D5E: (0x94E2, 0),  # East Asian ideograph
    0x213036: (0x51E1, 0),  # East Asian ideograph
    0x233037: (0x896D, 0),  # East Asian ideograph
    0x213038: (0x4E39, 0),  # East Asian ideograph
    0x213039: (0x4E3B, 0),  # East Asian ideograph
    0x23303A: (0x896B, 0),  # East Asian ideograph
    0x23303B: (0x896E, 0),  # East Asian ideograph
    0x23303C: (0x896C, 0),  # East Asian ideograph
    0x21303D: (0x4E4B, 0),  # East Asian ideograph
    0x21303E: (0x5C39, 0),  # East Asian ideograph
    0x21303F: (0x4E4F, 0),  # East Asian ideograph
    0x213040: (0x4E4E, 0),  # East Asian ideograph
    0x233041: (0x8976, 0),  # East Asian ideograph
    0x233042: (0x8974, 0),  # East Asian ideograph
    0x223043: (0x6282, 0),  # East Asian ideograph
    0x213044: (0x4E56, 0),  # East Asian ideograph
    0x213045: (0x4E58, 0),  # East Asian ideograph
    0x213046: (0x4E59, 0),  # East Asian ideograph
    0x215D61: (0x929C, 0),  # East Asian ideograph
    0x213048: (0x4E5F, 0),  # East Asian ideograph
    0x233049: (0x897B, 0),  # East Asian ideograph
    0x23304A: (0x897C, 0),  # East Asian ideograph
    0x22304B: (0x629D, 0),  # East Asian ideograph
    0x27304C: (0x5E72, 0),  # East Asian ideograph
    0x225D62: (0x7564, 0),  # East Asian ideograph
    0x6F4A55: (0xAE7C, 0),  # Korean hangul
    0x213050: (0x4E8B, 0),  # East Asian ideograph
    0x213051: (0x4E8C, 0),  # East Asian ideograph
    0x213052: (0x4E8E, 0),  # East Asian ideograph
    0x233053: (0x8984, 0),  # East Asian ideograph
    0x213054: (0x4E94, 0),  # East Asian ideograph
    0x233055: (0x8985, 0),  # East Asian ideograph
    0x223056: (0x62A6, 0),  # East Asian ideograph
    0x213057: (
        0x4E99,
        0,
    ),  # East Asian ideograph (variant of 4B3057 which maps to 4E99)
    0x273058: (0x4E9A, 0),  # East Asian ideograph
    0x215D64: (0x92B3, 0),  # East Asian ideograph
    0x21305A: (0x4E9F, 0),  # East Asian ideograph
    0x274C77: (0x7663, 0),  # East Asian ideograph
    0x21305C: (0x4EA6, 0),  # East Asian ideograph
    0x21305D: (0x4EA5, 0),  # East Asian ideograph
    0x21305E: (0x4EA4, 0),  # East Asian ideograph
    0x215D65: (0x92EA, 0),  # East Asian ideograph
    0x213060: (0x4EAB, 0),  # East Asian ideograph
    0x213061: (0x4EAC, 0),  # East Asian ideograph
    0x233062: (0x8991, 0),  # East Asian ideograph
    0x213063: (0x4EAE, 0),  # East Asian ideograph
    0x233064: (0x8997, 0),  # East Asian ideograph
    0x215D66: (0x92B7, 0),  # East Asian ideograph
    0x233066: (0x8998, 0),  # East Asian ideograph
    0x4B5830: (0x899A, 0),  # East Asian ideograph
    0x213068: (0x4EC3, 0),  # East Asian ideograph
    0x213069: (0x4EC4, 0),  # East Asian ideograph
    0x22306A: (0x62C3, 0),  # East Asian ideograph
    0x23306B: (0x899C, 0),  # East Asian ideograph
    0x21306C: (0x4EC7, 0),  # East Asian ideograph
    0x21306D: (0x4ECB, 0),  # East Asian ideograph
    0x21306E: (0x4EE4, 0),  # East Asian ideograph
    0x23306F: (0x89A1, 0),  # East Asian ideograph
    0x213070: (0x4ED5, 0),  # East Asian ideograph
    0x275D68: (0x9504, 0),  # East Asian ideograph
    0x223072: (0x630D, 0),  # East Asian ideograph
    0x213073: (0x4EE3, 0),  # East Asian ideograph
    0x213074: (0x4ED4, 0),  # East Asian ideograph
    0x213075: (0x4ED7, 0),  # East Asian ideograph
    0x233076: (0x89A5, 0),  # East Asian ideograph
    0x275D69: (0x9509, 0),  # East Asian ideograph
    0x213078: (0x4EFF, 0),  # East Asian ideograph
    0x233079: (0x89A9, 0),  # East Asian ideograph
    0x6F5B63: (0xD2F0, 0),  # Korean hangul
    0x21307C: (0x4EFB, 0),  # East Asian ideograph
    0x275D6A: (0x950B, 0),  # East Asian ideograph
    0x21307E: (0x4F15, 0),  # East Asian ideograph
    0x224547: (0x6BBD, 0),  # East Asian ideograph
    0x215D6B: (0x9320, 0),  # East Asian ideograph
    0x292A2F: (0x86F1, 0),  # East Asian ideograph
    0x6F5D6C: (0xD754, 0),  # Korean hangul
    0x29436A: (0x9512, 0),  # East Asian ideograph
    0x215D6D: (0x92F8, 0),  # East Asian ideograph
    0x235A53: (0x9D36, 0),  # East Asian ideograph
    0x225D6E: (0x757A, 0),  # East Asian ideograph
    0x6F535B: (0xC218, 0),  # Korean hangul
    0x274C79: (0x766B, 0),  # East Asian ideograph
    0x6F5B64: (0xD2F1, 0),  # Korean hangul
    0x275D6F: (0x9519, 0),  # East Asian ideograph
    0x29325E: (0x8BDC, 0),  # East Asian ideograph
    0x6F5721: (0xC7A1, 0),  # Korean hangul
    0x2F575F: (0x9ABE, 0),  # East Asian ideograph
    0x275D70: (0x94B1, 0),  # East Asian ideograph
    0x4B5832: (0x89B3, 0),  # East Asian ideograph
    0x225D71: (0x7577, 0),  # East Asian ideograph
    0x6F4A58: (0xAE85, 0),  # Korean hangul
    0x275D72: (0x9521, 0),  # East Asian ideograph
    0x22343C: (0x649D, 0),  # East Asian ideograph
    0x275D73: (0x94EE, 0),  # East Asian ideograph
    0x6F5B65: (0xD2F4, 0),  # Korean hangul
    0x275D74: (0x5F55, 0),  # East Asian ideograph
    0x6F5722: (0xC7A3, 0),  # Korean hangul
    0x69724E: (0x9BF2, 0),  # East Asian ideograph
    0x215D75: (0x9310, 0),  # East Asian ideograph
    0x234948: (0x95BC, 0),  # East Asian ideograph
    0x4B325F: (0x50BB, 0),  # East Asian ideograph
    0x215D76: (0x9326, 0),  # East Asian ideograph
    0x6F5835: (0xC9DA, 0),  # Korean hangul
    0x692153: (0x3009, 0),  # Ideographic greater than sign
    0x215D77: (0x934D, 0),  # East Asian ideograph
    0x2D632D: (0x4E80, 0),  # East Asian ideograph
    0x215D78: (0x9382, 0),  # East Asian ideograph
    0x274C7B: (0x53D1, 0),  # East Asian ideograph
    0x6F5B66: (0xD2F8, 0),  # Korean hangul
    0x225D79: (0x757D, 0),  # East Asian ideograph
    0x6F5432: (0xC2FC, 0),  # Korean hangul
    0x224824: (0x6CD8, 0),  # East Asian ideograph
    0x4B5C77: (0x9139, 0),  # East Asian ideograph
    0x235D7A: (0x9EB0, 0),  # East Asian ideograph
    0x6F5D7B: (0xD790, 0),  # Korean hangul
    0x27606D: (0x9974, 0),  # East Asian ideograph
    0x224826: (0x6CC6, 0),  # East Asian ideograph
    0x6F575B: (0xC8A0, 0),  # Korean hangul
    0x275D7C: (0x9505, 0),  # East Asian ideograph
    0x2E5452: (0x71FE, 0),  # East Asian ideograph
    0x234827: (0x93F4, 0),  # East Asian ideograph
    0x275D7D: (0x951A, 0),  # East Asian ideograph
    0x234828: (0x9436, 0),  # East Asian ideograph
    0x6F5B67: (0xD300, 0),  # Korean hangul
    0x275D7E: (0x953E, 0),  # East Asian ideograph
    0x224829: (0x6CE9, 0),  # East Asian ideograph
    0x226764: (0x799D, 0),  # East Asian ideograph
    0x23494A: (0x95CD, 0),  # East Asian ideograph
    0x395E3D: (0x9295, 0),  # East Asian ideograph
    0x6F4A5B: (0xAEBE, 0),  # Korean hangul
    0x23482B: (0x943B, 0),  # East Asian ideograph
    0x275946: (0x8BD1, 0),  # East Asian ideograph
    0x22527C: (0x717B, 0),  # East Asian ideograph
    0x23482D: (0x9424, 0),  # East Asian ideograph
    0x6F5B68: (0xD301, 0),  # Korean hangul
    0x6F5725: (0xC7A6, 0),  # Korean hangul
    0x284E42: (0x6D4D, 0),  # East Asian ideograph
    0x21482F: (0x6E34, 0),  # East Asian ideograph
    0x6F523E: (0xBF1D, 0),  # Korean hangul
    0x6F4A5C: (0xAEC0, 0),  # Korean hangul
    0x234830: (0x9437, 0),  # East Asian ideograph
    0x213122: (0x4F10, 0),  # East Asian ideograph
    0x213123: (0x4F0F, 0),  # East Asian ideograph
    0x213124: (0x4EF2, 0),  # East Asian ideograph
    0x223125: (0x62F5, 0),  # East Asian ideograph
    0x213126: (0x4EF3, 0),  # East Asian ideograph
    0x213127: (0x4EF6, 0),  # East Asian ideograph
    0x213128: (0x4EF0, 0),  # East Asian ideograph
    0x23312A: (0x89B8, 0),  # East Asian ideograph
    0x23312B: (0x89B7, 0),  # East Asian ideograph
    0x23312C: (0x89B6, 0),  # East Asian ideograph
    0x234832: (0x9440, 0),  # East Asian ideograph
    0x21312E: (0x4F57, 0),  # East Asian ideograph
    0x23312F: (0x89BC, 0),  # East Asian ideograph
    0x213130: (0x4F5E, 0),  # East Asian ideograph
    0x223131: (0x630C, 0),  # East Asian ideograph
    0x233132: (0x89BF, 0),  # East Asian ideograph
    0x213133: (0x4F55, 0),  # East Asian ideograph
    0x213134: (0x4F30, 0),  # East Asian ideograph
    0x213135: (0x4F50, 0),  # East Asian ideograph
    0x213136: (0x4F51, 0),  # East Asian ideograph
    0x223137: (0x62F6, 0),  # East Asian ideograph
    0x213138: (0x4F48, 0),  # East Asian ideograph
    0x213139: (0x4F46, 0),  # East Asian ideograph
    0x22313A: (0x6331, 0),  # East Asian ideograph
    0x23313B: (0x89D5, 0),  # East Asian ideograph
    0x21313C: (0x4F54, 0),  # East Asian ideograph
    0x21313D: (0x4F3C, 0),  # East Asian ideograph
    0x21313E: (0x4F63, 0),  # East Asian ideograph
    0x23313F: (0x89DA, 0),  # East Asian ideograph
    0x213140: (0x4F60, 0),  # East Asian ideograph
    0x213141: (0x4F2F, 0),  # East Asian ideograph
    0x223142: (0x6345, 0),  # East Asian ideograph
    0x233143: (0x89E5, 0),  # East Asian ideograph
    0x223144: (0x6343, 0),  # East Asian ideograph
    0x234836: (0x942D, 0),  # East Asian ideograph
    0x213146: (0x4F6F, 0),  # East Asian ideograph
    0x223147: (0x6353, 0),  # East Asian ideograph
    0x223148: (0x6364, 0),  # East Asian ideograph
    0x223149: (0x6336, 0),  # East Asian ideograph
    0x22314A: (0x6344, 0),  # East Asian ideograph
    0x224837: (0x6D1D, 0),  # East Asian ideograph
    0x23314C: (0x89E9, 0),  # East Asian ideograph
    0x23314D: (0x89EB, 0),  # East Asian ideograph
    0x21314E: (0x4F8B, 0),  # East Asian ideograph
    0x27314F: (0x4ED1, 0),  # East Asian ideograph
    0x234838: (0x9431, 0),  # East Asian ideograph
    0x213152: (0x4F7B, 0),  # East Asian ideograph
    0x233153: (0x89ED, 0),  # East Asian ideograph
    0x223154: (0x6339, 0),  # East Asian ideograph
    0x213155: (0x4F8F, 0),  # East Asian ideograph
    0x213156: (0x4F7E, 0),  # East Asian ideograph
    0x213157: (0x4FE1, 0),  # East Asian ideograph
    0x223158: (0x6357, 0),  # East Asian ideograph
    0x213159: (0x4FB5, 0),  # East Asian ideograph
    0x22315A: (0x633C, 0),  # East Asian ideograph
    0x22315B: (0x6358, 0),  # East Asian ideograph
    0x21315C: (0x4FDE, 0),  # East Asian ideograph
    0x27315D: (0x4FA0, 0),  # East Asian ideograph
    0x21315E: (0x4FCF, 0),  # East Asian ideograph
    0x22315F: (0x6354, 0),  # East Asian ideograph
    0x213160: (0x4FDA, 0),  # East Asian ideograph
    0x213161: (0x4FDD, 0),  # East Asian ideograph
    0x213162: (0x4FC3, 0),  # East Asian ideograph
    0x213163: (0x4FD8, 0),  # East Asian ideograph
    0x233164: (0x89F7, 0),  # East Asian ideograph
    0x213165: (0x4FCA, 0),  # East Asian ideograph
    0x213166: (0x4FAE, 0),  # East Asian ideograph
    0x213167: (0x4FD0, 0),  # East Asian ideograph
    0x223168: (0x637D, 0),  # East Asian ideograph
    0x273169: (0x7CFB, 0),  # East Asian ideograph (duplicate simplified)
    0x22316A: (0x63B6, 0),  # East Asian ideograph
    0x22316B: (0x6382, 0),  # East Asian ideograph
    0x27316C: (0x4ED3, 0),  # East Asian ideograph
    0x23316D: (0x8A07, 0),  # East Asian ideograph
    0x22316E: (0x639F, 0),  # East Asian ideograph
    0x21483D: (0x6E9D, 0),  # East Asian ideograph
    0x233170: (0x8A0F, 0),  # East Asian ideograph
    0x233171: (0x8A11, 0),  # East Asian ideograph
    0x233172: (0x8A12, 0),  # East Asian ideograph
    0x233173: (0x8A0D, 0),  # East Asian ideograph
    0x213174: (0x4FF8, 0),  # East Asian ideograph
    0x213175: (0x5028, 0),  # East Asian ideograph
    0x213176: (0x5014, 0),  # East Asian ideograph
    0x213177: (0x5016, 0),  # East Asian ideograph
    0x213178: (0x5029, 0),  # East Asian ideograph
    0x223179: (0x6381, 0),  # East Asian ideograph
    0x23317A: (0x8A27, 0),  # East Asian ideograph
    0x22317B: (0x6397, 0),  # East Asian ideograph
    0x21317C: (0x503C, 0),  # East Asian ideograph
    0x23317D: (0x8A29, 0),  # East Asian ideograph
    0x21317E: (0x4FFA, 0),  # East Asian ideograph
    0x234840: (0x9445, 0),  # East Asian ideograph
    0x274841: (0x6C85, 0),  # East Asian ideograph
    0x6F5B6C: (0xD30C, 0),  # Korean hangul
    0x234842: (0x9450, 0),  # East Asian ideograph
    0x273266: (0x4F18, 0),  # East Asian ideograph
    0x4B513B: (0x7CF8, 0),  # East Asian ideograph
    0x6F4B6D: (0xB0EC, 0),  # Korean hangul
    0x274844: (0x6E7F, 0),  # East Asian ideograph
    0x2D4845: (0x6E29, 0),  # East Asian ideograph
    0x4B4846: (0x78C6, 0),  # East Asian ideograph
    0x226F69: (0x7CC5, 0),  # East Asian ideograph
    0x274848: (0x6CA7, 0),  # East Asian ideograph
    0x4B3622: (0x8C18, 0),  # East Asian ideograph
    0x6F4A61: (0xAED0, 0),  # Korean hangul
    0x273733: (0x5578, 0),  # East Asian ideograph
    0x23484A: (0x944A, 0),  # East Asian ideograph
    0x27484B: (0x51C6, 0),  # East Asian ideograph
    0x6F5B6E: (0xD30E, 0),  # Korean hangul
    0x2F3639: (0x8C7C, 0),  # East Asian ideograph
    0x4B484C: (0x6F91, 0),  # East Asian ideograph
    0x22484D: (0x6D26, 0),  # East Asian ideograph
    0x22484E: (0x6D27, 0),  # East Asian ideograph
    0x294375: (0x9514, 0),  # East Asian ideograph
    0x22484F: (0x6D0F, 0),  # East Asian ideograph
    0x224850: (0x6D0A, 0),  # East Asian ideograph
    0x2D4466: (0x6973, 0),  # East Asian ideograph
    0x224851: (0x6D3F, 0),  # East Asian ideograph
    0x226329: (0x77BE, 0),  # East Asian ideograph
    0x234853: (0x9466, 0),  # East Asian ideograph
    0x47594E: (0x9C3A, 0),  # East Asian ideograph
    0x274854: (0x6E0D, 0),  # East Asian ideograph
    0x514E5B: (0x9271, 0),  # East Asian ideograph
    0x274855: (0x6DA8, 0),  # East Asian ideograph
    0x6F5B70: (0xD314, 0),  # Korean hangul
    0x274842: (0x706D, 0),  # East Asian ideograph
    0x6F572D: (0xC7BF, 0),  # Korean hangul
    0x284C41: (0x6CA4, 0),  # East Asian ideograph
    0x234560: (0x93BE, 0),  # East Asian ideograph (not in Unicode)
    0x29243A: (0x83BC, 0),  # East Asian ideograph
    0x274857: (0x6C49, 0),  # East Asian ideograph
    0x273B79: (0x5C9B, 0),  # East Asian ideograph
    0x234858: (0x9462, 0),  # East Asian ideograph
    0x2F252D: (0x6A22, 0),  # East Asian ideograph
    0x6F575D: (0xC8A8, 0),  # Korean hangul
    0x3F4621: (0x9A69, 0),  # East Asian ideograph
    0x274859: (0x6D9F, 0),  # East Asian ideograph
    0x286622: (0x7857, 0),  # East Asian ideograph
    0x22485A: (0x6D07, 0),  # East Asian ideograph
    0x4B4D7B: (
        0x77D7,
        0,
    ),  # East Asian ideograph (variant of 214D7B which maps to 77D7)
    0x6F5B71: (0xD31C, 0),  # Korean hangul
    0x213221: (0x5018, 0),  # East Asian ideograph
    0x213222: (0x4FF1, 0),  # East Asian ideograph
    0x22485B: (0x6D04, 0),  # East Asian ideograph
    0x273224: (0x4E2A, 0),  # East Asian ideograph
    0x213225: (0x5019, 0),  # East Asian ideograph
    0x273226: (0x4F25, 0),  # East Asian ideograph
    0x223227: (0x638E, 0),  # East Asian ideograph
    0x233228: (0x8A4A, 0),  # East Asian ideograph
    0x22485C: (0x6CDA, 0),  # East Asian ideograph
    0x23322A: (0x8A4E, 0),  # East Asian ideograph
    0x21322B: (0x4FFE, 0),  # East Asian ideograph
    0x21322C: (0x502A, 0),  # East Asian ideograph
    0x27322D: (0x4F26, 0),  # East Asian ideograph
    0x27322E: (0x4EC3, 0),  # East Asian ideograph (duplicate simplified)
    0x22322F: (0x6375, 0),  # East Asian ideograph
    0x223230: (0x63AF, 0),  # East Asian ideograph
    0x213231: (0x5047, 0),  # East Asian ideograph
    0x213232: (0x505A, 0),  # East Asian ideograph
    0x273233: (0x4F1F, 0),  # East Asian ideograph
    0x213234: (0x5043, 0),  # East Asian ideograph
    0x23485E: (0x945E, 0),  # East Asian ideograph
    0x213236: (0x5076, 0),  # East Asian ideograph
    0x213237: (0x504E, 0),  # East Asian ideograph
    0x223238: (0x63B0, 0),  # East Asian ideograph
    0x223239: (0x63AE, 0),  # East Asian ideograph
    0x22323A: (0x637C, 0),  # East Asian ideograph
    0x27485F: (0x6EDE, 0),  # East Asian ideograph
    0x21323C: (0x5077, 0),  # East Asian ideograph
    0x22323D: (0x63AD, 0),  # East Asian ideograph
    0x27323E: (0x5BB6, 0),  # East Asian ideograph
    0x21323F: (0x5085, 0),  # East Asian ideograph
    0x273240: (0x5907, 0),  # East Asian ideograph
    0x224860: (0x6D2E, 0),  # East Asian ideograph
    0x233242: (0x8A45, 0),  # East Asian ideograph
    0x273243: (0x4F27, 0),  # East Asian ideograph
    0x273244: (0x4F1E, 0),  # East Asian ideograph
    0x213245: (0x50AD, 0),  # East Asian ideograph
    0x273246: (0x4F20, 0),  # East Asian ideograph
    0x224861: (0x6D35, 0),  # East Asian ideograph
    0x213248: (0x50B2, 0),  # East Asian ideograph
    0x273249: (0x4EC5, 0),  # East Asian ideograph
    0x27324A: (0x503E, 0),  # East Asian ideograph
    0x21324B: (0x50AC, 0),  # East Asian ideograph
    0x27324C: (0x4F24, 0),  # East Asian ideograph
    0x224862: (0x6D3A, 0),  # East Asian ideograph
    0x21324E: (0x50E7, 0),  # East Asian ideograph
    0x22324F: (0x63BD, 0),  # East Asian ideograph
    0x223250: (0x63C3, 0),  # East Asian ideograph
    0x273251: (0x4FA5, 0),  # East Asian ideograph
    0x223252: (0x63F5, 0),  # East Asian ideograph
    0x213253: (0x50ED, 0),  # East Asian ideograph
    0x213254: (0x50DA, 0),  # East Asian ideograph
    0x273255: (0x4EC6, 0),  # East Asian ideograph
    0x273256: (0x4F2A, 0),  # East Asian ideograph
    0x273257: (0x8C61, 0),  # East Asian ideograph
    0x273258: (0x4FA8, 0),  # East Asian ideograph
    0x233259: (0x8A82, 0),  # East Asian ideograph
    0x27325A: (0x4EBF, 0),  # East Asian ideograph
    0x22325B: (0x63E0, 0),  # East Asian ideograph
    0x22325C: (0x63D5, 0),  # East Asian ideograph
    0x23325D: (0x8A84, 0),  # East Asian ideograph
    0x23325E: (0x8A75, 0),  # East Asian ideograph
    0x274865: (0x6E14, 0),  # East Asian ideograph
    0x273260: (0x4FA9, 0),  # East Asian ideograph
    0x273261: (0x4FED, 0),  # East Asian ideograph
    0x273262: (0x50A7, 0),  # East Asian ideograph
    0x273263: (0x5C3D, 0),  # East Asian ideograph (duplicate simplified)
    0x213264: (0x5112, 0),  # East Asian ideograph
    0x273265: (0x4FE6, 0),  # East Asian ideograph
    0x223266: (0x63C5, 0),  # East Asian ideograph (not in Unicode)
    0x213267: (0x511F, 0),  # East Asian ideograph
    0x213268: (0x5121, 0),  # East Asian ideograph
    0x273269: (0x50A8, 0),  # East Asian ideograph
    0x21326A: (0x5137, 0),  # East Asian ideograph
    0x27326B: (0x4FE8, 0),  # East Asian ideograph
    0x21326C: (0x5140, 0),  # East Asian ideograph
    0x21326D: (0x5143, 0),  # East Asian ideograph
    0x21326E: (0x5141, 0),  # East Asian ideograph
    0x23326F: (0x8A96, 0),  # East Asian ideograph
    0x213270: (0x5144, 0),  # East Asian ideograph
    0x233271: (0x8A9A, 0),  # East Asian ideograph
    0x213272: (0x5149, 0),  # East Asian ideograph
    0x273273: (0x51F6, 0),  # East Asian ideograph
    0x213274: (0x5148, 0),  # East Asian ideograph
    0x274C3C: (0x8FED, 0),  # East Asian ideograph
    0x223276: (0x63D1, 0),  # East Asian ideograph (not in Unicode)
    0x234869: (0x946D, 0),  # East Asian ideograph
    0x213278: (0x5155, 0),  # East Asian ideograph
    0x223279: (0x63C4, 0),  # East Asian ideograph
    0x27327A: (0x513F, 0),  # East Asian ideograph
    0x27327B: (0x5156, 0),  # East Asian ideograph
    0x21327C: (0x515C, 0),  # East Asian ideograph
    0x22486A: (0x6D2B, 0),  # East Asian ideograph
    0x22327E: (0x6412, 0),  # East Asian ideograph
    0x2D4F7C: (0x7B5E, 0),  # East Asian ideograph
    0x22486B: (0x6D11, 0),  # East Asian ideograph
    0x27486C: (0x6CFC, 0),  # East Asian ideograph
    0x6F5838: (0xC9DC, 0),  # Korean hangul
    0x21304D: (0x4E82, 0),  # East Asian ideograph
    0x22486D: (0x6D24, 0),  # East Asian ideograph
    0x6F4E5C: (0xB760, 0),  # Korean hangul
    0x235C65: (0x9DEF, 0),  # East Asian ideograph
    0x293B3F: (0x8F7A, 0),  # East Asian ideograph
    0x27486E: (0x6DA7, 0),  # East Asian ideograph
    0x6F5B75: (0xD321, 0),  # Korean hangul
    0x27486F: (0x6D01, 0),  # East Asian ideograph
    0x6F4870: (0xAC1B, 0),  # Korean hangul
    0x6F4C49: (0xB214, 0),  # Korean hangul
    0x234871: (0x9477, 0),  # East Asian ideograph
    0x275954: (0x5C82, 0),  # East Asian ideograph
    0x2F252E: (0x8507, 0),  # East Asian ideograph
    0x6F4872: (0xAC1D, 0),  # Korean hangul
    0x2D315F: (0x4FA3, 0),  # East Asian ideograph
    0x235622: (0x9B35, 0),  # East Asian ideograph
    0x6F5B76: (0xD325, 0),  # Korean hangul
    0x2D4874: (0x6F5C, 0),  # East Asian ideograph
    0x6F4875: (0xAC24, 0),  # Korean hangul
    0x29457A: (0x9550, 0),  # East Asian ideograph
    0x6F4876: (0xAC2C, 0),  # Korean hangul
    0x227321: (0x7E35, 0),  # East Asian ideograph
    0x224877: (0x6DA5, 0),  # East Asian ideograph
    0x213322: (0x5168, 0),  # East Asian ideograph
    0x4B5361: (0x89D2, 0),  # East Asian ideograph (duplicate simplified)
    0x274878: (0x6E83, 0),  # East Asian ideograph
    0x213323: (0x5169, 0),  # East Asian ideograph
    0x455E21: (0x953A, 0),  # East Asian ideograph
    0x293271: (0x8BEE, 0),  # East Asian ideograph
    0x213324: (0x516B, 0),  # East Asian ideograph
    0x22455B: (0x6BD6, 0),  # East Asian ideograph
    0x6F487A: (0xAC31, 0),  # Korean hangul
    0x213325: (0x516D, 0),  # East Asian ideograph
    0x23487B: (0x9482, 0),  # East Asian ideograph
    0x27373D: (0x5480, 0),  # East Asian ideograph
    0x27487C: (0x6D53, 0),  # East Asian ideograph
    0x213327: (0x516C, 0),  # East Asian ideograph
    0x6F5D56: (0xD6E0, 0),  # Korean hangul
    0x22487D: (0x6D92, 0),  # East Asian ideograph
    0x217328: (0x568C, 0),  # East Asian ideograph
    0x6F487E: (0xAC54, 0),  # Korean hangul
    0x213329: (0x5175, 0),  # East Asian ideograph
    0x215F33: (0x9694, 0),  # East Asian ideograph
    0x276225: (0x9CCF, 0),  # East Asian ideograph
    0x2D332A: (0x4E0C, 0),  # East Asian ideograph
    0x2D3E2B: (0x6060, 0),  # East Asian ideograph
    0x21332B: (0x5177, 0),  # East Asian ideograph
    0x4B5F62: (0x7668, 0),  # East Asian ideograph
    0x3F4629: (0x4E97, 0),  # East Asian ideograph
    0x513051: (0x8CAE, 0),  # East Asian ideograph
    0x22332C: (0x6424, 0),  # East Asian ideograph
    0x274C3B: (0x7574, 0),  # East Asian ideograph
    0x23463C: (0x9389, 0),  # East Asian ideograph
    0x22732D: (0x7E52, 0),  # East Asian ideograph
    0x22534A: (0x719B, 0),  # East Asian ideograph
    0x6F5736: (0xC804, 0),  # Korean hangul
    0x215F34: (0x9699, 0),  # East Asian ideograph
    0x21332F: (0x5189, 0),  # East Asian ideograph
    0x6F4A6D: (0xAF3F, 0),  # Korean hangul
    0x275958: (0x4E30, 0),  # East Asian ideograph
    0x233321: (0x8ABE, 0),  # East Asian ideograph
    0x223322: (0x6410, 0),  # East Asian ideograph
    0x273323: (0x4E24, 0),  # East Asian ideograph
    0x223324: (0x6434, 0),  # East Asian ideograph
    0x233325: (0x8ACF, 0),  # East Asian ideograph
    0x213326: (0x516E, 0),  # East Asian ideograph
    0x233327: (0x8AC6, 0),  # East Asian ideograph
    0x213328: (0x5171, 0),  # East Asian ideograph
    0x223329: (0x641B, 0),  # East Asian ideograph
    0x21332A: (0x5176, 0),  # East Asian ideograph
    0x22332B: (0x6420, 0),  # East Asian ideograph
    0x23332C: (0x8AD1, 0),  # East Asian ideograph
    0x23332D: (0x8AD3, 0),  # East Asian ideograph
    0x21332E: (0x5180, 0),  # East Asian ideograph
    0x22332F: (0x6426, 0),  # East Asian ideograph
    0x213330: (0x518C, 0),  # East Asian ideograph
    0x233331: (0x8AAF, 0),  # East Asian ideograph
    0x213332: (0x5192, 0),  # East Asian ideograph
    0x233333: (0x8AD4, 0),  # East Asian ideograph
    0x213334: (0x5195, 0),  # East Asian ideograph
    0x213335: (0x6700, 0),  # East Asian ideograph
    0x213336: (0x5197, 0),  # East Asian ideograph
    0x213337: (0x51A0, 0),  # East Asian ideograph
    0x233338: (0x8AB9, 0),  # East Asian ideograph
    0x223339: (0x3013, 0),  # East Asian ideograph (not found in unified han)
    0x23333B: (0x8ADB, 0),  # East Asian ideograph
    0x21333C: (0x51B0, 0),  # East Asian ideograph
    0x22333D: (0x6421, 0),  # East Asian ideograph
    0x21333E: (0x51B7, 0),  # East Asian ideograph
    0x23333F: (0x8AD0, 0),  # East Asian ideograph
    0x233340: (0x8AD7, 0),  # East Asian ideograph
    0x213341: (0x51CC, 0),  # East Asian ideograph
    0x233344: (0x8AF3, 0),  # East Asian ideograph
    0x233336: (0x8ACD, 0),  # East Asian ideograph
    0x213347: (0x51F0, 0),  # East Asian ideograph
    0x273348: (0x51EF, 0),  # East Asian ideograph
    0x233349: (0x8B4C, 0),  # East Asian ideograph
    0x223337: (0x6418, 0),  # East Asian ideograph
    0x22334C: (0x6409, 0),  # East Asian ideograph
    0x21334D: (0x51F8, 0),  # East Asian ideograph
    0x23334E: (0x8AF6, 0),  # East Asian ideograph
    0x21334F: (0x5200, 0),  # East Asian ideograph
    0x213350: (0x5201, 0),  # East Asian ideograph
    0x223338: (0x640E, 0),  # East Asian ideograph
    0x213352: (0x5207, 0),  # East Asian ideograph
    0x223353: (0x6440, 0),  # East Asian ideograph
    0x213354: (0x5208, 0),  # East Asian ideograph
    0x213355: (0x520A, 0),  # East Asian ideograph
    0x233356: (0x8B03, 0),  # East Asian ideograph
    0x233357: (0x8AE4, 0),  # East Asian ideograph
    0x233359: (0x8B14, 0),  # East Asian ideograph
    0x21335A: (0x5224, 0),  # East Asian ideograph
    0x21335B: (0x5225, 0),  # East Asian ideograph
    0x235749: (0x9B86, 0),  # East Asian ideograph
    0x23335D: (0x8AFC, 0),  # East Asian ideograph
    0x21335E: (0x5229, 0),  # East Asian ideograph
    0x21335F: (0x5238, 0),  # East Asian ideograph
    0x213360: (0x523B, 0),  # East Asian ideograph
    0x213361: (0x5237, 0),  # East Asian ideograph
    0x233362: (0x8ADE, 0),  # East Asian ideograph
    0x233363: (0x8AE1, 0),  # East Asian ideograph
    0x233364: (0x8B07, 0),  # East Asian ideograph
    0x2D537E: (0x81C8, 0),  # East Asian ideograph
    0x213366: (0x5241, 0),  # East Asian ideograph
    0x213367: (0x5239, 0),  # East Asian ideograph
    0x223368: (0x645B, 0),  # East Asian ideograph
    0x213369: (0x524D, 0),  # East Asian ideograph
    0x22336A: (0x644F, 0),  # East Asian ideograph
    0x27336B: (0x514B, 0),  # East Asian ideograph
    0x21336C: (0x524A, 0),  # East Asian ideograph
    0x27336D: (0x5219, 0),  # East Asian ideograph
    0x21336E: (0x525C, 0),  # East Asian ideograph
    0x22336F: (0x6476, 0),  # East Asian ideograph
    0x273370: (0x521A, 0),  # East Asian ideograph
    0x215F37: (0x969B, 0),  # East Asian ideograph
    0x213372: (0x525D, 0),  # East Asian ideograph
    0x233373: (0x8B16, 0),  # East Asian ideograph
    0x213374: (0x526F, 0),  # East Asian ideograph
    0x213375: (0x5272, 0),  # East Asian ideograph
    0x223376: (0x6474, 0),  # East Asian ideograph
    0x213377: (0x5269, 0),  # East Asian ideograph
    0x273378: (0x521B, 0),  # East Asian ideograph
    0x233379: (0x8B06, 0),  # East Asian ideograph
    0x23337A: (0x8B05, 0),  # East Asian ideograph
    0x21337B: (0x527F, 0),  # East Asian ideograph
    0x27337C: (0x5212, 0),  # East Asian ideograph
    0x21337D: (0x5288, 0),  # East Asian ideograph
    0x27337E: (0x5267, 0),  # East Asian ideograph
    0x213340: (0x51CD, 0),  # East Asian ideograph
    0x217341: (0x569C, 0),  # East Asian ideograph
    0x27484F: (0x6CAA, 0),  # East Asian ideograph
    0x276226: (0x9CA2, 0),  # East Asian ideograph
    0x234960: (0x95D5, 0),  # East Asian ideograph
    0x6F773B: (0xC6FD, 0),  # Korean hangul
    0x213344: (0x51DC, 0),  # East Asian ideograph
    0x23337C: (0x8B0F, 0),  # East Asian ideograph
    0x223345: (0x6441, 0),  # East Asian ideograph
    0x6F5B7E: (0xD33C, 0),  # Korean hangul
    0x282E79: (0x6079, 0),  # East Asian ideograph
    0x213E40: (
        0x6046,
        0,
    ),  # East Asian ideograph (variant of 4B3E40 which maps to 6046)
    0x286E68: (0x7B3E, 0),  # East Asian ideograph
    0x22677B: (0x79B4, 0),  # East Asian ideograph
    0x224562: (0x6BDC, 0),  # East Asian ideograph
    0x213348: (0x51F1, 0),  # East Asian ideograph
    0x695626: (0x4E62, 0),  # East Asian ideograph
    0x6F4A72: (0xAF49, 0),  # Korean hangul
    0x213349: (0x51F3, 0),  # East Asian ideograph
    0x513057: (0x4E98, 0),  # East Asian ideograph
    0x21334B: (0x51FA, 0),  # East Asian ideograph
    0x6F573C: (0xC814, 0),  # Korean hangul
    0x23334C: (0x8ADD, 0),  # East Asian ideograph
    0x224563: (0x6BDD, 0),  # East Asian ideograph
    0x234962: (0x95D2, 0),  # East Asian ideograph
    0x6F2525: (0x3160, 0),  # Korean hangul
    0x4C3A33: (
        0x80AD,
        0,
    ),  # East Asian ideograph (variant of 2E3A33 which maps to 80AD)
    0x276072: (0x9975, 0),  # East Asian ideograph
    0x27595E: (0x4E88, 0),  # East Asian ideograph
    0x21734E: (0x56AC, 0),  # East Asian ideograph
    0x273745: (0x55B7, 0),  # East Asian ideograph
    0x23334F: (0x8AF4, 0),  # East Asian ideograph
    0x233350: (0x8AF5, 0),  # East Asian ideograph
    0x6F573D: (0xC815, 0),  # Korean hangul
    0x213351: (0x5203, 0),  # East Asian ideograph
    0x395050: (0x7BED, 0),  # East Asian ideograph
    0x22633A: (0x77D1, 0),  # East Asian ideograph
    0x287352: (0x7F34, 0),  # East Asian ideograph
    0x6F4B71: (0xB10B, 0),  # Korean hangul
    0x6F4A74: (0xAF58, 0),  # Korean hangul
    0x233353: (0x8ADF, 0),  # East Asian ideograph
    0x4B3354: (0x82C5, 0),  # East Asian ideograph
    0x4B3355: (0x520B, 0),  # East Asian ideograph
    0x6F573E: (0xC816, 0),  # Korean hangul
    0x213356: (0x5211, 0),  # East Asian ideograph
    0x224565: (0x6BDF, 0),  # East Asian ideograph
    0x213357: (0x5217, 0),  # East Asian ideograph
    0x2D5C48: (0x9013, 0),  # East Asian ideograph
    0x273747: (0x54DD, 0),  # East Asian ideograph
    0x213359: (0x520E, 0),  # East Asian ideograph
    0x6F5D58: (0xD6E8, 0),  # Korean hangul
    0x27735A: (0x55BE, 0),  # East Asian ideograph
    0x2D4F41: (0x4E69, 0),  # East Asian ideograph
    0x4B5D2B: (0x9162, 0),  # East Asian ideograph
    0x273421: (0x5251, 0),  # East Asian ideograph
    0x213422: (0x5289, 0),  # East Asian ideograph
    0x273423: (0x5242, 0),  # East Asian ideograph
    0x223424: (0x6464, 0),  # East Asian ideograph
    0x213425: (0x529F, 0),  # East Asian ideograph
    0x213426: (0x52A0, 0),  # East Asian ideograph
    0x223427: (0x6482, 0),  # East Asian ideograph
    0x223428: (0x645E, 0),  # East Asian ideograph
    0x21335C: (0x5220, 0),  # East Asian ideograph
    0x21342A: (0x52AC, 0),  # East Asian ideograph
    0x21342B: (0x52AA, 0),  # East Asian ideograph
    0x22342C: (0x647B, 0),  # East Asian ideograph
    0x23342D: (0x8B26, 0),  # East Asian ideograph
    0x22342E: (0x645C, 0),  # East Asian ideograph
    0x27342F: (0x52B2, 0),  # East Asian ideograph
    0x233430: (0x8B33, 0),  # East Asian ideograph
    0x213431: (0x52D8, 0),  # East Asian ideograph
    0x21305B: (0x4EA1, 0),  # East Asian ideograph
    0x273433: (0x52A1, 0),  # East Asian ideograph
    0x273434: (0x52A8, 0),  # East Asian ideograph
    0x273435: (0x52B3, 0),  # East Asian ideograph
    0x273436: (0x52CB, 0),  # East Asian ideograph
    0x213437: (0x52DD, 0),  # East Asian ideograph
    0x273438: (0x52BF, 0),  # East Asian ideograph
    0x213439: (0x52E4, 0),  # East Asian ideograph
    0x23343A: (0x8B29, 0),  # East Asian ideograph
    0x2D335F: (0x52B5, 0),  # East Asian ideograph
    0x27343C: (0x52B1, 0),  # East Asian ideograph
    0x27343D: (0x529D, 0),  # East Asian ideograph
    0x21343E: (0x52FB, 0),  # East Asian ideograph
    0x22343F: (0x6499, 0),  # East Asian ideograph
    0x213440: (0x52FF, 0),  # East Asian ideograph
    0x217360: (0x56C5, 0),  # East Asian ideograph
    0x233442: (0x8B48, 0),  # East Asian ideograph
    0x215F3E: (0x96BB, 0),  # East Asian ideograph
    0x213444: (0x530D, 0),  # East Asian ideograph
    0x234966: (0x95DA, 0),  # East Asian ideograph
    0x213446: (0x530F, 0),  # East Asian ideograph
    0x213447: (0x5315, 0),  # East Asian ideograph
    0x213448: (0x5316, 0),  # East Asian ideograph
    0x213449: (0x5317, 0),  # East Asian ideograph
    0x23344A: (0x8B46, 0),  # East Asian ideograph
    0x21344B: (0x53F5, 0),  # East Asian ideograph
    0x21344C: (0x531D, 0),  # East Asian ideograph
    0x22344D: (0x6496, 0),  # East Asian ideograph
    0x21344E: (0x5320, 0),  # East Asian ideograph
    0x21344F: (0x5323, 0),  # East Asian ideograph
    0x213450: (0x532A, 0),  # East Asian ideograph
    0x273451: (0x6C47, 0),  # East Asian ideograph
    0x273452: (0x532E, 0),  # East Asian ideograph
    0x213363: (0x523A, 0),  # East Asian ideograph
    0x213454: (0x533E, 0),  # East Asian ideograph
    0x273455: (0x533A, 0),  # East Asian ideograph
    0x213456: (0x533F, 0),  # East Asian ideograph
    0x213457: (0x5341, 0),  # East Asian ideograph
    0x213458: (0x5343, 0),  # East Asian ideograph
    0x213459: (0x5345, 0),  # East Asian ideograph
    0x21345A: (0x5348, 0),  # East Asian ideograph
    0x22345B: (0x64B6, 0),  # East Asian ideograph
    0x21345C: (0x534A, 0),  # East Asian ideograph
    0x21345D: (
        0x5349,
        0,
    ),  # East Asian ideograph (variant of 2D345D which maps to 5349)
    0x6F5741: (0xC820, 0),  # Korean hangul
    0x27345F: (0x5346, 0),  # East Asian ideograph
    0x273460: (0x534F, 0),  # East Asian ideograph
    0x213461: (0x5353, 0),  # East Asian ideograph
    0x223462: (0x649F, 0),  # East Asian ideograph
    0x213463: (0x5357, 0),  # East Asian ideograph
    0x213464: (0x535A, 0),  # East Asian ideograph
    0x223465: (0x64A7, 0),  # East Asian ideograph (not in Unicode)
    0x213466: (0x535E, 0),  # East Asian ideograph
    0x213467: (0x5361, 0),  # East Asian ideograph
    0x233468: (0x8B6B, 0),  # East Asian ideograph
    0x213469: (0x5366, 0),  # East Asian ideograph
    0x22346A: (0x64D7, 0),  # East Asian ideograph
    0x21346B: (0x536E, 0),  # East Asian ideograph
    0x21346C: (0x5370, 0),  # East Asian ideograph
    0x21346D: (0x5371, 0),  # East Asian ideograph
    0x21346E: (0x537D, 0),  # East Asian ideograph
    0x21346F: (0x5375, 0),  # East Asian ideograph
    0x233470: (0x8B78, 0),  # East Asian ideograph
    0x213368: (0x5243, 0),  # East Asian ideograph
    0x213473: (0x537B, 0),  # East Asian ideograph
    0x223474: (0x64BE, 0),  # East Asian ideograph
    0x223475: (0x64D0, 0),  # East Asian ideograph
    0x213476: (0x539A, 0),  # East Asian ideograph
    0x213477: (0x539D, 0),  # East Asian ideograph
    0x213478: (0x539F, 0),  # East Asian ideograph
    0x233479: (0x8B81, 0),  # East Asian ideograph
    0x27347A: (0x538C, 0),  # East Asian ideograph
    0x27347B: (0x5389, 0),  # East Asian ideograph
    0x21347C: (0x53BB, 0),  # East Asian ideograph
    0x27347D: (0x53C2, 0),  # East Asian ideograph
    0x21347E: (0x53C8, 0),  # East Asian ideograph
    0x334968: (0x7133, 0),  # East Asian ideograph
    0x23336B: (0x8B0C, 0),  # East Asian ideograph
    0x6F4B72: (0xB10C, 0),  # Korean hangul
    0x6F4A79: (0xAF79, 0),  # Korean hangul
    0x22336C: (0x646B, 0),  # East Asian ideograph
    0x225676: (0x72EB, 0),  # East Asian ideograph
    0x29583E: (0x9CCA, 0),  # East Asian ideograph
    0x21736D: (0x56DD, 0),  # East Asian ideograph
    0x2D4F45: (0x9834, 0),  # East Asian ideograph
    0x274858: (0x6EE1, 0),  # East Asian ideograph
    0x6F5743: (0xC82C, 0),  # Korean hangul
    0x23336F: (0x8B1C, 0),  # East Asian ideograph
    0x234969: (0x95DE, 0),  # East Asian ideograph
    0x694677: (0x5302, 0),  # East Asian ideograph
    0x217370: (0x56DF, 0),  # East Asian ideograph
    0x6F4A7A: (0xAF80, 0),  # Korean hangul
    0x213371: (0x5254, 0),  # East Asian ideograph
    0x333377: (0x5270, 0),  # East Asian ideograph
    0x2D3372: (0x5265, 0),  # East Asian ideograph
    0x6F5D59: (0xD6F0, 0),  # Korean hangul
    0x6F502A: (0xBA53, 0),  # Korean hangul
    0x696F27: (0x933B, 0),  # East Asian ideograph
    0x295C65: (0x9E69, 0),  # East Asian ideograph
    0x213373: (0x526A, 0),  # East Asian ideograph
    0x395E2F: (0x5277, 0),  # East Asian ideograph
    0x287374: (0x7F35, 0),  # East Asian ideograph
    0x225F3C: (0x760A, 0),  # East Asian ideograph
    0x23496A: (0x95E0, 0),  # East Asian ideograph
    0x217375: (0x56EB, 0),  # East Asian ideograph
    0x334527: (0x6918, 0),  # East Asian ideograph
    0x273376: (0x5240, 0),  # East Asian ideograph
    0x6F516A: (0xBE1C, 0),  # Korean hangul
    0x275E21: (0x949F, 0),  # East Asian ideograph
    0x2D3377: (0x8CF8, 0),  # East Asian ideograph
    0x215E22: (0x9318, 0),  # East Asian ideograph
    0x27615F: (0x53D1, 0),  # East Asian ideograph (duplicate simplified)
    0x233378: (0x8B0B, 0),  # East Asian ideograph
    0x215E23: (0x936C, 0),  # East Asian ideograph
    0x27485A: (0x6E10, 0),  # East Asian ideograph
    0x275E24: (0x953B, 0),  # East Asian ideograph
    0x21337A: (0x527D, 0),  # East Asian ideograph
    0x225E25: (0x7583, 0),  # East Asian ideograph
    0x6F583C: (0xC9E4, 0),  # Korean hangul
    0x22337B: (0x6473, 0),  # East Asian ideograph
    0x27374E: (0x549B, 0),  # East Asian ideograph
    0x2D5E26: (0x7194, 0),  # East Asian ideograph
    0x293F4C: (0x90D3, 0),  # East Asian ideograph
    0x21337C: (0x5283, 0),  # East Asian ideograph
    0x215E27: (0x93AE, 0),  # East Asian ideograph
    0x335635: (0x85AC, 0),  # East Asian ideograph
    0x3F3F24: (0x614E, 0),  # East Asian ideograph
    0x23337D: (0x8B10, 0),  # East Asian ideograph
    0x215E28: (0x9396, 0),  # East Asian ideograph
    0x6F5746: (0xC838, 0),  # Korean hangul
    0x21337E: (0x5287, 0),  # East Asian ideograph
    0x275E29: (0x94A8, 0),  # East Asian ideograph
    0x6F4C4D: (0xB233, 0),  # Korean hangul
    0x215E2A: (0x93B3, 0),  # East Asian ideograph
    0x215E2B: (0x93E1, 0),  # East Asian ideograph
    0x213062: (0x4EAD, 0),  # East Asian ideograph
    0x692564: (0x30E4, 0),  # Katakana letter YA
    0x223461: (0x6498, 0),  # East Asian ideograph
    0x29516D: (0x9991, 0),  # East Asian ideograph
    0x215E2C: (0x93D1, 0),  # East Asian ideograph
    0x225E2D: (0x7592, 0),  # East Asian ideograph
    0x4C4D63: (0x6F99, 0),  # East Asian ideograph
    0x6F5747: (0xC83C, 0),  # Korean hangul
    0x215E2E: (0x93C3, 0),  # East Asian ideograph
    0x213D2C: (0x5EE0, 0),  # East Asian ideograph
    0x275E2F: (0x94F2, 0),  # East Asian ideograph
    0x2D6056: (0x980B, 0),  # East Asian ideograph
    0x6F4A7E: (0xAF95, 0),  # Korean hangul
    0x275969: (0x8D1E, 0),  # East Asian ideograph
    0x215E30: (0x93D7, 0),  # East Asian ideograph
    0x213522: (0x53CB, 0),  # East Asian ideograph
    0x233523: (0x8B8B, 0),  # East Asian ideograph
    0x213524: (0x53CD, 0),  # East Asian ideograph
    0x213525: (0x53D6, 0),  # East Asian ideograph
    0x233526: (0x8B87, 0),  # East Asian ideograph
    0x225E31: (0x7595, 0),  # East Asian ideograph
    0x213528: (0x53DB, 0),  # East Asian ideograph
    0x213529: (0x53DF, 0),  # East Asian ideograph
    0x22352A: (0x64EF, 0),  # East Asian ideograph
    0x27352B: (0x4E1B, 0),  # East Asian ideograph
    0x21352C: (0x53E3, 0),  # East Asian ideograph
    0x22352D: (0x64E1, 0),  # East Asian ideograph
    0x22352E: (0x64E5, 0),  # East Asian ideograph
    0x224873: (0x6D63, 0),  # East Asian ideograph
    0x213530: (0x53EF, 0),  # East Asian ideograph
    0x213531: (0x53E9, 0),  # East Asian ideograph
    0x213532: (0x53F3, 0),  # East Asian ideograph
    0x223533: (0x64E2, 0),  # East Asian ideograph
    0x213534: (0x53E8, 0),  # East Asian ideograph
    0x213535: (0x53E6, 0),  # East Asian ideograph
    0x223536: (0x64ED, 0),  # East Asian ideograph
    0x233537: (0x8B9C, 0),  # East Asian ideograph
    0x223538: (0x64E4, 0),  # East Asian ideograph
    0x275E34: (0x9542, 0),  # East Asian ideograph
    0x21353A: (0x53F1, 0),  # East Asian ideograph
    0x21353B: (0x53ED, 0),  # East Asian ideograph
    0x21353C: (0x53EA, 0),  # East Asian ideograph
    0x23353D: (0x8C3A, 0),  # East Asian ideograph
    0x235E35: (0x9EC6, 0),  # East Asian ideograph
    0x213540: (0x5409, 0),  # East Asian ideograph
    0x213541: (0x5410, 0),  # East Asian ideograph
    0x213542: (0x540F, 0),  # East Asian ideograph
    0x235A7B: (0x9D59, 0),  # East Asian ideograph
    0x233544: (0x8C40, 0),  # East Asian ideograph
    0x233545: (0x8C42, 0),  # East Asian ideograph
    0x213546: (0x5404, 0),  # East Asian ideograph
    0x213547: (0x5403, 0),  # East Asian ideograph
    0x213548: (0x5412, 0),  # East Asian ideograph
    0x2D7164: (
        0x55D4,
        0,
    ),  # East Asian ideograph (variant of 217164 which maps to 55D4)
    0x21354A: (0x5406, 0),  # East Asian ideograph (not in Unicode)
    0x23354B: (0x8C47, 0),  # East Asian ideograph
    0x21354D: (0x542D, 0),  # East Asian ideograph
    0x21354E: (0x541D, 0),  # East Asian ideograph
    0x21354F: (0x541E, 0),  # East Asian ideograph
    0x213550: (0x541B, 0),  # East Asian ideograph
    0x213551: (0x544E, 0),  # East Asian ideograph
    0x233552: (0x8C55, 0),  # East Asian ideograph
    0x23496F: (0x95E5, 0),  # East Asian ideograph
    0x233554: (0x8C57, 0),  # East Asian ideograph
    0x213555: (0x5431, 0),  # East Asian ideograph
    0x233556: (0x8C5D, 0),  # East Asian ideograph
    0x213557: (0x543C, 0),  # East Asian ideograph
    0x213558: (0x5443, 0),  # East Asian ideograph
    0x213559: (0x5426, 0),  # East Asian ideograph
    0x21355A: (0x5420, 0),  # East Asian ideograph
    0x22355B: (0x6516, 0),  # East Asian ideograph
    0x23355C: (0x86C3, 0),  # East Asian ideograph
    0x21355D: (0x5435, 0),  # East Asian ideograph
    0x234E26: (0x97B5, 0),  # East Asian ideograph
    0x21355F: (0x544A, 0),  # East Asian ideograph
    0x213560: (0x5448, 0),  # East Asian ideograph
    0x223561: (0x651B, 0),  # East Asian ideograph
    0x213562: (0x5438, 0),  # East Asian ideograph
    0x233563: (0x8C68, 0),  # East Asian ideograph
    0x213564: (0x5442, 0),  # East Asian ideograph
    0x233565: (0x8C6D, 0),  # East Asian ideograph
    0x213566: (0x541F, 0),  # East Asian ideograph
    0x213567: (0x5429, 0),  # East Asian ideograph
    0x213568: (0x5473, 0),  # East Asian ideograph
    0x223569: (0x6527, 0),  # East Asian ideograph
    0x21356A: (0x5475, 0),  # East Asian ideograph
    0x21356B: (0x5495, 0),  # East Asian ideograph
    0x21356C: (0x5478, 0),  # East Asian ideograph
    0x22356D: (0x6522, 0),  # East Asian ideograph
    0x21356E: (0x5477, 0),  # East Asian ideograph
    0x22356F: (0x6529, 0),  # East Asian ideograph
    0x213571: (0x5492, 0),  # East Asian ideograph
    0x223572: (0x6525, 0),  # East Asian ideograph
    0x213573: (0x547C, 0),  # East Asian ideograph
    0x233574: (0x8C76, 0),  # East Asian ideograph
    0x225E3E: (0x75BA, 0),  # East Asian ideograph
    0x213576: (0x548B, 0),  # East Asian ideograph
    0x213577: (0x548C, 0),  # East Asian ideograph
    0x213578: (0x5490, 0),  # East Asian ideograph
    0x213579: (0x547D, 0),  # East Asian ideograph
    0x21357A: (0x5476, 0),  # East Asian ideograph
    0x23357B: (0x8C78, 0),  # East Asian ideograph
    0x22357C: (0x6541, 0),  # East Asian ideograph
    0x23357D: (0x8C7B, 0),  # East Asian ideograph
    0x21357E: (0x54A9, 0),  # East Asian ideograph
    0x275E40: (0x956F, 0),  # East Asian ideograph
    0x23563A: (0x9B48, 0),  # East Asian ideograph
    0x333421: (0x91FC, 0),  # East Asian ideograph
    0x6F574B: (0xC874, 0),  # Korean hangul
    0x234566: (0x9355, 0),  # East Asian ideograph
    0x235E42: (0x9ECC, 0),  # East Asian ideograph
    0x213D30: (0x5EF7, 0),  # East Asian ideograph
    0x6F4C4E: (0xB234, 0),  # Korean hangul
    0x225E43: (0x75B0, 0),  # East Asian ideograph
    0x225E44: (0x75C3, 0),  # East Asian ideograph
    0x27552A: (0x82CB, 0),  # East Asian ideograph
    0x6F5763: (0xC8CC, 0),  # Korean hangul
    0x275E45: (0x94C4, 0),  # East Asian ideograph
    0x225E46: (0x75BF, 0),  # East Asian ideograph
    0x2D5927: (0x8ACC, 0),  # East Asian ideograph
    0x234C38: (0x971B, 0),  # East Asian ideograph
    0x6F574C: (0xC878, 0),  # Korean hangul
    0x225E47: (0x75B4, 0),  # East Asian ideograph
    0x6F5D29: (0xD5F5, 0),  # Korean hangul
    0x6F4B74: (0xB110, 0),  # Korean hangul
    0x23452F: (0x9342, 0),  # East Asian ideograph
    0x27596E: (0x8D2F, 0),  # East Asian ideograph
    0x273755: (0x5411, 0),  # East Asian ideograph
    0x275E49: (0x9523, 0),  # East Asian ideograph
    0x215E4A: (0x947D, 0),  # East Asian ideograph
    0x23563C: (0x9B4E, 0),  # East Asian ideograph
    0x333423: (0x5264, 0),  # East Asian ideograph
    0x275E4B: (0x51FF, 0),  # East Asian ideograph
    0x6F574D: (0xC87A, 0),  # Korean hangul
    0x235E4C: (0x9ED3, 0),  # East Asian ideograph
    0x275E4D: (0x95E8, 0),  # East Asian ideograph
    0x34492F: (0x6D34, 0),  # East Asian ideograph
    0x225E4E: (0x75C1, 0),  # East Asian ideograph
    0x277745: (0x57D9, 0),  # East Asian ideograph
    0x275E4F: (0x95EA, 0),  # East Asian ideograph
    0x4C6F43: (0x7CCD, 0),  # East Asian ideograph
    0x225E50: (0x75B1, 0),  # East Asian ideograph
    0x274863: (0x6D46, 0),  # East Asian ideograph
    0x6F574E: (0xC880, 0),  # Korean hangul
    0x284C62: (0x988D, 0),  # East Asian ideograph
    0x225E51: (0x75C4, 0),  # East Asian ideograph
    0x213D33: (0x5EFA, 0),  # East Asian ideograph
    0x275E52: (0x95F0, 0),  # East Asian ideograph
    0x275970: (0x8D2A, 0),  # East Asian ideograph
    0x215E53: (0x958B, 0),  # East Asian ideograph
    0x275E54: (0x95F2, 0),  # East Asian ideograph
    0x23563E: (0x9B4D, 0),  # East Asian ideograph
    0x215E55: (0x9593, 0),  # East Asian ideograph
    0x274864: (0x6E17, 0),  # East Asian ideograph
    0x6F574F: (0xC881, 0),  # Korean hangul
    0x6F4D29: (0xB355, 0),  # Korean hangul
    0x235E57: (0x9EE3, 0),  # East Asian ideograph
    0x275971: (0x8D2B, 0),  # East Asian ideograph
    0x225E58: (0x75CD, 0),  # East Asian ideograph
    0x215E59: (0x95A8, 0),  # East Asian ideograph
    0x275E5A: (0x95FD, 0),  # East Asian ideograph
    0x6F7727: (0xADD5, 0),  # Korean hangul
    0x213621: (0x54AA, 0),  # East Asian ideograph
    0x213622: (0x54A8, 0),  # East Asian ideograph
    0x213623: (0x54AC, 0),  # East Asian ideograph
    0x213624: (0x54C0, 0),  # East Asian ideograph
    0x213625: (0x54B3, 0),  # East Asian ideograph
    0x213626: (0x54A6, 0),  # East Asian ideograph
    0x213627: (0x54AB, 0),  # East Asian ideograph
    0x213628: (0x54C7, 0),  # East Asian ideograph
    0x213629: (0x54C9, 0),  # East Asian ideograph
    0x21362A: (0x54C4, 0),  # East Asian ideograph
    0x21362B: (0x54C2, 0),  # East Asian ideograph
    0x22362C: (0x6538, 0),  # East Asian ideograph
    0x21362D: (0x54C1, 0),  # East Asian ideograph
    0x23362E: (0x8C88, 0),  # East Asian ideograph
    0x21362F: (0x54CE, 0),  # East Asian ideograph
    0x213630: (0x54B1, 0),  # East Asian ideograph
    0x213631: (0x54BB, 0),  # East Asian ideograph
    0x213632: (0x54AF, 0),  # East Asian ideograph
    0x213633: (0x54C8, 0),  # East Asian ideograph
    0x223634: (0x6542, 0),  # East Asian ideograph
    0x225E5E: (0x75CC, 0),  # East Asian ideograph
    0x213636: (0x5510, 0),  # East Asian ideograph
    0x213637: (0x54EA, 0),  # East Asian ideograph
    0x213638: (0x5514, 0),  # East Asian ideograph
    0x233639: (0x8C94, 0),  # East Asian ideograph
    0x21363A: (0x54E5, 0),  # East Asian ideograph
    0x225E5F: (0x75D0, 0),  # East Asian ideograph
    0x21363C: (0x54F2, 0),  # East Asian ideograph
    0x21363D: (0x54E8, 0),  # East Asian ideograph
    0x21363E: (0x54E1, 0),  # East Asian ideograph
    0x22363F: (0x6555, 0),  # East Asian ideograph
    0x213640: (0x54ED, 0),  # East Asian ideograph
    0x233641: (0x8C9B, 0),  # East Asian ideograph
    0x213642: (0x5509, 0),  # East Asian ideograph
    0x213643: (0x54E6, 0),  # East Asian ideograph
    0x233644: (0x8CA4, 0),  # East Asian ideograph
    0x223645: (0x6567, 0),  # East Asian ideograph
    0x213646: (0x5546, 0),  # East Asian ideograph
    0x223647: (0x6561, 0),  # East Asian ideograph
    0x213648: (0x554F, 0),  # East Asian ideograph
    0x273649: (0x54D1, 0),  # East Asian ideograph
    0x21364A: (0x5566, 0),  # East Asian ideograph
    0x21364B: (0x556A, 0),  # East Asian ideograph
    0x21364C: (0x554A, 0),  # East Asian ideograph
    0x21364D: (0x5544, 0),  # East Asian ideograph
    0x21364E: (0x555C, 0),  # East Asian ideograph
    0x22364F: (0x656D, 0),  # East Asian ideograph
    0x213650: (0x5543, 0),  # East Asian ideograph
    0x213651: (0x552C, 0),  # East Asian ideograph
    0x213652: (0x5561, 0),  # East Asian ideograph
    0x233653: (0x8CB9, 0),  # East Asian ideograph
    0x223654: (0x657A, 0),  # East Asian ideograph
    0x213655: (0x5555, 0),  # East Asian ideograph
    0x213656: (0x552F, 0),  # East Asian ideograph
    0x233657: (0x8CCD, 0),  # East Asian ideograph
    0x213658: (0x5564, 0),  # East Asian ideograph
    0x213659: (0x5538, 0),  # East Asian ideograph
    0x21365A: (0x55A7, 0),  # East Asian ideograph
    0x21365B: (0x5580, 0),  # East Asian ideograph
    0x21365C: (0x557B, 0),  # East Asian ideograph
    0x21365D: (0x557C, 0),  # East Asian ideograph
    0x21365E: (0x5527, 0),  # East Asian ideograph
    0x21365F: (0x5594, 0),  # East Asian ideograph
    0x213660: (0x5587, 0),  # East Asian ideograph
    0x213661: (0x559C, 0),  # East Asian ideograph
    0x213662: (0x558B, 0),  # East Asian ideograph
    0x273663: (0x4E27, 0),  # East Asian ideograph
    0x213664: (0x55B3, 0),  # East Asian ideograph
    0x225E66: (0x75E1, 0),  # East Asian ideograph
    0x213666: (0x5583, 0),  # East Asian ideograph
    0x213667: (0x55B1, 0),  # East Asian ideograph
    0x273668: (0x5355, 0),  # East Asian ideograph
    0x213669: (0x5582, 0),  # East Asian ideograph
    0x21366A: (0x559F, 0),  # East Asian ideograph
    0x225E67: (0x75E6, 0),  # East Asian ideograph
    0x21366C: (0x5598, 0),  # East Asian ideograph
    0x21366D: (0x559A, 0),  # East Asian ideograph
    0x22366E: (0x658C, 0),  # East Asian ideograph
    0x27366F: (0x4E54, 0),  # East Asian ideograph
    0x223670: (0x6592, 0),  # East Asian ideograph
    0x213671: (0x55B2, 0),  # East Asian ideograph
    0x233672: (0x8CDD, 0),  # East Asian ideograph
    0x213673: (0x55E8, 0),  # East Asian ideograph
    0x233674: (0x8CD9, 0),  # East Asian ideograph
    0x223675: (0x659B, 0),  # East Asian ideograph
    0x213676: (0x55DC, 0),  # East Asian ideograph
    0x223677: (0x659D, 0),  # East Asian ideograph
    0x213678: (0x55C7, 0),  # East Asian ideograph
    0x213679: (0x55D3, 0),  # East Asian ideograph
    0x21367A: (0x55CE, 0),  # East Asian ideograph
    0x21367B: (0x55E3, 0),  # East Asian ideograph
    0x23367C: (0x8CF5, 0),  # East Asian ideograph
    0x21367D: (0x55E4, 0),  # East Asian ideograph
    0x23367E: (0x8CFB, 0),  # East Asian ideograph
    0x232760: (0x8600, 0),  # East Asian ideograph
    0x275E6B: (0x8F9F, 0),  # East Asian ideograph (duplicate simplified)
    0x285424: (0x70E8, 0),  # East Asian ideograph
    0x27375C: (0x556D, 0),  # East Asian ideograph
    0x4B5E6C: (0x961D, 0),  # East Asian ideograph (duplicate simplified)
    0x293F5A: (0x90E7, 0),  # East Asian ideograph
    0x235E6F: (0x9EF6, 0),  # East Asian ideograph
    0x4B5422: (0x81D3, 0),  # East Asian ideograph
    0x6F583F: (0xC9EC, 0),  # Korean hangul
    0x27375D: (0x55EB, 0),  # East Asian ideograph
    0x225E71: (0x75E4, 0),  # East Asian ideograph
    0x225E72: (0x75E0, 0),  # East Asian ideograph
    0x4B4759: (0x6D99, 0),  # East Asian ideograph
    0x6F4B66: (0xB0C7, 0),  # Korean hangul
    0x225E73: (0x75D7, 0),  # East Asian ideograph
    0x6F5755: (0xC88D, 0),  # Korean hangul
    0x235E74: (0x9EF9, 0),  # East Asian ideograph
    0x275977: (0x8D3A, 0),  # East Asian ideograph
    0x27375E: (0x56A3, 0),  # East Asian ideograph
    0x235E76: (0x9EFB, 0),  # East Asian ideograph
    0x274921: (0x6CFD, 0),  # East Asian ideograph
    0x293F5C: (0x90AC, 0),  # East Asian ideograph
    0x2D616A: (0x6B1D, 0),  # East Asian ideograph
    0x215E77: (0x964C, 0),  # East Asian ideograph
    0x274922: (0x6D4A, 0),  # East Asian ideograph
    0x6F5756: (0xC890, 0),  # Korean hangul
    0x6F4924: (0xAC74, 0),  # Korean hangul
    0x6F4B76: (0xB118, 0),  # Korean hangul
    0x215E7A: (0x9662, 0),  # East Asian ideograph
    0x224925: (0x6D6D, 0),  # East Asian ideograph
    0x275978: (0x8D35, 0),  # East Asian ideograph
    0x235E7B: (0x9EFE, 0),  # East Asian ideograph (not in Unicode)
    0x274926: (0x6D4E, 0),  # East Asian ideograph
    0x215E7C: (0x965B, 0),  # East Asian ideograph
    0x274927: (0x6CDE, 0),  # East Asian ideograph
    0x235E7D: (0x9F02, 0),  # East Asian ideograph
    0x274928: (0x6EE8, 0),  # East Asian ideograph
    0x6F5757: (0xC894, 0),  # Korean hangul
    0x215E7E: (0x965D, 0),  # East Asian ideograph
    0x224929: (0x6D91, 0),  # East Asian ideograph
    0x287065: (0x7EC2, 0),  # East Asian ideograph
    0x2F4231: (0x8019, 0),  # Unrelated variant of EACC 215266 which maps to 8019
    0x6F492A: (0xAC81, 0),  # Korean hangul
    0x33492E: (0x6F81, 0),  # East Asian ideograph
    0x27492B: (0x6EE5, 0),  # East Asian ideograph
    0x33337B: (0x52E6, 0),  # East Asian ideograph
    0x233871: (0x8DC2, 0),  # East Asian ideograph
    0x22492C: (0x6D81, 0),  # East Asian ideograph
    0x235647: (0x9B51, 0),  # East Asian ideograph
    0x33463C: (0x6BBB, 0),  # East Asian ideograph
    0x27492D: (0x6D9B, 0),  # East Asian ideograph
    0x6F553A: (0xC587, 0),  # Korean hangul
    0x27492E: (0x6DA9, 0),  # East Asian ideograph
    0x22413C: (0x6A5A, 0),  # East Asian ideograph
    0x2E492F: (0x6CD9, 0),  # East Asian ideograph
    0x27597A: (0x4E70, 0),  # East Asian ideograph
    0x213331: (0x518D, 0),  # East Asian ideograph
    0x273761: (0x7F57, 0),  # East Asian ideograph (duplicate simplified)
    0x213721: (0x55DA, 0),  # East Asian ideograph
    0x223722: (0x65A8, 0),  # East Asian ideograph
    0x223723: (0x65A6, 0),  # East Asian ideograph
    0x213724: (0x5600, 0),  # East Asian ideograph
    0x233725: (0x8D04, 0),  # East Asian ideograph
    0x213726: (0x55FE, 0),  # East Asian ideograph
    0x273727: (0x5567, 0),  # East Asian ideograph
    0x213728: (0x55F7, 0),  # East Asian ideograph
    0x213729: (0x5608, 0),  # East Asian ideograph
    0x22372A: (0x65B6, 0),  # East Asian ideograph
    0x21372B: (0x55FD, 0),  # East Asian ideograph
    0x22372C: (0x65B8, 0),  # East Asian ideograph
    0x23372D: (0x8D09, 0),  # East Asian ideograph
    0x21372E: (0x5614, 0),  # East Asian ideograph
    0x22372F: (0x65BF, 0),  # East Asian ideograph
    0x273730: (0x5C1D, 0),  # East Asian ideograph
    0x273731: (0x55BD, 0),  # East Asian ideograph
    0x273732: (0x5520, 0),  # East Asian ideograph
    0x213733: (0x562F, 0),  # East Asian ideograph
    0x223734: (0x65C2, 0),  # East Asian ideograph
    0x213735: (0x5636, 0),  # East Asian ideograph
    0x213736: (0x5632, 0),  # East Asian ideograph
    0x213737: (0x563B, 0),  # East Asian ideograph
    0x213738: (0x5639, 0),  # East Asian ideograph
    0x274934: (0x6E85, 0),  # East Asian ideograph
    0x23373A: (0x8D10, 0),  # East Asian ideograph
    0x22373B: (0x65D0, 0),  # East Asian ideograph
    0x22373C: (0x65D2, 0),  # East Asian ideograph
    0x21373D: (0x5634, 0),  # East Asian ideograph
    0x23373E: (0x8D18, 0),  # East Asian ideograph
    0x224935: (0x6DEF, 0),  # East Asian ideograph
    0x213740: (0x5630, 0),  # East Asian ideograph
    0x213741: (0x566B, 0),  # East Asian ideograph
    0x213742: (0x5664, 0),  # East Asian ideograph
    0x213743: (0x5669, 0),  # East Asian ideograph
    0x223744: (0x65DB, 0),  # East Asian ideograph
    0x213745: (0x5674, 0),  # East Asian ideograph
    0x273746: (0x5F53, 0),  # East Asian ideograph (duplicate simplified)
    0x213747: (0x5665, 0),  # East Asian ideograph
    0x213748: (0x566A, 0),  # East Asian ideograph
    0x213749: (0x5668, 0),  # East Asian ideograph
    0x22374A: (0x65E1, 0),  # East Asian ideograph
    0x27374B: (0x55F3, 0),  # East Asian ideograph
    0x225A23: (0x7429, 0),  # East Asian ideograph
    0x21374D: (0x566C, 0),  # East Asian ideograph
    0x21374E: (0x5680, 0),  # East Asian ideograph
    0x21374F: (0x568E, 0),  # East Asian ideograph
    0x213750: (0x5685, 0),  # East Asian ideograph
    0x214938: (0x701B, 0),  # East Asian ideograph
    0x233752: (0x8D78, 0),  # East Asian ideograph
    0x213753: (0x568F, 0),  # East Asian ideograph
    0x223754: (0x65F4, 0),  # East Asian ideograph
    0x213755: (
        0x56AE,
        0,
    ),  # East Asian ideograph (variant of 453755 which maps to 56AE)
    0x273756: (0x5499, 0),  # East Asian ideograph
    0x224939: (0x6D7F, 0),  # East Asian ideograph
    0x213758: (0x56A5, 0),  # East Asian ideograph
    0x213759: (0x56B7, 0),  # East Asian ideograph
    0x22375A: (0x6609, 0),  # East Asian ideograph
    0x27375B: (0x5624, 0),  # East Asian ideograph
    0x21375C: (0x56C0, 0),  # East Asian ideograph
    0x21493A: (0x7028, 0),  # East Asian ideograph
    0x22375E: (0x660A, 0),  # East Asian ideograph
    0x21375F: (0x56BC, 0),  # East Asian ideograph
    0x213760: (0x56CA, 0),  # East Asian ideograph
    0x213761: (0x56C9, 0),  # East Asian ideograph
    0x273762: (0x5453, 0),  # East Asian ideograph
    0x22493B: (0x6D85, 0),  # East Asian ideograph
    0x223764: (0x6603, 0),  # East Asian ideograph
    0x213765: (0x56DB, 0),  # East Asian ideograph
    0x213766: (0x56DA, 0),  # East Asian ideograph
    0x213767: (0x56E0, 0),  # East Asian ideograph
    0x213768: (0x56DE, 0),  # East Asian ideograph
    0x21493C: (0x7015, 0),  # East Asian ideograph
    0x22376A: (0x6611, 0),  # East Asian ideograph
    0x22376B: (0x6615, 0),  # East Asian ideograph
    0x21376C: (0x56FA, 0),  # East Asian ideograph
    0x22376D: (0x6604, 0),  # East Asian ideograph
    0x22376E: (0x6631, 0),  # East Asian ideograph
    0x21376F: (0x570B, 0),  # East Asian ideograph
    0x213770: (0x570D, 0),  # East Asian ideograph
    0x233771: (0x8D94, 0),  # East Asian ideograph
    0x223772: (0x6621, 0),  # East Asian ideograph
    0x273773: (0x56E2, 0),  # East Asian ideograph
    0x273774: (0x56FE, 0),  # East Asian ideograph
    0x223775: (0x662C, 0),  # East Asian ideograph
    0x223777: (0x6635, 0),  # East Asian ideograph
    0x213778: (0x572F, 0),  # East Asian ideograph
    0x213779: (0x5730, 0),  # East Asian ideograph
    0x21377A: (0x5728, 0),  # East Asian ideograph
    0x21377B: (0x5733, 0),  # East Asian ideograph
    0x22377C: (0x661E, 0),  # East Asian ideograph
    0x22377D: (0x663A, 0),  # East Asian ideograph
    0x224940: (0x6D67, 0),  # East Asian ideograph
    0x274941: (0x6D12, 0),  # East Asian ideograph
    0x2E3144: (0x651F, 0),  # East Asian ideograph
    0x274942: (0x6EE9, 0),  # East Asian ideograph
    0x212A34: (0xE8E1, 0),  # EACC component character
    0x214943: (0x7063, 0),  # East Asian ideograph
    0x274944: (0x6EE6, 0),  # East Asian ideograph
    0x4B5A3B: (0x8D08, 0),  # East Asian ideograph
    0x4B4761: (0x6E05, 0),  # East Asian ideograph
    0x213F21: (0x6148, 0),  # East Asian ideograph
    0x224946: (0x6D60, 0),  # East Asian ideograph
    0x2D4B35: (0x73C9, 0),  # East Asian ideograph
    0x2D4947: (0x7AC8, 0),  # East Asian ideograph
    0x394C2D: (0x7546, 0),  # East Asian ideograph
    0x224948: (0x6D98, 0),  # East Asian ideograph
    0x6F516F: (0xBE48, 0),  # Korean hangul
    0x234949: (0x95BE, 0),  # East Asian ideograph
    0x217068: (0x5530, 0),  # East Asian ideograph
    0x295D3A: (0x9E73, 0),  # East Asian ideograph
    0x27494A: (0x707E, 0),  # East Asian ideograph
    0x225352: (0x71A0, 0),  # East Asian ideograph
    0x234644: (0x93BD, 0),  # East Asian ideograph
    0x22494B: (0x6D7C, 0),  # East Asian ideograph
    0x6F575E: (0xC8AC, 0),  # Korean hangul
    0x22494C: (0x6D70, 0),  # East Asian ideograph
    0x21494D: (0x7092, 0),  # East Asian ideograph
    0x23494E: (0x95BA, 0),  # East Asian ideograph
    0x295D3B: (0x9E42, 0),  # East Asian ideograph
    0x23494F: (0x95B6, 0),  # East Asian ideograph
    0x2E3E3F: (0x7BA0, 0),  # East Asian ideograph
    0x234950: (0x95BF, 0),  # East Asian ideograph
    0x225278: (0x7178, 0),  # East Asian ideograph
    0x274951: (0x4E3A, 0),  # East Asian ideograph
    0x213D44: (0x5F29, 0),  # East Asian ideograph
    0x334674: (0x76C5, 0),  # East Asian ideograph
    0x234952: (0x95BD, 0),  # East Asian ideograph
    0x6F4953: (0xACF1, 0),  # Korean hangul
    0x21392A: (0x592E, 0),  # East Asian ideograph
    0x295D3C: (0x5364, 0),  # East Asian ideograph
    0x2D4954: (0x70F1, 0),  # East Asian ideograph
    0x6F4955: (0xACF5, 0),  # Korean hangul
    0x22526B: (0x7153, 0),  # East Asian ideograph
    0x6F5760: (0xC8B8, 0),  # Korean hangul
    0x2D4956: (0x70B0, 0),  # East Asian ideograph
    0x213D45: (0x5F2D, 0),  # East Asian ideograph
    0x4B5871: (0x8AA4, 0),  # East Asian ideograph
    0x6F4B78: (0xB11B, 0),  # Korean hangul
    0x6F4957: (0xACFA, 0),  # Korean hangul
    0x6F4958: (0xACFC, 0),  # Korean hangul
    0x284339: (0x680A, 0),  # East Asian ideograph
    0x22746A: (0x7F7F, 0),  # East Asian ideograph
    0x225251: (0x7146, 0),  # East Asian ideograph
    0x234959: (0x95C9, 0),  # East Asian ideograph
    0x22495A: (0x6DB4, 0),  # East Asian ideograph
    0x6F5761: (0xC8C4, 0),  # Korean hangul
    0x213821: (0x5740, 0),  # East Asian ideograph
    0x233822: (0x8D96, 0),  # East Asian ideograph
    0x213823: (0x574D, 0),  # East Asian ideograph
    0x213824: (0x573E, 0),  # East Asian ideograph
    0x213825: (0x574E, 0),  # East Asian ideograph
    0x223827: (0x6633, 0),  # East Asian ideograph
    0x223828: (0x662B, 0),  # East Asian ideograph
    0x22495C: (0x6DAA, 0),  # East Asian ideograph
    0x21382A: (0x5777, 0),  # East Asian ideograph
    0x22382B: (0x6634, 0),  # East Asian ideograph
    0x22382C: (0x6624, 0),  # East Asian ideograph
    0x21382D: (0x5766, 0),  # East Asian ideograph
    0x21382E: (0x5782, 0),  # East Asian ideograph
    0x21495D: (0x70CF, 0),  # East Asian ideograph
    0x213830: (0x57A0, 0),  # East Asian ideograph
    0x223831: (0x6645, 0),  # East Asian ideograph
    0x213832: (0x57A3, 0),  # East Asian ideograph
    0x233833: (0x8DA6, 0),  # East Asian ideograph
    0x213834: (0x57A2, 0),  # East Asian ideograph
    0x213835: (0x57D4, 0),  # East Asian ideograph
    0x213836: (0x57C2, 0),  # East Asian ideograph
    0x213837: (0x57CE, 0),  # East Asian ideograph
    0x213838: (0x57CB, 0),  # East Asian ideograph
    0x213839: (0x57C3, 0),  # East Asian ideograph
    0x21383A: (0x57F9, 0),  # East Asian ideograph
    0x27383B: (0x6267, 0),  # East Asian ideograph
    0x21383C: (0x57FA, 0),  # East Asian ideograph
    0x22383D: (0x6665, 0),  # East Asian ideograph
    0x22383E: (0x665C, 0),  # East Asian ideograph
    0x22383F: (0x6661, 0),  # East Asian ideograph
    0x213840: (0x5802, 0),  # East Asian ideograph
    0x224960: (0x6DEC, 0),  # East Asian ideograph
    0x213842: (0x57E4, 0),  # East Asian ideograph
    0x213843: (0x57E0, 0),  # East Asian ideograph
    0x273844: (0x62A5, 0),  # East Asian ideograph
    0x273845: (0x5C27, 0),  # East Asian ideograph
    0x213846: (0x5835, 0),  # East Asian ideograph
    0x213847: (0x582A, 0),  # East Asian ideograph
    0x223848: (0x665B, 0),  # East Asian ideograph
    0x223849: (0x6659, 0),  # East Asian ideograph
    0x22384A: (0x6667, 0),  # East Asian ideograph
    0x21384B: (0x5821, 0),  # East Asian ideograph
    0x21384C: (0x585E, 0),  # East Asian ideograph
    0x22384D: (0x6657, 0),  # East Asian ideograph
    0x275541: (0x83B1, 0),  # East Asian ideograph
    0x21384F: (0x5851, 0),  # East Asian ideograph
    0x213850: (0x586B, 0),  # East Asian ideograph
    0x223851: (0x666C, 0),  # East Asian ideograph
    0x233852: (0x8DAB, 0),  # East Asian ideograph
    0x234963: (0x95D3, 0),  # East Asian ideograph
    0x213854: (0x5854, 0),  # East Asian ideograph
    0x273855: (0x575E, 0),  # East Asian ideograph
    0x213856: (0x584A, 0),  # East Asian ideograph
    0x213857: (0x5883, 0),  # East Asian ideograph
    0x213858: (0x587E, 0),  # East Asian ideograph
    0x234964: (0x95D1, 0),  # East Asian ideograph
    0x23385A: (0x8DB0, 0),  # East Asian ideograph
    0x27385B: (0x5811, 0),  # East Asian ideograph
    0x216061: (0x98BC, 0),  # East Asian ideograph
    0x21385D: (0x5893, 0),  # East Asian ideograph
    0x21385E: (0x589E, 0),  # East Asian ideograph
    0x234965: (0x95C3, 0),  # East Asian ideograph
    0x273860: (0x575F, 0),  # East Asian ideograph
    0x273861: (0x5760, 0),  # East Asian ideograph
    0x273862: (0x5815, 0),  # East Asian ideograph
    0x213863: (0x589F, 0),  # East Asian ideograph
    0x273864: (0x575B, 0),  # East Asian ideograph
    0x274966: (0x65E0, 0),  # East Asian ideograph
    0x233866: (0x8DB2, 0),  # East Asian ideograph
    0x273867: (0x57A6, 0),  # East Asian ideograph
    0x223868: (0x6677, 0),  # East Asian ideograph
    0x273869: (0x538B, 0),  # East Asian ideograph
    0x21386A: (0x58D1, 0),  # East Asian ideograph
    0x27386B: (0x5739, 0),  # East Asian ideograph
    0x21386C: (0x58D8, 0),  # East Asian ideograph
    0x27386D: (0x5784, 0),  # East Asian ideograph
    0x23386E: (0x8DBC, 0),  # East Asian ideograph
    0x27386F: (0x575C, 0),  # East Asian ideograph
    0x233870: (0x8DB9, 0),  # East Asian ideograph
    0x223871: (0x668C, 0),  # East Asian ideograph
    0x233872: (0x8DC1, 0),  # East Asian ideograph
    0x213873: (0x58EC, 0),  # East Asian ideograph
    0x213874: (0x58EF, 0),  # East Asian ideograph
    0x223875: (0x668B, 0),  # East Asian ideograph
    0x273876: (0x58F6, 0),  # East Asian ideograph
    0x273877: (0x5BFF, 0),  # East Asian ideograph
    0x213878: (0x590F, 0),  # East Asian ideograph
    0x223879: (0x6694, 0),  # East Asian ideograph
    0x22387A: (0x668A, 0),  # East Asian ideograph
    0x21387B: (0x5916, 0),  # East Asian ideograph
    0x22387C: (0x6698, 0),  # East Asian ideograph
    0x22387D: (0x668D, 0),  # East Asian ideograph
    0x21387E: (0x591C, 0),  # East Asian ideograph
    0x234547: (0x936A, 0),  # East Asian ideograph
    0x22496B: (0x6DB7, 0),  # East Asian ideograph
    0x2D3F54: (0x61D0, 0),  # East Asian ideograph
    0x22496C: (0x6DE2, 0),  # East Asian ideograph
    0x6F5768: (0xC8E4, 0),  # Korean hangul
    0x4B393E: (0x5965, 0),  # East Asian ideograph
    0x27496D: (0x70E6, 0),  # East Asian ideograph
    0x22496E: (0x6DE9, 0),  # East Asian ideograph
    0x6F5765: (0xC8D5, 0),  # Korean hangul
    0x27496F: (0x7080, 0),  # East Asian ideograph
    0x21763E: (0x5810, 0),  # East Asian ideograph
    0x6F4B79: (0xB11C, 0),  # Korean hangul
    0x4D5053: (0x98DA, 0),  # East Asian ideograph
    0x6F4970: (0xAD70, 0),  # Korean hangul
    0x224247: (0x6A90, 0),  # East Asian ideograph
    0x224971: (0x6DF6, 0),  # East Asian ideograph
    0x28433A: (0x69E0, 0),  # East Asian ideograph
    0x295D42: (0x9E7E, 0),  # East Asian ideograph
    0x234972: (0x95E4, 0),  # East Asian ideograph
    0x6F7622: (0x3186, 0),  # Korean hangul
    0x27487B: (0x6DC0, 0),  # East Asian ideograph
    0x6F5766: (0xC8D7, 0),  # Korean hangul
    0x215F64: (0x971C, 0),  # East Asian ideograph
    0x213D4B: (0x5F48, 0),  # East Asian ideograph
    0x274975: (0x6247, 0),  # East Asian ideograph
    0x6F4976: (0xAD7D, 0),  # Korean hangul
    0x213421: (0x528D, 0),  # East Asian ideograph
    0x225257: (0x7160, 0),  # East Asian ideograph
    0x4B4977: (0x7188, 0),  # East Asian ideograph
    0x233422: (0x8B2B, 0),  # East Asian ideograph
    0x6F4978: (0xAD81, 0),  # Korean hangul
    0x4B4339: (0x6674, 0),  # East Asian ideograph
    0x223423: (0x644E, 0),  # East Asian ideograph
    0x223D6A: (0x6910, 0),  # East Asian ideograph
    0x224979: (0x6E0F, 0),  # East Asian ideograph
    0x213424: (0x529B, 0),  # East Asian ideograph
    0x22414B: (0x6A5C, 0),  # East Asian ideograph
    0x23497A: (0x961E, 0),  # East Asian ideograph
    0x283671: (0x6593, 0),  # East Asian ideograph
    0x23497B: (0x9624, 0),  # East Asian ideograph
    0x23497C: (0x9622, 0),  # East Asian ideograph
    0x213427: (0x52A3, 0),  # East Asian ideograph
    0x4B5963: (0x734F, 0),  # East Asian ideograph
    0x27497D: (0x70ED, 0),  # East Asian ideograph
    0x213428: (0x52AB, 0),  # East Asian ideograph
    0x27497E: (0x70EB, 0),  # East Asian ideograph
    0x213429: (0x52A9, 0),  # East Asian ideograph
    0x275D47: (0x9499, 0),  # East Asian ideograph
    0x23342A: (0x8B37, 0),  # East Asian ideograph
    0x273771: (0x56ED, 0),  # East Asian ideograph
    0x6F5843: (0xC9F1, 0),  # Korean hangul
    0x21342C: (0x52BE, 0),  # East Asian ideograph
    0x2D4F6B: (0x7AF8, 0),  # East Asian ideograph
    0x4C2962: (
        0x5F4D,
        0,
    ),  # East Asian ideograph (variant of 222962 which maps to 5F4D)
    0x21342D: (0x52C7, 0),  # East Asian ideograph
    0x334C37: (0x8E6F, 0),  # East Asian ideograph
    0x215F67: (0x9727, 0),  # East Asian ideograph
    0x21742E: (0x5707, 0),  # East Asian ideograph
    0x23454C: (0x934F, 0),  # East Asian ideograph
    0x2D6078: (0x9920, 0),  # East Asian ideograph
    0x21342F: (0x52C1, 0),  # East Asian ideograph
    0x273772: (0x5706, 0),  # East Asian ideograph
    0x233921: (0x8DCF, 0),  # East Asian ideograph
    0x233922: (0x8DD6, 0),  # East Asian ideograph
    0x273923: (0x4F19, 0),  # East Asian ideograph
    0x223924: (0x7A25, 0),  # East Asian ideograph
    0x213925: (0x5927, 0),  # East Asian ideograph
    0x213926: (0x592A, 0),  # East Asian ideograph
    0x233927: (0x8DD0, 0),  # East Asian ideograph
    0x213928: (0x5929, 0),  # East Asian ideograph
    0x213929: (0x592D, 0),  # East Asian ideograph
    0x22392A: (0x66A0, 0),  # East Asian ideograph
    0x23392B: (0x8DC5, 0),  # East Asian ideograph
    0x21392C: (0x5937, 0),  # East Asian ideograph
    0x217432: (0x5714, 0),  # East Asian ideograph
    0x27392E: (0x5939, 0),  # East Asian ideograph
    0x23392F: (0x8DE4, 0),  # East Asian ideograph
    0x223930: (0x5C21, 0),  # East Asian ideograph
    0x213931: (0x5948, 0),  # East Asian ideograph
    0x223932: (0x669D, 0),  # East Asian ideograph
    0x213433: (0x52D9, 0),  # East Asian ideograph
    0x213934: (0x5955, 0),  # East Asian ideograph
    0x233935: (0x8DEB, 0),  # East Asian ideograph
    0x233936: (0x8DF4, 0),  # East Asian ideograph
    0x213937: (0x594F, 0),  # East Asian ideograph
    0x233938: (0x8DE9, 0),  # East Asian ideograph
    0x213434: (0x52D5, 0),  # East Asian ideograph
    0x22393A: (0x66B2, 0),  # East Asian ideograph
    0x23393B: (0x8DE3, 0),  # East Asian ideograph
    0x21393C: (0x5960, 0),  # East Asian ideograph
    0x23393D: (0x8DE7, 0),  # East Asian ideograph
    0x21393E: (0x5967, 0),  # East Asian ideograph
    0x23393F: (0x8E09, 0),  # East Asian ideograph
    0x223940: (0x66B5, 0),  # East Asian ideograph
    0x273941: (0x594B, 0),  # East Asian ideograph
    0x213942: (0x5973, 0),  # East Asian ideograph
    0x223943: (0x66AC, 0),  # East Asian ideograph
    0x233944: (0x8DFF, 0),  # East Asian ideograph
    0x213945: (0x5984, 0),  # East Asian ideograph
    0x233946: (0x8E05, 0),  # East Asian ideograph
    0x223947: (0x66B1, 0),  # East Asian ideograph
    0x213948: (0x597D, 0),  # East Asian ideograph
    0x233949: (0x8E01, 0),  # East Asian ideograph
    0x21394A: (0x5982, 0),  # East Asian ideograph
    0x21394B: (0x5981, 0),  # East Asian ideograph
    0x21394C: (0x59A8, 0),  # East Asian ideograph
    0x21394D: (0x5992, 0),  # East Asian ideograph
    0x23394E: (0x8E04, 0),  # East Asian ideograph
    0x22394F: (0x66BE, 0),  # East Asian ideograph
    0x233950: (0x8E06, 0),  # East Asian ideograph
    0x233438: (0x8B3E, 0),  # East Asian ideograph
    0x233952: (0x8E2A, 0),  # East Asian ideograph
    0x273953: (0x5986, 0),  # East Asian ideograph
    0x223954: (0x66C0, 0),  # East Asian ideograph
    0x223955: (0x66C7, 0),  # East Asian ideograph
    0x213956: (0x598A, 0),  # East Asian ideograph
    0x233957: (0x8E2E, 0),  # East Asian ideograph
    0x233958: (0x8E21, 0),  # East Asian ideograph
    0x213959: (0x59BB, 0),  # East Asian ideograph
    0x22395A: (0x66BB, 0),  # East Asian ideograph
    0x21395B: (0x59D1, 0),  # East Asian ideograph
    0x22395C: (0x66C4, 0),  # East Asian ideograph
    0x21343A: (0x52DF, 0),  # East Asian ideograph
    0x21395E: (0x59D0, 0),  # East Asian ideograph
    0x21395F: (0x59D7, 0),  # East Asian ideograph
    0x223960: (0x66CF, 0),  # East Asian ideograph
    0x213961: (0x59D2, 0),  # East Asian ideograph
    0x213962: (0x59D3, 0),  # East Asian ideograph
    0x213963: (0x59CA, 0),  # East Asian ideograph
    0x233964: (0x8E16, 0),  # East Asian ideograph
    0x213965: (0x59CB, 0),  # East Asian ideograph
    0x233966: (0x8E26, 0),  # East Asian ideograph
    0x213967: (0x59E3, 0),  # East Asian ideograph
    0x233968: (0x8E14, 0),  # East Asian ideograph
    0x213969: (0x59FF, 0),  # East Asian ideograph
    0x21396A: (0x59D8, 0),  # East Asian ideograph
    0x21396B: (0x5A03, 0),  # East Asian ideograph
    0x21396C: (0x59E8, 0),  # East Asian ideograph
    0x21396D: (0x59E5, 0),  # East Asian ideograph
    0x21396E: (0x59EA, 0),  # East Asian ideograph
    0x23396F: (0x8E41, 0),  # East Asian ideograph
    0x213970: (0x59FB, 0),  # East Asian ideograph
    0x223971: (0x66DA, 0),  # East Asian ideograph
    0x223972: (0x66DB, 0),  # East Asian ideograph
    0x223973: (0x66E2, 0),  # East Asian ideograph
    0x213974: (0x5A18, 0),  # East Asian ideograph
    0x213975: (0x5A23, 0),  # East Asian ideograph
    0x223976: (0x66E1, 0),  # East Asian ideograph
    0x233977: (0x8E40, 0),  # East Asian ideograph
    0x223978: (0x66E8, 0),  # East Asian ideograph
    0x233979: (0x8E36, 0),  # East Asian ideograph
    0x21397A: (0x5A1F, 0),  # East Asian ideograph
    0x21397B: (0x5A1B, 0),  # East Asian ideograph
    0x22397C: (0x66E9, 0),  # East Asian ideograph
    0x21397D: (0x5A29, 0),  # East Asian ideograph
    0x23397E: (0x8E3D, 0),  # East Asian ideograph
    0x27785A: (0x5785, 0),  # East Asian ideograph
    0x217441: (0x5724, 0),  # East Asian ideograph
    0x6F532A: (0xC12A, 0),  # Korean hangul
    0x213442: (0x5306, 0),  # East Asian ideograph
    0x334550: (0x7F47, 0),  # East Asian ideograph
    0x232337: (0x846E, 0),  # East Asian ideograph
    0x217443: (0x5729, 0),  # East Asian ideograph
    0x4B5521: (0x8332, 0),  # East Asian ideograph
    0x233444: (0x8B54, 0),  # East Asian ideograph
    0x235C71: (0x9E07, 0),  # East Asian ideograph
    0x22525E: (0x7176, 0),  # East Asian ideograph
    0x213445: (0x5310, 0),  # East Asian ideograph
    0x2D4B45: (0x6BEC, 0),  # East Asian ideograph
    0x6F5435: (0xC309, 0),  # Korean hangul
    0x22527B: (0x7187, 0),  # East Asian ideograph
    0x6F576E: (0xC900, 0),  # Korean hangul
    0x6F532B: (0xC12C, 0),  # Korean hangul
    0x6F2527: (0x3162, 0),  # Korean hangul
    0x227447: (0x7F63, 0),  # East Asian ideograph
    0x4B3666: (0x5A1A, 0),  # East Asian ideograph
    0x233448: (0x8B53, 0),  # East Asian ideograph
    0x233449: (0x8B4A, 0),  # East Asian ideograph
    0x275124: (0x7EB8, 0),  # East Asian ideograph
    0x223046: (0x6285, 0),  # East Asian ideograph
    0x21344A: (0x5319, 0),  # East Asian ideograph
    0x6F576F: (0xC904, 0),  # Korean hangul
    0x6F532C: (0xC12D, 0),  # Korean hangul
    0x23356F: (0x8C74, 0),  # East Asian ideograph
    0x6F4B7B: (0xB11E, 0),  # Korean hangul
    0x215B2A: (0x8E91, 0),  # East Asian ideograph
    0x6F4F6F: (0xB9DB, 0),  # Korean hangul
    0x21344D: (0x5321, 0),  # East Asian ideograph
    0x22344E: (0x64A2, 0),  # East Asian ideograph
    0x23344F: (0x8B3F, 0),  # East Asian ideograph
    0x2E7450: (0x7F82, 0),  # East Asian ideograph
    0x213451: (0x532F, 0),  # East Asian ideograph
    0x335230: (
        0x7F6E,
        0,
    ),  # East Asian ideograph (variant of 215230 which maps to 7F6E)
    0x4B3668: (0x5358, 0),  # East Asian ideograph
    0x234553: (0x9356, 0),  # East Asian ideograph
    0x21725D: (0x5620, 0),  # East Asian ideograph
    0x27554F: (0x53F6, 0),  # East Asian ideograph
    0x213453: (0x5339, 0),  # East Asian ideograph
    0x223454: (0x6490, 0),  # East Asian ideograph
    0x213455: (0x5340, 0),  # East Asian ideograph
    0x215F6F: (0x9748, 0),  # East Asian ideograph
    0x215B2C: (0x8EAA, 0),  # East Asian ideograph
    0x234554: (0x9371, 0),  # East Asian ideograph
    0x6F5028: (0xBA4D, 0),  # Korean hangul
    0x283457: (0x63B8, 0),  # East Asian ideograph
    0x274B2D: (0x736D, 0),  # East Asian ideograph
    0x2D3458: (0x4EDF, 0),  # East Asian ideograph
    0x6F4C65: (0xB2D0, 0),  # Korean hangul
    0x284934: (0x6D43, 0),  # East Asian ideograph
    0x233459: (0x8B59, 0),  # East Asian ideograph
    0x6F5772: (0xC90D, 0),  # Korean hangul
    0x233A21: (0x8E30, 0),  # East Asian ideograph
    0x213A22: (0x5A49, 0),  # East Asian ideograph
    0x21345B: (0x5347, 0),  # East Asian ideograph
    0x233A24: (0x8E47, 0),  # East Asian ideograph
    0x213A25: (0x5A4A, 0),  # East Asian ideograph
    0x233A26: (0x8E46, 0),  # East Asian ideograph
    0x273A27: (0x5987, 0),  # East Asian ideograph
    0x273A28: (0x5A04, 0),  # East Asian ideograph
    0x213A29: (0x5A3C, 0),  # East Asian ideograph
    0x213A2A: (0x5A62, 0),  # East Asian ideograph
    0x213A2B: (0x5A5A, 0),  # East Asian ideograph
    0x213A2C: (0x5A77, 0),  # East Asian ideograph
    0x213A2D: (0x5A9A, 0),  # East Asian ideograph
    0x233A2E: (0x8E4C, 0),  # East Asian ideograph
    0x213A2F: (0x5A7F, 0),  # East Asian ideograph
    0x223A30: (0x670F, 0),  # East Asian ideograph
    0x224767: (0x6CAC, 0),  # East Asian ideograph
    0x233A32: (0x8E4F, 0),  # East Asian ideograph
    0x223A33: (0x6712, 0),  # East Asian ideograph
    0x223A34: (0x6713, 0),  # East Asian ideograph
    0x233A35: (0x8E62, 0),  # East Asian ideograph
    0x233A36: (0x8E60, 0),  # East Asian ideograph
    0x213A37: (0x5AB2, 0),  # East Asian ideograph
    0x223A38: (0x6719, 0),  # East Asian ideograph
    0x223A39: (0x6718, 0),  # East Asian ideograph
    0x233A3A: (0x8E54, 0),  # East Asian ideograph
    0x273A3B: (0x59AA, 0),  # East Asian ideograph
    0x213A3C: (0x5AD6, 0),  # East Asian ideograph
    0x213A3D: (0x5AE3, 0),  # East Asian ideograph
    0x233A3E: (0x8E5A, 0),  # East Asian ideograph
    0x233A3F: (0x8E5E, 0),  # East Asian ideograph
    0x233A40: (0x8E55, 0),  # East Asian ideograph
    0x273A41: (0x5A34, 0),  # East Asian ideograph
    0x213A42: (0x5B09, 0),  # East Asian ideograph
    0x273A43: (0x5A75, 0),  # East Asian ideograph
    0x273A44: (0x5A07, 0),  # East Asian ideograph
    0x273A45: (0x59A9, 0),  # East Asian ideograph
    0x233A46: (0x8E95, 0),  # East Asian ideograph
    0x223A47: (0x6723, 0),  # East Asian ideograph
    0x233A48: (0x8E6D, 0),  # East Asian ideograph
    0x213A49: (0x5B24, 0),  # East Asian ideograph
    0x273A4A: (0x5A74, 0),  # East Asian ideograph
    0x273A4B: (0x5A76, 0),  # East Asian ideograph
    0x223A4C: (0x673E, 0),  # East Asian ideograph
    0x213462: (0x5351, 0),  # East Asian ideograph
    0x223A4E: (0x673F, 0),  # East Asian ideograph
    0x213A4F: (0x5B53, 0),  # East Asian ideograph
    0x213A50: (0x5B54, 0),  # East Asian ideograph
    0x213A51: (0x5B55, 0),  # East Asian ideograph
    0x213A52: (0x5B57, 0),  # East Asian ideograph
    0x213A53: (0x5B58, 0),  # East Asian ideograph
    0x213A54: (0x5B5D, 0),  # East Asian ideograph
    0x213A55: (0x5B5C, 0),  # East Asian ideograph
    0x233A57: (0x8E8B, 0),  # East Asian ideograph
    0x223A58: (0x6757, 0),  # East Asian ideograph
    0x213A59: (0x5B64, 0),  # East Asian ideograph
    0x213A5A: (0x5B69, 0),  # East Asian ideograph
    0x273A5B: (0x5B59, 0),  # East Asian ideograph
    0x223A5C: (0x6747, 0),  # East Asian ideograph
    0x213A5D: (0x5B73, 0),  # East Asian ideograph
    0x233A5E: (0x8E9A, 0),  # East Asian ideograph
    0x273A5F: (0x5B5A, 0),  # East Asian ideograph
    0x273A60: (0x5B66, 0),  # East Asian ideograph
    0x223A61: (0x6755, 0),  # East Asian ideograph
    0x213A62: (0x5B7D, 0),  # East Asian ideograph
    0x233A63: (0x8E98, 0),  # East Asian ideograph
    0x233A64: (0x8E9E, 0),  # East Asian ideograph
    0x223466: (0x64B3, 0),  # East Asian ideograph
    0x223A66: (0x674C, 0),  # East Asian ideograph
    0x223A67: (0x6759, 0),  # East Asian ideograph
    0x223A68: (0x6748, 0),  # East Asian ideograph
    0x213A69: (0x5B8C, 0),  # East Asian ideograph
    0x275553: (0x8364, 0),  # East Asian ideograph
    0x233A6B: (0x8EA5, 0),  # East Asian ideograph
    0x213A6C: (0x5B97, 0),  # East Asian ideograph
    0x213A6D: (0x5B9A, 0),  # East Asian ideograph
    0x213A6E: (0x5B9C, 0),  # East Asian ideograph
    0x233A6F: (0x8EA7, 0),  # East Asian ideograph
    0x213A70: (0x5B99, 0),  # East Asian ideograph
    0x223A71: (0x674A, 0),  # East Asian ideograph
    0x233A72: (0x8E99, 0),  # East Asian ideograph
    0x213A73: (0x5BA3, 0),  # East Asian ideograph
    0x213A74: (0x5BA6, 0),  # East Asian ideograph
    0x213A75: (0x5BA4, 0),  # East Asian ideograph
    0x213A76: (0x5BA2, 0),  # East Asian ideograph
    0x213A77: (0x5BB0, 0),  # East Asian ideograph
    0x213A78: (0x5BB8, 0),  # East Asian ideograph
    0x233A7A: (0x8EBC, 0),  # East Asian ideograph
    0x213A7B: (0x5BB4, 0),  # East Asian ideograph
    0x223A7C: (0x6785, 0),  # East Asian ideograph
    0x213A7D: (0x5BB9, 0),  # East Asian ideograph
    0x213A7E: (0x5BB3, 0),  # East Asian ideograph
    0x23233F: (0x844A, 0),  # East Asian ideograph
    0x4B763D: (
        0x57F4,
        0,
    ),  # East Asian ideograph (variant of 21763D which maps to 57F4)
    0x22746B: (0x7F7E, 0),  # East Asian ideograph
    0x283B7D: (0x53F0, 0),  # East Asian ideograph (duplicate simplified)
    0x22346C: (0x64D3, 0),  # East Asian ideograph
    0x6F5927: (0xCC39, 0),  # Korean hangul
    0x393B39: (0x5BF3, 0),  # East Asian ideograph
    0x213F26: (0x614C, 0),  # East Asian ideograph
    0x235222: (
        0x9957,
        0,
    ),  # East Asian ideograph (variant of 475222 which maps to 9957)
    0x2D346E: (0x5373, 0),  # East Asian ideograph
    0x276232: (0x9E23, 0),  # East Asian ideograph
    0x6F5333: (0xC13C, 0),  # Korean hangul
    0x213D5B: (0x5F79, 0),  # East Asian ideograph
    0x213471: (0x5378, 0),  # East Asian ideograph
    0x287472: (0x7F74, 0),  # East Asian ideograph
    0x23344D: (0x8B56, 0),  # East Asian ideograph
    0x335223: (0x7E8E, 0),  # East Asian ideograph
    0x233473: (0x8B45, 0),  # East Asian ideograph
    0x273F3F: (0x51ED, 0),  # East Asian ideograph
    0x213474: (0x537F, 0),  # East Asian ideograph
    0x213475: (0x5384, 0),  # East Asian ideograph
    0x21325D: (0x50F9, 0),  # East Asian ideograph
    0x225F21: (0x75F9, 0),  # East Asian ideograph
    0x217477: (0x576D, 0),  # East Asian ideograph
    0x225F22: (0x75FC, 0),  # East Asian ideograph
    0x23456F: (0x9364, 0),  # East Asian ideograph
    0x275F23: (0x9648, 0),  # East Asian ideograph
    0x213479: (0x53A5, 0),  # East Asian ideograph
    0x275F24: (0x9646, 0),  # East Asian ideograph
    0x22747A: (0x7F91, 0),  # East Asian ideograph
    0x21347B: (0x53B2, 0),  # East Asian ideograph
    0x21392F: (0x5954, 0),  # East Asian ideograph
    0x225269: (0x7150, 0),  # East Asian ideograph
    0x4B4835: (0x6DA3, 0),  # East Asian ideograph
    0x21347D: (0x53C3, 0),  # East Asian ideograph
    0x2D5F28: (0x9665, 0),  # East Asian ideograph
    0x6F5336: (0xC149, 0),  # Korean hangul
    0x6F5329: (0xC127, 0),  # Korean hangul
    0x225F29: (0x7616, 0),  # East Asian ideograph
    0x275F2A: (0x9634, 0),  # East Asian ideograph
    0x275F2B: (0x961F, 0),  # East Asian ideograph
    0x216C41: (0x52D1, 0),  # East Asian ideograph
    0x225F2C: (0x7608, 0),  # East Asian ideograph
    0x6F577A: (0xC958, 0),  # Korean hangul
    0x225F2D: (0x7615, 0),  # East Asian ideograph
    0x295731: (0x9C8B, 0),  # East Asian ideograph
    0x276222: (0x9CC5, 0),  # East Asian ideograph
    0x225F2E: (0x760C, 0),  # East Asian ideograph
    0x23455D: (0x9349, 0),  # East Asian ideograph
    0x6F5567: (0xC5FE, 0),  # Korean hangul
    0x215F2F: (0x9685, 0),  # East Asian ideograph
    0x273340: (0x51BB, 0),  # East Asian ideograph
    0x223B21: (0x677B, 0),  # East Asian ideograph
    0x223B22: (0x6792, 0),  # East Asian ideograph
    0x223B23: (0x6776, 0),  # East Asian ideograph
    0x213B24: (0x5BC4, 0),  # East Asian ideograph
    0x223B25: (0x6791, 0),  # East Asian ideograph
    0x223B26: (0x6799, 0),  # East Asian ideograph
    0x215F31: (0x968D, 0),  # East Asian ideograph
    0x223B28: (0x67A4, 0),  # East Asian ideograph
    0x213B29: (0x5BD0, 0),  # East Asian ideograph
    0x213B2A: (0x5BD3, 0),  # East Asian ideograph
    0x213B2B: (0x5BE1, 0),  # East Asian ideograph
    0x213B2C: (0x5BE5, 0),  # East Asian ideograph
    0x215F32: (0x9698, 0),  # East Asian ideograph
    0x223B2E: (0x678F, 0),  # East Asian ideograph
    0x233B2F: (0x8ECF, 0),  # East Asian ideograph
    0x223B30: (0x6772, 0),  # East Asian ideograph
    0x223B31: (
        0x6798,
        0,
    ),  # East Asian ideograph (variant of 4C3B31 which maps to 6798)
    0x223B32: (0x676A, 0),  # East Asian ideograph
    0x233B33: (0x8ED5, 0),  # East Asian ideograph
    0x213B34: (0x5BEE, 0),  # East Asian ideograph
    0x273B35: (0x5BBD, 0),  # East Asian ideograph
    0x273B36: (0x5BA1, 0),  # East Asian ideograph
    0x273B37: (0x5199, 0),  # East Asian ideograph
    0x273B38: (0x5BA0, 0),  # East Asian ideograph
    0x223B39: (0x67AC, 0),  # East Asian ideograph
    0x213B3A: (0x5BF8, 0),  # East Asian ideograph
    0x223B3B: (0x67A0, 0),  # East Asian ideograph
    0x213B3C: (0x5C01, 0),  # East Asian ideograph
    0x213B3D: (0x5C04, 0),  # East Asian ideograph
    0x213B3E: (0x5C09, 0),  # East Asian ideograph
    0x233B3F: (0x8EFA, 0),  # East Asian ideograph
    0x273B40: (0x5C06, 0),  # East Asian ideograph
    0x213B41: (0x5C0A, 0),  # East Asian ideograph
    0x233B42: (0x8EF9, 0),  # East Asian ideograph
    0x273B43: (0x5BF9, 0),  # East Asian ideograph
    0x223B44: (0x67F9, 0),  # East Asian ideograph
    0x213B45: (0x5C0F, 0),  # East Asian ideograph
    0x213B46: (0x5C11, 0),  # East Asian ideograph
    0x213B47: (0x5C16, 0),  # East Asian ideograph
    0x223B48: (0x678D, 0),  # East Asian ideograph
    0x223B49: (0x678C, 0),  # East Asian ideograph
    0x213B4A: (0x5C2C, 0),  # East Asian ideograph
    0x233B4B: (0x8EE8, 0),  # East Asian ideograph
    0x223B4C: (0x67FC, 0),  # East Asian ideograph
    0x213B4D: (0x5C38, 0),  # East Asian ideograph
    0x223B4E: (0x6810, 0),  # East Asian ideograph
    0x233B4F: (0x8EEB, 0),  # East Asian ideograph
    0x213B50: (0x5C40, 0),  # East Asian ideograph
    0x223B51: (0x67C8, 0),  # East Asian ideograph
    0x23455F: (0x935A, 0),  # East Asian ideograph
    0x213B53: (0x5C3E, 0),  # East Asian ideograph
    0x223B54: (0x67CC, 0),  # East Asian ideograph
    0x213B55: (0x5C45, 0),  # East Asian ideograph
    0x233B56: (0x8F00, 0),  # East Asian ideograph
    0x213B57: (0x5C4E, 0),  # East Asian ideograph
    0x223B58: (0x67C5, 0),  # East Asian ideograph
    0x233B59: (0x8F05, 0),  # East Asian ideograph
    0x233B5A: (0x8F08, 0),  # East Asian ideograph
    0x233B5B: (0x8F07, 0),  # East Asian ideograph
    0x223B5C: (0x67BB, 0),  # East Asian ideograph
    0x213B5D: (0x5C5B, 0),  # East Asian ideograph (not in Unicode)
    0x213B5E: (0x5C60, 0),  # East Asian ideograph
    0x223B5F: (0x67B0, 0),  # East Asian ideograph
    0x223B60: (0x6803, 0),  # East Asian ideograph
    0x223B61: (0x67F8, 0),  # East Asian ideograph
    0x213B62: (0x5C65, 0),  # East Asian ideograph
    0x273B63: (0x5C5E, 0),  # East Asian ideograph
    0x233B64: (0x8F2C, 0),  # East Asian ideograph
    0x213B65: (0x5C71, 0),  # East Asian ideograph
    0x225A2A: (0x741B, 0),  # East Asian ideograph
    0x213B67: (0x5C90, 0),  # East Asian ideograph
    0x213B68: (0x5C8C, 0),  # East Asian ideograph
    0x213B69: (0x5C91, 0),  # East Asian ideograph
    0x213B6A: (0x5C94, 0),  # East Asian ideograph
    0x233B6B: (0x8F1E, 0),  # East Asian ideograph
    0x213B6C: (0x5CB8, 0),  # East Asian ideograph
    0x233B6D: (0x8F25, 0),  # East Asian ideograph
    0x233B6E: (0x8F20, 0),  # East Asian ideograph
    0x223B6F: (0x67E4, 0),  # East Asian ideograph
    0x223B70: (0x67D9, 0),  # East Asian ideograph
    0x223B71: (0x67DB, 0),  # East Asian ideograph
    0x223B72: (0x67B5, 0),  # East Asian ideograph
    0x213B73: (0x5D01, 0),  # East Asian ideograph
    0x273B74: (0x5CE1, 0),  # East Asian ideograph
    0x223B75: (0x67F7, 0),  # East Asian ideograph
    0x213B76: (0x5CFB, 0),  # East Asian ideograph
    0x223B77: (0x67B3, 0),  # East Asian ideograph
    0x233B78: (0x8F36, 0),  # East Asian ideograph
    0x233B79: (0x8F2E, 0),  # East Asian ideograph
    0x233B7A: (0x8F33, 0),  # East Asian ideograph
    0x215F3F: (0x96C0, 0),  # East Asian ideograph
    0x223B7C: (0x67EE, 0),  # East Asian ideograph
    0x223B7D: (0x6AAF, 0),  # East Asian ideograph
    0x223B7E: (0x67B2, 0),  # East Asian ideograph
    0x225F40: (0x761B, 0),  # East Asian ideograph
    0x6F577E: (0xC970, 0),  # Korean hangul
    0x6F533B: (0xC158, 0),  # Korean hangul
    0x213D63: (0x5F8A, 0),  # East Asian ideograph
    0x6F4B7E: (0xB125, 0),  # Korean hangul
    0x2D5D2F: (0x9196, 0),  # East Asian ideograph
    0x2D5F43: (0x9CEB, 0),  # East Asian ideograph
    0x6F2459: (0x3137, 0),  # Korean hangul
    0x293B42: (0x8F75, 0),  # East Asian ideograph
    0x235F45: (0x9F22, 0),  # East Asian ideograph
    0x2D5F46: (0x96BD, 0),  # East Asian ideograph
    0x6F533C: (0xC167, 0),  # Korean hangul
    0x213D64: (0x5F87, 0),  # East Asian ideograph
    0x225F47: (0x7619, 0),  # East Asian ideograph
    0x234562: (0x935F, 0),  # East Asian ideograph
    0x235F48: (0x9F2B, 0),  # East Asian ideograph
    0x2E604A: (0x7690, 0),  # East Asian ideograph
    0x235F49: (0x9F26, 0),  # East Asian ideograph
    0x225270: (0x7144, 0),  # East Asian ideograph
    0x6F5D65: (0xD72D, 0),  # Korean hangul
    0x224E2D: (0x6FC9, 0),  # East Asian ideograph
    0x2D4B3F: (0x73CE, 0),  # East Asian ideograph
    0x275F4B: (0x6742, 0),  # East Asian ideograph
    0x276234: (0x9E29, 0),  # East Asian ideograph
    0x6F533D: (0xC168, 0),  # Korean hangul
    0x225F4C: (0x761D, 0),  # East Asian ideograph
    0x275F4D: (0x96CF, 0),  # East Asian ideograph
    0x6F5773: (0xC90F, 0),  # Korean hangul
    0x6F245B: (0x3141, 0),  # Korean hangul
    0x275F4E: (0x53CC, 0),  # East Asian ideograph
    0x216C48: (0x52D6, 0),  # East Asian ideograph
    0x275F4F: (0x79BB, 0),  # East Asian ideograph
    0x215F50: (
        0x96E3,
        0,
    ),  # East Asian ideograph (variant of 4B5F50 which maps to 96E3)
    0x6F533E: (0xC170, 0),  # Korean hangul
    0x213D66: (0x5F92, 0),  # East Asian ideograph
    0x215F51: (0x96E8, 0),  # East Asian ideograph
    0x225F3B: (0x7610, 0),  # East Asian ideograph
    0x284345: (0x680C, 0),  # East Asian ideograph
    0x6F5848: (0xCA08, 0),  # Korean hangul
    0x6F245C: (0x3142, 0),  # Korean hangul
    0x235F53: (0x9F2F, 0),  # East Asian ideograph
    0x225F54: (0x762D, 0),  # East Asian ideograph
    0x234571: (0x936B, 0),  # East Asian ideograph
    0x6F505B: (0xBBC0, 0),  # Korean hangul
    0x275F55: (0x7535, 0),  # East Asian ideograph
    0x6F533F: (0xC18C, 0),  # Korean hangul
    0x213D67: (0x5F91, 0),  # East Asian ideograph
    0x6F4D64: (0xB4E0, 0),  # Korean hangul
    0x213924: (0x5922, 0),  # East Asian ideograph
    0x6F245D: (0x3145, 0),  # Korean hangul
    0x275128: (0x7ECB, 0),  # East Asian ideograph
    0x4B5F58: (0xF9B2, 0),  # East Asian ideograph
    0x227049: (0x7D0F, 0),  # East Asian ideograph
    0x224E30: (0x6FA0, 0),  # East Asian ideograph
    0x293338: (0x8BFD, 0),  # East Asian ideograph
    0x2E715A: (0x7E27, 0),  # East Asian ideograph
    0x215F5A: (0x9707, 0),  # East Asian ideograph
    0x6F5340: (0xC18D, 0),  # Korean hangul
    0x223C21: (0x67B9, 0),  # East Asian ideograph
    0x213C22: (0x5D11, 0),  # East Asian ideograph
    0x215B3E: (0x8EFE, 0),  # East Asian ideograph
    0x223C24: (0x67E3, 0),  # East Asian ideograph
    0x213C25: (0x5D14, 0),  # East Asian ideograph
    0x233C26: (0x8F39, 0),  # East Asian ideograph
    0x233C27: (0x8F34, 0),  # East Asian ideograph
    0x273C28: (0x5C9A, 0),  # East Asian ideograph
    0x223C29: (0x67E2, 0),  # East Asian ideograph
    0x273C2A: (0x5D2D, 0),  # East Asian ideograph
    0x273C2B: (0x5C96, 0),  # East Asian ideograph
    0x213C2C: (0x5D9D, 0),  # East Asian ideograph
    0x273C2D: (0x5C7F, 0),  # East Asian ideograph
    0x273C2E: (0x5CB3, 0),  # East Asian ideograph
    0x223C2F: (0x67E7, 0),  # East Asian ideograph
    0x223C30: (0x6849, 0),  # East Asian ideograph
    0x223C31: (0x683E, 0),  # East Asian ideograph
    0x273C32: (0x5DC5, 0),  # East Asian ideograph
    0x214A32: (0x71EC, 0),  # East Asian ideograph
    0x213C34: (0x5DDD, 0),  # East Asian ideograph
    0x215F5E: (0x9711, 0),  # East Asian ideograph
    0x223C36: (0x6814, 0),  # East Asian ideograph
    0x223C37: (0x684B, 0),  # East Asian ideograph
    0x223C38: (0x681E, 0),  # East Asian ideograph
    0x213C39: (0x5DE7, 0),  # East Asian ideograph
    0x213C3A: (0x5DE6, 0),  # East Asian ideograph
    0x223C3B: (0x6833, 0),  # East Asian ideograph
    0x213C3C: (0x5DEE, 0),  # East Asian ideograph
    0x233C3D: (0x8F52, 0),  # East Asian ideograph
    0x213C3E: (0x5DF2, 0),  # East Asian ideograph
    0x213C3F: (0x5DF3, 0),  # East Asian ideograph
    0x223C40: (0x6831, 0),  # East Asian ideograph
    0x215F60: (0x9716, 0),  # East Asian ideograph
    0x223C42: (0x6835, 0),  # East Asian ideograph
    0x223C43: (0x683B, 0),  # East Asian ideograph
    0x223C44: (0x684E, 0),  # East Asian ideograph
    0x213C46: (0x5E06, 0),  # East Asian ideograph
    0x234124: (0x918D, 0),  # East Asian ideograph
    0x233C48: (0x8F56, 0),  # East Asian ideograph
    0x213C49: (0x5E1A, 0),  # East Asian ideograph
    0x223C4A: (0x684D, 0),  # East Asian ideograph
    0x233C4B: (0x8F55, 0),  # East Asian ideograph
    0x233C4C: (0x8F58, 0),  # East Asian ideograph
    0x215F62: (0x970D, 0),  # East Asian ideograph
    0x233C4E: (0x8F5E, 0),  # East Asian ideograph
    0x273C4F: (0x5E05, 0),  # East Asian ideograph
    0x273C51: (0x5E08, 0),  # East Asian ideograph
    0x273C52: (0x5E10, 0),  # East Asian ideograph
    0x273C53: (0x5E26, 0),  # East Asian ideograph
    0x213C54: (0x5E38, 0),  # East Asian ideograph
    0x223C55: (0x685D, 0),  # East Asian ideograph
    0x223C56: (0x685E, 0),  # East Asian ideograph
    0x233C57: (0x8F62, 0),  # East Asian ideograph
    0x273C58: (0x5E27, 0),  # East Asian ideograph
    0x233C59: (0x8F63, 0),  # East Asian ideograph
    0x233C5A: (0x8F64, 0),  # East Asian ideograph
    0x213C5B: (0x5E54, 0),  # East Asian ideograph
    0x273C5C: (0x5E3C, 0),  # East Asian ideograph
    0x213C5D: (0x5E55, 0),  # East Asian ideograph
    0x273C5E: (0x5E01, 0),  # East Asian ideograph
    0x213C5F: (0x5E62, 0),  # East Asian ideograph
    0x273C60: (0x5E1C, 0),  # East Asian ideograph
    0x273C61: (0x5E2E, 0),  # East Asian ideograph
    0x213C63: (0x5E73, 0),  # East Asian ideograph
    0x6F5177: (0xBE5A, 0),  # Korean hangul
    0x223C65: (0x685A, 0),  # East Asian ideograph
    0x233C66: (0x8FA5, 0),  # East Asian ideograph
    0x273C67: (0x5E72, 0),  # East Asian ideograph (Version J extension)
    0x223C68: (0x686B, 0),  # East Asian ideograph
    0x223C69: (0x686C, 0),  # East Asian ideograph
    0x213C6A: (0x5E7D, 0),  # East Asian ideograph
    0x223C6B: (0x6879, 0),  # East Asian ideograph
    0x233C6C: (0x8FB5, 0),  # East Asian ideograph
    0x213C6D: (0x5E87, 0),  # East Asian ideograph
    0x233C6E: (0x8FBB, 0),  # East Asian ideograph
    0x213C6F: (0x5E9A, 0),  # East Asian ideograph
    0x233C70: (0x8FBC, 0),  # East Asian ideograph
    0x215F68: (0x9738, 0),  # East Asian ideograph
    0x223C72: (0x687E, 0),  # East Asian ideograph
    0x213C73: (0x5E95, 0),  # East Asian ideograph
    0x233C74: (0x8FBF, 0),  # East Asian ideograph
    0x233C75: (0x8FD2, 0),  # East Asian ideograph
    0x273C76: (0x5E93, 0),  # East Asian ideograph
    0x225F69: (0x7647, 0),  # East Asian ideograph
    0x213C78: (0x5EAD, 0),  # East Asian ideograph
    0x213C79: (0x5EB7, 0),  # East Asian ideograph
    0x233C7A: (0x8FCA, 0),  # East Asian ideograph
    0x233C7B: (0x8FD3, 0),  # East Asian ideograph
    0x213C7C: (0x5EB5, 0),  # East Asian ideograph
    0x215F6A: (0x9732, 0),  # East Asian ideograph
    0x273C7E: (0x5395, 0),  # East Asian ideograph
    0x275F6B: (0x9701, 0),  # East Asian ideograph
    0x6F5849: (0xCA09, 0),  # Korean hangul
    0x6F2461: (0x314B, 0),  # Korean hangul
    0x275725: (0x8682, 0),  # East Asian ideograph
    0x275122: (0x7EB3, 0),  # East Asian ideograph
    0x6F5273: (0xC0D8, 0),  # Korean hangul
    0x235F6D: (0x9F45, 0),  # East Asian ideograph
    0x4C476E: (0x6CAD, 0),  # East Asian ideograph
    0x225A2C: (0x7432, 0),  # East Asian ideograph
    0x225F6E: (0x764D, 0),  # East Asian ideograph
    0x6F2528: (0x3163, 0),  # Korean hangul
    0x2F312B: (0x89BB, 0),  # East Asian ideograph
    0x235F6F: (0x9F46, 0),  # East Asian ideograph
    0x4B5F70: (0x9752, 0),  # East Asian ideograph
    0x6F2462: (0x314C, 0),  # Korean hangul
    0x235F71: (0x9F48, 0),  # East Asian ideograph
    0x275123: (0x7EA7, 0),  # East Asian ideograph
    0x214A36: (0x720D, 0),  # East Asian ideograph
    0x224E35: (0x6FB4, 0),  # East Asian ideograph
    0x335234: (0x99E1, 0),  # East Asian ideograph
    0x2E3D62: (0x684A, 0),  # East Asian ideograph
    0x235F73: (0x9F49, 0),  # East Asian ideograph
    0x69253B: (0x30BB, 0),  # Katakana letter SE
    0x276230: (0x9E20, 0),  # East Asian ideograph
    0x23456B: (0x9374, 0),  # East Asian ideograph
    0x215F75: (0x9760, 0),  # East Asian ideograph
    0x692431: (0x3051, 0),  # Hiragana letter KE
    0x274A21: (0x70BD, 0),  # East Asian ideograph
    0x23345F: (0x8B4D, 0),  # East Asian ideograph
    0x224D63: (0x6F5F, 0),  # East Asian ideograph
    0x274A22: (0x7096, 0),  # East Asian ideograph
    0x4D446B: (0x954E, 0),  # East Asian ideograph
    0x6F4A23: (0xADC4, 0),  # Korean hangul
    0x6F5346: (0xC19F, 0),  # Korean hangul
    0x276231: (0x9E22, 0),  # East Asian ideograph
    0x215F79: (0x9768, 0),  # East Asian ideograph
    0x274A24: (0x706F, 0),  # East Asian ideograph
    0x345E3B: (0x80AC, 0),  # East Asian ideograph
    0x215F7A: (0x9769, 0),  # East Asian ideograph
    0x274A25: (0x7116, 0),  # East Asian ideograph
    0x275568: (0x8298, 0),  # East Asian ideograph
    0x215F7B: (0x9776, 0),  # East Asian ideograph
    0x274A26: (0x70E7, 0),  # East Asian ideograph
    0x6F5D67: (0xD73C, 0),  # Korean hangul
    0x215F7C: (0x9774, 0),  # East Asian ideograph
    0x6F4A27: (0xADD3, 0),  # Korean hangul
    0x2E3172: (0x5261, 0),  # East Asian ideograph
    0x276236: (0x9E35, 0),  # East Asian ideograph
    0x2D4A28: (0x8B8C, 0),  # East Asian ideograph
    0x6F5347: (0xC1A1, 0),  # Korean hangul
    0x213D6F: (0x5FA9, 0),  # East Asian ideograph
    0x215F7E: (0x9785, 0),  # East Asian ideograph
    0x33456D: (0x826A, 0),  # East Asian ideograph
    0x6F5178: (0xBE5B, 0),  # Korean hangul
    0x224A2A: (0x6DDF, 0),  # East Asian ideograph
    0x6F2465: (0x3132, 0),  # Korean hangul
    0x275126: (0x7ECA, 0),  # East Asian ideograph
    0x23567A: (0x9B95, 0),  # East Asian ideograph
    0x6F4A2C: (0xADF8, 0),  # Korean hangul
    0x224A2D: (0x6DD3, 0),  # East Asian ideograph
    0x6F5348: (0xC1A5, 0),  # Korean hangul
    0x276233: (0x51E4, 0),  # East Asian ideograph
    0x274A2E: (0x8425, 0),  # East Asian ideograph
    0x2E3328: (0x6528, 0),  # East Asian ideograph
    0x6F5D6B: (0xD751, 0),  # Korean hangul
    0x234A2F: (0x9642, 0),  # East Asian ideograph
    0x4B462A: (0x6B74, 0),  # East Asian ideograph
    0x233D21: (0x8FDA, 0),  # East Asian ideograph
    0x233D22: (0x8FD5, 0),  # East Asian ideograph
    0x213D23: (0x5EC9, 0),  # East Asian ideograph
    0x213D24: (0x5EC8, 0),  # East Asian ideograph
    0x223D25: (0x686D, 0),  # East Asian ideograph
    0x213D26: (0x5ED6, 0),  # East Asian ideograph
    0x273D27: (0x5E9F, 0),  # East Asian ideograph
    0x213D28: (0x5EDA, 0),  # East Asian ideograph
    0x213D29: (0x5EDD, 0),  # East Asian ideograph
    0x273D2A: (0x5E7F, 0),  # East Asian ideograph
    0x273D2B: (0x5E99, 0),  # East Asian ideograph
    0x273D2C: (0x5382, 0),  # East Asian ideograph
    0x273D2D: (0x5E9E, 0),  # East Asian ideograph
    0x273D2E: (0x5E90, 0),  # East Asian ideograph
    0x233D2F: (0x8FE4, 0),  # East Asian ideograph
    0x233D30: (0x8FEE, 0),  # East Asian ideograph
    0x223D32: (0x688B, 0),  # East Asian ideograph
    0x274A33: (0x70E9, 0),  # East Asian ideograph
    0x213D34: (0x5EFF, 0),  # East Asian ideograph
    0x233D35: (0x8FF9, 0),  # East Asian ideograph
    0x213D36: (0x5F04, 0),  # East Asian ideograph
    0x213D37: (0x5F08, 0),  # East Asian ideograph
    0x213D38: (0x5F0A, 0),  # East Asian ideograph
    0x223D39: (0x68A3, 0),  # East Asian ideograph
    0x213D3A: (0x5F12, 0),  # East Asian ideograph
    0x213D3B: (0x5F13, 0),  # East Asian ideograph
    0x233D3C: (0x8FFB, 0),  # East Asian ideograph
    0x213D3D: (0x5F14, 0),  # East Asian ideograph
    0x213D3E: (0x5F18, 0),  # East Asian ideograph
    0x214A35: (0x7206, 0),  # East Asian ideograph
    0x223D40: (0x688F, 0),  # East Asian ideograph
    0x213D41: (0x5F1F, 0),  # East Asian ideograph
    0x213D42: (0x5F26, 0),  # East Asian ideograph
    0x223D43: (0x687B, 0),  # East Asian ideograph
    0x233D44: (0x9011, 0),  # East Asian ideograph
    0x224A36: (0x6DDC, 0),  # East Asian ideograph
    0x213D46: (0x5F31, 0),  # East Asian ideograph
    0x273D47: (0x5F20, 0),  # East Asian ideograph
    0x213D48: (0x5F37, 0),  # East Asian ideograph
    0x233D49: (0x9021, 0),  # East Asian ideograph
    0x233D4A: (0x902D, 0),  # East Asian ideograph
    0x274A37: (0x7089, 0),  # East Asian ideograph
    0x273D4C: (0x5F25, 0),  # East Asian ideograph
    0x273D4D: (0x5F2F, 0),  # East Asian ideograph
    0x233D4E: (0x902C, 0),  # East Asian ideograph
    0x273D4F: (0x6C47, 0),  # East Asian ideograph (duplicate simplified)
    0x223D50: (0x692C, 0),  # East Asian ideograph
    0x274A38: (0x70C2, 0),  # East Asian ideograph
    0x213D52: (0x5F64, 0),  # East Asian ideograph
    0x223D53: (0x690C, 0),  # East Asian ideograph
    0x213D54: (0x5F6C, 0),  # East Asian ideograph
    0x213D55: (0x5F69, 0),  # East Asian ideograph
    0x233D56: (0x9037, 0),  # East Asian ideograph
    0x214A39: (0x7228, 0),  # East Asian ideograph
    0x223D58: (0x68D3, 0),  # East Asian ideograph
    0x213D59: (0x5F71, 0),  # East Asian ideograph
    0x223D5B: (0x690A, 0),  # East Asian ideograph
    0x223D5C: (0x6909, 0),  # East Asian ideograph
    0x233D5D: (0x9052, 0),  # East Asian ideograph
    0x213D5E: (0x5F7F, 0),  # East Asian ideograph
    0x213D5F: (0x5F7C, 0),  # East Asian ideograph
    0x213D60: (0x5F85, 0),  # East Asian ideograph
    0x213D61: (0x5F88, 0),  # East Asian ideograph
    0x223D62: (0x68EC, 0),  # East Asian ideograph
    0x223D63: (0x692A, 0),  # East Asian ideograph
    0x223D64: (0x68EA, 0),  # East Asian ideograph
    0x223D65: (0x681F, 0),  # East Asian ideograph
    0x223D66: (0x7439, 0),  # East Asian ideograph
    0x233D67: (0x9049, 0),  # East Asian ideograph
    0x213D68: (0x5F90, 0),  # East Asian ideograph
    0x234A3C: (0x9651, 0),  # East Asian ideograph
    0x233D6A: (0x9044, 0),  # East Asian ideograph
    0x213D6B: (0x5F99, 0),  # East Asian ideograph
    0x273D6C: (0x4ECE, 0),  # East Asian ideograph
    0x223D6E: (0x68D6, 0),  # East Asian ideograph
    0x223D6F: (0x68EB, 0),  # East Asian ideograph
    0x225F48: (0x761E, 0),  # East Asian ideograph
    0x213D71: (0x5FAA, 0),  # East Asian ideograph
    0x213D72: (0x5FAC, 0),  # East Asian ideograph
    0x223D73: (0x68F1, 0),  # East Asian ideograph
    0x273D74: (0x5F7B, 0),  # East Asian ideograph
    0x233D75: (0x905D, 0),  # East Asian ideograph
    0x273D76: (0x5F81, 0),  # East Asian ideograph
    0x213D77: (0x5FBD, 0),  # East Asian ideograph
    0x233D78: (0x905B, 0),  # East Asian ideograph
    0x223D79: (0x68FC, 0),  # East Asian ideograph
    0x213D7A: (0x5FD9, 0),  # East Asian ideograph
    0x233D7B: (0x906B, 0),  # East Asian ideograph
    0x223D7C: (0x6913, 0),  # East Asian ideograph
    0x213D7D: (0x5FD6, 0),  # East Asian ideograph
    0x224E3C: (0x6FA8, 0),  # East Asian ideograph
    0x23523B: (0x99A3, 0),  # East Asian ideograph
    0x6F534C: (0xC1C4, 0),  # Korean hangul
    0x276237: (0x9E2A, 0),  # East Asian ideograph
    0x224173: (0x6A8D, 0),  # East Asian ideograph
    0x274A42: (0x7237, 0),  # East Asian ideograph
    0x223D30: (0x6898, 0),  # East Asian ideograph
    0x6F5925: (0xCC30, 0),  # Korean hangul
    0x2D5C5B: (0x9089, 0),  # East Asian ideograph
    0x6F4A43: (0xAE4C, 0),  # Korean hangul
    0x234A44: (0x965C, 0),  # East Asian ideograph
    0x232435: (0x84DA, 0),  # East Asian ideograph
    0x696E5C: (0x91DF, 0),  # East Asian ideograph
    0x295929: (0x9CA3, 0),  # East Asian ideograph
    0x213E51: (0x608D, 0),  # East Asian ideograph
    0x274A45: (0x5C14, 0),  # East Asian ideograph
    0x233023: (0x8962, 0),  # East Asian ideograph
    0x214A46: (0x7246, 0),  # East Asian ideograph
    0x6F534D: (0xC1C8, 0),  # Korean hangul
    0x276238: (0x9E2D, 0),  # East Asian ideograph
    0x6F5740: (0xC81D, 0),  # Korean hangul
    0x213932: (0x5947, 0),  # East Asian ideograph
    0x295574: (0x9604, 0),  # East Asian ideograph
    0x6F4A48: (0xAE5C, 0),  # Korean hangul
    0x277345: (0x556E, 0),  # East Asian ideograph
    0x6F4A49: (0xAE5D, 0),  # Korean hangul
    0x29592A: (0x9CD3, 0),  # East Asian ideograph
    0x4B4352: (0x66F5, 0),  # East Asian ideograph
    0x234A4A: (0x965F, 0),  # East Asian ideograph
    0x234A4B: (0x9656, 0),  # East Asian ideograph
    0x6F534E: (0xC1D7, 0),  # Korean hangul
    0x213D76: (0x5FB5, 0),  # East Asian ideograph
    0x274A4C: (0x724D, 0),  # East Asian ideograph
    0x6F4A4D: (0xAE65, 0),  # Korean hangul
    0x6F5771: (0xC90C, 0),  # Korean hangul
    0x295928: (0x9CD5, 0),  # East Asian ideograph
    0x6F4A4E: (0xAE68, 0),  # Korean hangul
    0x334050: (0x62D5, 0),  # East Asian ideograph
    0x23523E: (0x99A6, 0),  # East Asian ideograph
    0x4C2539: (0x5D73, 0),  # East Asian ideograph
    0x4D3363: (0x8C25, 0),  # East Asian ideograph
    0x224A50: (0x6E27, 0),  # East Asian ideograph
    0x6F534F: (0xC1E0, 0),  # Korean hangul
    0x27623A: (0x9E33, 0),  # East Asian ideograph
    0x4B485F: (
        0x6EDE,
        0,
    ),  # East Asian ideograph (variant of 27485F which maps to 6EDE)
    0x234A51: (0x966C, 0),  # East Asian ideograph
    0x23235C: (0x84B4, 0),  # East Asian ideograph
    0x285A47: (0x73AE, 0),  # East Asian ideograph
    0x2D3165: (0x349E, 0),  # East Asian ideograph (not found in unified han)
    0x6F4A52: (0xAE78, 0),  # Korean hangul
    0x275571: (0x848B, 0),  # East Asian ideograph
    0x274A53: (0x5B83, 0),  # East Asian ideograph
    0x227059: (0x7D35, 0),  # East Asian ideograph
    0x33523F: (0x8B71, 0),  # East Asian ideograph
    0x473422: (0x8C2A, 0),  # East Asian ideograph
    0x224A55: (0x6E49, 0),  # East Asian ideograph
    0x213D78: (0x5FC3, 0),  # East Asian ideograph
    0x213935: (0x5951, 0),  # East Asian ideograph
    0x223D34: (0x686F, 0),  # East Asian ideograph
    0x4B3248: (0x50B2, 0),  # East Asian ideograph (not in Unicode)
    0x6F4A57: (0xAE84, 0),  # Korean hangul
    0x224A58: (0x6E3C, 0),  # East Asian ideograph
    0x6F5D69: (0xD749, 0),  # Korean hangul
    0x6F4A59: (0xAEBC, 0),  # Korean hangul
    0x274A5A: (0x7275, 0),  # East Asian ideograph
    0x6F5351: (0xC1E8, 0),  # Korean hangul
    0x27623C: (0x9E3F, 0),  # East Asian ideograph
    0x223E21: (0x6907, 0),  # East Asian ideograph
    0x213E22: (0x5FEB, 0),  # East Asian ideograph
    0x213E23: (0x5FE0, 0),  # East Asian ideograph
    0x213E24: (0x5FF1, 0),  # East Asian ideograph
    0x233E25: (0x906F, 0),  # East Asian ideograph
    0x233E26: (0x9079, 0),  # East Asian ideograph
    0x213E27: (0x5FF5, 0),  # East Asian ideograph
    0x233E28: (0x9076, 0),  # East Asian ideograph
    0x213E29: (0x6014, 0),  # East Asian ideograph
    0x223E2A: (0x68DE, 0),  # East Asian ideograph
    0x223E2B: (0x691B, 0),  # East Asian ideograph
    0x233E2C: (0x9085, 0),  # East Asian ideograph
    0x223E2D: (0x68FB, 0),  # East Asian ideograph
    0x213E2E: (0x601D, 0),  # East Asian ideograph
    0x234A5D: (0x967B, 0),  # East Asian ideograph
    0x213E30: (0x6021, 0),  # East Asian ideograph
    0x213E31: (0x6020, 0),  # East Asian ideograph
    0x213E32: (0x6028, 0),  # East Asian ideograph
    0x223E33: (0x68E1, 0),  # East Asian ideograph
    0x213E34: (0x6027, 0),  # East Asian ideograph
    0x214A5E: (0x7296, 0),  # East Asian ideograph
    0x213E36: (0x6015, 0),  # East Asian ideograph
    0x223E37: (0x68D1, 0),  # East Asian ideograph
    0x223E38: (0x68D0, 0),  # East Asian ideograph
    0x223E39: (0x6908, 0),  # East Asian ideograph
    0x233E3A: (0x908B, 0),  # East Asian ideograph
    0x213E3B: (0x6043, 0),  # East Asian ideograph
    0x213E3C: (0x6065, 0),  # East Asian ideograph
    0x213E3D: (0x6050, 0),  # East Asian ideograph
    0x223E3E: (0x68E8, 0),  # East Asian ideograph
    0x223E3F: (0x68F0, 0),  # East Asian ideograph
    0x223E40: (0x68C3, 0),  # East Asian ideograph
    0x214A60: (0x729B, 0),  # East Asian ideograph
    0x235164: (0x9940, 0),  # East Asian ideograph
    0x233E43: (0x909B, 0),  # East Asian ideograph
    0x233E44: (0x909C, 0),  # East Asian ideograph
    0x213E45: (0x606F, 0),  # East Asian ideograph
    0x223E46: (0x68D4, 0),  # East Asian ideograph
    0x274A61: (0x728A, 0),  # East Asian ideograph
    0x233E48: (0x90A1, 0),  # East Asian ideograph
    0x223E49: (0x68C6, 0),  # East Asian ideograph
    0x213E4A: (0x608C, 0),  # East Asian ideograph
    0x223E4B: (0x68C7, 0),  # East Asian ideograph
    0x213E4C: (0x607F, 0),  # East Asian ideograph
    0x214A62: (0x72A7, 0),  # East Asian ideograph
    0x213E4E: (0x609A, 0),  # East Asian ideograph
    0x213E4F: (0x6096, 0),  # East Asian ideograph
    0x213E50: (0x6084, 0),  # East Asian ideograph
    0x233E51: (0x90A8, 0),  # East Asian ideograph
    0x224828: (0x6CCE, 0),  # East Asian ideograph
    0x234A63: (0x9684, 0),  # East Asian ideograph
    0x233E54: (0x90A0, 0),  # East Asian ideograph
    0x223E55: (0x6938, 0),  # East Asian ideograph
    0x213E56: (0x60A8, 0),  # East Asian ideograph
    0x273E57: (0x5FF0, 0),  # East Asian ideograph
    0x233E58: (0x90AF, 0),  # East Asian ideograph
    0x233E59: (0x90B3, 0),  # East Asian ideograph
    0x6F4C5D: (0xB2A1, 0),  # Korean hangul
    0x213E5B: (
        0x60C5,
        0,
    ),  # East Asian ideograph (variant of 4B3E5B which maps to 60C5)
    0x273E5C: (0x95F7, 0),  # East Asian ideograph
    0x223E5D: (0x6958, 0),  # East Asian ideograph
    0x273E5E: (0x6005, 0),  # East Asian ideograph
    0x213E5F: (0x60BB, 0),  # East Asian ideograph
    0x213E60: (0x60E0, 0),  # East Asian ideograph
    0x233E61: (0x90B2, 0),  # East Asian ideograph
    0x213E62: (0x60DC, 0),  # East Asian ideograph
    0x213E63: (0x60D8, 0),  # East Asian ideograph
    0x223E64: (0x6945, 0),  # East Asian ideograph
    0x223E65: (0x695D, 0),  # East Asian ideograph
    0x223E66: (0x6932, 0),  # East Asian ideograph
    0x213E67: (0x60C6, 0),  # East Asian ideograph
    0x233E68: (0x90C9, 0),  # East Asian ideograph
    0x223E69: (0x696E, 0),  # East Asian ideograph
    0x223E6A: (0x6963, 0),  # East Asian ideograph
    0x223E6B: (0x6948, 0),  # East Asian ideograph
    0x273E6C: (0x60EC, 0),  # East Asian ideograph
    0x213E6D: (0x60F3, 0),  # East Asian ideograph
    0x223E6E: (0x6939, 0),  # East Asian ideograph
    0x233E6F: (0x90D5, 0),  # East Asian ideograph
    0x273E70: (0x607B, 0),  # East Asian ideograph
    0x214A68: (0x72C0, 0),  # East Asian ideograph
    0x233E72: (0x90BE, 0),  # East Asian ideograph
    0x223E73: (0x6937, 0),  # East Asian ideograph
    0x213E74: (0x60F9, 0),  # East Asian ideograph
    0x213E75: (0x6123, 0),  # East Asian ideograph
    0x213E76: (0x60F4, 0),  # East Asian ideograph
    0x273E77: (0x7231, 0),  # East Asian ideograph
    0x233E78: (0x90C8, 0),  # East Asian ideograph
    0x233E79: (0x90C3, 0),  # East Asian ideograph
    0x223E7A: (0x696C, 0),  # East Asian ideograph
    0x223E7B: (0x694E, 0),  # East Asian ideograph
    0x213E7C: (0x6109, 0),  # East Asian ideograph
    0x224A6A: (0x6E51, 0),  # East Asian ideograph
    0x273E7E: (0x607C, 0),  # East Asian ideograph
    0x234137: (0x91A8, 0),  # East Asian ideograph
    0x224A6B: (0x6E44, 0),  # East Asian ideograph
    0x275576: (0x8361, 0),  # East Asian ideograph
    0x27734C: (0x5456, 0),  # East Asian ideograph
    0x21385B: (0x5879, 0),  # East Asian ideograph
    0x293B5B: (0x8F81, 0),  # East Asian ideograph
    0x234A6D: (0x9682, 0),  # East Asian ideograph
    0x234A6E: (0x9683, 0),  # East Asian ideograph
    0x6F5355: (0xC1FC, 0),  # Korean hangul
    0x335238: (0x8989, 0),  # East Asian ideograph
    0x694C68: (0x5301, 0),  # East Asian ideograph
    0x21393A: (0x5958, 0),  # East Asian ideograph
    0x2D5C5A: (0x8FE9, 0),  # East Asian ideograph
    0x2D3A41: (0x5AFA, 0),  # East Asian ideograph
    0x214A70: (0x72F9, 0),  # East Asian ideograph
    0x6F4A71: (0xAF48, 0),  # Korean hangul
    0x213F2D: (0x6177, 0),  # East Asian ideograph
    0x295932: (0x9CD8, 0),  # East Asian ideograph
    0x274A72: (0x72C8, 0),  # East Asian ideograph
    0x23302C: (0x895C, 0),  # East Asian ideograph
    0x276239: (0x9E2F, 0),  # East Asian ideograph
    0x6F4A73: (0xAF4C, 0),  # Korean hangul
    0x6F5356: (0xC1FD, 0),  # Korean hangul
    0x276241: (0x9E45, 0),  # East Asian ideograph
    0x21393B: (0x595A, 0),  # East Asian ideograph
    0x4B324E: (
        0x50E7,
        0,
    ),  # East Asian ideograph (variant of 21324E which maps to 50E7)
    0x2E4E72: (0x6F74, 0),  # East Asian ideograph
    0x6F5774: (0xC911, 0),  # Korean hangul
    0x6F4A75: (0xAF5C, 0),  # Korean hangul
    0x6F4A76: (0xAF5D, 0),  # Korean hangul
    0x213521: (0x53C9, 0),  # East Asian ideograph
    0x224A77: (0x6E4E, 0),  # East Asian ideograph
    0x23302D: (0x895D, 0),  # East Asian ideograph
    0x4B4A78: (0x72F0, 0),  # East Asian ideograph
    0x6F5357: (0xC200, 0),  # Korean hangul
    0x213523: (0x53CA, 0),  # East Asian ideograph
    0x276242: (0x9E51, 0),  # East Asian ideograph
    0x275D49: (0x94AE, 0),  # East Asian ideograph
    0x274A79: (0x72B9, 0),  # East Asian ideograph
    0x223D3B: (0x6874, 0),  # East Asian ideograph
    0x234A7A: (0x9697, 0),  # East Asian ideograph
    0x224D68: (0x6F5D, 0),  # East Asian ideograph
    0x6F4A7B: (0xAF84, 0),  # Korean hangul
    0x213526: (0x53D4, 0),  # East Asian ideograph
    0x227061: (0x7D3A, 0),  # East Asian ideograph
    0x6F4A7C: (0xAF88, 0),  # Korean hangul
    0x225A30: (0x7415, 0),  # East Asian ideograph
    0x213527: (0x53D7, 0),  # East Asian ideograph
    0x227C49: (0x82BC, 0),  # East Asian ideograph
    0x6F4A7D: (0xAF90, 0),  # Korean hangul
    0x6F5358: (0xC204, 0),  # Korean hangul
    0x6F7623: (0x317F, 0),  # Korean hangul
    0x274A7E: (0x72F1, 0),  # East Asian ideograph
    0x223D3C: (0x6875, 0),  # East Asian ideograph
    0x227D2B: (0x8344, 0),  # East Asian ideograph
    0x21352A: (0x66FC, 0),  # East Asian ideograph
    0x213936: (0x594E, 0),  # East Asian ideograph
    0x21352B: (0x53E2, 0),  # East Asian ideograph
    0x2D4B5B: (0x78AF, 0),  # East Asian ideograph
    0x6F5359: (0xC20D, 0),  # Korean hangul
    0x23352D: (0x8B95, 0),  # East Asian ideograph
    0x276244: (0x9E4C, 0),  # East Asian ideograph
    0x23352E: (0x8B94, 0),  # East Asian ideograph
    0x3A7970: (0x81D5, 0),  # East Asian ideograph
    0x21352F: (0x53EE, 0),  # East Asian ideograph
    0x6F5331: (0xC138, 0),  # Korean hangul
    0x275138: (0x7EDC, 0),  # East Asian ideograph
    0x223F21: (0x6952, 0),  # East Asian ideograph
    0x213F22: (0x6168, 0),  # East Asian ideograph
    0x233F23: (0x90DF, 0),  # East Asian ideograph
    0x213F24: (0x613C, 0),  # East Asian ideograph
    0x223F25: (0x695B, 0),  # East Asian ideograph
    0x233F26: (0x90E2, 0),  # East Asian ideograph
    0x223531: (0x64EB, 0),  # East Asian ideograph
    0x233F28: (0x90DB, 0),  # East Asian ideograph
    0x273F29: (0x5FFE, 0),  # East Asian ideograph
    0x233F2A: (0x90DC, 0),  # East Asian ideograph
    0x273F2B: (0x6006, 0),  # East Asian ideograph
    0x233F2C: (0x90D7, 0),  # East Asian ideograph
    0x233F2D: (0x90E4, 0),  # East Asian ideograph
    0x233F2E: (0x90EF, 0),  # East Asian ideograph
    0x233F2F: (0x90EA, 0),  # East Asian ideograph
    0x213F30: (0x6170, 0),  # East Asian ideograph
    0x213F31: (0x615A, 0),  # East Asian ideograph
    0x233F32: (0x90F0, 0),  # East Asian ideograph
    0x233F33: (0x90F4, 0),  # East Asian ideograph
    0x233F34: (0x90F2, 0),  # East Asian ideograph
    0x223F35: (0x6978, 0),  # East Asian ideograph
    0x273F36: (0x8651, 0),  # East Asian ideograph
    0x223F37: (0x697B, 0),  # East Asian ideograph
    0x273F38: (0x60E8, 0),  # East Asian ideograph
    0x273F39: (0x60EF, 0),  # East Asian ideograph
    0x273F3A: (0x6078, 0),  # East Asian ideograph
    0x273F3B: (0x6002, 0),  # East Asian ideograph
    0x273F3C: (0x6B32, 0),  # East Asian ideograph
    0x223F3D: (0x6944, 0),  # East Asian ideograph
    0x233F3E: (0x90EB, 0),  # East Asian ideograph
    0x233F3F: (0x90F3, 0),  # East Asian ideograph
    0x213F40: (0x618E, 0),  # East Asian ideograph
    0x273F41: (0x60AF, 0),  # East Asian ideograph
    0x273F42: (0x6124, 0),  # East Asian ideograph
    0x213F43: (0x61AC, 0),  # East Asian ideograph
    0x273F44: (0x60EE, 0),  # East Asian ideograph
    0x273F45: (0x6187, 0),  # East Asian ideograph
    0x233F46: (0x90FC, 0),  # East Asian ideograph
    0x273F47: (0x60EB, 0),  # East Asian ideograph
    0x273F48: (0x5FC6, 0),  # East Asian ideograph
    0x233F49: (0x9104, 0),  # East Asian ideograph
    0x273F4A: (0x5E94, 0),  # East Asian ideograph
    0x213537: (0x53EB, 0),  # East Asian ideograph
    0x233F4C: (0x9106, 0),  # East Asian ideograph
    0x213F4D: (0x61C2, 0),  # East Asian ideograph
    0x273F4E: (0x6073, 0),  # East Asian ideograph
    0x213F4F: (0x61C8, 0),  # East Asian ideograph
    0x213940: (0x596A, 0),  # East Asian ideograph
    0x232368: (0x84CD, 0),  # East Asian ideograph
    0x213F52: (0x61E6, 0),  # East Asian ideograph
    0x213F53: (
        0x61F2,
        0,
    ),  # East Asian ideograph (variant of 4B3F53 which maps to 61F2)
    0x273F54: (0x6000, 0),  # East Asian ideograph
    0x273F55: (0x61D2, 0),  # East Asian ideograph
    0x273F56: (0x60AC, 0),  # East Asian ideograph
    0x233F57: (0x910F, 0),  # East Asian ideograph
    0x273F58: (0x5FCF, 0),  # East Asian ideograph
    0x273F59: (0x6151, 0),  # East Asian ideograph
    0x233F5A: (0x9116, 0),  # East Asian ideograph
    0x273F5B: (0x60E7, 0),  # East Asian ideograph
    0x233F5C: (0x9114, 0),  # East Asian ideograph
    0x23353A: (0x8B9F, 0),  # East Asian ideograph
    0x213F5E: (0x620A, 0),  # East Asian ideograph
    0x213F5F: (0x620E, 0),  # East Asian ideograph
    0x223F60: (0x69BC, 0),  # East Asian ideograph
    0x223F61: (0x69A7, 0),  # East Asian ideograph
    0x233F62: (0x9123, 0),  # East Asian ideograph (Version J extension)
    0x233F63: (0x9118, 0),  # East Asian ideograph
    0x233F64: (0x911C, 0),  # East Asian ideograph
    0x213F65: (0x6216, 0),  # East Asian ideograph
    0x233F66: (0x9120, 0),  # East Asian ideograph
    0x233F67: (0x9122, 0),  # East Asian ideograph
    0x223F68: (0x69D9, 0),  # East Asian ideograph
    0x213F69: (0x621F, 0),  # East Asian ideograph
    0x223F6A: (0x698E, 0),  # East Asian ideograph
    0x213F6B: (0x6222, 0),  # East Asian ideograph
    0x213F6C: (0x622A, 0),  # East Asian ideograph
    0x223F6D: (0x69D6, 0),  # East Asian ideograph
    0x273F6E: (0x6218, 0),  # East Asian ideograph
    0x273F6F: (0x620F, 0),  # East Asian ideograph
    0x213F70: (0x6234, 0),  # East Asian ideograph
    0x233F71: (0x9124, 0),  # East Asian ideograph
    0x233F72: (0x911A, 0),  # East Asian ideograph
    0x213F73: (0x623F, 0),  # East Asian ideograph
    0x233F74: (0x9125, 0),  # East Asian ideograph
    0x223F75: (0x69A5, 0),  # East Asian ideograph
    0x213F76: (0x6241, 0),  # East Asian ideograph
    0x233F77: (0x912F, 0),  # East Asian ideograph
    0x223F78: (0x69D1, 0),  # East Asian ideograph
    0x27513B: (0x4E1D, 0),  # East Asian ideograph
    0x223F7A: (0x69F6, 0),  # East Asian ideograph
    0x21753F: (0x579E, 0),  # East Asian ideograph
    0x213F7D: (0x6253, 0),  # East Asian ideograph
    0x223F7E: (0x69D5, 0),  # East Asian ideograph
    0x217540: (0x57B5, 0),  # East Asian ideograph
    0x6F535D: (0xC21C, 0),  # Korean hangul
    0x276248: (0x9E5E, 0),  # East Asian ideograph
    0x223542: (0x64F7, 0),  # East Asian ideograph
    0x213543: (0x540C, 0),  # East Asian ideograph
    0x213544: (0x540A, 0),  # East Asian ideograph
    0x29593A: (0x9C85, 0),  # East Asian ideograph
    0x23524D: (0x99BF, 0),  # East Asian ideograph
    0x213545: (0x540D, 0),  # East Asian ideograph
    0x6F535E: (0xC21F, 0),  # Korean hangul
    0x223546: (0x6504, 0),  # East Asian ideograph
    0x234E5E: (0x97E0, 0),  # East Asian ideograph
    0x2D3547: (0x55AB, 0),  # East Asian ideograph
    0x6F5C66: (0xD560, 0),  # Korean hangul
    0x234141: (0x91AF, 0),  # East Asian ideograph
    0x692436: (0x3056, 0),  # Hiragana letter ZA
    0x696868: (0x84D9, 0),  # East Asian ideograph
    0x233478: (0x8B85, 0),  # East Asian ideograph
    0x4C354A: (0x64B8, 0),  # East Asian ideograph
    0x22587D: (0x73CC, 0),  # East Asian ideograph
    0x22354B: (0x64FD, 0),  # East Asian ideograph
    0x333021: (0x58F9, 0),  # East Asian ideograph
    0x225F5C: (0x7633, 0),  # East Asian ideograph
    0x217933: (0x5940, 0),  # East Asian ideograph
    0x234142: (0x91B1, 0),  # East Asian ideograph
    0x23346B: (0x8B6D, 0),  # East Asian ideograph
    0x23354D: (0x8C4B, 0),  # East Asian ideograph
    0x2D7A44: (0x598D, 0),  # East Asian ideograph
    0x27513E: (0x7EE2, 0),  # East Asian ideograph
    0x23472C: (0x93D3, 0),  # East Asian ideograph
    0x22354F: (0x6508, 0),  # East Asian ideograph
    0x395E42: (0x9274, 0),  # East Asian ideograph
    0x233550: (0x8C4F, 0),  # East Asian ideograph
    0x3F5F35: (0x6B9E, 0),  # East Asian ideograph
    0x39303A: (0x5EFC, 0),  # East Asian ideograph
    0x213552: (0x543E, 0),  # East Asian ideograph
    0x27513F: (0x7EE5, 0),  # East Asian ideograph
    0x213553: (0x5427, 0),  # East Asian ideograph
    0x213554: (0x5440, 0),  # East Asian ideograph
    0x274476: (0x6808, 0),  # East Asian ideograph
    0x233555: (0x8C5C, 0),  # East Asian ideograph
    0x6F5A26: (0xCEE8, 0),  # Korean hangul
    0x213556: (0x5446, 0),  # East Asian ideograph
    0x217557: (0x57A1, 0),  # East Asian ideograph
    0x213266: (0x512A, 0),  # East Asian ideograph
    0x293C30: (0x8F98, 0),  # East Asian ideograph
    0x224B38: (0x6E69, 0),  # East Asian ideograph
    0x6F5332: (0xC139, 0),  # Korean hangul
    0x293725: (0x8D3D, 0),  # East Asian ideograph
    0x287229: (0x7F17, 0),  # East Asian ideograph
    0x223559: (0x651A, 0),  # East Asian ideograph
    0x6F5362: (0xC22B, 0),  # Korean hangul
    0x27624D: (0x9E6D, 0),  # East Asian ideograph
    0x214021: (0x6252, 0),  # East Asian ideograph
    0x214022: (0x625B, 0),  # East Asian ideograph
    0x214023: (0x6263, 0),  # East Asian ideograph
    0x214024: (0x6258, 0),  # East Asian ideograph
    0x214025: (0x6296, 0),  # East Asian ideograph
    0x214026: (0x6297, 0),  # East Asian ideograph
    0x214027: (0x6292, 0),  # East Asian ideograph
    0x214028: (0x6276, 0),  # East Asian ideograph
    0x214029: (0x6289, 0),  # East Asian ideograph
    0x21402A: (0x627F, 0),  # East Asian ideograph
    0x21402B: (0x6279, 0),  # East Asian ideograph
    0x21402C: (0x6280, 0),  # East Asian ideograph
    0x21402D: (0x628A, 0),  # East Asian ideograph
    0x21402E: (0x626D, 0),  # East Asian ideograph
    0x21402F: (0x627C, 0),  # East Asian ideograph
    0x214030: (0x627E, 0),  # East Asian ideograph
    0x214031: (0x626F, 0),  # East Asian ideograph
    0x214032: (0x6284, 0),  # East Asian ideograph
    0x214033: (0x6295, 0),  # East Asian ideograph
    0x214034: (0x6291, 0),  # East Asian ideograph
    0x214035: (0x6298, 0),  # East Asian ideograph
    0x214036: (0x626E, 0),  # East Asian ideograph
    0x214037: (0x6273, 0),  # East Asian ideograph
    0x214038: (0x6293, 0),  # East Asian ideograph
    0x214039: (0x62C9, 0),  # East Asian ideograph
    0x21403A: (0x62C4, 0),  # East Asian ideograph
    0x21403B: (0x62CC, 0),  # East Asian ideograph
    0x21403C: (0x62A8, 0),  # East Asian ideograph
    0x21403D: (0x62DC, 0),  # East Asian ideograph
    0x21403E: (0x62BF, 0),  # East Asian ideograph
    0x21403F: (0x62C2, 0),  # East Asian ideograph
    0x214040: (0x62B9, 0),  # East Asian ideograph
    0x214041: (0x62D2, 0),  # East Asian ideograph
    0x214042: (0x62D3, 0),  # East Asian ideograph
    0x214043: (0x62DB, 0),  # East Asian ideograph
    0x214044: (0x62AB, 0),  # East Asian ideograph
    0x214045: (0x62CB, 0),  # East Asian ideograph
    0x214046: (0x62D4, 0),  # East Asian ideograph
    0x214047: (0x62BD, 0),  # East Asian ideograph
    0x214048: (0x62BC, 0),  # East Asian ideograph
    0x214049: (
        0x62D0,
        0,
    ),  # East Asian ideograph (variant of 4B4049 which maps to 62D0)
    0x21404A: (0x62C8, 0),  # East Asian ideograph
    0x21404B: (0x62D9, 0),  # East Asian ideograph
    0x21404C: (0x62DA, 0),  # East Asian ideograph
    0x21404D: (0x62AC, 0),  # East Asian ideograph
    0x21404E: (0x62C7, 0),  # East Asian ideograph
    0x21404F: (0x62B1, 0),  # East Asian ideograph
    0x214050: (0x62D6, 0),  # East Asian ideograph
    0x214051: (0x62D8, 0),  # East Asian ideograph
    0x214052: (0x62CD, 0),  # East Asian ideograph
    0x214053: (0x62B5, 0),  # East Asian ideograph
    0x214054: (0x62CE, 0),  # East Asian ideograph
    0x214055: (0x62D7, 0),  # East Asian ideograph
    0x214056: (0x62C6, 0),  # East Asian ideograph
    0x214057: (0x6309, 0),  # East Asian ideograph
    0x214058: (0x6316, 0),  # East Asian ideograph
    0x214059: (0x62FC, 0),  # East Asian ideograph
    0x21405A: (0x62F3, 0),  # East Asian ideograph
    0x21405B: (0x6308, 0),  # East Asian ideograph
    0x21405C: (0x62ED, 0),  # East Asian ideograph
    0x21405D: (0x6301, 0),  # East Asian ideograph
    0x21405E: (0x62EE, 0),  # East Asian ideograph
    0x21405F: (0x62EF, 0),  # East Asian ideograph
    0x214060: (0x62F7, 0),  # East Asian ideograph
    0x214061: (0x6307, 0),  # East Asian ideograph
    0x214062: (0x62F1, 0),  # East Asian ideograph
    0x214063: (0x62FD, 0),  # East Asian ideograph
    0x214064: (0x6311, 0),  # East Asian ideograph
    0x214065: (0x62EC, 0),  # East Asian ideograph
    0x214066: (
        0x62F4,
        0,
    ),  # East Asian ideograph (variant of 4B4066 which maps to 62F4)
    0x214067: (0x62FF, 0),  # East Asian ideograph
    0x224068: (0x6A2D, 0),  # East Asian ideograph
    0x214069: (0x6342, 0),  # East Asian ideograph
    0x21406A: (0x632A, 0),  # East Asian ideograph
    0x21406B: (0x6355, 0),  # East Asian ideograph
    0x21406C: (0x633E, 0),  # East Asian ideograph
    0x21406D: (0x632F, 0),  # East Asian ideograph
    0x21406E: (0x634E, 0),  # East Asian ideograph
    0x21406F: (0x634F, 0),  # East Asian ideograph
    0x214070: (0x6350, 0),  # East Asian ideograph
    0x214071: (0x6349, 0),  # East Asian ideograph
    0x224072: (0x6A1D, 0),  # East Asian ideograph
    0x214073: (0x632B, 0),  # East Asian ideograph
    0x214074: (0x6328, 0),  # East Asian ideograph
    0x214075: (0x633A, 0),  # East Asian ideograph
    0x214076: (0x63A5, 0),  # East Asian ideograph
    0x214077: (0x6369, 0),  # East Asian ideograph
    0x214078: (0x63A0, 0),  # East Asian ideograph
    0x214079: (0x6396, 0),  # East Asian ideograph
    0x21407A: (0x63A7, 0),  # East Asian ideograph
    0x21407B: (0x6372, 0),  # East Asian ideograph
    0x21407C: (0x6377, 0),  # East Asian ideograph
    0x21407D: (0x6383, 0),  # East Asian ideograph
    0x21407E: (0x636B, 0),  # East Asian ideograph
    0x2D5C74: (0x96A3, 0),  # East Asian ideograph
    0x2D5831: (0x89A7, 0),  # East Asian ideograph
    0x21756C: (0x57BE, 0),  # East Asian ideograph
    0x693729: (0x7C82, 0),  # East Asian ideograph
    0x23356D: (0x8C73, 0),  # East Asian ideograph
    0x6F5966: (0xCE5C, 0),  # Korean hangul
    0x29252D: (0x8311, 0),  # East Asian ideograph
    0x6F5366: (0xC232, 0),  # Korean hangul
    0x276251: (0x76D0, 0),  # East Asian ideograph
    0x6F5463: (0xC46C, 0),  # Korean hangul
    0x6F4F23: (0xB800, 0),  # Korean hangul
    0x21356F: (0x547B, 0),  # East Asian ideograph
    0x6F4C71: (0xB2EB, 0),  # Korean hangul
    0x233571: (0x8C75, 0),  # East Asian ideograph
    0x28722A: (0x7F02, 0),  # East Asian ideograph
    0x213572: (0x5484, 0),  # East Asian ideograph
    0x6F4A54: (0xAE7B, 0),  # Korean hangul
    0x39593F: (0x8A3C, 0),  # East Asian ideograph
    0x233573: (0x8C77, 0),  # East Asian ideograph
    0x276252: (0x7877, 0),  # East Asian ideograph
    0x213D7B: (0x5FD8, 0),  # East Asian ideograph
    0x6F4F24: (0xB801, 0),  # Korean hangul
    0x213574: (0x5468, 0),  # East Asian ideograph
    0x223D4B: (0x68B4, 0),  # East Asian ideograph
    0x692568: (0x30E8, 0),  # Katakana letter YO
    0x213575: (0x5486, 0),  # East Asian ideograph
    0x213939: (0x5957, 0),  # East Asian ideograph
    0x6F5A2F: (0xCF01, 0),  # Korean hangul
    0x393B6E: (0x5C97, 0),  # East Asian ideograph
    0x2D6021: (0x978C, 0),  # East Asian ideograph
    0x335652: (0x87C1, 0),  # East Asian ideograph
    0x223577: (0x652E, 0),  # East Asian ideograph
    0x216022: (0x978B, 0),  # East Asian ideograph
    0x216023: (0x978F, 0),  # East Asian ideograph
    0x215B66: (0x8FC6, 0),  # East Asian ideograph
    0x694838: (0x567A, 0),  # East Asian ideograph
    0x216024: (0x9798, 0),  # East Asian ideograph
    0x4B5036: (0x7C14, 0),  # East Asian ideograph
    0x277360: (0x5181, 0),  # East Asian ideograph
    0x21357B: (0x5471, 0),  # East Asian ideograph
    0x21357C: (0x549A, 0),  # East Asian ideograph
    0x454E43: (
        0x788C,
        0,
    ),  # East Asian ideograph (variant of 214E43 which maps to 788C)
    0x21357D: (0x548E, 0),  # East Asian ideograph
    0x216028: (0x97AD, 0),  # East Asian ideograph
    0x6F4F26: (0xB808, 0),  # Korean hangul
    0x215724: (0x87A2, 0),  # East Asian ideograph
    0x275E7B: (0x9635, 0),  # East Asian ideograph
    0x6F5D6E: (0xD758, 0),  # Korean hangul
    0x21602B: (0x97C6, 0),  # East Asian ideograph
    0x335259: (0x7E59, 0),  # East Asian ideograph
    0x27602C: (0x97E6, 0),  # East Asian ideograph
    0x27623D: (0x9E3D, 0),  # East Asian ideograph
    0x4B4347: (0x66A8, 0),  # East Asian ideograph
    0x6F536A: (0xC26C, 0),  # Korean hangul
    0x27602D: (0x97E7, 0),  # East Asian ideograph
    0x6F4F27: (0xB809, 0),  # Korean hangul
    0x6F592B: (0xCC3E, 0),  # Korean hangul
    0x213938: (0x5950, 0),  # East Asian ideograph
    0x2D3A60: (0x6588, 0),  # East Asian ideograph
    0x27602F: (0x97EC, 0),  # East Asian ideograph
    0x214121: (0x6367, 0),  # East Asian ideograph
    0x214122: (0x6398, 0),  # East Asian ideograph
    0x214123: (0x639B, 0),  # East Asian ideograph
    0x214124: (0x63AA, 0),  # East Asian ideograph
    0x214125: (0x6371, 0),  # East Asian ideograph
    0x214126: (0x63A9, 0),  # East Asian ideograph
    0x214127: (0x638C, 0),  # East Asian ideograph
    0x214128: (0x6389, 0),  # East Asian ideograph
    0x214129: (0x63A2, 0),  # East Asian ideograph
    0x21412A: (0x6399, 0),  # East Asian ideograph
    0x21412B: (0x63A1, 0),  # East Asian ideograph
    0x21412C: (0x6388, 0),  # East Asian ideograph
    0x21412D: (0x63AC, 0),  # East Asian ideograph
    0x21412E: (0x633D, 0),  # East Asian ideograph
    0x21412F: (0x6392, 0),  # East Asian ideograph
    0x214130: (0x63A3, 0),  # East Asian ideograph
    0x214131: (0x6376, 0),  # East Asian ideograph
    0x214132: (0x638F, 0),  # East Asian ideograph
    0x214133: (0x63A8, 0),  # East Asian ideograph
    0x214134: (0x637B, 0),  # East Asian ideograph
    0x214135: (
        0x6368,
        0,
    ),  # East Asian ideograph (variant of 4B4135 which maps to 6368)
    0x214136: (0x6384, 0),  # East Asian ideograph
    0x214137: (0x6380, 0),  # East Asian ideograph
    0x214138: (0x63C6, 0),  # East Asian ideograph
    0x214139: (0x63C9, 0),  # East Asian ideograph
    0x21413A: (0x63CD, 0),  # East Asian ideograph
    0x21413B: (0x63E1, 0),  # East Asian ideograph
    0x21413C: (0x63C0, 0),  # East Asian ideograph
    0x21413D: (0x63E9, 0),  # East Asian ideograph
    0x21413E: (0x63D0, 0),  # East Asian ideograph
    0x21413F: (0x63DA, 0),  # East Asian ideograph
    0x214140: (0x63D6, 0),  # East Asian ideograph
    0x214141: (0x63ED, 0),  # East Asian ideograph
    0x214142: (0x63EE, 0),  # East Asian ideograph
    0x214143: (0x63CF, 0),  # East Asian ideograph
    0x214144: (0x63E3, 0),  # East Asian ideograph
    0x214145: (0x63F4, 0),  # East Asian ideograph
    0x214146: (
        0x63DB,
        0,
    ),  # East Asian ideograph (variant of 454146 which maps to 63DB)
    0x214147: (0x63D2, 0),  # East Asian ideograph
    0x234148: (0x91AE, 0),  # East Asian ideograph
    0x214149: (0x641E, 0),  # East Asian ideograph
    0x21414A: (0x642A, 0),  # East Asian ideograph
    0x23414B: (0x91B4, 0),  # East Asian ideograph
    0x23414C: (0x91B2, 0),  # East Asian ideograph
    0x21414D: (0x640F, 0),  # East Asian ideograph
    0x21414E: (0x6414, 0),  # East Asian ideograph
    0x21414F: (0x640D, 0),  # East Asian ideograph
    0x214150: (0x642D, 0),  # East Asian ideograph
    0x214151: (0x643D, 0),  # East Asian ideograph
    0x214152: (0x6416, 0),  # East Asian ideograph
    0x214153: (0x6417, 0),  # East Asian ideograph
    0x214154: (0x641C, 0),  # East Asian ideograph
    0x214155: (0x6436, 0),  # East Asian ideograph
    0x214156: (0x642C, 0),  # East Asian ideograph
    0x214157: (0x6458, 0),  # East Asian ideograph
    0x214158: (0x6469, 0),  # East Asian ideograph
    0x214159: (0x6454, 0),  # East Asian ideograph
    0x21415A: (0x6452, 0),  # East Asian ideograph
    0x21415B: (0x646F, 0),  # East Asian ideograph
    0x21415C: (0x6478, 0),  # East Asian ideograph
    0x21415D: (0x6479, 0),  # East Asian ideograph
    0x21415E: (0x647A, 0),  # East Asian ideograph
    0x21415F: (0x645F, 0),  # East Asian ideograph
    0x214160: (0x6451, 0),  # East Asian ideograph
    0x214161: (0x6467, 0),  # East Asian ideograph
    0x214162: (0x649E, 0),  # East Asian ideograph
    0x214163: (0x64A4, 0),  # East Asian ideograph
    0x214164: (0x6487, 0),  # East Asian ideograph
    0x214165: (0x6488, 0),  # East Asian ideograph
    0x214166: (0x64A5, 0),  # East Asian ideograph
    0x214167: (0x64B0, 0),  # East Asian ideograph
    0x214168: (0x6493, 0),  # East Asian ideograph
    0x214169: (0x6495, 0),  # East Asian ideograph
    0x21416A: (0x6492, 0),  # East Asian ideograph
    0x21416B: (0x64A9, 0),  # East Asian ideograph
    0x21416C: (0x6491, 0),  # East Asian ideograph
    0x21416D: (0x64AE, 0),  # East Asian ideograph
    0x21416E: (0x64B2, 0),  # East Asian ideograph
    0x21416F: (0x64AD, 0),  # East Asian ideograph
    0x214170: (0x649A, 0),  # East Asian ideograph
    0x214171: (0x64AB, 0),  # East Asian ideograph
    0x214172: (0x64AC, 0),  # East Asian ideograph
    0x214173: (0x64C5, 0),  # East Asian ideograph
    0x214174: (0x64C1, 0),  # East Asian ideograph
    0x214175: (0x64D8, 0),  # East Asian ideograph
    0x214176: (0x64CA, 0),  # East Asian ideograph
    0x214177: (0x64BB, 0),  # East Asian ideograph
    0x214178: (0x64C2, 0),  # East Asian ideograph
    0x214179: (0x64BC, 0),  # East Asian ideograph
    0x21417A: (0x64CB, 0),  # East Asian ideograph
    0x21417B: (0x64CD, 0),  # East Asian ideograph
    0x21417C: (0x64DA, 0),  # East Asian ideograph
    0x21417D: (0x64C4, 0),  # East Asian ideograph
    0x21417E: (0x64C7, 0),  # East Asian ideograph
    0x705C50: (0x82C4, 0),  # East Asian ideograph
    0x216040: (0x9813, 0),  # East Asian ideograph
    0x393E61: (0x60AA, 0),  # East Asian ideograph
    0x6F536E: (0xC27D, 0),  # Korean hangul
    0x216041: (0x9812, 0),  # East Asian ideograph
    0x2D3571: (0x546A, 0),  # East Asian ideograph
    0x6F4F2B: (0xB819, 0),  # Korean hangul
    0x29483E: (0x9554, 0),  # East Asian ideograph
    0x276042: (0x9882, 0),  # East Asian ideograph
    0x276043: (0x9887, 0),  # East Asian ideograph
    0x6F5D6F: (0xD759, 0),  # Korean hangul
    0x276044: (0x9886, 0),  # East Asian ideograph
    0x69594B: (0x6327, 0),  # East Asian ideograph
    0x276045: (0x9889, 0),  # East Asian ideograph
    0x27623E: (0x9E49, 0),  # East Asian ideograph
    0x6F536F: (0xC27F, 0),  # Korean hangul
    0x276046: (0x5934, 0),  # East Asian ideograph
    0x6F4F2C: (0xB81B, 0),  # Korean hangul
    0x213954: (0x5999, 0),  # East Asian ideograph
    0x29483F: (0x9572, 0),  # East Asian ideograph
    0x236047: (0x9F76, 0),  # East Asian ideograph
    0x6F5775: (0xC918, 0),  # Korean hangul
    0x216048: (0x9838, 0),  # East Asian ideograph
    0x6F503A: (0xBAA8, 0),  # Korean hangul
    0x216049: (0x983B, 0),  # East Asian ideograph
    0x213E58: (0x60E6, 0),  # East Asian ideograph
    0x222C47: (0x60D3, 0),  # East Asian ideograph
    0x21604A: (0x9839, 0),  # East Asian ideograph
    0x6F5370: (0xC281, 0),  # Korean hangul
    0x27625B: (0x9EA6, 0),  # East Asian ideograph
    0x27604B: (0x9894, 0),  # East Asian ideograph
    0x6F4F2D: (0xB81D, 0),  # Korean hangul
    0x27604C: (0x9890, 0),  # East Asian ideograph
    0x225B2A: (0x748A, 0),  # East Asian ideograph
    0x27604D: (0x9897, 0),  # East Asian ideograph
    0x213269: (0x5132, 0),  # East Asian ideograph
    0x4C725D: (0x7A39, 0),  # East Asian ideograph
    0x27604E: (0x989C, 0),  # East Asian ideograph
    0x27604F: (0x989D, 0),  # East Asian ideograph
    0x2D4730: (0x51B5, 0),  # East Asian ideograph
    0x27625C: (0x9EB8, 0),  # East Asian ideograph
    0x276050: (0x9898, 0),  # East Asian ideograph
    0x276051: (0x989A, 0),  # East Asian ideograph
    0x216052: (0x9853, 0),  # East Asian ideograph
    0x393B78: (0x5CC4, 0),  # East Asian ideograph (duplicate simplified)
    0x276053: (0x7C7B, 0),  # East Asian ideograph
    0x284F39: (0x6CF8, 0),  # East Asian ideograph
    0x276054: (0x98A0, 0),  # East Asian ideograph
    0x6F5372: (0xC289, 0),  # Korean hangul
    0x216055: (0x9858, 0),  # East Asian ideograph
    0x6F4F2F: (0xB825, 0),  # Korean hangul
    0x4B4866: (0x6E89, 0),  # East Asian ideograph
    0x276056: (0x987E, 0),  # East Asian ideograph
    0x69243A: (0x305A, 0),  # Hiragana letter ZU
    0x276057: (0x98A4, 0),  # East Asian ideograph
    0x276058: (0x663E, 0),  # East Asian ideograph
    0x213861: (0x589C, 0),  # East Asian ideograph
    0x4B614D: (0x9A13, 0),  # East Asian ideograph
    0x216059: (0x9871, 0),  # East Asian ideograph
    0x4C4333: (0x6AAA, 0),  # East Asian ideograph
    0x27625E: (0x9762, 0),  # East Asian ideograph
    0x27605A: (0x98A6, 0),  # East Asian ideograph
    0x6F4F30: (0xB828, 0),  # Korean hangul
    0x214221: (0x64CE, 0),  # East Asian ideograph
    0x214222: (0x64D4, 0),  # East Asian ideograph
    0x214223: (0x64D2, 0),  # East Asian ideograph
    0x214224: (0x64BF, 0),  # East Asian ideograph
    0x234225: (0x9201, 0),  # East Asian ideograph
    0x214226: (0x64F0, 0),  # East Asian ideograph
    0x214227: (0x64E6, 0),  # East Asian ideograph
    0x214228: (0x64EC, 0),  # East Asian ideograph
    0x214229: (0x64F1, 0),  # East Asian ideograph
    0x21422A: (0x64F4, 0),  # East Asian ideograph
    0x21422B: (0x64F2, 0),  # East Asian ideograph
    0x21422C: (0x6506, 0),  # East Asian ideograph
    0x21422D: (0x6500, 0),  # East Asian ideograph
    0x27422E: (0x6270, 0),  # East Asian ideograph
    0x21422F: (0x64FB, 0),  # East Asian ideograph
    0x214230: (0x64FA, 0),  # East Asian ideograph
    0x214231: (0x650F, 0),  # East Asian ideograph
    0x214232: (0x6518, 0),  # East Asian ideograph
    0x214233: (0x6514, 0),  # East Asian ideograph
    0x214234: (0x6519, 0),  # East Asian ideograph
    0x214235: (0x651D, 0),  # East Asian ideograph
    0x214236: (0x651C, 0),  # East Asian ideograph
    0x214237: (0x6523, 0),  # East Asian ideograph
    0x214238: (0x6524, 0),  # East Asian ideograph
    0x214239: (0x652B, 0),  # East Asian ideograph
    0x21423A: (0x652A, 0),  # East Asian ideograph
    0x21423B: (0x652C, 0),  # East Asian ideograph
    0x21423C: (0x652F, 0),  # East Asian ideograph
    0x21423D: (0x6536, 0),  # East Asian ideograph
    0x21423E: (0x6539, 0),  # East Asian ideograph
    0x21423F: (0x653B, 0),  # East Asian ideograph
    0x214240: (0x653E, 0),  # East Asian ideograph
    0x214241: (0x653F, 0),  # East Asian ideograph
    0x214242: (0x6545, 0),  # East Asian ideograph
    0x214243: (0x6548, 0),  # East Asian ideograph
    0x214244: (0x654E, 0),  # East Asian ideograph
    0x214245: (0x6556, 0),  # East Asian ideograph
    0x214246: (0x6551, 0),  # East Asian ideograph
    0x274247: (0x8D25, 0),  # East Asian ideograph
    0x214248: (0x655D, 0),  # East Asian ideograph
    0x214249: (0x6558, 0),  # East Asian ideograph
    0x21424A: (0x654F, 0),  # East Asian ideograph
    0x21424B: (0x6566, 0),  # East Asian ideograph
    0x21424C: (0x6562, 0),  # East Asian ideograph
    0x21424D: (0x6563, 0),  # East Asian ideograph
    0x21424E: (0x655E, 0),  # East Asian ideograph
    0x21424F: (0x5553, 0),  # East Asian ideograph
    0x214250: (0x656C, 0),  # East Asian ideograph
    0x214251: (0x6572, 0),  # East Asian ideograph
    0x214252: (0x6575, 0),  # East Asian ideograph
    0x214253: (0x6577, 0),  # East Asian ideograph
    0x214254: (0x6578, 0),  # East Asian ideograph
    0x214255: (0x6574, 0),  # East Asian ideograph
    0x214256: (0x6582, 0),  # East Asian ideograph
    0x214257: (0x6583, 0),  # East Asian ideograph
    0x214258: (0x6587, 0),  # East Asian ideograph
    0x214259: (0x6591, 0),  # East Asian ideograph
    0x21425A: (0x6590, 0),  # East Asian ideograph
    0x6F4F32: (0xB834, 0),  # Korean hangul
    0x21425C: (0x6599, 0),  # East Asian ideograph
    0x21425D: (0x659C, 0),  # East Asian ideograph
    0x21425E: (0x659F, 0),  # East Asian ideograph
    0x21425F: (0x65A1, 0),  # East Asian ideograph
    0x214260: (0x65A4, 0),  # East Asian ideograph
    0x214261: (0x65A5, 0),  # East Asian ideograph
    0x214262: (0x65A7, 0),  # East Asian ideograph
    0x274263: (0x65A9, 0),  # East Asian ideograph
    0x214264: (0x65AF, 0),  # East Asian ideograph
    0x214265: (0x65B0, 0),  # East Asian ideograph
    0x274266: (0x65AD, 0),  # East Asian ideograph
    0x214267: (0x65B9, 0),  # East Asian ideograph
    0x224268: (0x6AB4, 0),  # East Asian ideograph
    0x214269: (0x65BD, 0),  # East Asian ideograph
    0x21426A: (0x65C1, 0),  # East Asian ideograph
    0x21426B: (0x65C5, 0),  # East Asian ideograph
    0x21426C: (0x65CE, 0),  # East Asian ideograph
    0x21426D: (0x65CB, 0),  # East Asian ideograph
    0x21426E: (0x65CC, 0),  # East Asian ideograph
    0x21426F: (0x65CF, 0),  # East Asian ideograph
    0x214270: (0x65D7, 0),  # East Asian ideograph
    0x214271: (0x65D6, 0),  # East Asian ideograph
    0x214272: (0x65E2, 0),  # East Asian ideograph
    0x214273: (0x65E5, 0),  # East Asian ideograph
    0x234274: (0x923F, 0),  # East Asian ideograph
    0x214275: (0x65E9, 0),  # East Asian ideograph
    0x214276: (0x65EC, 0),  # East Asian ideograph
    0x214277: (0x65ED, 0),  # East Asian ideograph
    0x214278: (0x65E8, 0),  # East Asian ideograph
    0x214279: (0x65F1, 0),  # East Asian ideograph
    0x21427A: (0x65FA, 0),  # East Asian ideograph
    0x21427B: (0x6606, 0),  # East Asian ideograph
    0x21427C: (0x6614, 0),  # East Asian ideograph
    0x21427D: (0x660C, 0),  # East Asian ideograph
    0x21427E: (0x6600, 0),  # East Asian ideograph
    0x6F5779: (0xC954, 0),  # Korean hangul
    0x21606B: (0x98EF, 0),  # East Asian ideograph
    0x27606C: (0x9972, 0),  # East Asian ideograph
    0x453F6D: (0x52E0, 0),  # East Asian ideograph
    0x29373A: (0x8D46, 0),  # East Asian ideograph
    0x22606D: (0x76AD, 0),  # East Asian ideograph
    0x6F5377: (0xC2A4, 0),  # Korean hangul
    0x27606E: (0x9971, 0),  # East Asian ideograph
    0x6F4F34: (0xB837, 0),  # Korean hangul
    0x21395C: (0x59B9, 0),  # East Asian ideograph
    0x27606F: (0x9970, 0),  # East Asian ideograph
    0x69243B: (0x305B, 0),  # Hiragana letter SE
    0x276070: (0x997A, 0),  # East Asian ideograph
    0x2D362A: (0x95A7, 0),  # East Asian ideograph
    0x275156: (0x7F04, 0),  # East Asian ideograph
    0x277272: (0x54D2, 0),  # East Asian ideograph
    0x236071: (0x9FA5, 0),  # East Asian ideograph
    0x213862: (0x58AE, 0),  # East Asian ideograph
    0x216072: (0x990C, 0),  # East Asian ideograph
    0x6F5378: (0xC2A5, 0),  # Korean hangul
    0x276073: (0x9977, 0),  # East Asian ideograph
    0x215B76: (0x8FF7, 0),  # East Asian ideograph
    0x21395D: (0x59C6, 0),  # East Asian ideograph
    0x216074: (0x9910, 0),  # East Asian ideograph
    0x276075: (0x9981, 0),  # East Asian ideograph
    0x6F5D71: (0xD761, 0),  # Korean hangul
    0x276076: (0x4F59, 0),  # East Asian ideograph
    0x295955: (0x9C8E, 0),  # East Asian ideograph
    0x6F4B21: (0xAF9C, 0),  # Korean hangul
    0x216077: (0x9913, 0),  # East Asian ideograph
    0x214B22: (0x733E, 0),  # East Asian ideograph
    0x2D4738: (0x6FFC, 0),  # East Asian ideograph
    0x276078: (0x997C, 0),  # East Asian ideograph
    0x214B23: (0x7345, 0),  # East Asian ideograph
    0x276079: (0x9986, 0),  # East Asian ideograph
    0x4B553F: (
        0x83BD,
        0,
    ),  # East Asian ideograph (variant of 21553F which maps to 83BD)
    0x224B24: (0x6E5C, 0),  # East Asian ideograph
    0x27607A: (0x996F, 0),  # East Asian ideograph
    0x27607B: (0x9984, 0),  # East Asian ideograph
    0x224E6A: (0x700D, 0),  # East Asian ideograph
    0x27607C: (0x9985, 0),  # East Asian ideograph
    0x214B27: (0x7368, 0),  # East Asian ideograph
    0x6F537A: (0xC2AC, 0),  # Korean hangul
    0x217334: (0x5686, 0),  # East Asian ideograph
    0x214B28: (0x7370, 0),  # East Asian ideograph
    0x29484A: (0x956C, 0),  # East Asian ideograph
    0x27607E: (0x998F, 0),  # East Asian ideograph
    0x6F5D6D: (0xD757, 0),  # Korean hangul
    0x214B29: (0x7372, 0),  # East Asian ideograph
    0x4C5447: (
        0x71E0,
        0,
    ),  # East Asian ideograph (variant of 225447 which maps to 71E0)
    0x214B2A: (0x7377, 0),  # East Asian ideograph
    0x2E7374: (0x7E89, 0),  # East Asian ideograph
    0x214B2B: (0x7378, 0),  # East Asian ideograph
    0x2E6060: (0x76A1, 0),  # East Asian ideograph
    0x214B2C: (0x7375, 0),  # East Asian ideograph
    0x6F537B: (0xC2AD, 0),  # Korean hangul
    0x214B2D: (0x737A, 0),  # East Asian ideograph
    0x213960: (0x59AF, 0),  # East Asian ideograph
    0x286222: (0x7726, 0),  # East Asian ideograph
    0x214B2E: (0x737B, 0),  # East Asian ideograph
    0x335F34: (0x90C4, 0),  # East Asian ideograph
    0x21393D: (0x5962, 0),  # East Asian ideograph
    0x274B2F: (0x7321, 0),  # East Asian ideograph
    0x295958: (0x9C9A, 0),  # East Asian ideograph
    0x214321: (0x660E, 0),  # East Asian ideograph
    0x214322: (0x6613, 0),  # East Asian ideograph
    0x214323: (0x6602, 0),  # East Asian ideograph
    0x214324: (0x660F, 0),  # East Asian ideograph
    0x214325: (0x6625, 0),  # East Asian ideograph
    0x214326: (0x6627, 0),  # East Asian ideograph
    0x214327: (0x662F, 0),  # East Asian ideograph
    0x214328: (0x662D, 0),  # East Asian ideograph
    0x214329: (0x6620, 0),  # East Asian ideograph
    0x21432A: (0x661F, 0),  # East Asian ideograph
    0x21432B: (0x6628, 0),  # East Asian ideograph
    0x21432C: (0x664F, 0),  # East Asian ideograph
    0x21432D: (0x6642, 0),  # East Asian ideograph
    0x21432E: (0x6652, 0),  # East Asian ideograph
    0x21432F: (0x6649, 0),  # East Asian ideograph
    0x214330: (0x6643, 0),  # East Asian ideograph
    0x214331: (0x664C, 0),  # East Asian ideograph
    0x214332: (0x665D, 0),  # East Asian ideograph
    0x214333: (0x6664, 0),  # East Asian ideograph
    0x214334: (0x6668, 0),  # East Asian ideograph
    0x214335: (0x6666, 0),  # East Asian ideograph
    0x214336: (0x665A, 0),  # East Asian ideograph
    0x214337: (0x666F, 0),  # East Asian ideograph
    0x214338: (0x666E, 0),  # East Asian ideograph
    0x214339: (0xFA12, 0),  # East Asian ideograph
    0x21433A: (0x6691, 0),  # East Asian ideograph
    0x21433B: (0x6670, 0),  # East Asian ideograph
    0x21433C: (0x6676, 0),  # East Asian ideograph
    0x21433D: (0x667A, 0),  # East Asian ideograph
    0x21433E: (0x6697, 0),  # East Asian ideograph
    0x21433F: (0x6687, 0),  # East Asian ideograph
    0x214340: (0x6689, 0),  # East Asian ideograph
    0x214341: (0x6688, 0),  # East Asian ideograph
    0x214342: (0x6696, 0),  # East Asian ideograph
    0x214343: (0x66A2, 0),  # East Asian ideograph
    0x214344: (0x66AB, 0),  # East Asian ideograph
    0x214345: (0x66B4, 0),  # East Asian ideograph
    0x214346: (0x66AE, 0),  # East Asian ideograph
    0x214347: (0x66C1, 0),  # East Asian ideograph
    0x214348: (0x66C9, 0),  # East Asian ideograph
    0x214349: (0x66C6, 0),  # East Asian ideograph
    0x21434A: (0x66B9, 0),  # East Asian ideograph
    0x21434B: (0x66D6, 0),  # East Asian ideograph
    0x21434C: (0x66D9, 0),  # East Asian ideograph
    0x21434D: (0x66E0, 0),  # East Asian ideograph
    0x21434E: (0x66DD, 0),  # East Asian ideograph
    0x21434F: (0x66E6, 0),  # East Asian ideograph
    0x214350: (0x66F0, 0),  # East Asian ideograph
    0x214351: (0x66F2, 0),  # East Asian ideograph
    0x214352: (0x66F3, 0),  # East Asian ideograph
    0x214353: (0x66F4, 0),  # East Asian ideograph
    0x214354: (0x66F7, 0),  # East Asian ideograph
    0x214355: (0x66F8, 0),  # East Asian ideograph
    0x214356: (0x66F9, 0),  # East Asian ideograph
    0x214357: (0x52D7, 0),  # East Asian ideograph
    0x214358: (0x66FE, 0),  # East Asian ideograph
    0x214359: (0x66FF, 0),  # East Asian ideograph
    0x21435A: (0x6703, 0),  # East Asian ideograph
    0x21435B: (0x6708, 0),  # East Asian ideograph
    0x21435C: (0x6709, 0),  # East Asian ideograph
    0x21435D: (0x670D, 0),  # East Asian ideograph
    0x21435E: (0x670B, 0),  # East Asian ideograph
    0x21435F: (0x6717, 0),  # East Asian ideograph
    0x214360: (0x6715, 0),  # East Asian ideograph
    0x214361: (0x6714, 0),  # East Asian ideograph
    0x214362: (0x671B, 0),  # East Asian ideograph
    0x214363: (0x671D, 0),  # East Asian ideograph
    0x214364: (0x671F, 0),  # East Asian ideograph
    0x6F537E: (0xC2B5, 0),  # Korean hangul
    0x234366: (0x92C8, 0),  # East Asian ideograph
    0x214367: (0x6728, 0),  # East Asian ideograph
    0x214369: (0x672C, 0),  # East Asian ideograph
    0x23436A: (0x92C3, 0),  # East Asian ideograph
    0x21436B: (0x672A, 0),  # East Asian ideograph
    0x29436C: (0x950D, 0),  # East Asian ideograph
    0x21436D: (0x673D, 0),  # East Asian ideograph
    0x22436E: (0x6B17, 0),  # East Asian ideograph
    0x21436F: (0x6731, 0),  # East Asian ideograph
    0x214370: (0x6735, 0),  # East Asian ideograph
    0x214371: (0x675E, 0),  # East Asian ideograph
    0x214372: (0x6751, 0),  # East Asian ideograph
    0x214373: (0x674E, 0),  # East Asian ideograph
    0x214374: (0x675C, 0),  # East Asian ideograph
    0x234375: (0x92E6, 0),  # East Asian ideograph
    0x214376: (0x6756, 0),  # East Asian ideograph
    0x214377: (0x675F, 0),  # East Asian ideograph
    0x214378: (0x674F, 0),  # East Asian ideograph
    0x214379: (0x6749, 0),  # East Asian ideograph
    0x23437A: (0x92D9, 0),  # East Asian ideograph
    0x21437B: (0x676D, 0),  # East Asian ideograph
    0x21437C: (0x678B, 0),  # East Asian ideograph
    0x21437D: (0x6795, 0),  # East Asian ideograph
    0x21437E: (0x6789, 0),  # East Asian ideograph
    0x21777B: (0x58A9, 0),  # East Asian ideograph
    0x4B3F40: (0x618E, 0),  # East Asian ideograph (variant of 213F40)
    0x214B40: (0x73ED, 0),  # East Asian ideograph
    0x27626A: (0x70B9, 0),  # East Asian ideograph
    0x214B41: (0x73EE, 0),  # East Asian ideograph
    0x214B42: (0x73E0, 0),  # East Asian ideograph
    0x214B43: (0x7405, 0),  # East Asian ideograph
    0x6F4B44: (0xB07C, 0),  # Korean hangul
    0x23457E: (0x938B, 0),  # East Asian ideograph
    0x214B45: (0x7403, 0),  # East Asian ideograph
    0x336062: (0x98C3, 0),  # East Asian ideograph
    0x214B46: (0x740A, 0),  # East Asian ideograph
    0x517954: (0x734E, 0),  # East Asian ideograph
    0x274B47: (0x73B0, 0),  # East Asian ideograph
    0x6F577B: (0xC960, 0),  # Korean hangul
    0x214B48: (0x7406, 0),  # East Asian ideograph
    0x214B49: (0x740D, 0),  # East Asian ideograph
    0x282577: (0x5CE4, 0),  # East Asian ideograph
    0x214B4A: (0x743A, 0),  # East Asian ideograph
    0x6F5338: (0xC14D, 0),  # Korean hangul
    0x6F4B4B: (0xB090, 0),  # Korean hangul
    0x213966: (0x59D4, 0),  # East Asian ideograph
    0x6F4B4C: (0xB091, 0),  # Korean hangul
    0x2D584D: (0x548F, 0),  # East Asian ideograph
    0x214B4D: (0x7434, 0),  # East Asian ideograph
    0x2E3A33: (0x80AD, 0),  # East Asian ideograph
    0x213864: (
        0x58C7,
        0,
    ),  # East Asian ideograph (variant of 4B3864 which maps to 58C7)
    0x214B4F: (0x7433, 0),  # East Asian ideograph
    0x6F4B50: (0xB099, 0),  # Korean hangul
    0x6F5021: (0xBA38, 0),  # Korean hangul
    0x214B51: (0x7425, 0),  # East Asian ideograph
    0x6F4B52: (0xB09C, 0),  # Korean hangul
    0x213F36: (0x616E, 0),  # East Asian ideograph
    0x234B53: (0x96CA, 0),  # East Asian ideograph
    0x6F4B54: (0xB0A0, 0),  # Korean hangul
    0x6F4B55: (0xB0A1, 0),  # Korean hangul
    0x6F4F40: (0xB8B0, 0),  # Korean hangul
    0x6F5930: (0xCC4C, 0),  # Korean hangul
    0x6F4B56: (0xB0A8, 0),  # Korean hangul
    0x274B57: (0x73F2, 0),  # East Asian ideograph
    0x6F4B58: (0xB0AB, 0),  # Korean hangul
    0x214B59: (0x745E, 0),  # East Asian ideograph
    0x214B5A: (0x745C, 0),  # East Asian ideograph
    0x6F4F41: (0xB8CC, 0),  # Korean hangul
    0x214421: (0x6787, 0),  # East Asian ideograph
    0x214422: (0x6777, 0),  # East Asian ideograph
    0x214423: (0x679D, 0),  # East Asian ideograph
    0x214424: (0x6797, 0),  # East Asian ideograph
    0x214425: (0x676F, 0),  # East Asian ideograph
    0x214426: (0x6771, 0),  # East Asian ideograph
    0x214427: (0x6773, 0),  # East Asian ideograph
    0x214428: (0x679C, 0),  # East Asian ideograph
    0x214429: (0x6775, 0),  # East Asian ideograph
    0x21442A: (0x679A, 0),  # East Asian ideograph
    0x21442B: (0x6790, 0),  # East Asian ideograph
    0x22442C: (0x6B37, 0),  # East Asian ideograph
    0x21442D: (0x677E, 0),  # East Asian ideograph
    0x21442E: (0x67D3, 0),  # East Asian ideograph
    0x21442F: (0x67F1, 0),  # East Asian ideograph
    0x214430: (0x67FF, 0),  # East Asian ideograph
    0x214431: (0x67D4, 0),  # East Asian ideograph
    0x214432: (0x67C4, 0),  # East Asian ideograph
    0x214433: (0x67AF, 0),  # East Asian ideograph
    0x214434: (0x67D0, 0),  # East Asian ideograph
    0x214435: (0x67D1, 0),  # East Asian ideograph
    0x214436: (0x67EF, 0),  # East Asian ideograph
    0x214437: (0x67E9, 0),  # East Asian ideograph
    0x214438: (0x67B6, 0),  # East Asian ideograph
    0x214439: (0x67EC, 0),  # East Asian ideograph
    0x21443A: (0x67E5, 0),  # East Asian ideograph
    0x21443B: (0x67FA, 0),  # East Asian ideograph
    0x21443C: (0x67DA, 0),  # East Asian ideograph
    0x21443D: (0x6805, 0),  # East Asian ideograph
    0x21443E: (0x67DE, 0),  # East Asian ideograph
    0x21443F: (0x67B8, 0),  # East Asian ideograph
    0x214440: (0x67CF, 0),  # East Asian ideograph
    0x214441: (0x67F3, 0),  # East Asian ideograph
    0x214442: (0x6848, 0),  # East Asian ideograph
    0x214443: (0x6821, 0),  # East Asian ideograph
    0x214444: (0x6838, 0),  # East Asian ideograph
    0x214445: (0x6853, 0),  # East Asian ideograph
    0x214446: (0x6846, 0),  # East Asian ideograph
    0x214447: (0x6842, 0),  # East Asian ideograph
    0x214448: (0x6854, 0),  # East Asian ideograph
    0x214449: (0x6817, 0),  # East Asian ideograph
    0x21444A: (0x683D, 0),  # East Asian ideograph
    0x21444B: (0x6851, 0),  # East Asian ideograph
    0x21444C: (0x6829, 0),  # East Asian ideograph
    0x21444D: (0x6850, 0),  # East Asian ideograph
    0x21444E: (0x6839, 0),  # East Asian ideograph
    0x23444F: (0x9344, 0),  # East Asian ideograph
    0x214450: (0x67F4, 0),  # East Asian ideograph
    0x214451: (0x6843, 0),  # East Asian ideograph
    0x214452: (0x6840, 0),  # East Asian ideograph
    0x214453: (0x682A, 0),  # East Asian ideograph
    0x214454: (0x6845, 0),  # East Asian ideograph
    0x214455: (0x683C, 0),  # East Asian ideograph
    0x214456: (
        0x6813,
        0,
    ),  # East Asian ideograph (variant of 4B4456 which maps to 6813)
    0x214457: (0x6881, 0),  # East Asian ideograph
    0x214458: (0x6893, 0),  # East Asian ideograph
    0x214459: (0x68AF, 0),  # East Asian ideograph
    0x21445A: (0x6876, 0),  # East Asian ideograph
    0x21445B: (0x68B0, 0),  # East Asian ideograph
    0x21445C: (0x68A7, 0),  # East Asian ideograph
    0x21445D: (0x6897, 0),  # East Asian ideograph
    0x21445E: (0x68B5, 0),  # East Asian ideograph
    0x21445F: (0x68B3, 0),  # East Asian ideograph
    0x214460: (0x68A2, 0),  # East Asian ideograph
    0x214461: (0x687F, 0),  # East Asian ideograph
    0x214462: (0x68B1, 0),  # East Asian ideograph
    0x214463: (0x689D, 0),  # East Asian ideograph
    0x214464: (0x68AD, 0),  # East Asian ideograph
    0x214465: (0x6886, 0),  # East Asian ideograph
    0x234466: (0x9312, 0),  # East Asian ideograph
    0x214467: (0x68A8, 0),  # East Asian ideograph
    0x214468: (0x689F, 0),  # East Asian ideograph
    0x214469: (0x6894, 0),  # East Asian ideograph
    0x21446A: (0x6883, 0),  # East Asian ideograph
    0x21446B: (0x68D5, 0),  # East Asian ideograph
    0x21446C: (0x68FA, 0),  # East Asian ideograph
    0x21446D: (0x68C4, 0),  # East Asian ideograph
    0x21446E: (0x68F2, 0),  # East Asian ideograph
    0x21446F: (0x68D2, 0),  # East Asian ideograph
    0x214470: (0x68E3, 0),  # East Asian ideograph
    0x214471: (0x68DF, 0),  # East Asian ideograph
    0x214472: (0x68CB, 0),  # East Asian ideograph
    0x214473: (0x68EE, 0),  # East Asian ideograph
    0x214474: (0x690D, 0),  # East Asian ideograph
    0x214475: (0x6905, 0),  # East Asian ideograph
    0x214476: (0x68E7, 0),  # East Asian ideograph
    0x214477: (0x68E0, 0),  # East Asian ideograph
    0x214478: (0x68F5, 0),  # East Asian ideograph
    0x214479: (0x68CD, 0),  # East Asian ideograph
    0x21447A: (0x68D7, 0),  # East Asian ideograph
    0x21447B: (0x68D8, 0),  # East Asian ideograph
    0x27447C: (0x832D, 0),  # East Asian ideograph
    0x21447D: (0x68F9, 0),  # East Asian ideograph
    0x21447E: (0x68DA, 0),  # East Asian ideograph
    0x214B6B: (0x74CF, 0),  # East Asian ideograph
    0x275166: (0x7EE9, 0),  # East Asian ideograph
    0x214B6C: (0x74DC, 0),  # East Asian ideograph
    0x6F2457: (0x3131, 0),  # Korean hangul
    0x6F576C: (0xC8FC, 0),  # Korean hangul
    0x214B6D: (0x74E0, 0),  # East Asian ideograph
    0x6F4B6E: (0xB108, 0),  # Korean hangul
    0x70755D: (0x8E3A, 0),  # East Asian ideograph
    0x6F4B6F: (0xB109, 0),  # Korean hangul
    0x39525B: (0x66DC, 0),  # East Asian ideograph
    0x214B71: (0x74F6, 0),  # East Asian ideograph
    0x4B3F4A: (0x5FDC, 0),  # East Asian ideograph
    0x234E35: (0x97BE, 0),  # East Asian ideograph
    0x29474D: (0x956B, 0),  # East Asian ideograph
    0x6F4B73: (0xB10F, 0),  # Korean hangul
    0x6F4F46: (0xB8F0, 0),  # Korean hangul
    0x214B74: (0x750C, 0),  # East Asian ideograph
    0x224B75: (0x6EA4, 0),  # East Asian ideograph
    0x214B76: (0x7518, 0),  # East Asian ideograph
    0x4B3F4B: (0x601C, 0),  # East Asian ideograph (variant of 273F4B)
    0x234B77: (0x96F4, 0),  # East Asian ideograph
    0x2D3622: (0x8AEE, 0),  # East Asian ideograph
    0x6F4D67: (0xB4EC, 0),  # Korean hangul
    0x214B78: (0x751C, 0),  # East Asian ideograph
    0x275E32: (0x9556, 0),  # East Asian ideograph
    0x214B79: (0x751F, 0),  # East Asian ideograph
    0x6F577D: (0xC96C, 0),  # Korean hangul
    0x335F43: (0x9D08, 0),  # East Asian ideograph
    0x333D2A: (0x5E83, 0),  # East Asian ideograph
    0x2D5856: (0x612C, 0),  # East Asian ideograph
    0x274B7A: (0x4EA7, 0),  # East Asian ideograph
    0x4B5437: (0x820E, 0),  # East Asian ideograph
    0x694B7B: (0x9EBF, 0),  # East Asian ideograph
    0x213032: (0x4E26, 0),  # East Asian ideograph
    0x214B7C: (0x7525, 0),  # East Asian ideograph
    0x6F533A: (0xC154, 0),  # Korean hangul
    0x276276: (0x51AC, 0),  # East Asian ideograph
    0x214B7D: (0x7528, 0),  # East Asian ideograph
    0x6F4F48: (0xB8F9, 0),  # Korean hangul
    0x275E33: (0x9557, 0),  # East Asian ideograph
    0x21352D: (0x53F8, 0),  # East Asian ideograph
    0x217629: (0x57E3, 0),  # East Asian ideograph
    0x23362A: (0x8C86, 0),  # East Asian ideograph
    0x213866: (0x58C1, 0),  # East Asian ideograph
    0x23527B: (0x99E3, 0),  # East Asian ideograph
    0x21762C: (0x57F6, 0),  # East Asian ideograph
    0x6F4F49: (0xB8FB, 0),  # Korean hangul
    0x23362D: (0x8C85, 0),  # East Asian ideograph
    0x29485C: (0x9565, 0),  # East Asian ideograph
    0x21352E: (0x53E4, 0),  # East Asian ideograph
    0x4D5858: (0x9BE3, 0),  # East Asian ideograph
    0x6F5D75: (0xD76C, 0),  # Korean hangul
    0x214521: (0x690E, 0),  # East Asian ideograph
    0x214522: (0x68C9, 0),  # East Asian ideograph
    0x214523: (0x6954, 0),  # East Asian ideograph
    0x214524: (0x6930, 0),  # East Asian ideograph
    0x214525: (0x6977, 0),  # East Asian ideograph
    0x214526: (0x6975, 0),  # East Asian ideograph
    0x214527: (0x695A, 0),  # East Asian ideograph
    0x214528: (0x6960, 0),  # East Asian ideograph
    0x214529: (0x696B, 0),  # East Asian ideograph
    0x21452A: (0x694A, 0),  # East Asian ideograph
    0x21452B: (0x6968, 0),  # East Asian ideograph
    0x21452C: (0x695E, 0),  # East Asian ideograph
    0x21452D: (0x696D, 0),  # East Asian ideograph
    0x21452E: (0x6979, 0),  # East Asian ideograph
    0x21452F: (0x6953, 0),  # East Asian ideograph
    0x214530: (0x6986, 0),  # East Asian ideograph
    0x214531: (0x69A8, 0),  # East Asian ideograph
    0x214532: (0x6995, 0),  # East Asian ideograph
    0x214533: (0x699C, 0),  # East Asian ideograph
    0x214534: (0x6994, 0),  # East Asian ideograph
    0x214535: (0x69C1, 0),  # East Asian ideograph
    0x214536: (0x69B7, 0),  # East Asian ideograph
    0x214537: (0x69AE, 0),  # East Asian ideograph
    0x214538: (0x699B, 0),  # East Asian ideograph
    0x214539: (0x69CB, 0),  # East Asian ideograph
    0x21453A: (0x69D3, 0),  # East Asian ideograph
    0x21453B: (0x69BB, 0),  # East Asian ideograph
    0x21453C: (0x69AB, 0),  # East Asian ideograph
    0x21453D: (0x69CC, 0),  # East Asian ideograph
    0x21453E: (0x69AD, 0),  # East Asian ideograph
    0x21453F: (0x69D0, 0),  # East Asian ideograph
    0x214540: (0x69CD, 0),  # East Asian ideograph
    0x214541: (0x69B4, 0),  # East Asian ideograph
    0x214542: (0x6A1F, 0),  # East Asian ideograph
    0x214543: (0x69E8, 0),  # East Asian ideograph
    0x274544: (0x6837, 0),  # East Asian ideograph
    0x214545: (0x69EA, 0),  # East Asian ideograph
    0x274546: (0x6869, 0),  # East Asian ideograph
    0x214547: (0x6A19, 0),  # East Asian ideograph
    0x214548: (0x69FD, 0),  # East Asian ideograph
    0x214549: (0x6A1E, 0),  # East Asian ideograph
    0x21454A: (0x6A13, 0),  # East Asian ideograph
    0x21454B: (0x6A21, 0),  # East Asian ideograph
    0x21454C: (0x69F3, 0),  # East Asian ideograph
    0x21454D: (0x6A0A, 0),  # East Asian ideograph
    0x21454E: (0x6A02, 0),  # East Asian ideograph
    0x21454F: (0x6A05, 0),  # East Asian ideograph
    0x214550: (0x6A3D, 0),  # East Asian ideograph
    0x214551: (0x6A58, 0),  # East Asian ideograph
    0x214552: (0x6A59, 0),  # East Asian ideograph
    0x214553: (0x6A62, 0),  # East Asian ideograph
    0x214554: (0x6A44, 0),  # East Asian ideograph
    0x214555: (0x6A39, 0),  # East Asian ideograph
    0x214556: (0x6A6B, 0),  # East Asian ideograph
    0x214557: (0x6A3A, 0),  # East Asian ideograph
    0x214558: (0x6A38, 0),  # East Asian ideograph
    0x214559: (0x6A47, 0),  # East Asian ideograph
    0x21455A: (0x6A61, 0),  # East Asian ideograph
    0x21455B: (0x6A4B, 0),  # East Asian ideograph
    0x21455C: (0x6A35, 0),  # East Asian ideograph
    0x21455D: (0x6A5F, 0),  # East Asian ideograph
    0x21455E: (0x6A80, 0),  # East Asian ideograph
    0x21455F: (0x6A94, 0),  # East Asian ideograph
    0x214560: (0x6A84, 0),  # East Asian ideograph
    0x214561: (0x6AA2, 0),  # East Asian ideograph
    0x214562: (0x6A9C, 0),  # East Asian ideograph
    0x214563: (0x6AB8, 0),  # East Asian ideograph
    0x214564: (0x6AB3, 0),  # East Asian ideograph
    0x214565: (0x6AC3, 0),  # East Asian ideograph
    0x214566: (0x6ABB, 0),  # East Asian ideograph
    0x234567: (0x9354, 0),  # East Asian ideograph
    0x214568: (0x6AAC, 0),  # East Asian ideograph
    0x214569: (0x6AE5, 0),  # East Asian ideograph
    0x21456A: (0x6ADA, 0),  # East Asian ideograph
    0x21456B: (0x6ADD, 0),  # East Asian ideograph
    0x21456C: (0x6ADB, 0),  # East Asian ideograph
    0x21456D: (0x6AD3, 0),  # East Asian ideograph
    0x21456E: (0x6B04, 0),  # East Asian ideograph
    0x21456F: (0x6AFB, 0),  # East Asian ideograph
    0x214570: (0x6B0A, 0),  # East Asian ideograph
    0x214571: (0x6B16, 0),  # East Asian ideograph
    0x234572: (0x936D, 0),  # East Asian ideograph
    0x214573: (0x6B21, 0),  # East Asian ideograph
    0x214574: (0x6B23, 0),  # East Asian ideograph
    0x27363E: (0x5458, 0),  # East Asian ideograph
    0x214576: (0x6B3E, 0),  # East Asian ideograph
    0x214577: (0x6B3A, 0),  # East Asian ideograph
    0x214578: (0x6B3D, 0),  # East Asian ideograph
    0x214579: (0x6B47, 0),  # East Asian ideograph
    0x21457A: (0x6B49, 0),  # East Asian ideograph
    0x21457B: (0x6B4C, 0),  # East Asian ideograph
    0x21457C: (0x6B50, 0),  # East Asian ideograph
    0x21457D: (0x6B59, 0),  # East Asian ideograph
    0x21457E: (0x6B5F, 0),  # East Asian ideograph
    0x6F7640: (0xE8B2, 0),  # Korean hangul
    0x2D3B27: (0x51A8, 0),  # East Asian ideograph
    0x453421: (0x5271, 0),  # East Asian ideograph
    0x213641: (0x5506, 0),  # East Asian ideograph
    0x4C4D3D: (0x6F62, 0),  # East Asian ideograph
    0x2D3642: (0x6B38, 0),  # East Asian ideograph
    0x335F49: (0x9D70, 0),  # East Asian ideograph
    0x4D5B7E: (0x9DC6, 0),  # East Asian ideograph
    0x27516F: (0x7F2B, 0),  # East Asian ideograph
    0x213867: (0x58BE, 0),  # East Asian ideograph
    0x213644: (0x5556, 0),  # East Asian ideograph
    0x213645: (0x5533, 0),  # East Asian ideograph
    0x6F4F4E: (0xB959, 0),  # Korean hangul
    0x275E39: (0x94D9, 0),  # East Asian ideograph
    0x6F5449: (0xC372, 0),  # Korean hangul
    0x234174: (0x91F4, 0),  # East Asian ideograph
    0x213647: (0x5537, 0),  # East Asian ideograph (Version J extension)
    0x2D3644: (0x5557, 0),  # East Asian ideograph
    0x275170: (0x7F2E, 0),  # East Asian ideograph
    0x6F553F: (0xC591, 0),  # Korean hangul
    0x213649: (0x555E, 0),  # East Asian ideograph
    0x276245: (0x9E4F, 0),  # East Asian ideograph
    0x275E3A: (0x9570, 0),  # East Asian ideograph
    0x6F764C: (0xE8BE, 0),  # Korean hangul
    0x21764D: (0x57FD, 0),  # East Asian ideograph
    0x21764E: (0x57F8, 0),  # East Asian ideograph
    0x21364F: (0x5531, 0),  # East Asian ideograph
    0x2D5749: (0x885E, 0),  # East Asian ideograph
    0x275E3B: (0x9508, 0),  # East Asian ideograph
    0x21574E: (0x521D, 0),  # East Asian ideograph
    0x6F5859: (0xCAC0, 0),  # Korean hangul
    0x233651: (0x8CBA, 0),  # East Asian ideograph
    0x233652: (0x8CB5, 0),  # East Asian ideograph
    0x213653: (0x553E, 0),  # East Asian ideograph
    0x213654: (0x5563, 0),  # East Asian ideograph
    0x6F4F51: (0xB968, 0),  # Korean hangul
    0x275E3C: (0x956D, 0),  # East Asian ideograph
    0x234177: (0x91F1, 0),  # East Asian ideograph
    0x6F7656: (0xE8C8, 0),  # Korean hangul
    0x213657: (0x552E, 0),  # East Asian ideograph
    0x6F4A3A: (0xAE38, 0),  # Korean hangul
    0x34682A: (0x7C7C, 0),  # East Asian ideograph
    0x275E3D: (0x94C1, 0),  # East Asian ideograph
    0x214621: (0x6B61, 0),  # East Asian ideograph
    0x234622: (0x938C, 0),  # East Asian ideograph
    0x214623: (0x6B63, 0),  # East Asian ideograph
    0x214624: (0x6B64, 0),  # East Asian ideograph
    0x214625: (0x6B65, 0),  # East Asian ideograph
    0x214627: (0x6B66, 0),  # East Asian ideograph
    0x214628: (0x6B6A, 0),  # East Asian ideograph
    0x214629: (0x6B72, 0),  # East Asian ideograph
    0x22462A: (0x6BF6, 0),  # East Asian ideograph
    0x21462B: (0x6B78, 0),  # East Asian ideograph
    0x21462C: (0x6B79, 0),  # East Asian ideograph
    0x21462D: (0x6B7B, 0),  # East Asian ideograph
    0x21462E: (0x6B7F, 0),  # East Asian ideograph
    0x21462F: (0x6B83, 0),  # East Asian ideograph
    0x214630: (0x6B86, 0),  # East Asian ideograph
    0x214631: (0x6B8A, 0),  # East Asian ideograph
    0x214632: (0x6B89, 0),  # East Asian ideograph
    0x214633: (0x6B98, 0),  # East Asian ideograph
    0x214634: (0x6B96, 0),  # East Asian ideograph
    0x214635: (0x6BA4, 0),  # East Asian ideograph
    0x214636: (0x6BAE, 0),  # East Asian ideograph
    0x214637: (0x6BAF, 0),  # East Asian ideograph
    0x214638: (0x6BB2, 0),  # East Asian ideograph
    0x214639: (0x6BB5, 0),  # East Asian ideograph
    0x21463A: (0x6BB7, 0),  # East Asian ideograph
    0x21463B: (0x6BBA, 0),  # East Asian ideograph
    0x21463C: (0x6BBC, 0),  # East Asian ideograph
    0x21463D: (0x6BC0, 0),  # East Asian ideograph
    0x21463E: (0x6BBF, 0),  # East Asian ideograph
    0x21463F: (0x6BC5, 0),  # East Asian ideograph
    0x214640: (0x6BC6, 0),  # East Asian ideograph
    0x214641: (0x6BCB, 0),  # East Asian ideograph
    0x214642: (0x6BCD, 0),  # East Asian ideograph
    0x214643: (0x6BCF, 0),  # East Asian ideograph
    0x214644: (0x6BD2, 0),  # East Asian ideograph
    0x214646: (0x6BD4, 0),  # East Asian ideograph
    0x214647: (0x6BD7, 0),  # East Asian ideograph
    0x214648: (0x6BDB, 0),  # East Asian ideograph
    0x214649: (0x6BEB, 0),  # East Asian ideograph
    0x21464A: (0x6BEF, 0),  # East Asian ideograph
    0x21464B: (0x6BFD, 0),  # East Asian ideograph
    0x21464C: (0x6C0F, 0),  # East Asian ideograph
    0x21464D: (0x6C11, 0),  # East Asian ideograph
    0x21464E: (0x6C10, 0),  # East Asian ideograph
    0x21464F: (0x6C13, 0),  # East Asian ideograph
    0x214650: (0x6C16, 0),  # East Asian ideograph
    0x214651: (0x6C1B, 0),  # East Asian ideograph
    0x214652: (0x6C1F, 0),  # East Asian ideograph
    0x214653: (0x6C27, 0),  # East Asian ideograph
    0x214654: (0x6C26, 0),  # East Asian ideograph
    0x214655: (0x6C23, 0),  # East Asian ideograph
    0x214656: (0x6C28, 0),  # East Asian ideograph
    0x214657: (0x6C24, 0),  # East Asian ideograph
    0x214658: (0x6C2B, 0),  # East Asian ideograph
    0x214659: (0x6C2E, 0),  # East Asian ideograph
    0x21465A: (0x6C33, 0),  # East Asian ideograph
    0x21465B: (
        0x6C2F,
        0,
    ),  # East Asian ideograph (variant of 45465B which maps to 6C2F)
    0x21465C: (0x6C34, 0),  # East Asian ideograph
    0x21465D: (0x6C38, 0),  # East Asian ideograph
    0x21465E: (0x6C41, 0),  # East Asian ideograph
    0x23465F: (0x93E5, 0),  # East Asian ideograph
    0x214660: (0x6C40, 0),  # East Asian ideograph
    0x214661: (0x6C42, 0),  # East Asian ideograph
    0x214662: (0x6C5E, 0),  # East Asian ideograph
    0x214663: (0x6C57, 0),  # East Asian ideograph
    0x214664: (0x6C5F, 0),  # East Asian ideograph
    0x214665: (0x6C59, 0),  # East Asian ideograph
    0x214666: (0x6C60, 0),  # East Asian ideograph
    0x214667: (0x6C55, 0),  # East Asian ideograph
    0x214668: (0x6C50, 0),  # East Asian ideograph
    0x214669: (0x6C5D, 0),  # East Asian ideograph
    0x21466A: (0x6C9B, 0),  # East Asian ideograph
    0x21466B: (0x6C81, 0),  # East Asian ideograph
    0x21466D: (0x6C7A, 0),  # East Asian ideograph
    0x21466E: (0x6C6A, 0),  # East Asian ideograph
    0x21466F: (0x6C8C, 0),  # East Asian ideograph
    0x214670: (0x6C90, 0),  # East Asian ideograph
    0x214671: (0x6C72, 0),  # East Asian ideograph
    0x214672: (0x6C70, 0),  # East Asian ideograph
    0x214673: (0x6C68, 0),  # East Asian ideograph
    0x214674: (0x6C96, 0),  # East Asian ideograph
    0x234675: (0x93DB, 0),  # East Asian ideograph
    0x214676: (
        0x6C89,
        0,
    ),  # East Asian ideograph (variant of 4B4676 which maps to 6C89)
    0x214677: (0x6C99, 0),  # East Asian ideograph
    0x214678: (0x6C7E, 0),  # East Asian ideograph
    0x214679: (0x6C7D, 0),  # East Asian ideograph
    0x21467A: (0x6C92, 0),  # East Asian ideograph
    0x21467B: (0x6C83, 0),  # East Asian ideograph
    0x21467C: (0x6CB1, 0),  # East Asian ideograph
    0x23366A: (0x8CE1, 0),  # East Asian ideograph
    0x21467E: (0x6CF3, 0),  # East Asian ideograph
    0x21366B: (0x559D, 0),  # East Asian ideograph
    0x2D5421: (0x9AD7, 0),  # East Asian ideograph
    0x6F4A56: (0xAE7D, 0),  # Korean hangul
    0x4C4359: (0x6B05, 0),  # East Asian ideograph
    0x27366D: (0x5524, 0),  # East Asian ideograph
    0x21366E: (0x557E, 0),  # East Asian ideograph
    0x294869: (0x9567, 0),  # East Asian ideograph
    0x284027: (0x6864, 0),  # East Asian ideograph
    0x21366F: (0x55AC, 0),  # East Asian ideograph
    0x213670: (0x5589, 0),  # East Asian ideograph
    0x223671: (0x6595, 0),  # East Asian ideograph
    0x213672: (0x55BB, 0),  # East Asian ideograph
    0x27406C: (0x631F, 0),  # East Asian ideograph
    0x4C3B60: (0x6764, 0),  # East Asian ideograph
    0x294228: (0x94AC, 0),  # East Asian ideograph
    0x213674: (0x55DF, 0),  # East Asian ideograph
    0x213675: (0x55D1, 0),  # East Asian ideograph
    0x213869: (0x58D3, 0),  # East Asian ideograph
    0x28734E: (0x7F32, 0),  # East Asian ideograph
    0x233676: (0x8CEE, 0),  # East Asian ideograph
    0x216121: (0x993F, 0),  # East Asian ideograph
    0x213677: (0x55E6, 0),  # East Asian ideograph
    0x4B6122: (0x994B, 0),  # East Asian ideograph
    0x6F4F58: (0xB985, 0),  # Korean hangul
    0x273678: (0x556C, 0),  # East Asian ideograph
    0x275E43: (0x94F8, 0),  # East Asian ideograph
    0x216123: (0x9945, 0),  # East Asian ideograph
    0x6F5263: (0xC0B0, 0),  # Korean hangul
    0x21353D: (0x53F2, 0),  # East Asian ideograph
    0x276124: (0x9976, 0),  # East Asian ideograph
    0x27367A: (0x5417, 0),  # East Asian ideograph
    0x2D5424: (0x5367, 0),  # East Asian ideograph
    0x23367B: (0x8CF1, 0),  # East Asian ideograph
    0x216126: (0x995C, 0),  # East Asian ideograph
    0x6F5851: (0xCA54, 0),  # Korean hangul
    0x21367C: (0x55EF, 0),  # East Asian ideograph
    0x2D475B: (0x51C9, 0),  # East Asian ideograph
    0x276127: (0x998B, 0),  # East Asian ideograph
    0x6F4F59: (0xB987, 0),  # Korean hangul
    0x21767D: (0x5844, 0),  # East Asian ideograph
    0x275E44: (0x9573, 0),  # East Asian ideograph
    0x21367E: (0x55C5, 0),  # East Asian ideograph
    0x396C6B: (0x60A4, 0),  # East Asian ideograph
    0x6F5B37: (0xD168, 0),  # Korean hangul
    0x213E61: (0x60E1, 0),  # East Asian ideograph
    0x224A4A: (0x6DE6, 0),  # East Asian ideograph
    0x4B5D34: (0x91B8, 0),  # East Asian ideograph
    0x27612C: (0x9A6C, 0),  # East Asian ideograph
    0x217971: (0x59A0, 0),  # East Asian ideograph
    0x21353F: (0x540B, 0),  # East Asian ideograph
    0x27612E: (0x9A6D, 0),  # East Asian ideograph
    0x2D6260: (0x5E85, 0),  # East Asian ideograph
    0x27612F: (0x9A70, 0),  # East Asian ideograph
    0x287351: (0x7F33, 0),  # East Asian ideograph
    0x214721: (0x6CE3, 0),  # East Asian ideograph
    0x214722: (0x6CF0, 0),  # East Asian ideograph
    0x214723: (0x6CB8, 0),  # East Asian ideograph
    0x214724: (0x6CD3, 0),  # East Asian ideograph
    0x214725: (0x6CAB, 0),  # East Asian ideograph
    0x214726: (0x6CE5, 0),  # East Asian ideograph
    0x214727: (0x6CBD, 0),  # East Asian ideograph
    0x214728: (0x6CB3, 0),  # East Asian ideograph
    0x214729: (0x6CC4, 0),  # East Asian ideograph
    0x21472A: (0x6CD5, 0),  # East Asian ideograph
    0x21472B: (0x6CE2, 0),  # East Asian ideograph
    0x21472C: (0x6CBC, 0),  # East Asian ideograph
    0x21472D: (0x6CAE, 0),  # East Asian ideograph
    0x21472E: (0x6CB9, 0),  # East Asian ideograph
    0x21472F: (0x6CF1, 0),  # East Asian ideograph
    0x214730: (0x6CC1, 0),  # East Asian ideograph
    0x214731: (0x6CBE, 0),  # East Asian ideograph
    0x214732: (0x6CC5, 0),  # East Asian ideograph
    0x214733: (0x6CD7, 0),  # East Asian ideograph
    0x234734: (0x9413, 0),  # East Asian ideograph
    0x214735: (0x6CDB, 0),  # East Asian ideograph
    0x214736: (0x6CE1, 0),  # East Asian ideograph
    0x214737: (0x6CBF, 0),  # East Asian ideograph
    0x214738: (0x6CCA, 0),  # East Asian ideograph
    0x214739: (0x6CCC, 0),  # East Asian ideograph
    0x21473A: (0x6CC9, 0),  # East Asian ideograph
    0x21473B: (0x6D41, 0),  # East Asian ideograph
    0x21473C: (0x6D0B, 0),  # East Asian ideograph
    0x21473D: (0x6D32, 0),  # East Asian ideograph
    0x21473E: (0x6D25, 0),  # East Asian ideograph
    0x21473F: (0x6D31, 0),  # East Asian ideograph
    0x214740: (0x6D2A, 0),  # East Asian ideograph
    0x214741: (0x6D0C, 0),  # East Asian ideograph
    0x214742: (0x6D1E, 0),  # East Asian ideograph
    0x214743: (0x6D17, 0),  # East Asian ideograph
    0x214744: (0x6D3B, 0),  # East Asian ideograph
    0x214745: (0x6D1B, 0),  # East Asian ideograph
    0x214746: (0x6D36, 0),  # East Asian ideograph
    0x214747: (0x6D3D, 0),  # East Asian ideograph
    0x214748: (0x6D3E, 0),  # East Asian ideograph
    0x214749: (0x6D6A, 0),  # East Asian ideograph
    0x21474A: (0x6D95, 0),  # East Asian ideograph
    0x21474B: (0x6D78, 0),  # East Asian ideograph
    0x21474C: (0x6D66, 0),  # East Asian ideograph
    0x21474D: (0x6D59, 0),  # East Asian ideograph
    0x21474E: (0x6D87, 0),  # East Asian ideograph
    0x21474F: (0x6D88, 0),  # East Asian ideograph
    0x214750: (0x6D6C, 0),  # East Asian ideograph
    0x214751: (0x6D93, 0),  # East Asian ideograph
    0x214752: (0x6D89, 0),  # East Asian ideograph
    0x214753: (0x6D6E, 0),  # East Asian ideograph
    0x214754: (0x6D74, 0),  # East Asian ideograph
    0x214755: (0x6D5A, 0),  # East Asian ideograph
    0x214756: (0x6D69, 0),  # East Asian ideograph
    0x214757: (0x6D77, 0),  # East Asian ideograph
    0x214758: (0x6DD9, 0),  # East Asian ideograph
    0x214759: (0x6DDA, 0),  # East Asian ideograph
    0x21475A: (0x6DF3, 0),  # East Asian ideograph
    0x21475B: (0x6DBC, 0),  # East Asian ideograph
    0x21475C: (0x6DE4, 0),  # East Asian ideograph
    0x21475D: (0x6DB2, 0),  # East Asian ideograph
    0x21475E: (0x6DE1, 0),  # East Asian ideograph
    0x21475F: (0x6DD2, 0),  # East Asian ideograph
    0x214760: (0x6DAE, 0),  # East Asian ideograph
    0x214761: (0x6DF8, 0),  # East Asian ideograph
    0x214762: (0x6DC7, 0),  # East Asian ideograph
    0x214763: (0x6DCB, 0),  # East Asian ideograph
    0x214764: (0x6DC5, 0),  # East Asian ideograph
    0x214765: (0x6DDE, 0),  # East Asian ideograph
    0x214766: (0x6DAF, 0),  # East Asian ideograph
    0x214767: (0x6DB5, 0),  # East Asian ideograph
    0x214768: (0x6DFA, 0),  # East Asian ideograph
    0x214769: (0x6DF9, 0),  # East Asian ideograph
    0x21476A: (0x6DCC, 0),  # East Asian ideograph
    0x21476B: (0x6DF7, 0),  # East Asian ideograph
    0x21476C: (0x6DB8, 0),  # East Asian ideograph
    0x21476D: (0x6DD1, 0),  # East Asian ideograph
    0x21476E: (0x6DF1, 0),  # East Asian ideograph
    0x21476F: (0x6DE8, 0),  # East Asian ideograph
    0x214770: (0x6DEB, 0),  # East Asian ideograph
    0x214771: (0x6DD8, 0),  # East Asian ideograph
    0x214772: (0x6DFB, 0),  # East Asian ideograph
    0x214773: (0x6DEE, 0),  # East Asian ideograph
    0x214774: (0x6DF5, 0),  # East Asian ideograph
    0x214775: (0x6D8E, 0),  # East Asian ideograph
    0x214776: (0x6DC6, 0),  # East Asian ideograph
    0x214777: (0x6DEA, 0),  # East Asian ideograph
    0x214778: (0x6DC4, 0),  # East Asian ideograph
    0x214779: (0x6E54, 0),  # East Asian ideograph
    0x21477A: (0x6E21, 0),  # East Asian ideograph
    0x21477B: (0x6E38, 0),  # East Asian ideograph
    0x21477C: (0x6E32, 0),  # East Asian ideograph
    0x21477D: (0x6E67, 0),  # East Asian ideograph
    0x21477E: (0x6E20, 0),  # East Asian ideograph
    0x4B5D38: (0x91C8, 0),  # East Asian ideograph
    0x226140: (0x76EC, 0),  # East Asian ideograph
    0x6F4F5E: (0xB9B0, 0),  # Korean hangul
    0x6F5936: (0xCC64, 0),  # Korean hangul
    0x276141: (0x9A97, 0),  # East Asian ideograph
    0x6F5777: (0xC950, 0),  # Korean hangul
    0x29442E: (0x9502, 0),  # East Asian ideograph
    0x276142: (0x9A9B, 0),  # East Asian ideograph
    0x276143: (0x9A9E, 0),  # East Asian ideograph
    0x274D3D: (0x76D1, 0),  # East Asian ideograph
    0x6F5C28: (0xD38D, 0),  # Korean hangul
    0x216144: (0x9A30, 0),  # East Asian ideograph
    0x4B624F: (0x9D49, 0),  # East Asian ideograph
    0x276145: (0x9A9A, 0),  # East Asian ideograph
    0x6F4F5F: (0xB9B4, 0),  # Korean hangul
    0x275E4A: (0x94BB, 0),  # East Asian ideograph
    0x273C31: (0x5CE6, 0),  # East Asian ideograph
    0x21575D: (0x88C2, 0),  # East Asian ideograph
    0x6F585C: (0xCACD, 0),  # Korean hangul
    0x217533: (0x5788, 0),  # East Asian ideograph
    0x276147: (0x9A71, 0),  # East Asian ideograph
    0x213860: (0x58B3, 0),  # East Asian ideograph
    0x216148: (0x9A40, 0),  # East Asian ideograph
    0x6F772D: (0xAE5F, 0),  # Korean hangul
    0x287236: (0x7F07, 0),  # East Asian ideograph
    0x6F5C29: (0xD38F, 0),  # Korean hangul
    0x276149: (0x9AA1, 0),  # East Asian ideograph
    0x27614A: (0x9A84, 0),  # East Asian ideograph
    0x6F4C6D: (0xB2E4, 0),  # Korean hangul
    0x6F4F60: (0xB9BC, 0),  # Korean hangul
    0x22614B: (0x7704, 0),  # East Asian ideograph
    0x225B5D: (0x74A1, 0),  # East Asian ideograph
    0x27614C: (0x9A7F, 0),  # East Asian ideograph
    0x27614D: (0x9A8C, 0),  # East Asian ideograph
    0x27614E: (0x9AA4, 0),  # East Asian ideograph
    0x21614F: (0x9A62, 0),  # East Asian ideograph
    0x6F4F61: (0xB9BD, 0),  # Korean hangul
    0x275E4C: (0x957F, 0),  # East Asian ideograph
    0x216150: (0x9A65, 0),  # East Asian ideograph
    0x21575F: (0x88DF, 0),  # East Asian ideograph
    0x216151: (0x9A6A, 0),  # East Asian ideograph
    0x226153: (0x76F7, 0),  # East Asian ideograph
    0x293325: (0x8BF9, 0),  # East Asian ideograph
    0x216154: (0x9AB0, 0),  # East Asian ideograph
    0x6F4F62: (0xB9BF, 0),  # Korean hangul
    0x235F5E: (0x9F39, 0),  # East Asian ideograph
    0x213F3D: (0x61A7, 0),  # East Asian ideograph
    0x216157: (0x9ABC, 0),  # East Asian ideograph
    0x287359: (0x7F31, 0),  # East Asian ideograph
    0x276158: (0x9AC5, 0),  # East Asian ideograph
    0x216159: (0x9AD3, 0),  # East Asian ideograph
    0x6F4F63: (0xB9C1, 0),  # Korean hangul
    0x275E4E: (0x95E9, 0),  # East Asian ideograph
    0x27615A: (0x4F53, 0),  # East Asian ideograph
    0x277C24: (0x5A32, 0),  # East Asian ideograph
    0x456036: (0x97FF, 0),  # East Asian ideograph
    0x214821: (0x6E5B, 0),  # East Asian ideograph
    0x214822: (0x6E1A, 0),  # East Asian ideograph
    0x214823: (0x6E56, 0),  # East Asian ideograph
    0x214824: (0x6E2F, 0),  # East Asian ideograph
    0x214825: (0x6E6E, 0),  # East Asian ideograph
    0x214826: (0x6E58, 0),  # East Asian ideograph
    0x214827: (0x6E23, 0),  # East Asian ideograph
    0x214828: (0x6E24, 0),  # East Asian ideograph
    0x214829: (0x6E1B, 0),  # East Asian ideograph
    0x21482A: (0x6E25, 0),  # East Asian ideograph
    0x21482B: (0x6E4A, 0),  # East Asian ideograph
    0x21482C: (0x6E3A, 0),  # East Asian ideograph
    0x21482D: (0x6E6F, 0),  # East Asian ideograph
    0x21482E: (0x6E2D, 0),  # East Asian ideograph
    0x22482F: (0x6CE0, 0),  # East Asian ideograph
    0x214830: (0x6E2C, 0),  # East Asian ideograph
    0x214831: (0x6E26, 0),  # East Asian ideograph
    0x214832: (0x6E4D, 0),  # East Asian ideograph
    0x214833: (0x6E3E, 0),  # East Asian ideograph
    0x214834: (0x6E43, 0),  # East Asian ideograph
    0x214835: (0x6E19, 0),  # East Asian ideograph
    0x214836: (0x6E1D, 0),  # East Asian ideograph
    0x214837: (0x6ED3, 0),  # East Asian ideograph
    0x214838: (0x6EB6, 0),  # East Asian ideograph
    0x214839: (0x6EC2, 0),  # East Asian ideograph
    0x21483B: (0x6EAF, 0),  # East Asian ideograph
    0x21483C: (0x6EA2, 0),  # East Asian ideograph
    0x27483D: (0x6C9F, 0),  # East Asian ideograph
    0x23483E: (0x944C, 0),  # East Asian ideograph
    0x21483F: (0x6EA5, 0),  # East Asian ideograph
    0x214840: (0x6E98, 0),  # East Asian ideograph
    0x214841: (0x6E90, 0),  # East Asian ideograph
    0x214842: (0x6EC5, 0),  # East Asian ideograph
    0x214843: (0x6EC7, 0),  # East Asian ideograph
    0x214844: (0x6EBC, 0),  # East Asian ideograph
    0x214845: (0x6EAB, 0),  # East Asian ideograph
    0x214846: (0x6ED1, 0),  # East Asian ideograph
    0x214847: (0x6ECB, 0),  # East Asian ideograph
    0x214848: (0x6EC4, 0),  # East Asian ideograph
    0x214849: (0x6ED4, 0),  # East Asian ideograph
    0x21484A: (0x6EAA, 0),  # East Asian ideograph
    0x21484B: (0x6E96, 0),  # East Asian ideograph
    0x21484C: (0x6E9C, 0),  # East Asian ideograph
    0x21484D: (0x6F33, 0),  # East Asian ideograph
    0x21484E: (0x6EF4, 0),  # East Asian ideograph
    0x21484F: (0x6EEC, 0),  # East Asian ideograph
    0x214850: (0x6EFE, 0),  # East Asian ideograph
    0x214851: (0x6F29, 0),  # East Asian ideograph
    0x214852: (0x6F14, 0),  # East Asian ideograph
    0x214853: (0x6F3E, 0),  # East Asian ideograph
    0x214854: (0x6F2C, 0),  # East Asian ideograph
    0x214855: (0x6F32, 0),  # East Asian ideograph
    0x214856: (0x6F0F, 0),  # East Asian ideograph
    0x214857: (
        0x6F22,
        0,
    ),  # East Asian ideograph (variant of 4B4857 which maps to 6F22)
    0x214858: (0x6EFF, 0),  # East Asian ideograph
    0x214859: (0x6F23, 0),  # East Asian ideograph
    0x21485A: (0x6F38, 0),  # East Asian ideograph
    0x21485B: (0x6F15, 0),  # East Asian ideograph
    0x21485C: (0x6F31, 0),  # East Asian ideograph
    0x21485D: (0x6F02, 0),  # East Asian ideograph
    0x21485E: (0x6F06, 0),  # East Asian ideograph
    0x21485F: (0x6EEF, 0),  # East Asian ideograph
    0x214860: (0x6F2B, 0),  # East Asian ideograph
    0x214861: (0x6F2F, 0),  # East Asian ideograph
    0x214862: (0x6F20, 0),  # East Asian ideograph
    0x214863: (0x6F3F, 0),  # East Asian ideograph
    0x214864: (0x6EF2, 0),  # East Asian ideograph
    0x214865: (0x6F01, 0),  # East Asian ideograph
    0x214866: (0x6F11, 0),  # East Asian ideograph
    0x214867: (0x6ECC, 0),  # East Asian ideograph
    0x214868: (0x6F2A, 0),  # East Asian ideograph
    0x214869: (0x6F7C, 0),  # East Asian ideograph
    0x21486A: (0x6F88, 0),  # East Asian ideograph
    0x21486B: (0x6F84, 0),  # East Asian ideograph
    0x21486C: (0x6F51, 0),  # East Asian ideograph
    0x21486D: (0x6F64, 0),  # East Asian ideograph
    0x21486E: (0x6F97, 0),  # East Asian ideograph
    0x21486F: (0x6F54, 0),  # East Asian ideograph
    0x214870: (0x6F7A, 0),  # East Asian ideograph
    0x214871: (0x6F86, 0),  # East Asian ideograph
    0x214872: (0x6F8E, 0),  # East Asian ideograph
    0x214873: (0x6F6D, 0),  # East Asian ideograph
    0x214874: (0x6F5B, 0),  # East Asian ideograph
    0x214875: (0x6F6E, 0),  # East Asian ideograph
    0x214876: (0x6F78, 0),  # East Asian ideograph
    0x214877: (0x6F66, 0),  # East Asian ideograph
    0x214878: (0x6F70, 0),  # East Asian ideograph
    0x214879: (0x6F58, 0),  # East Asian ideograph
    0x21487A: (0x6FC2, 0),  # East Asian ideograph
    0x21487B: (0x6FB1, 0),  # East Asian ideograph
    0x21487C: (0x6FC3, 0),  # East Asian ideograph
    0x21487D: (0x6FA7, 0),  # East Asian ideograph
    0x21487E: (0x6FA1, 0),  # East Asian ideograph
    0x4D5875: (0x9CD0, 0),  # East Asian ideograph
    0x2D5D65: (0x8216, 0),  # East Asian ideograph
    0x28735D: (0x7EA9, 0),  # East Asian ideograph
    0x6F5C30: (0xD3A8, 0),  # Korean hangul
    0x22616C: (0x7722, 0),  # East Asian ideograph
    0x22616D: (0x771A, 0),  # East Asian ideograph
    0x6F4F67: (0xB9C9, 0),  # Korean hangul
    0x6F4B24: (0xAFBC, 0),  # Korean hangul
    0x21616F: (0x9B45, 0),  # East Asian ideograph
    0x28336F: (0x629F, 0),  # East Asian ideograph
    0x6F5C31: (0xD3A9, 0),  # Korean hangul
    0x6F245E: (0x3147, 0),  # Korean hangul
    0x4B5D42: (0x91E1, 0),  # East Asian ideograph
    0x27407D: (0x626B, 0),  # East Asian ideograph
    0x6F5029: (0xBA4E, 0),  # Korean hangul
    0x2D4327: (0x6630, 0),  # East Asian ideograph
    0x275E53: (0x5F00, 0),  # East Asian ideograph
    0x276173: (0x9B47, 0),  # East Asian ideograph
    0x3F3573: (0x8B3C, 0),  # East Asian ideograph
    0x226174: (0x7740, 0),  # East Asian ideograph
    0x6F4E41: (0xB610, 0),  # Korean hangul
    0x4B4C36: (0x7575, 0),  # East Asian ideograph
    0x216175: (0x9B77, 0),  # East Asian ideograph
    0x224B34: (0x6E53, 0),  # East Asian ideograph
    0x216176: (0x9B6F, 0),  # East Asian ideograph
    0x214C21: (0x752C, 0),  # East Asian ideograph
    0x226177: (0x7731, 0),  # East Asian ideograph
    0x214C22: (0x752B, 0),  # East Asian ideograph
    0x6F4F69: (0xB9CE, 0),  # Korean hangul
    0x276178: (0x9C9B, 0),  # East Asian ideograph
    0x6F4B26: (0xAFC7, 0),  # Korean hangul
    0x276179: (0x9C9C, 0),  # East Asian ideograph
    0x295269: (0x9A80, 0),  # East Asian ideograph
    0x214C24: (0x7530, 0),  # East Asian ideograph
    0x27617A: (0x9C94, 0),  # East Asian ideograph
    0x2F3143: (0x89F5, 0),  # Unrelated variant of EACC 23315E which maps to 89F5
    0x213A6B: (0x5B8F, 0),  # East Asian ideograph
    0x27617B: (0x9CA8, 0),  # East Asian ideograph
    0x214C26: (0x7531, 0),  # East Asian ideograph
    0x27617C: (0x9CA4, 0),  # East Asian ideograph
    0x214C27: (0x7533, 0),  # East Asian ideograph
    0x6F4F6A: (0xB9CF, 0),  # Korean hangul
    0x275E55: (0x95F4, 0),  # East Asian ideograph
    0x27617D: (0x9CB8, 0),  # East Asian ideograph
    0x6F4B27: (0xAFC8, 0),  # Korean hangul
    0x29593B: (0x9C9F, 0),  # East Asian ideograph
    0x27617E: (0x9CB3, 0),  # East Asian ideograph
    0x214C29: (0x7538, 0),  # East Asian ideograph
    0x215B60: (0x8FAD, 0),  # East Asian ideograph
    0x214C2A: (0x753D, 0),  # East Asian ideograph
    0x294237: (0x949B, 0),  # East Asian ideograph
    0x6F5C34: (0xD3B4, 0),  # Korean hangul
    0x39553C: (0x5D0B, 0),  # East Asian ideograph
    0x6F5360: (0xC228, 0),  # Korean hangul
    0x6F4C2B: (0xB153, 0),  # Korean hangul
    0x2D4C2C: (0x583A, 0),  # East Asian ideograph
    0x6F4F6B: (0xB9D0, 0),  # Korean hangul
    0x274C2D: (0x4EA9, 0),  # East Asian ideograph
    0x214C2E: (0x755C, 0),  # East Asian ideograph
    0x2D3661: (0x6199, 0),  # East Asian ideograph
    0x6F4C2F: (0xB15C, 0),  # Korean hangul
    0x214921: (0x6FA4, 0),  # East Asian ideograph
    0x214922: (0x6FC1, 0),  # East Asian ideograph
    0x214924: (0x6FC0, 0),  # East Asian ideograph
    0x214925: (0x6FB3, 0),  # East Asian ideograph
    0x214926: (0x6FDF, 0),  # East Asian ideograph
    0x214927: (0x6FD8, 0),  # East Asian ideograph
    0x214928: (0x6FF1, 0),  # East Asian ideograph
    0x214929: (0x6FE0, 0),  # East Asian ideograph
    0x21492A: (0x6FEF, 0),  # East Asian ideograph
    0x21492B: (
        0x6FEB,
        0,
    ),  # East Asian ideograph (variant of 4B492B which maps to 6FEB)
    0x21492C: (0x6FE1, 0),  # East Asian ideograph
    0x21492D: (0x6FE4, 0),  # East Asian ideograph
    0x21492E: (0x6F80, 0),  # East Asian ideograph
    0x22492F: (
        0x6D34,
        0,
    ),  # East Asian ideograph (variant of 34492F which maps to 6D34)
    0x234930: (0x9588, 0),  # East Asian ideograph
    0x214931: (0x700B, 0),  # East Asian ideograph
    0x214932: (0x7009, 0),  # East Asian ideograph
    0x214933: (0x7006, 0),  # East Asian ideograph
    0x214934: (0x6FFA, 0),  # East Asian ideograph
    0x214935: (0x7011, 0),  # East Asian ideograph
    0x214936: (0x6FFE, 0),  # East Asian ideograph
    0x214937: (0x700F, 0),  # East Asian ideograph
    0x234938: (0x959F, 0),  # East Asian ideograph
    0x214939: (0x701A, 0),  # East Asian ideograph
    0x23493A: (0x95A0, 0),  # East Asian ideograph
    0x21493B: (0x701D, 0),  # East Asian ideograph
    0x22493C: (0x6D65, 0),  # East Asian ideograph
    0x21493D: (0x701F, 0),  # East Asian ideograph
    0x22493E: (0x6D5E, 0),  # East Asian ideograph
    0x21493F: (0x703E, 0),  # East Asian ideograph
    0x214940: (0x704C, 0),  # East Asian ideograph
    0x214941: (0x7051, 0),  # East Asian ideograph
    0x214942: (0x7058, 0),  # East Asian ideograph
    0x274943: (0x6E7E, 0),  # East Asian ideograph
    0x214944: (0x7064, 0),  # East Asian ideograph
    0x214945: (0x706B, 0),  # East Asian ideograph
    0x214946: (0x7070, 0),  # East Asian ideograph
    0x214947: (0x7076, 0),  # East Asian ideograph
    0x214948: (0x707C, 0),  # East Asian ideograph
    0x214949: (0x7078, 0),  # East Asian ideograph
    0x21494A: (0x707D, 0),  # East Asian ideograph
    0x21494B: (0x7095, 0),  # East Asian ideograph
    0x21494C: (0x708E, 0),  # East Asian ideograph
    0x23494D: (0x95B9, 0),  # East Asian ideograph
    0x21494E: (0x7099, 0),  # East Asian ideograph
    0x21494F: (0x708A, 0),  # East Asian ideograph
    0x214950: (0x70AB, 0),  # East Asian ideograph
    0x214951: (0x70BA, 0),  # East Asian ideograph
    0x214952: (0x70AC, 0),  # East Asian ideograph
    0x214953: (0x70B3, 0),  # East Asian ideograph
    0x214954: (0x70AF, 0),  # East Asian ideograph
    0x214955: (0x70AD, 0),  # East Asian ideograph
    0x214956: (0x70AE, 0),  # East Asian ideograph
    0x214957: (0x70B8, 0),  # East Asian ideograph
    0x214958: (0x70CA, 0),  # East Asian ideograph
    0x214959: (0x70E4, 0),  # East Asian ideograph
    0x21495A: (0x70D8, 0),  # East Asian ideograph
    0x21495B: (0x70C8, 0),  # East Asian ideograph
    0x21495C: (0x70D9, 0),  # East Asian ideograph
    0x23495D: (0x95CE, 0),  # East Asian ideograph
    0x21495E: (0x70F9, 0),  # East Asian ideograph
    0x21495F: (0x7109, 0),  # East Asian ideograph
    0x214960: (0x710A, 0),  # East Asian ideograph
    0x214961: (0x70FD, 0),  # East Asian ideograph
    0x214962: (0x7119, 0),  # East Asian ideograph
    0x214963: (0x716E, 0),  # East Asian ideograph
    0x214964: (0x711A, 0),  # East Asian ideograph
    0x214965: (0x7136, 0),  # East Asian ideograph
    0x214966: (0x7121, 0),  # East Asian ideograph
    0x214967: (0x7130, 0),  # East Asian ideograph
    0x214968: (0x7126, 0),  # East Asian ideograph
    0x214969: (0x714E, 0),  # East Asian ideograph
    0x21496A: (0x7149, 0),  # East Asian ideograph
    0x21496B: (0x7159, 0),  # East Asian ideograph
    0x21496C: (0x7164, 0),  # East Asian ideograph
    0x21496D: (0x7169, 0),  # East Asian ideograph
    0x21496E: (0x715C, 0),  # East Asian ideograph
    0x21496F: (0x716C, 0),  # East Asian ideograph
    0x214970: (0x7166, 0),  # East Asian ideograph
    0x214971: (0x7167, 0),  # East Asian ideograph
    0x214972: (0x715E, 0),  # East Asian ideograph
    0x214973: (0x7165, 0),  # East Asian ideograph
    0x214974: (0x714C, 0),  # East Asian ideograph
    0x214975: (0x717D, 0),  # East Asian ideograph
    0x234976: (0x95E7, 0),  # East Asian ideograph
    0x214977: (0x7199, 0),  # East Asian ideograph
    0x214978: (0x718A, 0),  # East Asian ideograph
    0x214979: (0x7184, 0),  # East Asian ideograph
    0x21497A: (0x719F, 0),  # East Asian ideograph
    0x21497B: (0x71A8, 0),  # East Asian ideograph
    0x21497C: (0x71AC, 0),  # East Asian ideograph
    0x21497D: (0x71B1, 0),  # East Asian ideograph
    0x21497E: (0x71D9, 0),  # East Asian ideograph
    0x6F4C40: (0xB1DC, 0),  # Korean hangul
    0x2D432E: (0x66EC, 0),  # East Asian ideograph
    0x214C41: (0x7599, 0),  # East Asian ideograph
    0x395E71: (0x5742, 0),  # East Asian ideograph
    0x214C42: (0x759A, 0),  # East Asian ideograph
    0x6F586E: (0xCB64, 0),  # Korean hangul
    0x214C43: (0x75A4, 0),  # East Asian ideograph
    0x6F5C39: (0xD3C5, 0),  # Korean hangul
    0x224C44: (0x6F00, 0),  # East Asian ideograph
    0x4B3B31: (0x5B9F, 0),  # East Asian ideograph
    0x6F4C45: (0xB208, 0),  # Korean hangul
    0x6F4F70: (0xB9DD, 0),  # Korean hangul
    0x275E5B: (0x9601, 0),  # East Asian ideograph
    0x6F4B2D: (0xAFD8, 0),  # Korean hangul
    0x294440: (0x9506, 0),  # East Asian ideograph
    0x333475: (0x9628, 0),  # East Asian ideograph
    0x234C47: (0x9723, 0),  # East Asian ideograph
    0x27727E: (0x54D9, 0),  # East Asian ideograph
    0x21386E: (0x58DE, 0),  # East Asian ideograph
    0x6F4C48: (0xB213, 0),  # Korean hangul
    0x6F5C3A: (0xD3C8, 0),  # Korean hangul
    0x214C49: (0x75B2, 0),  # East Asian ideograph
    0x234E60: (0x97E1, 0),  # East Asian ideograph
    0x214C4A: (0x75BD, 0),  # East Asian ideograph
    0x6F4F71: (0xB9DE, 0),  # Korean hangul
    0x275E5C: (0x9600, 0),  # East Asian ideograph
    0x6F4877: (0xAC2D, 0),  # Korean hangul
    0x214C4B: (0x75BE, 0),  # East Asian ideograph
    0x294441: (0x9507, 0),  # East Asian ideograph
    0x333D54: (0x4EFD, 0),  # East Asian ideograph
    0x695C71: (0x6A78, 0),  # East Asian ideograph
    0x276F69: (0x5459, 0),  # East Asian ideograph
    0x6F5C3B: (0xD3C9, 0),  # Korean hangul
    0x70603A: (0x55EA, 0),  # East Asian ideograph
    0x69554E: (0x5B36, 0),  # East Asian ideograph
    0x214C4E: (0x75D5, 0),  # East Asian ideograph
    0x6F5852: (0xCA5C, 0),  # Korean hangul
    0x6F2460: (0x314A, 0),  # Korean hangul
    0x6F4C4F: (0xB258, 0),  # Korean hangul
    0x6F4F72: (0xB9E1, 0),  # Korean hangul
    0x275E5D: (0x5408, 0),  # East Asian ideograph
    0x214C50: (0x75B5, 0),  # East Asian ideograph
    0x214C51: (
        0x75CA,
        0,
    ),  # East Asian ideograph (variant of 4B4C51 which maps to 75CA)
    0x2E3F2D: (0x69B2, 0),  # East Asian ideograph
    0x2F2A73: (0x87CA, 0),  # East Asian ideograph
    0x214C52: (0x75DB, 0),  # East Asian ideograph
    0x6F5C3C: (0xD3D0, 0),  # Korean hangul
    0x285150: (0x70C3, 0),  # East Asian ideograph
    0x213E66: (0x60B2, 0),  # East Asian ideograph
    0x293336: (0x8BE4, 0),  # East Asian ideograph
    0x6F4C54: (0xB274, 0),  # Korean hangul
    0x6F4F73: (0xB9E3, 0),  # Korean hangul
    0x275E5E: (0x9605, 0),  # East Asian ideograph
    0x2E4731: (0x6C73, 0),  # East Asian ideograph
    0x6F4B30: (0xB000, 0),  # Korean hangul
    0x214C56: (0x75D9, 0),  # East Asian ideograph
    0x214C57: (0x75E2, 0),  # East Asian ideograph
    0x6F5C3D: (0xD3EC, 0),  # Korean hangul
    0x234C58: (0x9730, 0),  # East Asian ideograph
    0x6F4C59: (0xB294, 0),  # Korean hangul
    0x275E5F: (0x95FE, 0),  # East Asian ideograph
    0x214C5A: (0x75F0, 0),  # East Asian ideograph
    0x394444: (0x8988, 0),  # East Asian ideograph
    0x214A21: (0x71BE, 0),  # East Asian ideograph
    0x214A22: (0x71C9, 0),  # East Asian ideograph
    0x214A23: (0x71D0, 0),  # East Asian ideograph
    0x214A24: (0x71C8, 0),  # East Asian ideograph
    0x214A25: (0x71DC, 0),  # East Asian ideograph
    0x214A26: (0x71D2, 0),  # East Asian ideograph
    0x214A27: (0x71B9, 0),  # East Asian ideograph
    0x214A28: (0x71D5, 0),  # East Asian ideograph
    0x214A29: (0x71CE, 0),  # East Asian ideograph
    0x214A2A: (0x71C3, 0),  # East Asian ideograph
    0x214A2B: (0x71C4, 0),  # East Asian ideograph
    0x214A2C: (0x71EE, 0),  # East Asian ideograph
    0x214A2D: (0x71E7, 0),  # East Asian ideograph
    0x214A2E: (0x71DF, 0),  # East Asian ideograph
    0x214A2F: (0x71E5, 0),  # East Asian ideograph
    0x214A30: (0x71ED, 0),  # East Asian ideograph
    0x214A31: (0x71E6, 0),  # East Asian ideograph
    0x234A32: (0x963C, 0),  # East Asian ideograph
    0x214A33: (0x71F4, 0),  # East Asian ideograph
    0x214A34: (0x71FB, 0),  # East Asian ideograph
    0x224A35: (0x6DDD, 0),  # East Asian ideograph
    0x274A36: (0x70C1, 0),  # East Asian ideograph
    0x214A37: (0x7210, 0),  # East Asian ideograph
    0x214A38: (0x721B, 0),  # East Asian ideograph
    0x224A39: (0x6DDB, 0),  # East Asian ideograph
    0x214A3A: (0x722A, 0),  # East Asian ideograph
    0x214A3B: (0x722D, 0),  # East Asian ideograph
    0x214A3C: (0x722C, 0),  # East Asian ideograph
    0x214A3D: (0x7230, 0),  # East Asian ideograph
    0x214A3E: (
        0x7235,
        0,
    ),  # East Asian ideograph (variant of 4B4A3E which maps to 7235)
    0x214A3F: (0x7236, 0),  # East Asian ideograph
    0x214A40: (0x7238, 0),  # East Asian ideograph
    0x214A41: (0x7239, 0),  # East Asian ideograph
    0x214A42: (0x723A, 0),  # East Asian ideograph
    0x214A43: (0x723B, 0),  # East Asian ideograph
    0x214A44: (0x723D, 0),  # East Asian ideograph
    0x214A45: (0x723E, 0),  # East Asian ideograph
    0x224A46: (0x6DF0, 0),  # East Asian ideograph
    0x214A47: (0x7247, 0),  # East Asian ideograph
    0x214A48: (0x7248, 0),  # East Asian ideograph
    0x214A49: (0x724C, 0),  # East Asian ideograph
    0x214A4A: (0x7252, 0),  # East Asian ideograph
    0x214A4B: (0x7256, 0),  # East Asian ideograph
    0x214A4C: (0x7258, 0),  # East Asian ideograph
    0x214A4D: (0x7259, 0),  # East Asian ideograph
    0x214A4E: (0x725B, 0),  # East Asian ideograph
    0x214A4F: (0x725F, 0),  # East Asian ideograph
    0x214A50: (0x725D, 0),  # East Asian ideograph
    0x214A51: (0x7262, 0),  # East Asian ideograph
    0x214A52: (0x7261, 0),  # East Asian ideograph
    0x214A53: (0x7260, 0),  # East Asian ideograph
    0x214A54: (0x7267, 0),  # East Asian ideograph
    0x214A55: (0x7269, 0),  # East Asian ideograph
    0x214A56: (0x726F, 0),  # East Asian ideograph
    0x214A57: (0x7272, 0),  # East Asian ideograph
    0x214A58: (0x7274, 0),  # East Asian ideograph
    0x214A59: (0x7279, 0),  # East Asian ideograph
    0x214A5A: (0x727D, 0),  # East Asian ideograph
    0x214A5B: (0x7281, 0),  # East Asian ideograph
    0x214A5C: (0x7280, 0),  # East Asian ideograph
    0x214A5D: (0x7284, 0),  # East Asian ideograph
    0x274A5E: (0x8366, 0),  # East Asian ideograph
    0x214A5F: (0x7292, 0),  # East Asian ideograph
    0x224A60: (0x6E8A, 0),  # East Asian ideograph
    0x214A61: (0x72A2, 0),  # East Asian ideograph
    0x274A62: (0x727A, 0),  # East Asian ideograph
    0x214A63: (0x72AC, 0),  # East Asian ideograph
    0x214A64: (0x72AF, 0),  # East Asian ideograph
    0x214A65: (0x72C4, 0),  # East Asian ideograph
    0x214A66: (0x72C2, 0),  # East Asian ideograph
    0x214A67: (0x72D9, 0),  # East Asian ideograph
    0x274A68: (0x72B6, 0),  # East Asian ideograph
    0x214A69: (0x72CE, 0),  # East Asian ideograph
    0x214A6A: (0x72D7, 0),  # East Asian ideograph
    0x214A6B: (0x72D0, 0),  # East Asian ideograph
    0x214A6C: (0x72E1, 0),  # East Asian ideograph
    0x214A6D: (0x72E9, 0),  # East Asian ideograph
    0x214A6E: (0x72E0, 0),  # East Asian ideograph
    0x214A6F: (0x72FC, 0),  # East Asian ideograph
    0x274A70: (0x72ED, 0),  # East Asian ideograph
    0x224A71: (0x6E73, 0),  # East Asian ideograph
    0x214A72: (0x72FD, 0),  # East Asian ideograph
    0x214A73: (0x72F7, 0),  # East Asian ideograph
    0x214A74: (0x731C, 0),  # East Asian ideograph
    0x214A75: (0x731B, 0),  # East Asian ideograph
    0x214A76: (0x7313, 0),  # East Asian ideograph
    0x214A77: (0x7316, 0),  # East Asian ideograph
    0x214A78: (0x7319, 0),  # East Asian ideograph
    0x214A79: (0x7336, 0),  # East Asian ideograph
    0x214A7A: (0x7337, 0),  # East Asian ideograph
    0x214A7B: (0x7329, 0),  # East Asian ideograph
    0x214A7C: (0x7325, 0),  # East Asian ideograph
    0x214A7D: (0x7334, 0),  # East Asian ideograph
    0x214A7E: (0x7344, 0),  # East Asian ideograph
    0x2D4C3C: (0x53E0, 0),  # East Asian ideograph
    0x214C6B: (0x7634, 0),  # East Asian ideograph
    0x6F5C41: (0xD3FC, 0),  # Korean hangul
    0x213D4A: (0x5F46, 0),  # East Asian ideograph
    0x214C6C: (0x7638, 0),  # East Asian ideograph
    0x214C6D: (0x7646, 0),  # East Asian ideograph
    0x6F4F78: (0xB9F4, 0),  # Korean hangul
    0x275E63: (0x9611, 0),  # East Asian ideograph
    0x234C6E: (0x9749, 0),  # East Asian ideograph
    0x233D5B: (0x9046, 0),  # East Asian ideograph
    0x6F4C6F: (0xB2E6, 0),  # Korean hangul
    0x6F4C70: (0xB2E8, 0),  # Korean hangul
    0x214C71: (0x7658, 0),  # East Asian ideograph
    0x4D477B: (0x943E, 0),  # East Asian ideograph
    0x35344D: (0x8B5B, 0),  # East Asian ideograph
    0x6F4F79: (0xB9F5, 0),  # Korean hangul
    0x275E64: (0x95F1, 0),  # East Asian ideograph
    0x274C73: (0x75D2, 0),  # East Asian ideograph
    0x21355E: (0x542E, 0),  # East Asian ideograph
    0x275A21: (0x8D45, 0),  # East Asian ideograph
    0x6F4C74: (0xB2EE, 0),  # Korean hangul
    0x234147: (0x91AD, 0),  # East Asian ideograph
    0x217D7C: (0x5B56, 0),  # East Asian ideograph
    0x214C75: (0x7669, 0),  # East Asian ideograph
    0x6F5C43: (0xD3FF, 0),  # Korean hangul
    0x234C76: (0x975A, 0),  # East Asian ideograph
    0x233721: (0x8CF7, 0),  # East Asian ideograph
    0x287161: (0x7EFB, 0),  # East Asian ideograph
    0x3A787D: (0x80FC, 0),  # East Asian ideograph
    0x214C77: (0x766C, 0),  # East Asian ideograph
    0x273722: (0x545B, 0),  # East Asian ideograph
    0x275E65: (0x677F, 0),  # East Asian ideograph
    0x214C78: (0x7671, 0),  # East Asian ideograph
    0x213723: (0x55E1, 0),  # East Asian ideograph
    0x21754E: (0x579D, 0),  # East Asian ideograph
    0x214C79: (
        0x7672,
        0,
    ),  # East Asian ideograph (variant of 4B4C79 which maps to 7672)
    0x694C7A: (0x9453, 0),  # East Asian ideograph
    0x213725: (0x561B, 0),  # East Asian ideograph
    0x6F5C44: (0xD401, 0),  # Korean hangul
    0x214C7B: (0x767C, 0),  # East Asian ideograph
    0x233726: (0x8CFE, 0),  # East Asian ideograph
    0x6F4C7C: (0xB2FF, 0),  # Korean hangul
    0x223727: (0x65AE, 0),  # East Asian ideograph
    0x2E4739: (
        0x6C67,
        0,
    ),  # East Asian ideograph (variant of 224739 which maps to 6C67)
    0x214C7D: (0x767D, 0),  # East Asian ideograph
    0x6F7728: (0xAE07, 0),  # Korean hangul
    0x215336: (0x80B4, 0),  # East Asian ideograph
    0x2D4C7E: (0x4F70, 0),  # East Asian ideograph
    0x217729: (0x582D, 0),  # East Asian ideograph
    0x2D5447: (0x824A, 0),  # East Asian ideograph
    0x21372A: (0x561F, 0),  # East Asian ideograph
    0x6F5C45: (0xD440, 0),  # Korean hangul
    0x2D3A47: (0x5ACB, 0),  # East Asian ideograph
    0x4B4358: (0x66FD, 0),  # East Asian ideograph
    0x23372B: (0x8D07, 0),  # East Asian ideograph
    0x217850: (0x58D6, 0),  # East Asian ideograph
    0x334A28: (0x91BC, 0),  # East Asian ideograph
    0x27372C: (0x53F9, 0),  # East Asian ideograph
    0x6F593C: (0xCCA0, 0),  # Korean hangul
    0x275E67: (0x95EF, 0),  # East Asian ideograph
    0x6F4B39: (0xB044, 0),  # Korean hangul
    0x275A24: (0x8D3E, 0),  # East Asian ideograph
    0x27372E: (0x5455, 0),  # East Asian ideograph
    0x21372F: (0x560E, 0),  # East Asian ideograph
    0x6F5C46: (0xD444, 0),  # Korean hangul
    0x224A6D: (0x6E63, 0),  # East Asian ideograph
    0x293340: (0x8C02, 0),  # East Asian ideograph
    0x214B21: (0x733F, 0),  # East Asian ideograph
    0x224B22: (0x6E28, 0),  # East Asian ideograph
    0x274B23: (0x72EE, 0),  # East Asian ideograph
    0x214B24: (0x7350, 0),  # East Asian ideograph
    0x6F4B25: (0xAFC0, 0),  # Korean hangul
    0x214B26: (0x7357, 0),  # East Asian ideograph
    0x274B27: (0x72EC, 0),  # East Asian ideograph
    0x224B28: (0x6E5E, 0),  # East Asian ideograph
    0x274B29: (0x83B7, 0),  # East Asian ideograph
    0x274B2A: (0x72B7, 0),  # East Asian ideograph
    0x274B2B: (0x517D, 0),  # East Asian ideograph
    0x224B2C: (0x6E84, 0),  # East Asian ideograph
    0x223732: (0x65C3, 0),  # East Asian ideograph
    0x224B2E: (0x6E2E, 0),  # East Asian ideograph
    0x234B2F: (0x96A4, 0),  # East Asian ideograph
    0x214B30: (0x7384, 0),  # East Asian ideograph
    0x214B31: (0x7387, 0),  # East Asian ideograph
    0x214B32: (0x7389, 0),  # East Asian ideograph
    0x223733: (0x65C4, 0),  # East Asian ideograph
    0x214B34: (0x7396, 0),  # East Asian ideograph
    0x214B35: (0x739F, 0),  # East Asian ideograph
    0x214B36: (0x73A8, 0),  # East Asian ideograph
    0x214B37: (0x73A9, 0),  # East Asian ideograph
    0x214B38: (0x73AB, 0),  # East Asian ideograph
    0x214B39: (0x73BB, 0),  # East Asian ideograph
    0x214B3A: (0x73CA, 0),  # East Asian ideograph
    0x214B3B: (0x73B7, 0),  # East Asian ideograph
    0x214B3C: (0x73C0, 0),  # East Asian ideograph
    0x6F4B3D: (0xB04C, 0),  # Korean hangul
    0x214B3E: (0x73B2, 0),  # East Asian ideograph
    0x214B3F: (0x73CD, 0),  # East Asian ideograph
    0x224B40: (0x6E2A, 0),  # East Asian ideograph
    0x224B41: (0x6E4C, 0),  # East Asian ideograph
    0x224B42: (0x6E22, 0),  # East Asian ideograph
    0x224B43: (0x6ECE, 0),  # East Asian ideograph
    0x214B44: (0x7409, 0),  # East Asian ideograph
    0x224B45: (0x6E9B, 0),  # East Asian ideograph
    0x224B46: (0x6E9F, 0),  # East Asian ideograph
    0x214B47: (0x73FE, 0),  # East Asian ideograph
    0x224B48: (0x6EC8, 0),  # East Asian ideograph
    0x224B49: (0x6ED8, 0),  # East Asian ideograph
    0x224B4A: (0x6E8F, 0),  # East Asian ideograph
    0x214B4B: (0x7435, 0),  # East Asian ideograph
    0x214B4C: (0x7436, 0),  # East Asian ideograph
    0x224B4D: (0x6E93, 0),  # East Asian ideograph
    0x214B4E: (0x742A, 0),  # East Asian ideograph
    0x224B4F: (0x6EA0, 0),  # East Asian ideograph
    0x214B50: (0x7422, 0),  # East Asian ideograph
    0x224B51: (0x6EB1, 0),  # East Asian ideograph
    0x234B52: (0x96CE, 0),  # East Asian ideograph
    0x214B53: (0x7455, 0),  # East Asian ideograph
    0x214B54: (0x745F, 0),  # East Asian ideograph
    0x214B55: (0x745A, 0),  # East Asian ideograph
    0x214B56: (0x7441, 0),  # East Asian ideograph
    0x214B57: (0x743F, 0),  # East Asian ideograph
    0x214B58: (0x745B, 0),  # East Asian ideograph
    0x224B59: (0x6E92, 0),  # East Asian ideograph
    0x224B5A: (0x6EA7, 0),  # East Asian ideograph
    0x214B5B: (0x7459, 0),  # East Asian ideograph
    0x214B5C: (0x7483, 0),  # East Asian ideograph
    0x214B5D: (0x7469, 0),  # East Asian ideograph
    0x274B5E: (0x739B, 0),  # East Asian ideograph
    0x214B5F: (0x7463, 0),  # East Asian ideograph
    0x214B60: (0x7464, 0),  # East Asian ideograph
    0x214B61: (0x7470, 0),  # East Asian ideograph
    0x214B62: (0x748B, 0),  # East Asian ideograph
    0x214B63: (
        0x749C,
        0,
    ),  # East Asian ideograph (variant of 4B4B63 which maps to 749C)
    0x214B64: (0x74A3, 0),  # East Asian ideograph
    0x214B65: (0x74A7, 0),  # East Asian ideograph
    0x214B66: (0x74A9, 0),  # East Asian ideograph
    0x214B67: (0x74B0, 0),  # East Asian ideograph
    0x214B68: (0x74A6, 0),  # East Asian ideograph
    0x214B69: (0x74BD, 0),  # East Asian ideograph
    0x224B6A: (0x6EC9, 0),  # East Asian ideograph
    0x274B6B: (0x73D1, 0),  # East Asian ideograph
    0x224B6C: (0x6EB3, 0),  # East Asian ideograph
    0x224B6D: (0x6EB7, 0),  # East Asian ideograph
    0x214B6E: (0x74E2, 0),  # East Asian ideograph
    0x214B6F: (0x74E3, 0),  # East Asian ideograph
    0x214B70: (0x74E6, 0),  # East Asian ideograph
    0x234B71: (0x96E9, 0),  # East Asian ideograph
    0x214B72: (0x74F7, 0),  # East Asian ideograph
    0x214B73: (0x7504, 0),  # East Asian ideograph
    0x234B74: (0x96F1, 0),  # East Asian ideograph
    0x214B75: (0x7515, 0),  # East Asian ideograph
    0x234B76: (0x96F0, 0),  # East Asian ideograph
    0x214B77: (0x751A, 0),  # East Asian ideograph
    0x234B78: (0x96FA, 0),  # East Asian ideograph
    0x224B79: (0x6ECF, 0),  # East Asian ideograph
    0x214B7A: (0x7522, 0),  # East Asian ideograph
    0x214B7B: (0x7526, 0),  # East Asian ideograph
    0x224B7C: (0x6ECA, 0),  # East Asian ideograph
    0x224B7D: (0x6ED5, 0),  # East Asian ideograph
    0x214B7E: (0x7529, 0),  # East Asian ideograph
    0x273740: (0x53FD, 0),  # East Asian ideograph
    0x6F526B: (0xC0C0, 0),  # Korean hangul
    0x294C76: (0x9753, 0),  # East Asian ideograph
    0x213565: (0x542B, 0),  # East Asian ideograph
    0x277742: (0x57D8, 0),  # East Asian ideograph
    0x293344: (0x8C19, 0),  # East Asian ideograph
    0x273744: (0x5428, 0),  # East Asian ideograph
    0x27624F: (0x9E3E, 0),  # East Asian ideograph
    0x223745: (0x65DC, 0),  # East Asian ideograph
    0x6F593D: (0xCCA8, 0),  # Korean hangul
    0x6F4B3E: (0xB053, 0),  # Korean hangul
    0x213746: (0x5679, 0),  # East Asian ideograph
    0x223747: (0x65DD, 0),  # East Asian ideograph
    0x223748: (0x65DF, 0),  # East Asian ideograph
    0x293345: (0x8BE8, 0),  # East Asian ideograph
    0x217749: (0x583D, 0),  # East Asian ideograph
    0x4B3B43: (0x5BFE, 0),  # East Asian ideograph
    0x276175: (0x9C7F, 0),  # East Asian ideograph
    0x21374A: (0x5671, 0),  # East Asian ideograph
    0x6F5D70: (0xD760, 0),  # Korean hangul
    0x6F4B3F: (0xB054, 0),  # Korean hangul
    0x21374B: (0x566F, 0),  # East Asian ideograph
    0x6F5863: (0xCB14, 0),  # Korean hangul
    0x21374C: (
        0x5662,
        0,
    ),  # East Asian ideograph (variant of 4B374C which maps to 5662)
    0x282F47: (0x620B, 0),  # East Asian ideograph
    0x22374E: (0x65E4, 0),  # East Asian ideograph
    0x6F543A: (0xC314, 0),  # Korean hangul
    0x6F4B40: (0xB055, 0),  # Korean hangul
    0x692525: (0x30A5, 0),  # Katakana letter small U
    0x4B4C51: (0x75CA, 0),  # East Asian ideograph
    0x273751: (0x5413, 0),  # East Asian ideograph
    0x213752: (0x5690, 0),  # East Asian ideograph
    0x6F5C4D: (0xD488, 0),  # Korean hangul
    0x70604C: (0x55F5, 0),  # East Asian ideograph
    0x224A74: (0x6E4F, 0),  # East Asian ideograph
    0x334E73: (0x79A5, 0),  # East Asian ideograph
    0x234A30: (0x963D, 0),  # East Asian ideograph
    0x273754: (0x565C, 0),  # East Asian ideograph
    0x2D4343: (0x6636, 0),  # East Asian ideograph
    0x2D4768: (
        0x6D45,
        0,
    ),  # East Asian ideograph (variant of 274768 which maps to 6D45)
    0x223755: (0x65F0, 0),  # East Asian ideograph
    0x213756: (0x56A8, 0),  # East Asian ideograph
    0x4B375A: (0x53B3, 0),  # East Asian ideograph
    0x213757: (0x56B0, 0),  # East Asian ideograph
    0x2D3758: (0x54BD, 0),  # East Asian ideograph
    0x294162: (0x9486, 0),  # East Asian ideograph
    0x212A3B: (0xE8E8, 0),  # EACC component character
    0x284056: (0x6920, 0),  # East Asian ideograph
    0x21375A: (0x56B4, 0),  # East Asian ideograph
    0x6F592D: (0xCC44, 0),  # Korean hangul
    0x224C21: (0x6EC3, 0),  # East Asian ideograph
    0x234C22: (0x96FF, 0),  # East Asian ideograph
    0x214C23: (0x752D, 0),  # East Asian ideograph
    0x224C24: (0x6EB4, 0),  # East Asian ideograph
    0x214C25: (0x7532, 0),  # East Asian ideograph
    0x224C26: (0x6EB2, 0),  # East Asian ideograph
    0x234C27: (0x9702, 0),  # East Asian ideograph
    0x214C28: (0x7537, 0),  # East Asian ideograph
    0x224C29: (0x6EB5, 0),  # East Asian ideograph
    0x234C2A: (0x9705, 0),  # East Asian ideograph
    0x214C2B: (0x754F, 0),  # East Asian ideograph
    0x214C2C: (0x754C, 0),  # East Asian ideograph
    0x214C2D: (0x755D, 0),  # East Asian ideograph
    0x224C2E: (0x6EF8, 0),  # East Asian ideograph
    0x214C2F: (0x7554, 0),  # East Asian ideograph
    0x224C30: (0x6F37, 0),  # East Asian ideograph
    0x214C31: (0x7559, 0),  # East Asian ideograph
    0x214C32: (0x7566, 0),  # East Asian ideograph
    0x214C33: (0x7562, 0),  # East Asian ideograph
    0x224C34: (0x6EFD, 0),  # East Asian ideograph
    0x224C35: (0x6F09, 0),  # East Asian ideograph
    0x214C36: (0x756B, 0),  # East Asian ideograph
    0x214C37: (0x756A, 0),  # East Asian ideograph
    0x214C38: (0x7578, 0),  # East Asian ideograph
    0x214C39: (0x7576, 0),  # East Asian ideograph
    0x214C3A: (0x7586, 0),  # East Asian ideograph
    0x214C3B: (0x7587, 0),  # East Asian ideograph
    0x214C3C: (0x758A, 0),  # East Asian ideograph
    0x224C3D: (0x6F63, 0),  # East Asian ideograph
    0x224C3E: (0x6F12, 0),  # East Asian ideograph
    0x214C3F: (0x7591, 0),  # East Asian ideograph
    0x214C40: (0x759D, 0),  # East Asian ideograph
    0x224C41: (0x6F1A, 0),  # East Asian ideograph
    0x224C42: (0x6EF6, 0),  # East Asian ideograph
    0x224C43: (0x6F19, 0),  # East Asian ideograph
    0x214C44: (0x75AB, 0),  # East Asian ideograph
    0x214C45: (0x75A5, 0),  # East Asian ideograph
    0x214C46: (0x75C7, 0),  # East Asian ideograph
    0x214C47: (0x75C5, 0),  # East Asian ideograph
    0x214C48: (0x75B3, 0),  # East Asian ideograph
    0x234C49: (0x9722, 0),  # East Asian ideograph
    0x234C4A: (0x9724, 0),  # East Asian ideograph
    0x224C4B: (0x6F24, 0),  # East Asian ideograph
    0x214C4C: (0x75BC, 0),  # East Asian ideograph
    0x214C4D: (0x75B9, 0),  # East Asian ideograph
    0x234C4E: (0x9728, 0),  # East Asian ideograph
    0x214C4F: (0x75D4, 0),  # East Asian ideograph
    0x234C50: (0x9726, 0),  # East Asian ideograph
    0x224C51: (0x6F18, 0),  # East Asian ideograph
    0x234C52: (0x9731, 0),  # East Asian ideograph
    0x214C53: (0x75E3, 0),  # East Asian ideograph
    0x214C54: (0x75D8, 0),  # East Asian ideograph
    0x214C55: (0x75DE, 0),  # East Asian ideograph
    0x274C56: (0x75C9, 0),  # East Asian ideograph
    0x224C57: (0x6F1F, 0),  # East Asian ideograph
    0x214C58: (0x7601, 0),  # East Asian ideograph
    0x214C59: (0x7600, 0),  # East Asian ideograph
    0x224C5A: (0x6F0A, 0),  # East Asian ideograph
    0x214C5B: (0x75F2, 0),  # East Asian ideograph
    0x234C5C: (0x9736, 0),  # East Asian ideograph
    0x214C5D: (0x75F4, 0),  # East Asian ideograph
    0x214C5E: (0x75FF, 0),  # East Asian ideograph
    0x214C5F: (0x75FA, 0),  # East Asian ideograph
    0x224C60: (0x6EF9, 0),  # East Asian ideograph
    0x224C61: (0x6EEE, 0),  # East Asian ideograph
    0x224C62: (0x6F41, 0),  # East Asian ideograph
    0x214C63: (0x760B, 0),  # East Asian ideograph
    0x224C64: (0x6F95, 0),  # East Asian ideograph
    0x214C65: (0x7620, 0),  # East Asian ideograph
    0x214C66: (0x7629, 0),  # East Asian ideograph
    0x214C67: (0x761F, 0),  # East Asian ideograph
    0x214C68: (0x7624, 0),  # East Asian ideograph
    0x214C69: (0x7626, 0),  # East Asian ideograph
    0x214C6A: (0x7621, 0),  # East Asian ideograph
    0x224C6B: (0x6F49, 0),  # East Asian ideograph
    0x234C6C: (0x9746, 0),  # East Asian ideograph
    0x224C6D: (0x6F30, 0),  # East Asian ideograph
    0x214C6E: (0x7642, 0),  # East Asian ideograph
    0x214C6F: (0x764C, 0),  # East Asian ideograph
    0x214C70: (0x7656, 0),  # East Asian ideograph
    0x274C71: (0x75A0, 0),  # East Asian ideograph
    0x6F4C72: (0xB2EC, 0),  # Korean hangul
    0x214C73: (0x7662, 0),  # East Asian ideograph
    0x214C74: (0x7665, 0),  # East Asian ideograph
    0x234C75: (0x9758, 0),  # East Asian ideograph
    0x214C76: (0x766E, 0),  # East Asian ideograph
    0x224C77: (0x6EEB, 0),  # East Asian ideograph
    0x224C78: (0x6F08, 0),  # East Asian ideograph
    0x224C79: (0x6F0E, 0),  # East Asian ideograph
    0x214C7A: (0x7678, 0),  # East Asian ideograph
    0x224C7B: (0x6F35, 0),  # East Asian ideograph
    0x214C7C: (0x767B, 0),  # East Asian ideograph
    0x234C7D: (0x9764, 0),  # East Asian ideograph
    0x214C7E: (0x767E, 0),  # East Asian ideograph
    0x21376B: (0x56F1, 0),  # East Asian ideograph
    0x6F5C52: (0xD4E8, 0),  # Korean hangul
    0x21376D: (0x5703, 0),  # East Asian ideograph
    0x2D4348: (0x6681, 0),  # East Asian ideograph
    0x2E4747: (0x6D64, 0),  # East Asian ideograph
    0x3F424F: (
        0x542F,
        0,
    ),  # East Asian ideograph (variant of 27424F which maps to 542F)
    0x6F4B46: (0xB080, 0),  # Korean hangul
    0x21376E: (0x5708, 0),  # East Asian ideograph
    0x212A2F: (0xE8DD, 0),  # EACC component character
    0x27376F: (0x56EF, 0),  # East Asian ideograph
    0x273770: (0x56F4, 0),  # East Asian ideograph
    0x6F5C53: (0xD504, 0),  # Korean hangul
    0x27632B: (0x9F99, 0),  # East Asian ideograph
    0x213771: (0x5712, 0),  # East Asian ideograph
    0x294163: (0x948C, 0),  # East Asian ideograph
    0x224637: (0x6BFA, 0),  # East Asian ideograph
    0x213772: (0x5713, 0),  # East Asian ideograph
    0x2D4349: (0x66A6, 0),  # East Asian ideograph
    0x6F526D: (0xC0C5, 0),  # Korean hangul
    0x213430: (0x52C9, 0),  # East Asian ideograph
    0x6F4B47: (0xB084, 0),  # Korean hangul
    0x275A32: (0x8D4F, 0),  # East Asian ideograph
    0x216F21: (0x544F, 0),  # East Asian ideograph
    0x213774: (0x5716, 0),  # East Asian ideograph
    0x233775: (0x8D8D, 0),  # East Asian ideograph
    0x6F4E2A: (0xB554, 0),  # Korean hangul
    0x29334E: (0x8C0C, 0),  # East Asian ideograph
    0x276221: (0x9CC3, 0),  # East Asian ideograph
    0x213777: (0x572D, 0),  # East Asian ideograph
    0x216222: (0x9C0D, 0),  # East Asian ideograph
    0x6F4B48: (0xB08C, 0),  # Korean hangul
    0x29445B: (0x9516, 0),  # East Asian ideograph
    0x276223: (0x9CAB, 0),  # East Asian ideograph
    0x276224: (0x9CCD, 0),  # East Asian ideograph
    0x694C5D: (0x6762, 0),  # East Asian ideograph
    0x222225: (0x5BEF, 0),  # East Asian ideograph
    0x706054: (0x5623, 0),  # East Asian ideograph
    0x395568: (0x83DD, 0),  # East Asian ideograph
    0x234E7B: (0x980F, 0),  # East Asian ideograph
    0x216226: (0x9C31, 0),  # East Asian ideograph
    0x276177: (0x9C8D, 0),  # East Asian ideograph
    0x21377C: (0x5751, 0),  # East Asian ideograph
    0x276227: (0x9CD4, 0),  # East Asian ideograph
    0x6F4B49: (0xB08D, 0),  # Korean hangul
    0x21377D: (0x574A, 0),  # East Asian ideograph
    0x276228: (0x9CD7, 0),  # East Asian ideograph
    0x276229: (0x9CDD, 0),  # East Asian ideograph
    0x6F5C56: (0xD50C, 0),  # Korean hangul
    0x27622A: (0x9CDE, 0),  # East Asian ideograph
    0x284D27: (0x6D9D, 0),  # East Asian ideograph
    0x27622B: (0x9CDC, 0),  # East Asian ideograph
    0x27622C: (0x9CD6, 0),  # East Asian ideograph
    0x28405E: (0x67FD, 0),  # East Asian ideograph
    0x21622D: (0x9C77, 0),  # East Asian ideograph
    0x4B4C5B: (0x75F3, 0),  # East Asian ideograph
    0x27622E: (0x9C88, 0),  # East Asian ideograph
    0x2D5238: (0x898A, 0),  # East Asian ideograph
    0x2E363F: (0x52C5, 0),  # East Asian ideograph
    0x6F5C57: (0xD514, 0),  # Korean hangul
    0x27622F: (0x9E1F, 0),  # East Asian ideograph
    0x6F5959: (0xCDA7, 0),  # Korean hangul
    0x214D21: (0x7682, 0),  # East Asian ideograph
    0x214D22: (0x7684, 0),  # East Asian ideograph
    0x214D23: (0x7687, 0),  # East Asian ideograph
    0x214D24: (0x7686, 0),  # East Asian ideograph
    0x234D25: (0x9767, 0),  # East Asian ideograph
    0x214D26: (0x768E, 0),  # East Asian ideograph
    0x214D27: (0x7696, 0),  # East Asian ideograph
    0x214D28: (0x7693, 0),  # East Asian ideograph
    0x214D29: (0x769A, 0),  # East Asian ideograph
    0x214D2A: (0x76AE, 0),  # East Asian ideograph
    0x214D2B: (0x76B0, 0),  # East Asian ideograph
    0x214D2C: (0x76B4, 0),  # East Asian ideograph
    0x274D2D: (0x76B1, 0),  # East Asian ideograph
    0x214D2E: (0x76BF, 0),  # East Asian ideograph
    0x214D2F: (0x76C2, 0),  # East Asian ideograph
    0x224D30: (0x6F60, 0),  # East Asian ideograph
    0x234D31: (0x9777, 0),  # East Asian ideograph
    0x214D32: (0x76C6, 0),  # East Asian ideograph
    0x214D33: (0x76CA, 0),  # East Asian ideograph
    0x214D34: (0x76CD, 0),  # East Asian ideograph
    0x214D35: (0x76CE, 0),  # East Asian ideograph
    0x214D36: (0x76D4, 0),  # East Asian ideograph
    0x214D37: (0x76D2, 0),  # East Asian ideograph
    0x214D38: (0x76DC, 0),  # East Asian ideograph
    0x214D39: (0x76DB, 0),  # East Asian ideograph
    0x234D3A: (0x9780, 0),  # East Asian ideograph
    0x214D3B: (0x76DF, 0),  # East Asian ideograph
    0x234D3C: (0x9781, 0),  # East Asian ideograph
    0x214D3D: (0x76E3, 0),  # East Asian ideograph
    0x274D3E: (0x76D8, 0),  # East Asian ideograph
    0x274D3F: (0x5362, 0),  # East Asian ideograph
    0x214D40: (0x76E5, 0),  # East Asian ideograph
    0x214D41: (0x76EA, 0),  # East Asian ideograph
    0x214D42: (0x76EE, 0),  # East Asian ideograph
    0x214D43: (0x76EF, 0),  # East Asian ideograph
    0x214D44: (0x76F2, 0),  # East Asian ideograph
    0x214D45: (0x76F4, 0),  # East Asian ideograph
    0x214D46: (0x7709, 0),  # East Asian ideograph
    0x214D47: (0x76F9, 0),  # East Asian ideograph
    0x214D48: (0x76F8, 0),  # East Asian ideograph
    0x214D49: (0x7701, 0),  # East Asian ideograph
    0x214D4A: (0x770B, 0),  # East Asian ideograph
    0x214D4B: (0x76FC, 0),  # East Asian ideograph
    0x214D4C: (0x76FE, 0),  # East Asian ideograph
    0x214D4D: (0x7729, 0),  # East Asian ideograph
    0x214D4E: (0x7720, 0),  # East Asian ideograph
    0x214D4F: (0x771E, 0),  # East Asian ideograph
    0x214D50: (0x7728, 0),  # East Asian ideograph
    0x214D51: (0x7737, 0),  # East Asian ideograph
    0x214D52: (0x773C, 0),  # East Asian ideograph
    0x214D53: (0x7736, 0),  # East Asian ideograph
    0x214D54: (0x7738, 0),  # East Asian ideograph
    0x214D55: (0x773A, 0),  # East Asian ideograph
    0x274D56: (0x4F17, 0),  # East Asian ideograph
    0x274D57: (0x56F0, 0),  # East Asian ideograph
    0x214D58: (0x776B, 0),  # East Asian ideograph
    0x214D59: (0x775B, 0),  # East Asian ideograph
    0x214D5A: (0x776A, 0),  # East Asian ideograph
    0x214D5B: (0x7766, 0),  # East Asian ideograph
    0x214D5C: (0x7779, 0),  # East Asian ideograph
    0x274D5D: (0x7750, 0),  # East Asian ideograph
    0x214D5E: (0x7763, 0),  # East Asian ideograph
    0x214D5F: (0x775C, 0),  # East Asian ideograph
    0x214D60: (0x776C, 0),  # East Asian ideograph
    0x214D61: (0x7768, 0),  # East Asian ideograph
    0x214D62: (0x7765, 0),  # East Asian ideograph
    0x214D63: (0x777D, 0),  # East Asian ideograph
    0x214D64: (0x7771, 0),  # East Asian ideograph
    0x214D65: (0x777F, 0),  # East Asian ideograph
    0x214D66: (0x7784, 0),  # East Asian ideograph
    0x214D67: (0x7761, 0),  # East Asian ideograph
    0x214D68: (0x7787, 0),  # East Asian ideograph
    0x214D69: (0x778E, 0),  # East Asian ideograph
    0x214D6A: (0x778C, 0),  # East Asian ideograph
    0x214D6B: (0x7791, 0),  # East Asian ideograph
    0x214D6C: (0x779F, 0),  # East Asian ideograph
    0x214D6D: (0x779E, 0),  # East Asian ideograph
    0x214D6E: (0x77A0, 0),  # East Asian ideograph
    0x214D6F: (0x77A5, 0),  # East Asian ideograph
    0x214D70: (0x77B3, 0),  # East Asian ideograph
    0x214D71: (0x77AA, 0),  # East Asian ideograph
    0x214D72: (0x77B0, 0),  # East Asian ideograph
    0x214D73: (0x77AD, 0),  # East Asian ideograph
    0x214D74: (0x77AC, 0),  # East Asian ideograph
    0x214D75: (0x77A7, 0),  # East Asian ideograph
    0x214D76: (0x77BD, 0),  # East Asian ideograph
    0x214D77: (0x77BF, 0),  # East Asian ideograph
    0x214D78: (0x77BB, 0),  # East Asian ideograph
    0x224D79: (0x6FA6, 0),  # East Asian ideograph
    0x214D7A: (0x77D3, 0),  # East Asian ideograph
    0x214D7B: (0x77D7, 0),  # East Asian ideograph
    0x214D7C: (0x77DA, 0),  # East Asian ideograph
    0x214D7D: (0x77DB, 0),  # East Asian ideograph
    0x214D7E: (0x77DC, 0),  # East Asian ideograph
    0x276240: (0x9E44, 0),  # East Asian ideograph
    0x216241: (0x9D5D, 0),  # East Asian ideograph
    0x233D74: (0x9062, 0),  # East Asian ideograph
    0x216242: (0x9D89, 0),  # East Asian ideograph
    0x293B6D: (0x8F8A, 0),  # East Asian ideograph
    0x276243: (0x9E4A, 0),  # East Asian ideograph
    0x6F4D6A: (0xB4F1, 0),  # Korean hangul
    0x216244: (0x9D6A, 0),  # East Asian ideograph
    0x216245: (0x9D6C, 0),  # East Asian ideograph
    0x6F4B4F: (0xB098, 0),  # Korean hangul
    0x276246: (0x9E64, 0),  # East Asian ideograph
    0x333D75: (0x5FB3, 0),  # East Asian ideograph
    0x276247: (0x83BA, 0),  # East Asian ideograph
    0x6F5C5C: (0xD544, 0),  # Korean hangul
    0x232248: (0x8453, 0),  # East Asian ideograph
    0x276249: (0x9E67, 0),  # East Asian ideograph
    0x27624A: (0x9E25, 0),  # East Asian ideograph
    0x27624B: (0x9E36, 0),  # East Asian ideograph
    0x27624C: (0x9E70, 0),  # East Asian ideograph
    0x2E3645: (0x69E3, 0),  # East Asian ideograph
    0x21624D: (0x9DFA, 0),  # East Asian ideograph
    0x293357: (0x8C14, 0),  # East Asian ideograph
    0x27624E: (0x9E66, 0),  # East Asian ideograph
    0x21624F: (0x9E1E, 0),  # East Asian ideograph
    0x4B4F4C: (0x7A4F, 0),  # East Asian ideograph
    0x6F4B51: (0xB09A, 0),  # Korean hangul
    0x276250: (0x54B8, 0),  # East Asian ideograph
    0x294021: (0x90F8, 0),  # East Asian ideograph
    0x235B4D: (0x9D7B, 0),  # East Asian ideograph
    0x233934: (0x8DEC, 0),  # East Asian ideograph
    0x6F5C5E: (0xD54D, 0),  # Korean hangul
    0x216252: (0x9E7C, 0),  # East Asian ideograph
    0x344177: (0x8264, 0),  # East Asian ideograph
    0x39526B: (0x7094, 0),  # East Asian ideograph
    0x216256: (0x9E97, 0),  # East Asian ideograph
    0x2D5461: (0x8306, 0),  # East Asian ideograph
    0x6F5C5F: (0xD54F, 0),  # Korean hangul
    0x274931: (0x6C88, 0),  # East Asian ideograph
    0x293359: (0x8C11, 0),  # East Asian ideograph
    0x4B5D70: (0x92AD, 0),  # East Asian ideograph
    0x234A42: (0x9660, 0),  # East Asian ideograph
    0x216259: (0x9E9D, 0),  # East Asian ideograph
    0x6F4B53: (0xB09F, 0),  # Korean hangul
    0x294466: (0x9515, 0),  # East Asian ideograph
    0x214E21: (0x77E2, 0),  # East Asian ideograph
    0x214E22: (0x77E3, 0),  # East Asian ideograph
    0x214E23: (0x77E5, 0),  # East Asian ideograph
    0x214E24: (0x77E9, 0),  # East Asian ideograph
    0x214E25: (0x77ED, 0),  # East Asian ideograph
    0x214E26: (0x77EE, 0),  # East Asian ideograph
    0x214E27: (0x77EF, 0),  # East Asian ideograph
    0x214E28: (0x77F3, 0),  # East Asian ideograph
    0x214E29: (0x77FD, 0),  # East Asian ideograph
    0x214E2A: (0x7802, 0),  # East Asian ideograph
    0x214E2B: (0x780D, 0),  # East Asian ideograph
    0x214E2C: (0x780C, 0),  # East Asian ideograph
    0x234E2D: (0x97B8, 0),  # East Asian ideograph
    0x214E2E: (0x7830, 0),  # East Asian ideograph
    0x214E2F: (0x781D, 0),  # East Asian ideograph
    0x214E30: (0x7834, 0),  # East Asian ideograph
    0x214E31: (0x7838, 0),  # East Asian ideograph
    0x214E32: (0x7837, 0),  # East Asian ideograph
    0x214E33: (0x7827, 0),  # East Asian ideograph
    0x214E34: (0x782D, 0),  # East Asian ideograph
    0x214E35: (0x7825, 0),  # East Asian ideograph
    0x214E36: (0x786B, 0),  # East Asian ideograph
    0x214E37: (0x784F, 0),  # East Asian ideograph
    0x234E38: (0x97C0, 0),  # East Asian ideograph
    0x214E39: (0x786C, 0),  # East Asian ideograph
    0x214E3A: (0x785D, 0),  # East Asian ideograph
    0x214E3B: (0x786F, 0),  # East Asian ideograph
    0x214E3C: (0x78B0, 0),  # East Asian ideograph
    0x214E3D: (0x7897, 0),  # East Asian ideograph
    0x214E3E: (0x788E, 0),  # East Asian ideograph
    0x214E3F: (0x7898, 0),  # East Asian ideograph
    0x214E40: (0x7889, 0),  # East Asian ideograph
    0x214E41: (0x7891, 0),  # East Asian ideograph
    0x214E42: (0x787C, 0),  # East Asian ideograph
    0x214E43: (0x788C, 0),  # East Asian ideograph
    0x214E44: (0x78A7, 0),  # East Asian ideograph
    0x214E45: (0x78A9, 0),  # East Asian ideograph
    0x214E46: (0x789F, 0),  # East Asian ideograph
    0x214E47: (0x78B3, 0),  # East Asian ideograph
    0x214E48: (0x78CB, 0),  # East Asian ideograph
    0x214E49: (0x78BA, 0),  # East Asian ideograph
    0x214E4A: (0x78C1, 0),  # East Asian ideograph
    0x214E4B: (0x78C5, 0),  # East Asian ideograph
    0x214E4C: (0x78BC, 0),  # East Asian ideograph
    0x214E4D: (0x78D5, 0),  # East Asian ideograph
    0x214E4E: (0x78BE, 0),  # East Asian ideograph
    0x214E4F: (0x78CA, 0),  # East Asian ideograph
    0x214E50: (0x78D0, 0),  # East Asian ideograph
    0x214E51: (0x78E8, 0),  # East Asian ideograph
    0x214E52: (0x78EC, 0),  # East Asian ideograph
    0x214E53: (0x78DA, 0),  # East Asian ideograph
    0x214E54: (0x78F7, 0),  # East Asian ideograph
    0x214E55: (0x78F4, 0),  # East Asian ideograph
    0x214E56: (
        0x78FA,
        0,
    ),  # East Asian ideograph (variant of 4B4E56 which maps to 78FA)
    0x214E57: (0x7901, 0),  # East Asian ideograph
    0x214E58: (0x78EF, 0),  # East Asian ideograph
    0x234E59: (0x97DD, 0),  # East Asian ideograph
    0x214E5A: (0x7919, 0),  # East Asian ideograph
    0x214E5B: (0x7926, 0),  # East Asian ideograph
    0x214E5C: (0x792C, 0),  # East Asian ideograph
    0x224E5D: (0x6FDE, 0),  # East Asian ideograph
    0x214E5E: (0x792B, 0),  # East Asian ideograph
    0x214E5F: (0x793A, 0),  # East Asian ideograph
    0x214E60: (0x7940, 0),  # East Asian ideograph
    0x214E61: (0x793E, 0),  # East Asian ideograph
    0x214E62: (0x7941, 0),  # East Asian ideograph
    0x214E63: (0x7945, 0),  # East Asian ideograph
    0x214E64: (0x7949, 0),  # East Asian ideograph
    0x214E65: (0x7948, 0),  # East Asian ideograph
    0x214E66: (0x7947, 0),  # East Asian ideograph
    0x224E67: (0x700C, 0),  # East Asian ideograph
    0x214E68: (0x7960, 0),  # East Asian ideograph
    0x214E69: (0x7950, 0),  # East Asian ideograph
    0x214E6A: (0x7956, 0),  # East Asian ideograph
    0x214E6B: (0x795E, 0),  # East Asian ideograph
    0x214E6C: (0x795D, 0),  # East Asian ideograph
    0x214E6D: (0x795F, 0),  # East Asian ideograph
    0x214E6E: (0x795A, 0),  # East Asian ideograph
    0x214E6F: (0x7957, 0),  # East Asian ideograph
    0x214E70: (0x7965, 0),  # East Asian ideograph
    0x214E71: (0x7968, 0),  # East Asian ideograph
    0x214E72: (0x796D, 0),  # East Asian ideograph
    0x234E73: (0x97FA, 0),  # East Asian ideograph
    0x214E74: (0x7981, 0),  # East Asian ideograph
    0x214E75: (0x797F, 0),  # East Asian ideograph
    0x214E76: (0x798F, 0),  # East Asian ideograph
    0x214E77: (0x798D, 0),  # East Asian ideograph
    0x214E78: (0x798E, 0),  # East Asian ideograph
    0x214E79: (0x79A6, 0),  # East Asian ideograph
    0x214E7A: (0x79A7, 0),  # East Asian ideograph
    0x214E7B: (0x79AA, 0),  # East Asian ideograph
    0x214E7C: (0x79AE, 0),  # East Asian ideograph
    0x214E7D: (0x79B1, 0),  # East Asian ideograph
    0x214E7E: (0x79B9, 0),  # East Asian ideograph
    0x6F5C63: (0xD558, 0),  # Korean hangul
    0x6F4E2D: (0xB55F, 0),  # Korean hangul
    0x29335D: (0x8C16, 0),  # East Asian ideograph
    0x216461: (0x4EC8, 0),  # East Asian ideograph
    0x234A46: (0x9658, 0),  # East Asian ideograph
    0x69626D: (0x7874, 0),  # East Asian ideograph
    0x6F4B57: (0xB0A9, 0),  # Korean hangul
    0x27626F: (0x515A, 0),  # East Asian ideograph
    0x6F5C64: (0xD559, 0),  # Korean hangul
    0x274936: (0x6EE4, 0),  # East Asian ideograph
    0x6F5821: (0xC974, 0),  # Korean hangul
    0x6F4D53: (0xB450, 0),  # Korean hangul
    0x216271: (0x9EF4, 0),  # East Asian ideograph
    0x216272: (0x9EF7, 0),  # East Asian ideograph
    0x4B6159: (0x81B8, 0),  # East Asian ideograph
    0x216273: (0x9F07, 0),  # East Asian ideograph
    0x216275: (0x9F13, 0),  # East Asian ideograph
    0x274937: (0x6D4F, 0),  # East Asian ideograph
    0x6F5822: (0xC988, 0),  # Korean hangul
    0x216276: (0x9F15, 0),  # East Asian ideograph
    0x274633: (0x6B8B, 0),  # East Asian ideograph
    0x6F4D22: (0xB308, 0),  # Korean hangul
    0x6F4B59: (0xB0AC, 0),  # Korean hangul
    0x4B6278: (0x9F21, 0),  # East Asian ideograph
    0x224D23: (0x6F7E, 0),  # East Asian ideograph
    0x21712D: (0x5593, 0),  # East Asian ideograph
    0x224D24: (0x6F9D, 0),  # East Asian ideograph
    0x21627A: (0x9F34, 0),  # East Asian ideograph
    0x6F4D25: (0xB313, 0),  # Korean hangul
    0x6F5823: (0xC989, 0),  # Korean hangul
    0x23227B: (0x8484, 0),  # East Asian ideograph
    0x22464A: (0x6C05, 0),  # East Asian ideograph
    0x6F4D26: (0xB314, 0),  # Korean hangul
    0x6F534B: (0xC1B0, 0),  # Korean hangul
    0x23227C: (0x8478, 0),  # East Asian ideograph
    0x224D27: (0x6F87, 0),  # East Asian ideograph
    0x6F4B5A: (0xB0AD, 0),  # Korean hangul
    0x21627D: (0x9F4A, 0),  # East Asian ideograph
    0x6F4D28: (0xB354, 0),  # Korean hangul
    0x27627E: (0x658E, 0),  # East Asian ideograph
    0x274D29: (0x7691, 0),  # East Asian ideograph
    0x274D7C: (0x77A9, 0),  # East Asian ideograph
    0x6F5C67: (0xD565, 0),  # Korean hangul
    0x6F4D2A: (0xB358, 0),  # Korean hangul
    0x6F5824: (0xC98C, 0),  # Korean hangul
    0x213C7A: (0x5EB8, 0),  # East Asian ideograph
    0x224D2B: (0x6F6F, 0),  # East Asian ideograph
    0x6F5271: (0xC0CF, 0),  # Korean hangul
    0x234D2C: (0x976B, 0),  # East Asian ideograph
    0x6F4B5B: (0xB0AE, 0),  # Korean hangul
    0x214D2D: (0x76BA, 0),  # East Asian ideograph
    0x6F4C39: (0xB192, 0),  # Korean hangul
    0x29402B: (0x90BA, 0),  # East Asian ideograph
    0x23393E: (0x8DF2, 0),  # East Asian ideograph
    0x282D79: (0x60AB, 0),  # East Asian ideograph
    0x6F4D2E: (0xB364, 0),  # Korean hangul
    0x2D3251: (0x510C, 0),  # East Asian ideograph
    0x6F492C: (0xAC84, 0),  # Korean hangul
    0x6F5C68: (0xD568, 0),  # Korean hangul
    0x224D2F: (0x6F5A, 0),  # East Asian ideograph
    0x293362: (0x8C1D, 0),  # East Asian ideograph
    0x214F21: (0x79BD, 0),  # East Asian ideograph
    0x214F22: (0x842C, 0),  # East Asian ideograph
    0x214F23: (0x79BE, 0),  # East Asian ideograph
    0x214F24: (0x79C0, 0),  # East Asian ideograph
    0x214F25: (0x79C1, 0),  # East Asian ideograph
    0x214F26: (0x79BF, 0),  # East Asian ideograph
    0x214D31: (0x76C8, 0),  # East Asian ideograph
    0x214F28: (0x79D1, 0),  # East Asian ideograph
    0x214F29: (0x79CB, 0),  # East Asian ideograph
    0x214F2A: (0x79D2, 0),  # East Asian ideograph
    0x214F2B: (0x79E4, 0),  # East Asian ideograph
    0x214F2C: (0x79E6, 0),  # East Asian ideograph
    0x214F2D: (0x79E3, 0),  # East Asian ideograph
    0x214F2E: (0x79DF, 0),  # East Asian ideograph
    0x214F2F: (0x79E7, 0),  # East Asian ideograph
    0x214F30: (0x79E9, 0),  # East Asian ideograph
    0x224F31: (0x702D, 0),  # East Asian ideograph
    0x214F32: (0x7A05, 0),  # East Asian ideograph
    0x214F33: (0x7A0D, 0),  # East Asian ideograph
    0x214F34: (0x7A08, 0),  # East Asian ideograph
    0x214F35: (0x7A0B, 0),  # East Asian ideograph
    0x214F36: (0x7A00, 0),  # East Asian ideograph
    0x214F37: (0x7A1F, 0),  # East Asian ideograph
    0x234F38: (0x981F, 0),  # East Asian ideograph
    0x214F39: (0x7A20, 0),  # East Asian ideograph
    0x214F3A: (0x7A1A, 0),  # East Asian ideograph
    0x214F3B: (0x7A14, 0),  # East Asian ideograph
    0x214F3C: (0x7A31, 0),  # East Asian ideograph
    0x214F3D: (0x7A2E, 0),  # East Asian ideograph
    0x214F3E: (0x7A3F, 0),  # East Asian ideograph
    0x214F3F: (0x7A3C, 0),  # East Asian ideograph
    0x274F40: (0x8C37, 0),  # East Asian ideograph
    0x214F41: (0x7A3D, 0),  # East Asian ideograph
    0x214F42: (0x7A37, 0),  # East Asian ideograph
    0x214F43: (0x7A3B, 0),  # East Asian ideograph
    0x214F44: (0x7A4D, 0),  # East Asian ideograph
    0x214F45: (0x7A4E, 0),  # East Asian ideograph
    0x214F46: (0x7A4C, 0),  # East Asian ideograph
    0x214F47: (0x7A46, 0),  # East Asian ideograph
    0x214F48: (0x7A57, 0),  # East Asian ideograph
    0x274F49: (0x7A51, 0),  # East Asian ideograph
    0x214F4A: (0x7A62, 0),  # East Asian ideograph
    0x274F4B: (0x83B7, 0),  # East Asian ideograph (duplicate simplified)
    0x214F4C: (0x7A69, 0),  # East Asian ideograph
    0x214F4D: (0x7A74, 0),  # East Asian ideograph
    0x214F4E: (0x7A76, 0),  # East Asian ideograph
    0x214F4F: (0x7A79, 0),  # East Asian ideograph
    0x214F50: (0x7A7A, 0),  # East Asian ideograph
    0x214F51: (0x7A7F, 0),  # East Asian ideograph
    0x214F52: (0x7A81, 0),  # East Asian ideograph
    0x214F53: (0x7A84, 0),  # East Asian ideograph
    0x214F54: (0x7A88, 0),  # East Asian ideograph
    0x214F55: (0x7A92, 0),  # East Asian ideograph
    0x214F56: (0x7A95, 0),  # East Asian ideograph
    0x214F57: (0x7A98, 0),  # East Asian ideograph
    0x214F58: (0x7A96, 0),  # East Asian ideograph
    0x214F59: (0x7A97, 0),  # East Asian ideograph
    0x214F5A: (0x7A9F, 0),  # East Asian ideograph
    0x214F5B: (0x7AA0, 0),  # East Asian ideograph
    0x214F5C: (0x7AAA, 0),  # East Asian ideograph
    0x214D3A: (0x76DE, 0),  # East Asian ideograph
    0x214F5E: (0x7AAF, 0),  # East Asian ideograph
    0x214F5F: (0x7AAE, 0),  # East Asian ideograph
    0x274F60: (0x7AA5, 0),  # East Asian ideograph
    0x274F61: (0x7A8D, 0),  # East Asian ideograph
    0x274F62: (0x7A9C, 0),  # East Asian ideograph
    0x274F63: (0x7AA6, 0),  # East Asian ideograph
    0x214F64: (0x7ACA, 0),  # East Asian ideograph
    0x214F65: (0x7ACB, 0),  # East Asian ideograph
    0x214F66: (0x7AD9, 0),  # East Asian ideograph
    0x214F67: (0x7AE5, 0),  # East Asian ideograph
    0x214F68: (0x7AE3, 0),  # East Asian ideograph
    0x214D3C: (0x76E1, 0),  # East Asian ideograph
    0x214F6A: (0x7AEF, 0),  # East Asian ideograph
    0x274F6B: (0x7ADE, 0),  # East Asian ideograph
    0x214F6C: (0x7AF9, 0),  # East Asian ideograph
    0x214F6D: (0x7AFA, 0),  # East Asian ideograph
    0x214F6E: (0x7AFF, 0),  # East Asian ideograph
    0x214F6F: (0x7AFD, 0),  # East Asian ideograph
    0x214F70: (0x7B06, 0),  # East Asian ideograph
    0x214F71: (0x7B11, 0),  # East Asian ideograph
    0x214F72: (0x7B20, 0),  # East Asian ideograph
    0x214F73: (0x7B2C, 0),  # East Asian ideograph
    0x214F74: (0x7B28, 0),  # East Asian ideograph
    0x214D3E: (0x76E4, 0),  # East Asian ideograph
    0x214F76: (0x7B1E, 0),  # East Asian ideograph
    0x214F77: (0x7B19, 0),  # East Asian ideograph
    0x214F78: (0x7B26, 0),  # East Asian ideograph
    0x214F79: (0x7B46, 0),  # East Asian ideograph
    0x214F7A: (0x7B49, 0),  # East Asian ideograph
    0x214D3F: (0x76E7, 0),  # East Asian ideograph
    0x214F7C: (0x7B56, 0),  # East Asian ideograph
    0x214F7D: (0x7B52, 0),  # East Asian ideograph
    0x214F7E: (0x7B4B, 0),  # East Asian ideograph
    0x234D40: (0x9784, 0),  # East Asian ideograph
    0x6F4B5F: (0xB0B4, 0),  # Korean hangul
    0x294472: (0x951E, 0),  # East Asian ideograph
    0x4B4D41: (0x862F, 0),  # East Asian ideograph
    0x6F4D42: (0xB3CC, 0),  # Korean hangul
    0x2E3654: (0x657F, 0),  # East Asian ideograph
    0x2D502B: (0x693E, 0),  # East Asian ideograph
    0x234D43: (0x977F, 0),  # East Asian ideograph
    0x6F5829: (0xC9C0, 0),  # Korean hangul
    0x224D44: (0x6F0B, 0),  # East Asian ideograph
    0x2D4362: (0x6722, 0),  # East Asian ideograph
    0x4B4D45: (
        0x76F4,
        0,
    ),  # East Asian ideograph (variant of 214D45 which maps to 76F4)
    0x6F4B60: (0xB0B5, 0),  # Korean hangul
    0x217577: (0x57D2, 0),  # East Asian ideograph
    0x6F4D46: (0xB3D7, 0),  # Korean hangul
    0x213145: (0x4F9D, 0),  # East Asian ideograph
    0x217134: (0x5588, 0),  # East Asian ideograph
    0x6F4D47: (0xB3D9, 0),  # Korean hangul
    0x6F5C6D: (0xD571, 0),  # Korean hangul
    0x27493F: (0x6F9C, 0),  # East Asian ideograph
    0x6F582A: (0xC9C1, 0),  # Korean hangul
    0x276256: (0x4E3D, 0),  # East Asian ideograph
    0x224651: (0x6C0C, 0),  # East Asian ideograph
    0x234D49: (0x9789, 0),  # East Asian ideograph
    0x6F4D4A: (0xB400, 0),  # Korean hangul
    0x6F4B61: (0xB0B8, 0),  # Korean hangul
    0x294474: (0x951F, 0),  # East Asian ideograph
    0x224D4B: (0x6F6C, 0),  # East Asian ideograph
    0x294031: (0x909D, 0),  # East Asian ideograph
    0x333944: (0x5B2D, 0),  # East Asian ideograph
    0x6F4D4C: (0xB418, 0),  # Korean hangul
    0x283F30: (0x6966, 0),  # East Asian ideograph
    0x224D4D: (0x6F8B, 0),  # East Asian ideograph
    0x6F582B: (0xC9C4, 0),  # Korean hangul
    0x6F4D4E: (0xB420, 0),  # Korean hangul
    0x2D4364: (0x671E, 0),  # East Asian ideograph
    0x2D4D4F: (0x771F, 0),  # East Asian ideograph
    0x276327: (0x9F89, 0),  # East Asian ideograph
    0x6F586A: (0xCB50, 0),  # Korean hangul
    0x6F4D50: (0xB429, 0),  # Korean hangul
    0x213147: (0x4F75, 0),  # East Asian ideograph
    0x6F4D51: (0xB42B, 0),  # Korean hangul
    0x212329: (0xFF09, 0),  # Ideographic right parenthesis
    0x6F4D52: (0xB42C, 0),  # Korean hangul
    0x6F582C: (0xC9C7, 0),  # Korean hangul
    0x4B3B67: (0x6B67, 0),  # East Asian ideograph
    0x234D54: (0x9794, 0),  # East Asian ideograph
    0x6F4B63: (0xB0BC, 0),  # Korean hangul
    0x335773: (0x88B4, 0),  # East Asian ideograph
    0x6F4D55: (0xB454, 0),  # Korean hangul
    0x27514A: (0x7EF0, 0),  # East Asian ideograph
    0x214D56: (0x773E, 0),  # East Asian ideograph
    0x6F5C70: (0xD578, 0),  # Korean hangul
    0x276B5B: (0x5250, 0),  # East Asian ideograph
    0x214D57: (0x774F, 0),  # East Asian ideograph
    0x3F5959: (0x8276, 0),  # East Asian ideograph
    0x224D58: (0x6E88, 0),  # East Asian ideograph
    0x35347B: (0x8B2D, 0),  # East Asian ideograph
    0x234D59: (0x979B, 0),  # East Asian ideograph
    0x6F4B64: (0xB0C4, 0),  # Korean hangul
    0x224D5A: (0x6F55, 0),  # East Asian ideograph
    0x213149: (0x4F73, 0),  # East Asian ideograph
    0x21623E: (0x9D61, 0),  # East Asian ideograph
    0x235021: (0x9865, 0),  # East Asian ideograph
    0x235022: (0x9866, 0),  # East Asian ideograph
    0x215023: (0x7B54, 0),  # East Asian ideograph
    0x215024: (0x7B60, 0),  # East Asian ideograph
    0x215025: (0x7B77, 0),  # East Asian ideograph
    0x215026: (0x7B75, 0),  # East Asian ideograph
    0x215027: (0x7BA1, 0),  # East Asian ideograph
    0x215028: (0x7B94, 0),  # East Asian ideograph
    0x235029: (0x986C, 0),  # East Asian ideograph
    0x21502A: (0x7B9D, 0),  # East Asian ideograph
    0x21502B: (0x7B8B, 0),  # East Asian ideograph
    0x21502C: (0x7B97, 0),  # East Asian ideograph
    0x21502D: (0x7B8F, 0),  # East Asian ideograph
    0x21502E: (0x7BC7, 0),  # East Asian ideograph
    0x214D5D: (0x775E, 0),  # East Asian ideograph
    0x235030: (0x9873, 0),  # East Asian ideograph
    0x215031: (0x7BB1, 0),  # East Asian ideograph
    0x215032: (0x7BB4, 0),  # East Asian ideograph
    0x215033: (0x7BC0, 0),  # East Asian ideograph
    0x215034: (0x7BC6, 0),  # East Asian ideograph
    0x215035: (0x7BC1, 0),  # East Asian ideograph
    0x215036: (0x7C11, 0),  # East Asian ideograph
    0x215037: (0x7BD9, 0),  # East Asian ideograph
    0x215038: (0x7BDB, 0),  # East Asian ideograph
    0x235039: (0x98AD, 0),  # East Asian ideograph
    0x21503A: (0x7BC9, 0),  # East Asian ideograph
    0x21503B: (0x7BE1, 0),  # East Asian ideograph
    0x21503C: (0x7BE9, 0),  # East Asian ideograph
    0x21503D: (0x7C07, 0),  # East Asian ideograph
    0x21503E: (0x7C0D, 0),  # East Asian ideograph
    0x21503F: (0x7BFE, 0),  # East Asian ideograph
    0x235040: (0x98B4, 0),  # East Asian ideograph
    0x215041: (0x7C21, 0),  # East Asian ideograph
    0x215042: (0x7C2B, 0),  # East Asian ideograph
    0x215043: (0x7C2A, 0),  # East Asian ideograph
    0x215044: (0x7C27, 0),  # East Asian ideograph
    0x215045: (0x7C1E, 0),  # East Asian ideograph
    0x215046: (0x7C23, 0),  # East Asian ideograph
    0x215047: (0x7C3F, 0),  # East Asian ideograph
    0x215048: (0x7C3E, 0),  # East Asian ideograph
    0x215049: (0x7C38, 0),  # East Asian ideograph
    0x21504A: (0x7C37, 0),  # East Asian ideograph
    0x27504B: (0x7B7E, 0),  # East Asian ideograph
    0x21504C: (0x7C43, 0),  # East Asian ideograph
    0x23504D: (0x98BB, 0),  # East Asian ideograph
    0x23504E: (0x98C0, 0),  # East Asian ideograph
    0x21504F: (0x7C50, 0),  # East Asian ideograph
    0x215050: (0x7C60, 0),  # East Asian ideograph
    0x215051: (0x7C5F, 0),  # East Asian ideograph
    0x215052: (0x7C64, 0),  # East Asian ideograph
    0x215053: (0x7C6C, 0),  # East Asian ideograph
    0x215054: (0x7C6E, 0),  # East Asian ideograph
    0x215055: (0x7C72, 0),  # East Asian ideograph
    0x215056: (0x7C73, 0),  # East Asian ideograph
    0x215057: (0x7C89, 0),  # East Asian ideograph
    0x215058: (0x7C92, 0),  # East Asian ideograph
    0x215059: (0x7C97, 0),  # East Asian ideograph
    0x21505A: (0x7C9F, 0),  # East Asian ideograph
    0x21505B: (0x7CA5, 0),  # East Asian ideograph
    0x21505C: (0x7CA4, 0),  # East Asian ideograph
    0x21505D: (0x7CB1, 0),  # East Asian ideograph
    0x21505E: (0x7CB3, 0),  # East Asian ideograph
    0x23505F: (0x98E1, 0),  # East Asian ideograph
    0x275060: (0x7C8B, 0),  # East Asian ideograph
    0x215061: (0xFA1D, 0),  # East Asian ideograph
    0x275062: (0x80E1, 0),  # East Asian ideograph (duplicate simplified)
    0x215063: (0x7CD6, 0),  # East Asian ideograph
    0x215064: (0x7CD5, 0),  # East Asian ideograph
    0x215065: (0x7CE0, 0),  # East Asian ideograph
    0x215066: (0x7CDC, 0),  # East Asian ideograph
    0x215067: (0x7CDF, 0),  # East Asian ideograph
    0x215068: (0x7CDE, 0),  # East Asian ideograph
    0x215069: (0x7CE2, 0),  # East Asian ideograph
    0x21506A: (0x7CD9, 0),  # East Asian ideograph
    0x21506B: (0x7CE7, 0),  # East Asian ideograph
    0x21506C: (0x7CEF, 0),  # East Asian ideograph
    0x2E506D: (0x70B1, 0),  # East Asian ideograph
    0x21506E: (0x7CFB, 0),  # East Asian ideograph
    0x21506F: (0x7CFE, 0),  # East Asian ideograph
    0x215070: (0x7D00, 0),  # East Asian ideograph
    0x215071: (0x7D02, 0),  # East Asian ideograph
    0x215072: (0x7D05, 0),  # East Asian ideograph
    0x225073: (0x70A9, 0),  # East Asian ideograph
    0x215074: (0x7D04, 0),  # East Asian ideograph
    0x215075: (0x7D07, 0),  # East Asian ideograph
    0x215076: (0x7D21, 0),  # East Asian ideograph
    0x215077: (0x7D0B, 0),  # East Asian ideograph
    0x225078: (0x70EA, 0),  # East Asian ideograph
    0x215079: (0x7D20, 0),  # East Asian ideograph
    0x21507A: (0x7D1C, 0),  # East Asian ideograph
    0x21507B: (0x7D22, 0),  # East Asian ideograph
    0x27507C: (0x7EB0, 0),  # East Asian ideograph
    0x234D6A: (0x97AC, 0),  # East Asian ideograph
    0x21507E: (0x7D10, 0),  # East Asian ideograph
    0x6F5C74: (0xD587, 0),  # Korean hangul
    0x6F4D6B: (0xB514, 0),  # Korean hangul
    0x6F5831: (0xC9D3, 0),  # Korean hangul
    0x6F4D6C: (0xB515, 0),  # Korean hangul
    0x6F7641: (0xE8B3, 0),  # Korean hangul
    0x2D4D6D: (0x7792, 0),  # East Asian ideograph
    0x2D3F27: (0x6120, 0),  # East Asian ideograph
    0x69252D: (0x30AD, 0),  # Katakana letter KI
    0x6F4D6E: (0xB51B, 0),  # Korean hangul
    0x4B4C79: (0x7672, 0),  # East Asian ideograph
    0x6F4D6F: (0xB51C, 0),  # Korean hangul
    0x4C4C35: (0x6E0C, 0),  # East Asian ideograph
    0x6F5C75: (0xD588, 0),  # Korean hangul
    0x234D70: (0x97AE, 0),  # East Asian ideograph
    0x6F5832: (0xC9D5, 0),  # Korean hangul
    0x234D71: (0x97A8, 0),  # East Asian ideograph
    0x334A58: (0x89DD, 0),  # East Asian ideograph
    0x6F4D72: (0xB527, 0),  # Korean hangul
    0x4B537D: (0x9ACC, 0),  # East Asian ideograph
    0x6F592A: (0xCC3D, 0),  # Korean hangul
    0x6F5337: (0xC14B, 0),  # Korean hangul
    0x274D73: (0x4E86, 0),  # East Asian ideograph
    0x224D74: (0x6F9F, 0),  # East Asian ideograph
    0x2D325F: (
        0x50BB,
        0,
    ),  # East Asian ideograph (variant of 4B325F which maps to 50BB)
    0x6F4D75: (0xB52A, 0),  # Korean hangul
    0x6F5833: (0xC9D6, 0),  # Korean hangul
    0x29416A: (0x948D, 0),  # East Asian ideograph
    0x22465A: (0x6C18, 0),  # East Asian ideograph
    0x2D3821: (0x962F, 0),  # East Asian ideograph
    0x6F5274: (0xC0D9, 0),  # Korean hangul
    0x213822: (0x5747, 0),  # East Asian ideograph
    0x39447D: (0x6AC2, 0),  # East Asian ideograph
    0x234D78: (0x97A5, 0),  # East Asian ideograph
    0x2D4D21: (0x7681, 0),  # East Asian ideograph
    0x6F4D79: (0xB531, 0),  # Korean hangul
    0x287360: (0x7F2C, 0),  # East Asian ideograph
    0x2F3A5E: (0x8E6E, 0),  # East Asian ideograph
    0x234D7A: (0x97B2, 0),  # East Asian ideograph
    0x2D5836: (0x89E6, 0),  # East Asian ideograph
    0x6F5834: (0xC9D9, 0),  # Korean hangul
    0x22465B: (0x6C19, 0),  # East Asian ideograph
    0x216032: (0x7AE0, 0),  # East Asian ideograph
    0x4B372C: (0x5606, 0),  # East Asian ideograph
    0x234D7C: (0x97B4, 0),  # East Asian ideograph
    0x213827: (0x5783, 0),  # East Asian ideograph
    0x224D7D: (0x6FBC, 0),  # East Asian ideograph
    0x213828: (0x576A, 0),  # East Asian ideograph
    0x235B67: (0x9DAA, 0),  # East Asian ideograph
    0x4B3773: (0x56E3, 0),  # East Asian ideograph
    0x213829: (0x5769, 0),  # East Asian ideograph
    0x34782A: (0x90C5, 0),  # East Asian ideograph
    0x284D49: (0x6DA0, 0),  # East Asian ideograph
    0x213F35: (0x6162, 0),  # East Asian ideograph
    0x21382B: (0x5761, 0),  # East Asian ideograph
    0x4B5946: (0x8A33, 0),  # East Asian ideograph
    0x21382C: (0x5764, 0),  # East Asian ideograph
    0x27383E: (0x57A9, 0),  # East Asian ideograph
    0x6F586C: (0xCB59, 0),  # Korean hangul
    0x6F543D: (0xC31C, 0),  # Korean hangul
    0x4B382E: (0x57C0, 0),  # East Asian ideograph
    0x23382F: (0x8DA1, 0),  # East Asian ideograph
    0x693C32: (0x9D2B, 0),  # East Asian ideograph
    0x215121: (0x7D17, 0),  # East Asian ideograph
    0x215122: (
        0x7D0D,
        0,
    ),  # East Asian ideograph (variant of 455122 which maps to 7D0D)
    0x215123: (0x7D1A, 0),  # East Asian ideograph
    0x215124: (0x7D19, 0),  # East Asian ideograph
    0x215125: (0x7D1B, 0),  # East Asian ideograph
    0x215126: (0x7D46, 0),  # East Asian ideograph
    0x213831: (0x578B, 0),  # East Asian ideograph
    0x215128: (0x7D3C, 0),  # East Asian ideograph
    0x215129: (0x7D2E, 0),  # East Asian ideograph
    0x21512A: (0x7D39, 0),  # East Asian ideograph
    0x27512B: (0x7EC4, 0),  # East Asian ideograph
    0x21512C: (0x7D30, 0),  # East Asian ideograph
    0x21512D: (0x7D33, 0),  # East Asian ideograph
    0x21512E: (0x7D2F, 0),  # East Asian ideograph
    0x27512F: (0x7ECC, 0),  # East Asian ideograph
    0x275130: (0x7EC8, 0),  # East Asian ideograph
    0x275131: (0x7EDF, 0),  # East Asian ideograph
    0x275132: (0x7EDE, 0),  # East Asian ideograph
    0x215133: (0x7D68, 0),  # East Asian ideograph
    0x275134: (0x7ED3, 0),  # East Asian ideograph
    0x215135: (0x7D2B, 0),  # East Asian ideograph
    0x215136: (0x7D62, 0),  # East Asian ideograph
    0x215137: (0x7D76, 0),  # East Asian ideograph
    0x215138: (0x7D61, 0),  # East Asian ideograph
    0x275139: (0x7ED9, 0),  # East Asian ideograph
    0x21513A: (0x7D6E, 0),  # East Asian ideograph
    0x21513B: (0x7D72, 0),  # East Asian ideograph
    0x27513C: (0x7ECF, 0),  # East Asian ideograph
    0x21513D: (0x7D91, 0),  # East Asian ideograph
    0x21513E: (0x7D79, 0),  # East Asian ideograph
    0x21513F: (0x7D8F, 0),  # East Asian ideograph
    0x275140: (0x7ED1, 0),  # East Asian ideograph
    0x275141: (0x7EFC, 0),  # East Asian ideograph
    0x225142: (0x70F7, 0),  # East Asian ideograph
    0x215143: (0x7DB0, 0),  # East Asian ideograph
    0x275144: (0x7D27, 0),  # East Asian ideograph
    0x275145: (0x7EEB, 0),  # East Asian ideograph
    0x275146: (0x7F00, 0),  # East Asian ideograph
    0x215147: (0x7DBA, 0),  # East Asian ideograph
    0x275148: (0x7F51, 0),  # East Asian ideograph
    0x275149: (0x7EB2, 0),  # East Asian ideograph
    0x22514A: (0x7110, 0),  # East Asian ideograph
    0x21514B: (0x7DB5, 0),  # East Asian ideograph
    0x21514C: (0x7DA0, 0),  # East Asian ideograph
    0x27514D: (0x7EF8, 0),  # East Asian ideograph
    0x27514E: (0x7EF4, 0),  # East Asian ideograph
    0x27514F: (0x7EF5, 0),  # East Asian ideograph
    0x275150: (0x7EB6, 0),  # East Asian ideograph
    0x275151: (0x7F01, 0),  # East Asian ideograph
    0x215152: (0x7DE0, 0),  # East Asian ideograph
    0x235153: (0x9933, 0),  # East Asian ideograph
    0x235154: (
        0x9942,
        0,
    ),  # East Asian ideograph (variant of 4D5154 which maps to 9942)
    0x275155: (0x7EEA, 0),  # East Asian ideograph
    0x215156: (0x7DD8, 0),  # East Asian ideograph
    0x275157: (0x7F05, 0),  # East Asian ideograph
    0x275158: (0x7F09, 0),  # East Asian ideograph
    0x275159: (0x7F13, 0),  # East Asian ideograph
    0x27515A: (0x7F18, 0),  # East Asian ideograph
    0x21515B: (0x7DE8, 0),  # East Asian ideograph
    0x21515C: (0x7DDA, 0),  # East Asian ideograph
    0x27515D: (0x7F0D, 0),  # East Asian ideograph
    0x27515E: (0x7F0E, 0),  # East Asian ideograph
    0x27515F: (0x7F23, 0),  # East Asian ideograph
    0x275160: (0x7F22, 0),  # East Asian ideograph
    0x275161: (0x8426, 0),  # East Asian ideograph
    0x275162: (0x7F1A, 0),  # East Asian ideograph
    0x215163: (0x7DFB, 0),  # East Asian ideograph
    0x275164: (
        0x53BF,
        0,
    ),  # East Asian ideograph (variant of 455164 which maps to 53BF)
    0x215165: (0x7E2E, 0),  # East Asian ideograph
    0x215166: (0x7E3E, 0),  # East Asian ideograph
    0x275167: (0x7F2A, 0),  # East Asian ideograph
    0x275168: (0x7F15, 0),  # East Asian ideograph
    0x215169: (0x7E32, 0),  # East Asian ideograph
    0x23516A: (0x9948, 0),  # East Asian ideograph
    0x21516B: (0x7E41, 0),  # East Asian ideograph
    0x23516C: (0x9947, 0),  # East Asian ideograph
    0x23516D: (0x9949, 0),  # East Asian ideograph
    0x21516E: (0x7E31, 0),  # East Asian ideograph
    0x22516F: (0x713F, 0),  # East Asian ideograph
    0x235170: (0x9943, 0),  # East Asian ideograph
    0x275171: (0x7EC7, 0),  # East Asian ideograph
    0x215172: (0x7E61, 0),  # East Asian ideograph
    0x235173: (0x994E, 0),  # East Asian ideograph
    0x235174: (0x9950, 0),  # East Asian ideograph
    0x215175: (0x7E6B, 0),  # East Asian ideograph
    0x215176: (0x7E69, 0),  # East Asian ideograph
    0x215177: (0x7E6D, 0),  # East Asian ideograph
    0x215178: (0x7E79, 0),  # East Asian ideograph
    0x215179: (0x7E6A, 0),  # East Asian ideograph
    0x21517A: (0x8FAE, 0),  # East Asian ideograph
    0x27517B: (0x7F24, 0),  # East Asian ideograph
    0x21517C: (0x7E82, 0),  # East Asian ideograph
    0x21517D: (0x7E7C, 0),  # East Asian ideograph
    0x21517E: (0x7E8F, 0),  # East Asian ideograph
    0x6F5947: (0xCCE4, 0),  # Korean hangul
    0x227841: (0x80EF, 0),  # East Asian ideograph
    0x217144: (0x5581, 0),  # East Asian ideograph
    0x4B3774: (0x56F3, 0),  # East Asian ideograph
    0x235729: (0x9B8E, 0),  # East Asian ideograph
    0x287321: (0x7F26, 0),  # East Asian ideograph
    0x6F5C7D: (0xD5D2, 0),  # Korean hangul
    0x6F583A: (0xC9E0, 0),  # Korean hangul
    0x216038: (0x9802, 0),  # East Asian ideograph
    0x213844: (0x5831, 0),  # East Asian ideograph
    0x4B594B: (0x5909, 0),  # East Asian ideograph
    0x6F5D72: (0xD763, 0),  # Korean hangul
    0x4C3B31: (0x6798, 0),  # East Asian ideograph
    0x213845: (0x582F, 0),  # East Asian ideograph
    0x213A30: (0x5ABC, 0),  # East Asian ideograph
    0x6F5C7E: (0xD5D8, 0),  # Korean hangul
    0x213848: (0x5830, 0),  # East Asian ideograph
    0x274638: (0x6B7C, 0),  # East Asian ideograph
    0x213849: (0x5824, 0),  # East Asian ideograph
    0x21384A: (0x5834, 0),  # East Asian ideograph
    0x21784B: (0x58C6, 0),  # East Asian ideograph
    0x394042: (0x646D, 0),  # East Asian ideograph
    0x284B28: (0x6D48, 0),  # East Asian ideograph
    0x22384C: (0x665E, 0),  # East Asian ideograph
    0x69525D: (0x53FA, 0),  # East Asian ideograph
    0x705D46: (0x841C, 0),  # East Asian ideograph
    0x27384D: (0x6D82, 0),  # East Asian ideograph
    0x21603A: (0x9805, 0),  # East Asian ideograph
    0x234A62: (0x967E, 0),  # East Asian ideograph
    0x213158: (0x4FD1, 0),  # East Asian ideograph
    0x223850: (0x667E, 0),  # East Asian ideograph
    0x21387C: (0x5919, 0),  # East Asian ideograph
    0x213851: (0x584C, 0),  # East Asian ideograph
    0x213852: (0x585A, 0),  # East Asian ideograph
    0x213853: (0x586D, 0),  # East Asian ideograph
    0x6F5276: (0xC0DC, 0),  # Korean hangul
    0x217854: (0x58D2, 0),  # East Asian ideograph
    0x213855: (0x5862, 0),  # East Asian ideograph
    0x335B70: (0x5EF8, 0),  # East Asian ideograph
    0x213F4E: (0x61C7, 0),  # East Asian ideograph
    0x273856: (0x5757, 0),  # East Asian ideograph
    0x6F4E33: (0xB5A8, 0),  # Korean hangul
    0x6F583E: (0xC9E7, 0),  # Korean hangul
    0x22687E: (0x7A2D, 0),  # East Asian ideograph
    0x4B3B79: (0x5D8C, 0),  # East Asian ideograph
    0x217428: (0x5704, 0),  # East Asian ideograph
    0x334621: (0x8B99, 0),  # East Asian ideograph
    0x233859: (0x8DAF, 0),  # East Asian ideograph
    0x21385A: (0x588A, 0),  # East Asian ideograph
    0x215221: (0x7E8C, 0),  # East Asian ideograph
    0x275222: (0x7F28, 0),  # East Asian ideograph
    0x215223: (0x7E96, 0),  # East Asian ideograph
    0x215224: (0x7E9C, 0),  # East Asian ideograph
    0x6F5225: (0xBE75, 0),  # Korean hangul
    0x215226: (0x7F38, 0),  # East Asian ideograph
    0x215227: (0x7F3A, 0),  # East Asian ideograph
    0x225228: (0x7135, 0),  # East Asian ideograph
    0x235229: (0x995D, 0),  # East Asian ideograph
    0x6F522A: (0xBE84, 0),  # Korean hangul
    0x21522B: (0x7F50, 0),  # East Asian ideograph
    0x21522C: (0x7F55, 0),  # East Asian ideograph
    0x21522D: (0x7F54, 0),  # East Asian ideograph
    0x21522E: (0x7F5F, 0),  # East Asian ideograph
    0x21522F: (0x7F72, 0),  # East Asian ideograph
    0x215230: (0x7F6E, 0),  # East Asian ideograph
    0x224223: (0x6A89, 0),  # East Asian ideograph
    0x215232: (0x7F6A, 0),  # East Asian ideograph
    0x215233: (0x7F70, 0),  # East Asian ideograph
    0x215234: (0x7F75, 0),  # East Asian ideograph
    0x215235: (0x7F77, 0),  # East Asian ideograph
    0x215236: (0x7F79, 0),  # East Asian ideograph
    0x215237: (0x7F85, 0),  # East Asian ideograph
    0x275238: (0x7F81, 0),  # East Asian ideograph
    0x215239: (0x7F8A, 0),  # East Asian ideograph
    0x21523A: (0x7F8C, 0),  # East Asian ideograph
    0x21523B: (0x7F8E, 0),  # East Asian ideograph
    0x21523C: (0x7F94, 0),  # East Asian ideograph
    0x21523D: (0x7F9E, 0),  # East Asian ideograph
    0x21523E: (0x7F9A, 0),  # East Asian ideograph
    0x21523F: (0x5584, 0),  # East Asian ideograph
    0x215240: (0x7FA8, 0),  # East Asian ideograph
    0x215241: (0x7FA4, 0),  # East Asian ideograph
    0x235242: (0x99AA, 0),  # East Asian ideograph
    0x215243: (0x7FAF, 0),  # East Asian ideograph
    0x215244: (0x7FB2, 0),  # East Asian ideograph
    0x215245: (0x7FB6, 0),  # East Asian ideograph
    0x215246: (0x7FB8, 0),  # East Asian ideograph
    0x215247: (0x7FB9, 0),  # East Asian ideograph
    0x215248: (0x7FBD, 0),  # East Asian ideograph
    0x235249: (0x99B5, 0),  # East Asian ideograph
    0x21524A: (0x7FC5, 0),  # East Asian ideograph
    0x21524B: (0x7FC1, 0),  # East Asian ideograph
    0x21524C: (0x7FCC, 0),  # East Asian ideograph
    0x21524D: (0x7FD2, 0),  # East Asian ideograph
    0x21524E: (
        0x7FCE,
        0,
    ),  # East Asian ideograph (variant of 4B524E which maps to 7FCE)
    0x21524F: (0x7FD4, 0),  # East Asian ideograph
    0x215250: (0x7FD5, 0),  # East Asian ideograph
    0x215251: (0x7FE0, 0),  # East Asian ideograph
    0x215252: (0x7FE1, 0),  # East Asian ideograph
    0x215253: (0x7FDF, 0),  # East Asian ideograph
    0x235254: (0x99BD, 0),  # East Asian ideograph
    0x215255: (0x7FF0, 0),  # East Asian ideograph
    0x215256: (0x7FF3, 0),  # East Asian ideograph
    0x215257: (0x7FFC, 0),  # East Asian ideograph
    0x215258: (0x7FF9, 0),  # East Asian ideograph
    0x215259: (0x7FFB, 0),  # East Asian ideograph
    0x21525A: (0x7FF1, 0),  # East Asian ideograph
    0x21525B: (0x8000, 0),  # East Asian ideograph
    0x22525C: (0x7143, 0),  # East Asian ideograph
    0x21525D: (0x8003, 0),  # East Asian ideograph
    0x21525E: (0x8006, 0),  # East Asian ideograph
    0x21525F: (0x8005, 0),  # East Asian ideograph
    0x215260: (0x800C, 0),  # East Asian ideograph
    0x215261: (0x8010, 0),  # East Asian ideograph
    0x215262: (0x800D, 0),  # East Asian ideograph
    0x215263: (0x8012, 0),  # East Asian ideograph
    0x215264: (0x8015, 0),  # East Asian ideograph
    0x215265: (0x8018, 0),  # East Asian ideograph
    0x215266: (0x8019, 0),  # East Asian ideograph
    0x215267: (0x8017, 0),  # East Asian ideograph
    0x215268: (0x801C, 0),  # East Asian ideograph
    0x235269: (0x99D8, 0),  # East Asian ideograph
    0x21526A: (0x8036, 0),  # East Asian ideograph
    0x21526B: (0x803F, 0),  # East Asian ideograph
    0x21526C: (0x803D, 0),  # East Asian ideograph
    0x21526D: (0x804A, 0),  # East Asian ideograph
    0x21526E: (0x8046, 0),  # East Asian ideograph
    0x21526F: (0x8056, 0),  # East Asian ideograph
    0x215270: (0x8058, 0),  # East Asian ideograph
    0x215271: (0x805E, 0),  # East Asian ideograph
    0x215272: (0x805A, 0),  # East Asian ideograph
    0x215273: (0x8071, 0),  # East Asian ideograph
    0x215274: (0x8072, 0),  # East Asian ideograph
    0x215275: (0x8073, 0),  # East Asian ideograph
    0x215276: (0x8070, 0),  # East Asian ideograph
    0x215277: (0x806F, 0),  # East Asian ideograph
    0x215278: (0x8077, 0),  # East Asian ideograph
    0x275279: (0x8042, 0),  # East Asian ideograph
    0x23527A: (0x99F0, 0),  # East Asian ideograph
    0x27527B: (0x542C, 0),  # East Asian ideograph
    0x21527C: (0x807F, 0),  # East Asian ideograph
    0x6F527C: (0xC0F4, 0),  # Korean hangul
    0x21527E: (0x8084, 0),  # East Asian ideograph
    0x21386B: (0x58D9, 0),  # East Asian ideograph
    0x6F5842: (0xC9F0, 0),  # Korean hangul
    0x27386C: (0x5792, 0),  # East Asian ideograph
    0x6F5A23: (0xCEAD, 0),  # Korean hangul
    0x21386D: (0x58DF, 0),  # East Asian ideograph
    0x27386E: (0x574F, 0),  # East Asian ideograph
    0x4B3850: (0x5861, 0),  # East Asian ideograph (variant of 213850)
    0x23395C: (0x8E1E, 0),  # East Asian ideograph
    0x235732: (0x9B98, 0),  # East Asian ideograph
    0x6F4E34: (0xB5AB, 0),  # Korean hangul
    0x213870: (0x58E4, 0),  # East Asian ideograph
    0x276065: (0x9965, 0),  # East Asian ideograph
    0x4B3B7E: (0x5D15, 0),  # East Asian ideograph
    0x273871: (0x575D, 0),  # East Asian ideograph
    0x6F5D76: (0xD770, 0),  # Korean hangul
    0x223872: (0x6693, 0),  # East Asian ideograph
    0x233873: (0x8DBF, 0),  # East Asian ideograph
    0x273874: (0x58EE, 0),  # East Asian ideograph
    0x343875: (0x5FDE, 0),  # East Asian ideograph
    0x284D58: (0x6CA9, 0),  # East Asian ideograph
    0x705C43: (0x82CA, 0),  # East Asian ideograph
    0x223876: (0x6690, 0),  # East Asian ideograph
    0x276321: (0x9F7F, 0),  # East Asian ideograph
    0x213877: (0x58FD, 0),  # East Asian ideograph
    0x276322: (0x9F83, 0),  # East Asian ideograph
    0x4D5D49: (0x9E81, 0),  # East Asian ideograph
    0x226323: (0x77B6, 0),  # East Asian ideograph
    0x213879: (0x5914, 0),  # East Asian ideograph
    0x276324: (0x9F84, 0),  # East Asian ideograph
    0x2E765F: (0x8037, 0),  # East Asian ideograph
    0x21387A: (0x5915, 0),  # East Asian ideograph
    0x284D59: (0x6ED7, 0),  # East Asian ideograph
    0x276325: (0x9F88, 0),  # East Asian ideograph
    0x6F542C: (0xC2F1, 0),  # Korean hangul
    0x213E2A: (
        0x6035,
        0,
    ),  # East Asian ideograph (variant of 4B3E2A which maps to 6035)
    0x6F5675: (0xC78A, 0),  # Korean hangul
    0x276326: (0x9F87, 0),  # East Asian ideograph
    0x22787C: (0x8153, 0),  # East Asian ideograph
    0x216327: (0x9F6C, 0),  # East Asian ideograph
    0x21387D: (0x591A, 0),  # East Asian ideograph
    0x276328: (0x9F8A, 0),  # East Asian ideograph
    0x2D517D: (0x7D99, 0),  # East Asian ideograph
    0x4B484A: (0x6E13, 0),  # East Asian ideograph
    0x2D3272: (0x706E, 0),  # East Asian ideograph
    0x232329: (0x845C, 0),  # East Asian ideograph
    0x6F5846: (0xC9FC, 0),  # Korean hangul
    0x27632A: (0x9F8B, 0),  # East Asian ideograph
    0x234A6C: (0x9689, 0),  # East Asian ideograph
    0x22632B: (0x77B9, 0),  # East Asian ideograph
    0x453051: (0x8D30, 0),  # East Asian ideograph
    0x6F4B7D: (0xB124, 0),  # Korean hangul
    0x21632C: (0x9F94, 0),  # East Asian ideograph
    0x27632D: (0x9F9F, 0),  # East Asian ideograph
    0x4B484B: (0x51D6, 0),  # East Asian ideograph
    0x235736: (0x9B9F, 0),  # East Asian ideograph
    0x6F5847: (0xCA00, 0),  # Korean hangul
    0x6F5427: (0xC2E4, 0),  # Korean hangul
    0x275321: (0x8083, 0),  # East Asian ideograph
    0x215322: (0x8087, 0),  # East Asian ideograph
    0x215323: (0x8089, 0),  # East Asian ideograph
    0x235324: (0x9A02, 0),  # East Asian ideograph
    0x215325: (0x808C, 0),  # East Asian ideograph
    0x215326: (0x8093, 0),  # East Asian ideograph
    0x215327: (0x809D, 0),  # East Asian ideograph
    0x215328: (0x8098, 0),  # East Asian ideograph
    0x215329: (0x809B, 0),  # East Asian ideograph
    0x21532A: (0x809A, 0),  # East Asian ideograph
    0x22532B: (0x7180, 0),  # East Asian ideograph
    0x22532C: (0x7189, 0),  # East Asian ideograph
    0x21532D: (0x80AA, 0),  # East Asian ideograph
    0x21532E: (0x80BA, 0),  # East Asian ideograph
    0x21532F: (0x80A5, 0),  # East Asian ideograph
    0x235330: (0x99FB, 0),  # East Asian ideograph
    0x235331: (0x99FD, 0),  # East Asian ideograph
    0x215332: (0x80B1, 0),  # East Asian ideograph
    0x225333: (0x7196, 0),  # East Asian ideograph
    0x215334: (0x80A1, 0),  # East Asian ideograph
    0x215335: (0x80A9, 0),  # East Asian ideograph
    0x27495D: (0x4E4C, 0),  # East Asian ideograph
    0x215337: (0x80D6, 0),  # East Asian ideograph
    0x215338: (0x80CC, 0),  # East Asian ideograph
    0x215339: (0x80E5, 0),  # East Asian ideograph
    0x21533A: (0x80DA, 0),  # East Asian ideograph
    0x21533B: (0x80E1, 0),  # East Asian ideograph
    0x21533C: (0x80C3, 0),  # East Asian ideograph
    0x21533D: (0x80DB, 0),  # East Asian ideograph
    0x21533E: (0x80C4, 0),  # East Asian ideograph
    0x21533F: (0x80CE, 0),  # East Asian ideograph
    0x215340: (0x80DE, 0),  # East Asian ideograph
    0x215341: (0x80E4, 0),  # East Asian ideograph
    0x215342: (0x80F0, 0),  # East Asian ideograph
    0x215343: (0x8102, 0),  # East Asian ideograph
    0x215344: (0x8105, 0),  # East Asian ideograph
    0x215345: (0x80F1, 0),  # East Asian ideograph
    0x215346: (0x80F4, 0),  # East Asian ideograph
    0x215347: (0x80ED, 0),  # East Asian ideograph
    0x235348: (0x9A10, 0),  # East Asian ideograph
    0x215349: (0x8106, 0),  # East Asian ideograph
    0x21534A: (0x80F3, 0),  # East Asian ideograph
    0x21534B: (0x80F8, 0),  # East Asian ideograph
    0x23534C: (0x9A24, 0),  # East Asian ideograph
    0x21534D: (0x8108, 0),  # East Asian ideograph
    0x21534E: (0x812B, 0),  # East Asian ideograph
    0x21534F: (0x812F, 0),  # East Asian ideograph
    0x215350: (0x8116, 0),  # East Asian ideograph
    0x225351: (0x71A4, 0),  # East Asian ideograph
    0x215352: (0x8129, 0),  # East Asian ideograph
    0x215353: (0x8155, 0),  # East Asian ideograph
    0x215354: (0x8154, 0),  # East Asian ideograph
    0x215355: (0x814B, 0),  # East Asian ideograph
    0x215356: (0x8151, 0),  # East Asian ideograph
    0x215357: (0x8150, 0),  # East Asian ideograph
    0x215358: (0x814E, 0),  # East Asian ideograph
    0x275359: (0x80C0, 0),  # East Asian ideograph
    0x21535A: (0x8146, 0),  # East Asian ideograph
    0x21535B: (0x813E, 0),  # East Asian ideograph
    0x21535C: (0x8171, 0),  # East Asian ideograph
    0x21535D: (0x8170, 0),  # East Asian ideograph
    0x21535E: (0x8178, 0),  # East Asian ideograph
    0x21535F: (0x8165, 0),  # East Asian ideograph
    0x215360: (0x816E, 0),  # East Asian ideograph
    0x215361: (0x8173, 0),  # East Asian ideograph
    0x275362: (0x80BF, 0),  # East Asian ideograph
    0x215363: (0x8179, 0),  # East Asian ideograph
    0x215364: (0x817A, 0),  # East Asian ideograph
    0x215365: (0x8166, 0),  # East Asian ideograph
    0x215366: (0x8180, 0),  # East Asian ideograph
    0x225367: (0x71D1, 0),  # East Asian ideograph
    0x215368: (0x817F, 0),  # East Asian ideograph
    0x215369: (0x818A, 0),  # East Asian ideograph
    0x21536A: (0x8188, 0),  # East Asian ideograph
    0x21536B: (0x819D, 0),  # East Asian ideograph
    0x21536C: (0x81A0, 0),  # East Asian ideograph
    0x22536D: (0x71CA, 0),  # East Asian ideograph
    0x21536E: (0x819A, 0),  # East Asian ideograph
    0x21536F: (0x819C, 0),  # East Asian ideograph
    0x215370: (0x81B3, 0),  # East Asian ideograph
    0x275371: (0x817B, 0),  # East Asian ideograph
    0x215372: (0x81A8, 0),  # East Asian ideograph
    0x215373: (0x81C6, 0),  # East Asian ideograph
    0x215374: (0x81BA, 0),  # East Asian ideograph
    0x215375: (0x81C3, 0),  # East Asian ideograph
    0x215376: (0x81C0, 0),  # East Asian ideograph
    0x215377: (0x81C2, 0),  # East Asian ideograph
    0x275378: (0x8113, 0),  # East Asian ideograph
    0x275379: (0x80C6, 0),  # East Asian ideograph
    0x27537A: (0x8138, 0),  # East Asian ideograph
    0x27537B: (0x810D, 0),  # East Asian ideograph
    0x21537C: (0x81CD, 0),  # East Asian ideograph
    0x27537D: (0x8191, 0),  # East Asian ideograph
    0x27537E: (0x814A, 0),  # East Asian ideograph
    0x234156: (0x91BF, 0),  # East Asian ideograph
    0x276B79: (0x523F, 0),  # East Asian ideograph
    0x6F584B: (0xCA0C, 0),  # Korean hangul
    0x2D3B3F: (0x5C02, 0),  # East Asian ideograph
    0x21313B: (0x4F43, 0),  # East Asian ideograph
    0x2D615A: (0x8EC6, 0),  # East Asian ideograph
    0x6F2526: (0x3161, 0),  # Korean hangul
    0x276B7A: (0x523D, 0),  # East Asian ideograph
    0x6F584C: (0xCA0D, 0),  # Korean hangul
    0x69543A: (0x57AA, 0),  # East Asian ideograph
    0x232349: (0x8497, 0),  # East Asian ideograph
    0x6F5279: (0xC0E5, 0),  # Korean hangul
    0x274C33: (0x6BD5, 0),  # East Asian ideograph
    0x213168: (0x4FC4, 0),  # East Asian ideograph
    0x22234B: (0x5C8D, 0),  # East Asian ideograph
    0x213F51: (0x61E3, 0),  # East Asian ideograph
    0x2D3279: (0x514E, 0),  # East Asian ideograph
    0x6F4E36: (0xB5B1, 0),  # Korean hangul
    0x6F2471: (0x3149, 0),  # Korean hangul
    0x6F584D: (0xCA18, 0),  # Korean hangul
    0x224674: (0x6C3F, 0),  # East Asian ideograph
    0x6F4929: (0xAC80, 0),  # Korean hangul
    0x6F5164: (0xBDD4, 0),  # Korean hangul
    0x217E21: (0x5B5B, 0),  # East Asian ideograph
    0x213169: (0x4FC2, 0),  # East Asian ideograph
    0x217158: (0x55CC, 0),  # East Asian ideograph
    0x233967: (0x8E27, 0),  # East Asian ideograph
    0x4B594A: (0x8AAD, 0),  # East Asian ideograph
    0x6F5158: (0xBD80, 0),  # Korean hangul
    0x6F584E: (0xCA4C, 0),  # Korean hangul
    0x6F7721: (0xAD35, 0),  # Korean hangul
    0x213E33: (0x6025, 0),  # East Asian ideograph
    0x295A28: (0x9E28, 0),  # East Asian ideograph
    0x2D4B72: (0x7506, 0),  # East Asian ideograph
    0x6F584F: (0xCA4D, 0),  # Korean hangul
    0x232358: (0x84B9, 0),  # East Asian ideograph
    0x347431: (0x58DC, 0),  # East Asian ideograph
    0x21715A: (0x55DB, 0),  # East Asian ideograph
    0x233969: (0x8E18, 0),  # East Asian ideograph
    0x215421: (0x81DA, 0),  # East Asian ideograph
    0x235422: (0x9A4D, 0),  # East Asian ideograph
    0x215423: (0x81E3, 0),  # East Asian ideograph
    0x235424: (0x9A52, 0),  # East Asian ideograph
    0x275425: (0x4E34, 0),  # East Asian ideograph
    0x215426: (0x81EA, 0),  # East Asian ideograph
    0x215427: (0x81EC, 0),  # East Asian ideograph
    0x215428: (0x81ED, 0),  # East Asian ideograph
    0x215429: (0x81F3, 0),  # East Asian ideograph
    0x22542A: (0x71DE, 0),  # East Asian ideograph
    0x21542B: (0x81FA, 0),  # East Asian ideograph
    0x21542C: (0x81FB, 0),  # East Asian ideograph
    0x21542D: (0x81FC, 0),  # East Asian ideograph
    0x21542E: (0x81FE, 0),  # East Asian ideograph
    0x21542F: (0x8200, 0),  # East Asian ideograph
    0x215430: (0x8202, 0),  # East Asian ideograph
    0x215431: (0x8205, 0),  # East Asian ideograph
    0x215432: (0x8207, 0),  # East Asian ideograph
    0x275433: (0x5174, 0),  # East Asian ideograph
    0x275434: (0x4E3E, 0),  # East Asian ideograph
    0x215435: (0x820A, 0),  # East Asian ideograph
    0x215436: (0x820C, 0),  # East Asian ideograph
    0x215437: (0x820D, 0),  # East Asian ideograph
    0x215438: (0x8210, 0),  # East Asian ideograph
    0x215439: (0x8212, 0),  # East Asian ideograph
    0x23543A: (0x9A6B, 0),  # East Asian ideograph
    0x21543B: (0x821B, 0),  # East Asian ideograph
    0x21543C: (0x821C, 0),  # East Asian ideograph
    0x21543D: (0x821E, 0),  # East Asian ideograph
    0x21543E: (0x821F, 0),  # East Asian ideograph
    0x21543F: (0x8222, 0),  # East Asian ideograph
    0x215440: (0x822A, 0),  # East Asian ideograph
    0x235441: (0x9AAB, 0),  # East Asian ideograph
    0x215442: (0x822C, 0),  # East Asian ideograph
    0x215443: (0x8228, 0),  # East Asian ideograph
    0x215444: (0x8237, 0),  # East Asian ideograph
    0x215445: (0x8235, 0),  # East Asian ideograph
    0x215446: (0x8239, 0),  # East Asian ideograph
    0x215447: (0x8236, 0),  # East Asian ideograph
    0x215448: (0x8247, 0),  # East Asian ideograph
    0x215449: (0x8258, 0),  # East Asian ideograph
    0x21544A: (0x8259, 0),  # East Asian ideograph
    0x21544B: (0x8266, 0),  # East Asian ideograph
    0x21544C: (0x826E, 0),  # East Asian ideograph
    0x21544D: (0x826F, 0),  # East Asian ideograph
    0x21544E: (0x8271, 0),  # East Asian ideograph
    0x21544F: (0x8272, 0),  # East Asian ideograph
    0x215450: (0x827E, 0),  # East Asian ideograph
    0x215451: (0x8292, 0),  # East Asian ideograph
    0x215452: (0x828B, 0),  # East Asian ideograph
    0x215453: (0x828D, 0),  # East Asian ideograph
    0x215454: (0x82B3, 0),  # East Asian ideograph
    0x215455: (0x829D, 0),  # East Asian ideograph
    0x215456: (0x8299, 0),  # East Asian ideograph
    0x215457: (0x82BD, 0),  # East Asian ideograph
    0x215458: (0x82AD, 0),  # East Asian ideograph
    0x215459: (0x82AC, 0),  # East Asian ideograph
    0x21545A: (0x82A5, 0),  # East Asian ideograph
    0x21545B: (0x829F, 0),  # East Asian ideograph
    0x27545C: (0x520D, 0),  # East Asian ideograph
    0x21545D: (0x82B1, 0),  # East Asian ideograph
    0x21545E: (0x82B9, 0),  # East Asian ideograph
    0x69545F: (0x58E5, 0),  # East Asian ideograph
    0x215460: (0x82E7, 0),  # East Asian ideograph
    0x215461: (0x8305, 0),  # East Asian ideograph
    0x215462: (0x8309, 0),  # East Asian ideograph
    0x215463: (0x82E3, 0),  # East Asian ideograph
    0x215464: (0x82DB, 0),  # East Asian ideograph
    0x215465: (0x82E6, 0),  # East Asian ideograph
    0x215466: (0x8304, 0),  # East Asian ideograph
    0x215467: (0x82E5, 0),  # East Asian ideograph
    0x215468: (0x8302, 0),  # East Asian ideograph
    0x215469: (0x82DC, 0),  # East Asian ideograph
    0x21546A: (0x82D7, 0),  # East Asian ideograph
    0x21546B: (0x82F1, 0),  # East Asian ideograph
    0x21546C: (0x8301, 0),  # East Asian ideograph
    0x23546D: (0x9AD6, 0),  # East Asian ideograph
    0x21546E: (0x82D4, 0),  # East Asian ideograph
    0x21546F: (0x82D1, 0),  # East Asian ideograph
    0x215470: (0x82DE, 0),  # East Asian ideograph
    0x215471: (0x82DF, 0),  # East Asian ideograph
    0x215472: (0x832B, 0),  # East Asian ideograph
    0x215473: (0x8352, 0),  # East Asian ideograph
    0x235474: (0x9ADF, 0),  # East Asian ideograph
    0x215475: (0x8338, 0),  # East Asian ideograph
    0x215476: (0x8354, 0),  # East Asian ideograph
    0x235477: (0x9AE2, 0),  # East Asian ideograph
    0x215478: (0x8349, 0),  # East Asian ideograph
    0x215479: (0x8335, 0),  # East Asian ideograph
    0x21547A: (0x8334, 0),  # East Asian ideograph
    0x21547B: (0x8336, 0),  # East Asian ideograph
    0x21547C: (0x8331, 0),  # East Asian ideograph
    0x21547D: (0x8340, 0),  # East Asian ideograph
    0x21547E: (0x8317, 0),  # East Asian ideograph
    0x6F5853: (0xCA5D, 0),  # Korean hangul
    0x295166: (0x9969, 0),  # East Asian ideograph
    0x234A79: (0x9696, 0),  # East Asian ideograph
    0x226450: (0x7826, 0),  # East Asian ideograph
    0x6F5D73: (0xD765, 0),  # Korean hangul
    0x6F4B35: (0xB014, 0),  # Korean hangul
    0x2D6162: (0x9A0C, 0),  # East Asian ideograph
    0x6F5872: (0xCBE7, 0),  # Korean hangul
    0x21316F: (0x4FEF, 0),  # East Asian ideograph
    0x4B4858: (0x6E80, 0),  # East Asian ideograph
    0x6F5854: (0xCA61, 0),  # Korean hangul
    0x222370: (0x5CD5, 0),  # East Asian ideograph
    0x22467B: (0x6C62, 0),  # East Asian ideograph
    0x213E39: (0x6063, 0),  # East Asian ideograph
    0x6F7648: (0xE8BA, 0),  # Korean hangul
    0x4B374C: (0x5662, 0),  # East Asian ideograph
    0x29594F: (0x9CE2, 0),  # East Asian ideograph
    0x696373: (0x7B02, 0),  # East Asian ideograph
    0x295A70: (0x9E48, 0),  # East Asian ideograph
    0x6F5364: (0xC22F, 0),  # Korean hangul
    0x27496A: (0x70BC, 0),  # East Asian ideograph
    0x6F5855: (0xCA84, 0),  # Korean hangul
    0x292375: (0x83B3, 0),  # East Asian ideograph
    0x22467C: (0x6C4A, 0),  # East Asian ideograph
    0x224E21: (0x6FAA, 0),  # East Asian ideograph
    0x6F4E22: (0xB541, 0),  # Korean hangul
    0x6F4E23: (0xB543, 0),  # Korean hangul
    0x225346: (0x719E, 0),  # East Asian ideograph
    0x222379: (0x5C8D, 0),  # East Asian ideograph (not in Unicode)
    0x234E24: (0x97B3, 0),  # East Asian ideograph
    0x6F5856: (0xCA98, 0),  # Korean hangul
    0x224E25: (0x6FBF, 0),  # East Asian ideograph
    0x6F527B: (0xC0EC, 0),  # Korean hangul
    0x224E26: (0x6FC7, 0),  # East Asian ideograph
    0x275A78: (0x8E52, 0),  # East Asian ideograph
    0x274E27: (0x77EB, 0),  # East Asian ideograph
    0x213172: (0x5025, 0),  # East Asian ideograph
    0x6F4E28: (0xB54D, 0),  # Korean hangul
    0x27574A: (0x51B2, 0),  # East Asian ideograph (duplicate simplified)
    0x227E23: (0x83A6, 0),  # East Asian ideograph
    0x234E29: (0x97B9, 0),  # East Asian ideograph
    0x6F5857: (0xCABC, 0),  # Korean hangul
    0x29516A: (0x9990, 0),  # East Asian ideograph
    0x51356A: (0x8BC3, 0),  # East Asian ideograph
    0x6F4E2B: (0xB55C, 0),  # Korean hangul
    0x6F594D: (0xCD19, 0),  # Korean hangul
    0x6F5D5C: (0xD700, 0),  # Korean hangul
    0x6F4E2C: (0xB55D, 0),  # Korean hangul
    0x213173: (0x5011, 0),  # East Asian ideograph
    0x4B613F: (0x9A08, 0),  # East Asian ideograph
    0x214E2D: (0x65AB, 0),  # East Asian ideograph
    0x224E2E: (0x6F5E, 0),  # East Asian ideograph
    0x6F5858: (0xCABD, 0),  # Korean hangul
    0x6F546A: (0xC4F0, 0),  # Korean hangul
    0x224E2F: (0x6FC8, 0),  # East Asian ideograph
    0x2D5763: (0x88E1, 0),  # East Asian ideograph
    0x235521: (0x9AE7, 0),  # East Asian ideograph
    0x215522: (0x834F, 0),  # East Asian ideograph
    0x215523: (0x8339, 0),  # East Asian ideograph
    0x215524: (0x838E, 0),  # East Asian ideograph
    0x215525: (0x8398, 0),  # East Asian ideograph
    0x215526: (0x839E, 0),  # East Asian ideograph
    0x215527: (0x8378, 0),  # East Asian ideograph
    0x215528: (0x83A2, 0),  # East Asian ideograph
    0x225529: (0x7225, 0),  # East Asian ideograph
    0x22552A: (0x7226, 0),  # East Asian ideograph
    0x21552B: (0x83AB, 0),  # East Asian ideograph
    0x21552C: (
        0x8392,
        0,
    ),  # East Asian ideograph (variant of 4B552C which maps to 8392)
    0x21552D: (0x838A, 0),  # East Asian ideograph
    0x21552E: (0x8393, 0),  # East Asian ideograph
    0x21552F: (0x83A0, 0),  # East Asian ideograph
    0x215530: (0x8389, 0),  # East Asian ideograph
    0x215531: (0x8377, 0),  # East Asian ideograph
    0x215532: (0x837C, 0),  # East Asian ideograph
    0x215533: (0x837B, 0),  # East Asian ideograph
    0x215534: (0x840D, 0),  # East Asian ideograph
    0x215535: (0x83E0, 0),  # East Asian ideograph
    0x215536: (0x83E9, 0),  # East Asian ideograph
    0x6F5537: (0xC57D, 0),  # Korean hangul
    0x215538: (0x8403, 0),  # East Asian ideograph
    0x215539: (0x83C5, 0),  # East Asian ideograph
    0x21553A: (0x83C1, 0),  # East Asian ideograph
    0x21553B: (0x840B, 0),  # East Asian ideograph
    0x21553C: (0x83EF, 0),  # East Asian ideograph
    0x6F553D: (0xC58F, 0),  # Korean hangul
    0x21553E: (0x83F1, 0),  # East Asian ideograph
    0x21553F: (0x83BD, 0),  # East Asian ideograph
    0x6F5540: (0xC595, 0),  # Korean hangul
    0x235541: (0x9B05, 0),  # East Asian ideograph
    0x215542: (0x840C, 0),  # East Asian ideograph
    0x225543: (0x7241, 0),  # East Asian ideograph
    0x215544: (0x83DC, 0),  # East Asian ideograph
    0x215545: (0x83CA, 0),  # East Asian ideograph
    0x215546: (0x83F2, 0),  # East Asian ideograph
    0x215547: (0x840E, 0),  # East Asian ideograph
    0x215548: (0x8404, 0),  # East Asian ideograph
    0x215549: (0x843D, 0),  # East Asian ideograph
    0x21554A: (0x8482, 0),  # East Asian ideograph
    0x21554B: (0x8431, 0),  # East Asian ideograph
    0x21554C: (0x8475, 0),  # East Asian ideograph
    0x21554D: (0x8466, 0),  # East Asian ideograph
    0x21554E: (0x8457, 0),  # East Asian ideograph
    0x22554F: (0x7250, 0),  # East Asian ideograph
    0x215550: (0x846C, 0),  # East Asian ideograph
    0x214E38: (0x7843, 0),  # East Asian ideograph
    0x215552: (0x845B, 0),  # East Asian ideograph
    0x215553: (0x8477, 0),  # East Asian ideograph
    0x215554: (0x843C, 0),  # East Asian ideograph
    0x215555: (0x8435, 0),  # East Asian ideograph
    0x225556: (0x725A, 0),  # East Asian ideograph
    0x215557: (0x8463, 0),  # East Asian ideograph
    0x215558: (0x8469, 0),  # East Asian ideograph
    0x225559: (0x7263, 0),  # East Asian ideograph
    0x21555A: (0x84B2, 0),  # East Asian ideograph
    0x21555B: (0x849E, 0),  # East Asian ideograph
    0x21555C: (0x84BF, 0),  # East Asian ideograph
    0x21555D: (0x84C6, 0),  # East Asian ideograph
    0x21555E: (0x84C4, 0),  # East Asian ideograph
    0x21555F: (0x84C9, 0),  # East Asian ideograph
    0x215560: (0x849C, 0),  # East Asian ideograph
    0x215561: (0x84CB, 0),  # East Asian ideograph
    0x215562: (0x84B8, 0),  # East Asian ideograph
    0x275563: (0x836A, 0),  # East Asian ideograph
    0x275564: (0x82CE, 0),  # East Asian ideograph
    0x215565: (0x84D3, 0),  # East Asian ideograph
    0x225566: (0x7276, 0),  # East Asian ideograph
    0x215567: (0x84BC, 0),  # East Asian ideograph
    0x225568: (0x7277, 0),  # East Asian ideograph
    0x215569: (0x84FF, 0),  # East Asian ideograph
    0x21556A: (0x8517, 0),  # East Asian ideograph
    0x22556B: (0x727E, 0),  # East Asian ideograph
    0x21556C: (0x84EE, 0),  # East Asian ideograph
    0x21556D: (0x852C, 0),  # East Asian ideograph
    0x27556E: (0x836B, 0),  # East Asian ideograph
    0x21556F: (0x8513, 0),  # East Asian ideograph
    0x6F5570: (0xC61B, 0),  # Korean hangul
    0x215571: (0x8523, 0),  # East Asian ideograph
    0x215572: (0x8521, 0),  # East Asian ideograph
    0x275573: (0x535C, 0),  # East Asian ideograph
    0x225574: (0x7289, 0),  # East Asian ideograph
    0x215575: (0x8525, 0),  # East Asian ideograph
    0x235576: (0x9B2F, 0),  # East Asian ideograph
    0x215577: (0x854A, 0),  # East Asian ideograph
    0x215578: (0x8559, 0),  # East Asian ideograph
    0x215579: (0x8548, 0),  # East Asian ideograph
    0x21557A: (0x8568, 0),  # East Asian ideograph
    0x21557B: (0x8543, 0),  # East Asian ideograph
    0x21557C: (0x856A, 0),  # East Asian ideograph
    0x21557D: (0x8549, 0),  # East Asian ideograph
    0x21557E: (0x8584, 0),  # East Asian ideograph
    0x224E40: (0x6FA5, 0),  # East Asian ideograph
    0x224E41: (0x6FB0, 0),  # East Asian ideograph
    0x4B6048: (0x981A, 0),  # East Asian ideograph
    0x224E42: (0x6FAE, 0),  # East Asian ideograph
    0x2F585C: (0x9C51, 0),  # Unrelated variant of EACC 235945 which maps to 9C51
    0x224E43: (0x6FD9, 0),  # East Asian ideograph
    0x276260: (0x4E48, 0),  # East Asian ideograph
    0x21393F: (0x5969, 0),  # East Asian ideograph
    0x224E44: (0x6FDA, 0),  # East Asian ideograph
    0x274E45: (0x7855, 0),  # East Asian ideograph
    0x6F5B3C: (0xD1B0, 0),  # Korean hangul
    0x273422: (0x5218, 0),  # East Asian ideograph
    0x6F4E46: (0xB664, 0),  # Korean hangul
    0x286B7C: (0x7B15, 0),  # East Asian ideograph
    0x22316C: (0x636C, 0),  # East Asian ideograph
    0x6F4E47: (0xB69C, 0),  # Korean hangul
    0x6F585D: (0xCAD1, 0),  # Korean hangul
    0x295170: (0x998D, 0),  # East Asian ideograph
    0x274E49: (0x786E, 0),  # East Asian ideograph
    0x6F4C4C: (0xB220, 0),  # Korean hangul
    0x6F4E4A: (0xB6AB, 0),  # Korean hangul
    0x213179: (0x5006, 0),  # East Asian ideograph
    0x234E4B: (0x97CE, 0),  # East Asian ideograph
    0x2D753A: (0x9654, 0),  # East Asian ideograph
    0x2D5321: (0x7C9B, 0),  # East Asian ideograph
    0x274E4C: (0x7801, 0),  # East Asian ideograph
    0x3F3078: (0x5023, 0),  # East Asian ideograph
    0x6F585E: (0xCAD2, 0),  # Korean hangul
    0x6F4E4D: (0xB6F0, 0),  # Korean hangul
    0x234E4E: (0x97D0, 0),  # East Asian ideograph
    0x4B552C: (0x8392, 0),  # East Asian ideograph
    0x29546D: (0x9ACB, 0),  # East Asian ideograph
    0x333564: (0x5415, 0),  # East Asian ideograph
    0x275154: (0x7EC3, 0),  # East Asian ideograph
    0x224E50: (0x6FD4, 0),  # East Asian ideograph
    0x213930: (0x5949, 0),  # East Asian ideograph
    0x234E51: (0x97D4, 0),  # East Asian ideograph
    0x6F585F: (0xCAD3, 0),  # Korean hangul
    0x295172: (0x9994, 0),  # East Asian ideograph
    0x21605D: (0x98B1, 0),  # East Asian ideograph
    0x213E44: (0x606C, 0),  # East Asian ideograph
    0x274E53: (0x7816, 0),  # East Asian ideograph
    0x234642: (0x93A7, 0),  # East Asian ideograph
    0x234E54: (0x97D9, 0),  # East Asian ideograph
    0x69245C: (0x307C, 0),  # Hiragana letter BO
    0x6F4E55: (0xB72F, 0),  # Korean hangul
    0x224E56: (0x6FE9, 0),  # East Asian ideograph
    0x6F5860: (0xCAD8, 0),  # Korean hangul
    0x224E57: (0x6FF8, 0),  # East Asian ideograph
    0x4B3758: (
        0x56A5,
        0,
    ),  # East Asian ideograph (variant of 213758 which maps to 56A5)
    0x274E58: (0x77F6, 0),  # East Asian ideograph
    0x214E59: (0x790E, 0),  # East Asian ideograph
    0x274E5A: (0x788D, 0),  # East Asian ideograph
    0x2D5C40: (0x5FA8, 0),  # East Asian ideograph
    0x215621: (0x85AA, 0),  # East Asian ideograph
    0x215622: (0x856D, 0),  # East Asian ideograph
    0x235623: (0x9B37, 0),  # East Asian ideograph
    0x275624: (0x59DC, 0),  # East Asian ideograph
    0x215625: (0x857E, 0),  # East Asian ideograph
    0x215626: (0x8594, 0),  # East Asian ideograph
    0x215627: (0x859C, 0),  # East Asian ideograph
    0x225628: (0x728F, 0),  # East Asian ideograph
    0x215629: (
        0x85CD,
        0,
    ),  # East Asian ideograph (variant of 4B5629 which maps to 85CD)
    0x27562A: (0x8428, 0),  # East Asian ideograph
    0x21562B: (0x85CF, 0),  # East Asian ideograph
    0x21562C: (0x85AF, 0),  # East Asian ideograph
    0x21562D: (0x85D0, 0),  # East Asian ideograph
    0x27562E: (0x501F, 0),  # East Asian ideograph
    0x214E5D: (0x792A, 0),  # East Asian ideograph
    0x215630: (0x85E9, 0),  # East Asian ideograph
    0x215631: (0x85DD, 0),  # East Asian ideograph
    0x275632: (0x85AE, 0),  # East Asian ideograph
    0x215633: (0x85E4, 0),  # East Asian ideograph
    0x215634: (0x85D5, 0),  # East Asian ideograph
    0x224E5E: (0x6FEE, 0),  # East Asian ideograph
    0x215636: (0x85FB, 0),  # East Asian ideograph
    0x215637: (0x85F9, 0),  # East Asian ideograph
    0x215638: (0x8611, 0),  # East Asian ideograph
    0x215639: (0x85FA, 0),  # East Asian ideograph
    0x27563A: (0x82A6, 0),  # East Asian ideograph
    0x27563B: (0x82F9, 0),  # East Asian ideograph
    0x27563C: (0x82CF, 0),  # East Asian ideograph
    0x27563D: (0x8574, 0),  # East Asian ideograph
    0x27563E: (0x5170, 0),  # East Asian ideograph
    0x21563F: (0x8617, 0),  # East Asian ideograph
    0x215640: (0x861A, 0),  # East Asian ideograph
    0x215641: (0x8638, 0),  # East Asian ideograph
    0x275642: (0x841D, 0),  # East Asian ideograph
    0x215643: (0x864E, 0),  # East Asian ideograph
    0x215644: (0x8650, 0),  # East Asian ideograph
    0x215645: (0x8654, 0),  # East Asian ideograph
    0x215646: (0x5F6A, 0),  # East Asian ideograph
    0x215647: (0x8655, 0),  # East Asian ideograph
    0x275648: (0x864F, 0),  # East Asian ideograph
    0x215649: (0x865B, 0),  # East Asian ideograph
    0x27564A: (0x53F7, 0),  # East Asian ideograph
    0x21564B: (0x865E, 0),  # East Asian ideograph
    0x22564C: (0x72AB, 0),  # East Asian ideograph
    0x224E62: (0x6FF0, 0),  # East Asian ideograph
    0x22564E: (0x72B0, 0),  # East Asian ideograph
    0x21564F: (0x8679, 0),  # East Asian ideograph
    0x215650: (0x86A9, 0),  # East Asian ideograph
    0x215651: (0x86AA, 0),  # East Asian ideograph
    0x215652: (0x868A, 0),  # East Asian ideograph
    0x215653: (0x8693, 0),  # East Asian ideograph
    0x215654: (0x86A4, 0),  # East Asian ideograph
    0x215655: (0x868C, 0),  # East Asian ideograph
    0x215656: (0x86A3, 0),  # East Asian ideograph
    0x215657: (0x86C0, 0),  # East Asian ideograph
    0x215658: (0x86C7, 0),  # East Asian ideograph
    0x215659: (0x86B5, 0),  # East Asian ideograph
    0x27565A: (0x65E6, 0),  # East Asian ideograph
    0x21565B: (0x86B6, 0),  # East Asian ideograph
    0x21565C: (0x86C4, 0),  # East Asian ideograph
    0x21565D: (0x86C6, 0),  # East Asian ideograph
    0x21565E: (0x86B1, 0),  # East Asian ideograph
    0x21565F: (0x86AF, 0),  # East Asian ideograph
    0x225660: (0x72D6, 0),  # East Asian ideograph
    0x215661: (0x86D9, 0),  # East Asian ideograph
    0x215662: (0x86ED, 0),  # East Asian ideograph
    0x215663: (0x86D4, 0),  # East Asian ideograph
    0x225664: (0x72D2, 0),  # East Asian ideograph
    0x224E66: (0x7005, 0),  # East Asian ideograph
    0x215666: (0x86FB, 0),  # East Asian ideograph
    0x225667: (0x72C9, 0),  # East Asian ideograph
    0x215668: (0x8707, 0),  # East Asian ideograph
    0x215669: (0x8703, 0),  # East Asian ideograph
    0x21566A: (0x8708, 0),  # East Asian ideograph
    0x214E67: (0x7955, 0),  # East Asian ideograph
    0x21566C: (0x86FE, 0),  # East Asian ideograph
    0x21566D: (0x8713, 0),  # East Asian ideograph
    0x21566E: (0x8702, 0),  # East Asian ideograph
    0x21566F: (0x871C, 0),  # East Asian ideograph
    0x215670: (0x873F, 0),  # East Asian ideograph
    0x215671: (0x873B, 0),  # East Asian ideograph
    0x215672: (0x8722, 0),  # East Asian ideograph
    0x225673: (0x72E8, 0),  # East Asian ideograph
    0x215674: (0x8734, 0),  # East Asian ideograph
    0x215675: (0x8718, 0),  # East Asian ideograph
    0x215676: (0x8755, 0),  # East Asian ideograph
    0x215677: (0x8760, 0),  # East Asian ideograph
    0x215678: (0x8776, 0),  # East Asian ideograph
    0x225679: (0x72E5, 0),  # East Asian ideograph
    0x27567A: (0x867E, 0),  # East Asian ideograph
    0x21567B: (0x8778, 0),  # East Asian ideograph
    0x21567C: (0x8768, 0),  # East Asian ideograph
    0x21567D: (0x874C, 0),  # East Asian ideograph
    0x22567E: (0x72FA, 0),  # East Asian ideograph
    0x6F4E6B: (0xB790, 0),  # Korean hangul
    0x6F5421: (0xC2B7, 0),  # Korean hangul
    0x234E6C: (0x97F5, 0),  # East Asian ideograph
    0x6F5339: (0xC151, 0),  # Korean hangul
    0x6F4E6D: (0xB797, 0),  # Korean hangul
    0x69245D: (0x307D, 0),  # Hiragana letter PO
    0x6F4E6E: (0xB798, 0),  # Korean hangul
    0x274E6F: (0x53EA, 0),  # East Asian ideograph (duplicate simplified)
    0x6F5865: (0xCB20, 0),  # Korean hangul
    0x6F4E70: (0xB79C, 0),  # Korean hangul
    0x6F5422: (0xC2B9, 0),  # Korean hangul
    0x6F5A2A: (0xCEF7, 0),  # Korean hangul
    0x6F4E71: (0xB7A0, 0),  # Korean hangul
    0x234648: (0x939A, 0),  # East Asian ideograph
    0x213441: (0x5305, 0),  # East Asian ideograph
    0x224E72: (0x7026, 0),  # East Asian ideograph
    0x214E73: (0x797A, 0),  # East Asian ideograph
    0x286C58: (0x7BA7, 0),  # East Asian ideograph
    0x6F5633: (0xC68D, 0),  # Korean hangul
    0x6F4E3B: (0xB5BC, 0),  # Korean hangul
    0x6F5866: (0xCB21, 0),  # Korean hangul
    0x395179: (0x7D75, 0),  # East Asian ideograph
    0x6F4E76: (0xB7AD, 0),  # Korean hangul
    0x213921: (0x5920, 0),  # East Asian ideograph
    0x274E77: (0x7978, 0),  # East Asian ideograph
    0x27785E: (0x5786, 0),  # East Asian ideograph
    0x213922: (0x5924, 0),  # East Asian ideograph
    0x274E78: (0x796F, 0),  # East Asian ideograph
    0x213923: (0x5925, 0),  # East Asian ideograph
    0x234E79: (0x9807, 0),  # East Asian ideograph
    0x273924: (0x68A6, 0),  # East Asian ideograph
    0x6F5867: (0xCB41, 0),  # Korean hangul
    0x213F37: (0x6155, 0),  # East Asian ideograph
    0x6F4E7A: (0xB7EC, 0),  # Korean hangul
    0x6F4D61: (0xB4D0, 0),  # Korean hangul
    0x226464: (0x7876, 0),  # East Asian ideograph
    0x274E7B: (0x7985, 0),  # East Asian ideograph
    0x69482B: (0x7560, 0),  # East Asian ideograph
    0x274E7C: (0x793C, 0),  # East Asian ideograph
    0x4B4F3C: (
        0x79F0,
        0,
    ),  # East Asian ideograph (variant of 274F3C which maps to 79F0)
    0x213927: (0x592B, 0),  # East Asian ideograph
    0x274E7D: (0x7977, 0),  # East Asian ideograph
    0x2D5323: (0x5B8D, 0),  # East Asian ideograph
    0x234E7E: (0x980D, 0),  # East Asian ideograph
    0x2D3929: (0x6B80, 0),  # East Asian ideograph
    0x213376: (0x5274, 0),  # East Asian ideograph
    0x6F5868: (0xCB48, 0),  # Korean hangul
    0x6F5433: (0xC300, 0),  # Korean hangul
    0x216066: (0x98E7, 0),  # East Asian ideograph
    0x21392B: (0x5931, 0),  # East Asian ideograph
    0x3F304C: (0x5E79, 0),  # East Asian ideograph
    0x2E3A26: (0x661D, 0),  # East Asian ideograph
    0x225359: (0x71B4, 0),  # East Asian ideograph
    0x21392E: (0x593E, 0),  # East Asian ideograph
    0x6F5869: (0xCB49, 0),  # Korean hangul
    0x396B33: (0x5259, 0),  # East Asian ideograph (not in Unicode)
    0x216067: (0x98E9, 0),  # East Asian ideograph
    0x235721: (0x9B83, 0),  # East Asian ideograph
    0x215722: (0x8783, 0),  # East Asian ideograph
    0x215723: (0x8782, 0),  # East Asian ideograph
    0x275724: (0x8424, 0),  # East Asian ideograph
    0x225725: (0x72FE, 0),  # East Asian ideograph
    0x215726: (0x878D, 0),  # East Asian ideograph
    0x215727: (0x879F, 0),  # East Asian ideograph
    0x215728: (0x87D1, 0),  # East Asian ideograph
    0x215729: (0x87C0, 0),  # East Asian ideograph
    0x21572A: (0x87AB, 0),  # East Asian ideograph
    0x23572B: (0x9B90, 0),  # East Asian ideograph
    0x27572C: (0x877C, 0),  # East Asian ideograph
    0x22572D: (0x7301, 0),  # East Asian ideograph
    0x22572E: (0x72F3, 0),  # East Asian ideograph
    0x23572F: (0x9B97, 0),  # East Asian ideograph
    0x215730: (0x87C6, 0),  # East Asian ideograph
    0x215731: (0x87CB, 0),  # East Asian ideograph
    0x215732: (0x87EF, 0),  # East Asian ideograph
    0x215733: (0x87F2, 0),  # East Asian ideograph
    0x215734: (0x87EC, 0),  # East Asian ideograph
    0x225735: (0x730B, 0),  # East Asian ideograph
    0x225736: (0x7317, 0),  # East Asian ideograph
    0x215737: (0x880D, 0),  # East Asian ideograph
    0x215738: (0x87F9, 0),  # East Asian ideograph
    0x215739: (0x8814, 0),  # East Asian ideograph
    0x21573A: (0x8815, 0),  # East Asian ideograph
    0x22573B: (0x7307, 0),  # East Asian ideograph
    0x23573C: (0x9BAD, 0),  # East Asian ideograph
    0x23573D: (0x9B9A, 0),  # East Asian ideograph
    0x22573E: (0x7318, 0),  # East Asian ideograph
    0x27573F: (0x86CA, 0),  # East Asian ideograph
    0x215740: (0x8839, 0),  # East Asian ideograph
    0x275741: (0x8695, 0),  # East Asian ideograph
    0x215742: (0x883B, 0),  # East Asian ideograph
    0x235743: (0x9B99, 0),  # East Asian ideograph
    0x215744: (0x884C, 0),  # East Asian ideograph
    0x215745: (0x884D, 0),  # East Asian ideograph
    0x225746: (0x7331, 0),  # East Asian ideograph
    0x215747: (0x8857, 0),  # East Asian ideograph
    0x215748: (0x8859, 0),  # East Asian ideograph
    0x225749: (0x7338, 0),  # East Asian ideograph
    0x22574A: (0x7322, 0),  # East Asian ideograph
    0x21574B: (0x8861, 0),  # East Asian ideograph
    0x22574C: (0x7332, 0),  # East Asian ideograph
    0x22574D: (0x732C, 0),  # East Asian ideograph
    0x22574E: (0x7327, 0),  # East Asian ideograph
    0x22574F: (0x732B, 0),  # East Asian ideograph
    0x215750: (0x886B, 0),  # East Asian ideograph
    0x215751: (0x8882, 0),  # East Asian ideograph
    0x225752: (0x732F, 0),  # East Asian ideograph
    0x215753: (0x8870, 0),  # East Asian ideograph
    0x215754: (0x8877, 0),  # East Asian ideograph
    0x225755: (0x7328, 0),  # East Asian ideograph
    0x235756: (0x9BC7, 0),  # East Asian ideograph
    0x215757: (0x8892, 0),  # East Asian ideograph
    0x215758: (0x8896, 0),  # East Asian ideograph
    0x235759: (0x9BD2, 0),  # East Asian ideograph
    0x22575A: (0x7347, 0),  # East Asian ideograph
    0x22575B: (0x7348, 0),  # East Asian ideograph
    0x22575C: (0x7349, 0),  # East Asian ideograph
    0x23393A: (0x8DE6, 0),  # East Asian ideograph
    0x21575E: (0x88B1, 0),  # East Asian ideograph
    0x23575F: (0x9BC1, 0),  # East Asian ideograph
    0x215760: (0x88D9, 0),  # East Asian ideograph
    0x215761: (0x88D8, 0),  # East Asian ideograph
    0x215762: (0x88DC, 0),  # East Asian ideograph
    0x215763: (0x88CF, 0),  # East Asian ideograph
    0x215764: (0x88D4, 0),  # East Asian ideograph
    0x225765: (0x7340, 0),  # East Asian ideograph
    0x215766: (0x88D5, 0),  # East Asian ideograph
    0x215767: (0x8902, 0),  # East Asian ideograph
    0x225768: (0x734D, 0),  # East Asian ideograph
    0x215769: (0x88F8, 0),  # East Asian ideograph
    0x21576A: (0x88F9, 0),  # East Asian ideograph
    0x21576B: (0x88F4, 0),  # East Asian ideograph
    0x23576C: (0x9BD3, 0),  # East Asian ideograph
    0x21576D: (0x88E8, 0),  # East Asian ideograph
    0x21576E: (0x891A, 0),  # East Asian ideograph
    0x21576F: (0x8910, 0),  # East Asian ideograph
    0x6F5770: (0xC906, 0),  # Korean hangul
    0x215771: (0x8913, 0),  # East Asian ideograph
    0x235772: (0x9BC8, 0),  # East Asian ideograph
    0x215773: (0x8932, 0),  # East Asian ideograph
    0x225774: (0x735D, 0),  # East Asian ideograph
    0x215775: (0x8925, 0),  # East Asian ideograph
    0x215776: (0x892B, 0),  # East Asian ideograph
    0x235777: (0x9BD7, 0),  # East Asian ideograph
    0x215778: (0x8936, 0),  # East Asian ideograph
    0x225779: (0x7360, 0),  # East Asian ideograph
    0x23577A: (0x9BD6, 0),  # East Asian ideograph
    0x21577B: (0x895F, 0),  # East Asian ideograph
    0x23577C: (0x9BEB, 0),  # East Asian ideograph
    0x21577D: (0x8956, 0),  # East Asian ideograph
    0x22577E: (0x7362, 0),  # East Asian ideograph
    0x273940: (0x593A, 0),  # East Asian ideograph
    0x223941: (0x66AA, 0),  # East Asian ideograph
    0x232B33: (0x874D, 0),  # East Asian ideograph
    0x2D506F: (0x7CFA, 0),  # East Asian ideograph
    0x6F586D: (0xCB5D, 0),  # Korean hangul
    0x6F7643: (0xE8B5, 0),  # Korean hangul
    0x213943: (0x5974, 0),  # East Asian ideograph
    0x213944: (0x5976, 0),  # East Asian ideograph
    0x4B3322: (
        0x5168,
        0,
    ),  # East Asian ideograph (variant of 213322 which maps to 5168)
    0x27564C: (0x4E8F, 0),  # East Asian ideograph
    0x4B5E3D: (0x9421, 0),  # East Asian ideograph
    0x213946: (0x5983, 0),  # East Asian ideograph
    0x6F5365: (0xC231, 0),  # Korean hangul
    0x6F516D: (0xBE44, 0),  # Korean hangul
    0x213947: (0x5978, 0),  # East Asian ideograph
    0x2D4C2D: (0x756E, 0),  # East Asian ideograph
    0x6F542B: (0xC2EF, 0),  # Korean hangul
    0x213E53: (0x6089, 0),  # East Asian ideograph
    0x213949: (0x5979, 0),  # East Asian ideograph
    0x21794B: (0x595C, 0),  # East Asian ideograph
    0x454E75: (0x7984, 0),  # East Asian ideograph
    0x213C7D: (0x5EC2, 0),  # East Asian ideograph
    0x6F586F: (0xCBB8, 0),  # Korean hangul
    0x2D394D: (0x59AC, 0),  # East Asian ideograph
    0x217E43: (0x5B93, 0),  # East Asian ideograph
    0x22394E: (0x66C8, 0),  # East Asian ideograph
    0x4B3324: (
        0x634C,
        0,
    ),  # East Asian ideograph (variant of 2D3324 which maps to 634C)
    0x21394F: (0x59A4, 0),  # East Asian ideograph
    0x213F58: (0x61FA, 0),  # East Asian ideograph
    0x213950: (0x59A3, 0),  # East Asian ideograph
    0x6F4E3D: (0xB5C4, 0),  # Korean hangul
    0x213951: (0x5993, 0),  # East Asian ideograph
    0x2F5870: (0x9C1B, 0),  # East Asian ideograph
    0x6F7646: (0xE8B8, 0),  # Korean hangul
    0x213952: (0x599E, 0),  # East Asian ideograph
    0x213E55: (0x60A0, 0),  # East Asian ideograph
    0x4B3768: (0x56D8, 0),  # East Asian ideograph
    0x213953: (0x599D, 0),  # East Asian ideograph
    0x233954: (0x8E23, 0),  # East Asian ideograph
    0x213955: (0x59A5, 0),  # East Asian ideograph
    0x335760: (0x88E0, 0),  # East Asian ideograph
    0x2D3956: (0x59D9, 0),  # East Asian ideograph
    0x6F4F22: (0xB7FF, 0),  # Korean hangul
    0x6F5871: (0xCBE4, 0),  # Korean hangul
    0x6F7647: (0xE8B9, 0),  # Korean hangul
    0x213957: (0x5996, 0),  # East Asian ideograph
    0x213958: (0x59BE, 0),  # East Asian ideograph
    0x333642: (0x8A92, 0),  # East Asian ideograph
    0x2D3F67: (0x621E, 0),  # East Asian ideograph
    0x6F5878: (0xCC1D, 0),  # Korean hangul
    0x4C7959: (0x817D, 0),  # East Asian ideograph
    0x273437: (0x80DC, 0),  # East Asian ideograph
    0x214F63: (0x7AC7, 0),  # East Asian ideograph
    0x4B524E: (0x7FCE, 0),  # East Asian ideograph
    0x21395A: (0x59AE, 0),  # East Asian ideograph
    0x3A4034: (0x6855, 0),  # East Asian ideograph
    0x275821: (0x889C, 0),  # East Asian ideograph
    0x275822: (0x886C, 0),  # East Asian ideograph
    0x215823: (0x8972, 0),  # East Asian ideograph
    0x215824: (0x897F, 0),  # East Asian ideograph
    0x225825: (0x7367, 0),  # East Asian ideograph
    0x215826: (0x8983, 0),  # East Asian ideograph
    0x235827: (0x9BE4, 0),  # East Asian ideograph
    0x275828: (0x89C1, 0),  # East Asian ideograph
    0x275829: (0x89C4, 0),  # East Asian ideograph
    0x27582A: (0x89C5, 0),  # East Asian ideograph
    0x27582B: (0x89C6, 0),  # East Asian ideograph
    0x27582C: (0x4EB2, 0),  # East Asian ideograph
    0x27582D: (0x89CE, 0),  # East Asian ideograph
    0x21582E: (0x89AC, 0),  # East Asian ideograph
    0x27582F: (0x89D0, 0),  # East Asian ideograph
    0x215830: (0x89BA, 0),  # East Asian ideograph
    0x275831: (0x89C8, 0),  # East Asian ideograph
    0x215832: (0x89C0, 0),  # East Asian ideograph
    0x215833: (0x89D2, 0),  # East Asian ideograph
    0x235834: (0x9BD4, 0),  # East Asian ideograph
    0x215835: (0x89F4, 0),  # East Asian ideograph
    0x225836: (0x737C, 0),  # East Asian ideograph
    0x215837: (0x8A00, 0),  # East Asian ideograph
    0x215838: (0x8A08, 0),  # East Asian ideograph
    0x215839: (0x8A02, 0),  # East Asian ideograph
    0x21583A: (0x8A03, 0),  # East Asian ideograph
    0x21583B: (0x8A10, 0),  # East Asian ideograph
    0x21583C: (0x8A18, 0),  # East Asian ideograph
    0x21583D: (0x8A0E, 0),  # East Asian ideograph
    0x23583E: (0x9BFF, 0),  # East Asian ideograph
    0x21583F: (0x8A15, 0),  # East Asian ideograph
    0x215840: (0x8A0A, 0),  # East Asian ideograph
    0x275841: (0x8BAB, 0),  # East Asian ideograph
    0x225842: (0x738E, 0),  # East Asian ideograph
    0x235843: (0x9C06, 0),  # East Asian ideograph
    0x235844: (0x9C15, 0),  # East Asian ideograph
    0x215845: (0x8A23, 0),  # East Asian ideograph
    0x275846: (0x8BB6, 0),  # East Asian ideograph
    0x225847: (0x7392, 0),  # East Asian ideograph
    0x215848: (0x8A31, 0),  # East Asian ideograph
    0x275849: (0x8BBE, 0),  # East Asian ideograph
    0x27584A: (0x8BB9, 0),  # East Asian ideograph
    0x27584B: (0x8BBC, 0),  # East Asian ideograph
    0x27584C: (0x6CE8, 0),  # East Asian ideograph
    0x21584D: (0x8A60, 0),  # East Asian ideograph
    0x27584E: (0x8BC4, 0),  # East Asian ideograph
    0x27584F: (0x8BCD, 0),  # East Asian ideograph
    0x6F5850: (0xCA50, 0),  # Korean hangul
    0x215851: (0x8A41, 0),  # East Asian ideograph
    0x235852: (0x9C02, 0),  # East Asian ideograph
    0x215853: (0x8A5B, 0),  # East Asian ideograph
    0x235854: (0x9C10, 0),  # East Asian ideograph
    0x215855: (0x8A46, 0),  # East Asian ideograph
    0x215856: (0x8A34, 0),  # East Asian ideograph
    0x275857: (0x8BCA, 0),  # East Asian ideograph
    0x275858: (0x8BE7, 0),  # East Asian ideograph
    0x215859: (0x8A72, 0),  # East Asian ideograph
    0x21585A: (0x8A73, 0),  # East Asian ideograph
    0x21585B: (0x8A66, 0),  # East Asian ideograph
    0x27585C: (0x8BD7, 0),  # East Asian ideograph
    0x27585D: (0x8BD8, 0),  # East Asian ideograph
    0x27585E: (0x8BE3, 0),  # East Asian ideograph
    0x27585F: (0x8BD9, 0),  # East Asian ideograph
    0x275860: (0x8BDA, 0),  # East Asian ideograph
    0x215861: (0x8A87, 0),  # East Asian ideograph
    0x275862: (0x8BDB, 0),  # East Asian ideograph
    0x215863: (0x8A6D, 0),  # East Asian ideograph
    0x215864: (0x8A79, 0),  # East Asian ideograph
    0x275865: (0x8BE2, 0),  # East Asian ideograph
    0x275866: (0x8BDD, 0),  # East Asian ideograph
    0x275867: (0x8BE0, 0),  # East Asian ideograph
    0x215868: (0x8A6C, 0),  # East Asian ideograph
    0x235869: (0x9C2F, 0),  # East Asian ideograph
    0x22586A: (0x73C2, 0),  # East Asian ideograph
    0x22586B: (0x73D0, 0),  # East Asian ideograph
    0x21586C: (0x8A9E, 0),  # East Asian ideograph
    0x21586D: (0x8A8C, 0),  # East Asian ideograph
    0x21586E: (0x8A93, 0),  # East Asian ideograph
    0x22586F: (0x73BF, 0),  # East Asian ideograph
    0x275870: (0x8BA4, 0),  # East Asian ideograph
    0x275871: (0x8BEF, 0),  # East Asian ideograph
    0x275872: (0x8BF2, 0),  # East Asian ideograph
    0x275873: (0x8BF0, 0),  # East Asian ideograph
    0x275874: (0x8BF1, 0),  # East Asian ideograph
    0x275875: (0x8BF3, 0),  # East Asian ideograph
    0x215876: (0x8ABC, 0),  # East Asian ideograph
    0x275877: (0x8C06, 0),  # East Asian ideograph
    0x275878: (0x8C05, 0),  # East Asian ideograph
    0x215879: (0x8AC7, 0),  # East Asian ideograph
    0x21587A: (
        0x8ACB,
        0,
    ),  # East Asian ideograph (variant of 4B587A which maps to 8ACB)
    0x27587B: (0x8BF8, 0),  # East Asian ideograph
    0x27587C: (0x8BFE, 0),  # East Asian ideograph
    0x27587D: (0x8C03, 0),  # East Asian ideograph
    0x23587E: (0x9C46, 0),  # East Asian ideograph
    0x6F5875: (0xCC10, 0),  # Korean hangul
    0x6F764B: (0xE8BD, 0),  # Korean hangul
    0x21796B: (0x5998, 0),  # East Asian ideograph
    0x6F4B62: (0xB0BB, 0),  # Korean hangul
    0x293C5A: (0x8F73, 0),  # East Asian ideograph
    0x2D396E: (0x4F84, 0),  # East Asian ideograph
    0x28732D: (0x7F2F, 0),  # East Asian ideograph
    0x4B6145: (0x9A12, 0),  # East Asian ideograph
    0x21396F: (0x5A01, 0),  # East Asian ideograph
    0x2D4C35: (0x7567, 0),  # East Asian ideograph
    0x2D3970: (0x5A63, 0),  # East Asian ideograph
    0x213971: (0x59E6, 0),  # East Asian ideograph
    0x6F5879: (0xCC21, 0),  # Korean hangul
    0x213972: (0x59DA, 0),  # East Asian ideograph
    0x213973: (0x5A11, 0),  # East Asian ideograph
    0x2D3974: (0x5B43, 0),  # East Asian ideograph
    0x6F5877: (0xCC1C, 0),  # Korean hangul
    0x6F764D: (0xE8BF, 0),  # Korean hangul
    0x6F5434: (0xC308, 0),  # Korean hangul
    0x213E5C: (0x60B6, 0),  # East Asian ideograph
    0x4B376F: (0x56FD, 0),  # East Asian ideograph
    0x213976: (0x5A1C, 0),  # East Asian ideograph
    0x692421: (0x3041, 0),  # Hiragana letter small A
    0x213977: (0x5A13, 0),  # East Asian ideograph
    0x2D5773: (0x7D5D, 0),  # East Asian ideograph
    0x213978: (0x59EC, 0),  # East Asian ideograph
    0x33354E: (0x608B, 0),  # East Asian ideograph
    0x213979: (0x5A20, 0),  # East Asian ideograph
    0x216424: (0x4E0F, 0),  # East Asian ideograph
    0x6F764E: (0xE8C0, 0),  # Korean hangul
    0x6F535C: (0xC219, 0),  # Korean hangul
    0x213E5D: (0x60D1, 0),  # East Asian ideograph
    0x2D397B: (0x5A31, 0),  # East Asian ideograph
    0x2D3F6E: (0x6226, 0),  # East Asian ideograph
    0x21397C: (0x5A0C, 0),  # East Asian ideograph
    0x692427: (0x3047, 0),  # Hiragana letter small E
    0x6F5841: (0xC9EF, 0),  # Korean hangul
    0x22797D: (0x81A6, 0),  # East Asian ideograph
    0x692428: (0x3048, 0),  # Hiragana letter E
    0x21397E: (0x5A25, 0),  # East Asian ideograph
    0x222429: (0x5CDD, 0),  # East Asian ideograph
    0x6F764F: (0xE8C1, 0),  # Korean hangul
    0x6F5436: (0xC30B, 0),  # Korean hangul
    0x213E5E: (0x60B5, 0),  # East Asian ideograph
    0x33304C: (0x4E79, 0),  # East Asian ideograph
    0x215C34: (0x904B, 0),  # East Asian ideograph
    0x2D3F6F: (0x622F, 0),  # East Asian ideograph
    0x27742E: (0x56F5, 0),  # East Asian ideograph
    0x216D41: (0x534C, 0),  # East Asian ideograph
    0x6F587A: (0xCC22, 0),  # Korean hangul
    0x6F7650: (0xE8C2, 0),  # Korean hangul
    0x6F5437: (0xC30C, 0),  # Korean hangul
    0x69242F: (0x304F, 0),  # Hiragana letter KU
    0x4B3772: (0x5186, 0),  # East Asian ideograph
    0x4B5631: (0x82B8, 0),  # East Asian ideograph
    0x225921: (0x73D3, 0),  # East Asian ideograph
    0x215922: (0x8AB0, 0),  # East Asian ideograph
    0x215923: (0x8A95, 0),  # East Asian ideograph
    0x215924: (0x8AD6, 0),  # East Asian ideograph
    0x275925: (0x8C1B, 0),  # East Asian ideograph
    0x235926: (0x9C44, 0),  # East Asian ideograph
    0x215927: (0x8AEB, 0),  # East Asian ideograph
    0x225928: (0x73E5, 0),  # East Asian ideograph
    0x235929: (0x9C39, 0),  # East Asian ideograph
    0x22592A: (0x73D9, 0),  # East Asian ideograph
    0x22592B: (0x73EF, 0),  # East Asian ideograph
    0x21592C: (
        0x8B01,
        0,
    ),  # East Asian ideograph (variant of 2D592C which maps to 8B01)
    0x21592D: (0x8B02, 0),  # East Asian ideograph
    0x21592E: (0x8AFE, 0),  # East Asian ideograph
    0x27592F: (0x8BBD, 0),  # East Asian ideograph
    0x235930: (0x9C47, 0),  # East Asian ideograph
    0x215931: (0x8B17, 0),  # East Asian ideograph
    0x225932: (0x73D6, 0),  # East Asian ideograph
    0x215933: (0x8B0E, 0),  # East Asian ideograph
    0x235934: (0x9C37, 0),  # East Asian ideograph
    0x225935: (0x73BC, 0),  # East Asian ideograph
    0x215936: (0x8B21, 0),  # East Asian ideograph
    0x215937: (0x8B04, 0),  # East Asian ideograph
    0x235938: (0x9C52, 0),  # East Asian ideograph
    0x275939: (0x8C28, 0),  # East Asian ideograph
    0x22593A: (0x73DE, 0),  # East Asian ideograph
    0x23593B: (0x9C58, 0),  # East Asian ideograph
    0x22593C: (0x73E6, 0),  # East Asian ideograph
    0x21593D: (0x8B5C, 0),  # East Asian ideograph
    0x21593E: (0x8B4E, 0),  # East Asian ideograph
    0x21593F: (0x8B49, 0),  # East Asian ideograph
    0x275940: (0x8C2D, 0),  # East Asian ideograph
    0x215941: (0x8B41, 0),  # East Asian ideograph
    0x275942: (0x8BA5, 0),  # East Asian ideograph
    0x215943: (0x8B70, 0),  # East Asian ideograph
    0x215944: (0x8B6C, 0),  # East Asian ideograph
    0x225945: (0x73F6, 0),  # East Asian ideograph
    0x215946: (0x8B6F, 0),  # East Asian ideograph
    0x225947: (0x73FA, 0),  # East Asian ideograph
    0x275948: (0x62A4, 0),  # East Asian ideograph
    0x215949: (0x8B7D, 0),  # East Asian ideograph
    0x27594A: (0x8BFB, 0),  # East Asian ideograph
    0x21594B: (0x8B8A, 0),  # East Asian ideograph
    0x27594C: (0x8BA9, 0),  # East Asian ideograph
    0x21594D: (0x8B96, 0),  # East Asian ideograph
    0x21594E: (0x8B92, 0),  # East Asian ideograph
    0x23594F: (0x9C67, 0),  # East Asian ideograph
    0x6F5950: (0xCD2C, 0),  # Korean hangul
    0x215951: (0x8C41, 0),  # East Asian ideograph
    0x215952: (0x8C3F, 0),  # East Asian ideograph
    0x215953: (0x8C46, 0),  # East Asian ideograph
    0x225954: (0x73F5, 0),  # East Asian ideograph
    0x235955: (0x9C5F, 0),  # East Asian ideograph
    0x235956: (0x9C60, 0),  # East Asian ideograph
    0x215957: (0x8C4E, 0),  # East Asian ideograph
    0x235958: (0x9C6D, 0),  # East Asian ideograph
    0x215959: (0x8C54, 0),  # East Asian ideograph
    0x21595A: (0x8C5A, 0),  # East Asian ideograph
    0x23595B: (0x9C68, 0),  # East Asian ideograph
    0x22595C: (0x7407, 0),  # East Asian ideograph
    0x21595D: (0x8C6A, 0),  # East Asian ideograph
    0x22595E: (0x7412, 0),  # East Asian ideograph
    0x21595F: (0x8C6C, 0),  # East Asian ideograph
    0x215960: (0x8C7A, 0),  # East Asian ideograph
    0x215961: (0x8C79, 0),  # East Asian ideograph
    0x215962: (0x8C82, 0),  # East Asian ideograph
    0x225963: (0x743C, 0),  # East Asian ideograph
    0x215964: (0x8C89, 0),  # East Asian ideograph
    0x215965: (0x8C8D, 0),  # East Asian ideograph
    0x225966: (0x742E, 0),  # East Asian ideograph
    0x225967: (0x742F, 0),  # East Asian ideograph
    0x275968: (0x8D1D, 0),  # East Asian ideograph
    0x225969: (0x7414, 0),  # East Asian ideograph
    0x22596A: (0x742C, 0),  # East Asian ideograph
    0x27596B: (0x8D21, 0),  # East Asian ideograph
    0x27596C: (0x8D22, 0),  # East Asian ideograph
    0x27596D: (0x8D23, 0),  # East Asian ideograph
    0x22596E: (0x742B, 0),  # East Asian ideograph
    0x21596F: (0x8CA8, 0),  # East Asian ideograph
    0x225970: (0x73F7, 0),  # East Asian ideograph
    0x225971: (0x741A, 0),  # East Asian ideograph
    0x275972: (0x8D29, 0),  # East Asian ideograph
    0x235973: (0x9CE7, 0),  # East Asian ideograph
    0x235974: (0x9CF0, 0),  # East Asian ideograph
    0x215975: (0x8CBB, 0),  # East Asian ideograph
    0x215976: (0x8CC1, 0),  # East Asian ideograph
    0x235977: (0x9CF2, 0),  # East Asian ideograph
    0x225978: (0x7416, 0),  # East Asian ideograph
    0x215979: (0x8CBC, 0),  # East Asian ideograph
    0x22597A: (0x7426, 0),  # East Asian ideograph
    0x21597B: (0x8CB6, 0),  # East Asian ideograph
    0x21597C: (0x8CBD, 0),  # East Asian ideograph
    0x27597D: (0x8D37, 0),  # East Asian ideograph
    0x21597E: (0x8CBF, 0),  # East Asian ideograph
    0x222441: (0x5CF4, 0),  # East Asian ideograph
    0x224F2B: (
        0x701E,
        0,
    ),  # East Asian ideograph (variant of 4C4F2B which maps to 701E)
    0x6F587E: (0xCC28, 0),  # Korean hangul
    0x275E58: (0x9602, 0),  # East Asian ideograph
    0x6F543B: (0xC315, 0),  # Korean hangul
    0x217E52: (0x5BA7, 0),  # East Asian ideograph
    0x333573: (0x8656, 0),  # East Asian ideograph
    0x222446: (0x5CF1, 0),  # East Asian ideograph
    0x69243F: (0x305F, 0),  # Hiragana letter TA
    0x27613E: (0x9A8F, 0),  # East Asian ideograph
    0x6F5B69: (0xD305, 0),  # Korean hangul
    0x2D5C2F: (0x8FE8, 0),  # East Asian ideograph
    0x2D4C3E: (0x758E, 0),  # East Asian ideograph
    0x6F4E74: (0xB7AB, 0),  # Korean hangul
    0x6F7655: (0xE8C7, 0),  # Korean hangul
    0x225F7B: (0x7657, 0),  # East Asian ideograph
    0x213E64: (0x60D5, 0),  # East Asian ideograph
    0x234662: (0x93F9, 0),  # East Asian ideograph
    0x696449: (0x7C13, 0),  # East Asian ideograph
    0x276137: (0x9A76, 0),  # East Asian ideograph
    0x69244A: (0x306A, 0),  # Hiragana letter NA
    0x4B6147: (0x99C6, 0),  # East Asian ideograph
    0x333556: (0x9A03, 0),  # East Asian ideograph
    0x69644C: (0x7C17, 0),  # East Asian ideograph
    0x6F4D66: (0xB4E4, 0),  # Korean hangul
    0x213E65: (0x60BC, 0),  # East Asian ideograph
    0x69644E: (0x7BF6, 0),  # East Asian ideograph
    0x6F587B: (0xCC27, 0),  # Korean hangul
    0x2D3B33: (0x8A67, 0),  # East Asian ideograph
    0x214B2F: (0x7380, 0),  # East Asian ideograph
    0x6F5438: (0xC30D, 0),  # Korean hangul
    0x6F543E: (0xC324, 0),  # Korean hangul
    0x6F7651: (0xE8C3, 0),  # Korean hangul
    0x216452: (0x4EB3, 0),  # East Asian ideograph
    0x294E43: (0x97AF, 0),  # East Asian ideograph
    0x234664: (0x93C4, 0),  # East Asian ideograph
    0x342453: (0x5CBD, 0),  # East Asian ideograph
    0x692454: (0x3074, 0),  # Hiragana letter PI
    0x225372: (0x71BA, 0),  # East Asian ideograph
    0x4B6455: (0x4EB6, 0),  # East Asian ideograph
    0x6F4F7A: (0xB9F7, 0),  # Korean hangul
    0x6F543F: (0xC327, 0),  # Korean hangul
    0x4B503B: (0x7C12, 0),  # East Asian ideograph
    0x692457: (0x3077, 0),  # Hiragana letter PU
    0x223E23: (0x691A, 0),  # East Asian ideograph
    0x234222: (0x91E4, 0),  # East Asian ideograph
    0x692459: (0x3079, 0),  # Hiragana letter BE
    0x21645A: (0x4EBC, 0),  # East Asian ideograph
    0x4B4444: (0x8988, 0),  # East Asian ideograph (Version J extension)
    0x215A21: (0x8CC5, 0),  # East Asian ideograph
    0x275A22: (0x8D44, 0),  # East Asian ideograph
    0x275A23: (0x8D3C, 0),  # East Asian ideograph
    0x215A24: (0x8CC8, 0),  # East Asian ideograph
    0x275A25: (0x8D3F, 0),  # East Asian ideograph
    0x215A26: (0x8CB2, 0),  # East Asian ideograph
    0x275A27: (0x8D41, 0),  # East Asian ideograph
    0x225A28: (0x7420, 0),  # East Asian ideograph
    0x275A29: (0x5BBE, 0),  # East Asian ideograph
    0x275A2A: (0x8D48, 0),  # East Asian ideograph
    0x275A2B: (0x8D4A, 0),  # East Asian ideograph
    0x215A2C: (0x8CE0, 0),  # East Asian ideograph
    0x275A2D: (0x8D4B, 0),  # East Asian ideograph
    0x6F5A2E: (0xCF00, 0),  # Korean hangul
    0x275A2F: (0x5356, 0),  # East Asian ideograph
    0x235A30: (0x9D25, 0),  # East Asian ideograph
    0x215A31: (0x8CE4, 0),  # East Asian ideograph
    0x215A32: (0x8CDE, 0),  # East Asian ideograph
    0x275A33: (0x8D50, 0),  # East Asian ideograph
    0x215A34: (0x8CEA, 0),  # East Asian ideograph
    0x275A35: (0x8D4C, 0),  # East Asian ideograph
    0x215A36: (0x8CF4, 0),  # East Asian ideograph
    0x215A37: (0x8CFD, 0),  # East Asian ideograph
    0x275A38: (0x8D5A, 0),  # East Asian ideograph
    0x275A39: (0x8D58, 0),  # East Asian ideograph
    0x275A3A: (0x8D2D, 0),  # East Asian ideograph
    0x275A3B: (0x8D60, 0),  # East Asian ideograph
    0x275A3C: (0x8D5D, 0),  # East Asian ideograph
    0x275A3D: (0x8D5E, 0),  # East Asian ideograph
    0x275A3E: (0x8D62, 0),  # East Asian ideograph
    0x275A3F: (0x8D61, 0),  # East Asian ideograph
    0x275A40: (0x8D43, 0),  # East Asian ideograph
    0x275A41: (0x8D4E, 0),  # East Asian ideograph
    0x275A42: (0x8D63, 0),  # East Asian ideograph
    0x215A43: (0x8D64, 0),  # East Asian ideograph
    0x215A44: (0x8D67, 0),  # East Asian ideograph
    0x215A45: (0x8D66, 0),  # East Asian ideograph
    0x215A46: (0x8D6B, 0),  # East Asian ideograph
    0x215A47: (0x8D6D, 0),  # East Asian ideograph
    0x235A48: (0x9D1F, 0),  # East Asian ideograph
    0x215A49: (0x8D74, 0),  # East Asian ideograph
    0x215A4A: (0x8D73, 0),  # East Asian ideograph
    0x215A4B: (0x8D77, 0),  # East Asian ideograph
    0x215A4C: (0x8D85, 0),  # East Asian ideograph
    0x215A4D: (0x8D8A, 0),  # East Asian ideograph
    0x215A4E: (0x8D81, 0),  # East Asian ideograph
    0x275A4F: (0x8D75, 0),  # East Asian ideograph
    0x215A50: (0x8D95, 0),  # East Asian ideograph
    0x215A51: (0x8DA3, 0),  # East Asian ideograph
    0x215A52: (0x8D9F, 0),  # East Asian ideograph
    0x275A53: (0x8D8B, 0),  # East Asian ideograph
    0x215A54: (0x8DB3, 0),  # East Asian ideograph
    0x215A55: (0x8DB4, 0),  # East Asian ideograph
    0x215A56: (0x8DBE, 0),  # East Asian ideograph
    0x215A57: (0x8DCE, 0),  # East Asian ideograph
    0x215A58: (0x8DDD, 0),  # East Asian ideograph
    0x214B33: (0x738B, 0),  # East Asian ideograph
    0x215A5A: (0x8DCB, 0),  # East Asian ideograph
    0x215A5B: (0x8DDA, 0),  # East Asian ideograph
    0x215A5C: (0x8DC6, 0),  # East Asian ideograph
    0x215A5D: (0x8DD1, 0),  # East Asian ideograph
    0x215A5E: (0x8DCC, 0),  # East Asian ideograph
    0x215A5F: (0x8DE1, 0),  # East Asian ideograph
    0x215A60: (0x8DDF, 0),  # East Asian ideograph
    0x215A61: (0x8DE8, 0),  # East Asian ideograph
    0x225A62: (0x7473, 0),  # East Asian ideograph
    0x235A63: (0x9D3E, 0),  # East Asian ideograph
    0x215A64: (0x8DEA, 0),  # East Asian ideograph
    0x215A65: (0x8DEF, 0),  # East Asian ideograph
    0x215A66: (0x8DFC, 0),  # East Asian ideograph
    0x215A67: (0x8E2B, 0),  # East Asian ideograph
    0x235A68: (0x9D42, 0),  # East Asian ideograph
    0x235A69: (0x9D40, 0),  # East Asian ideograph
    0x215A6A: (0x8E1D, 0),  # East Asian ideograph
    0x215A6B: (0x8E0F, 0),  # East Asian ideograph
    0x215A6C: (0x8E29, 0),  # East Asian ideograph
    0x215A6D: (0x8E1F, 0),  # East Asian ideograph
    0x215A6E: (0x8E44, 0),  # East Asian ideograph
    0x215A6F: (0x8E31, 0),  # East Asian ideograph
    0x215A70: (0x8E42, 0),  # East Asian ideograph
    0x215A71: (0x8E34, 0),  # East Asian ideograph
    0x215A72: (0x8E39, 0),  # East Asian ideograph
    0x215A73: (0x8E35, 0),  # East Asian ideograph
    0x215A74: (0x8E49, 0),  # East Asian ideograph
    0x235A75: (0x9D53, 0),  # East Asian ideograph
    0x215A76: (0x8E48, 0),  # East Asian ideograph
    0x215A77: (0x8E4A, 0),  # East Asian ideograph
    0x215A78: (0x8E63, 0),  # East Asian ideograph
    0x215A79: (0x8E59, 0),  # East Asian ideograph
    0x215A7A: (0x8E66, 0),  # East Asian ideograph
    0x215A7B: (0x8E64, 0),  # East Asian ideograph
    0x215A7C: (0x8E72, 0),  # East Asian ideograph
    0x215A7D: (0x8E6C, 0),  # East Asian ideograph
    0x275A7E: (0x8DF7, 0),  # East Asian ideograph
    0x6F5439: (0xC313, 0),  # Korean hangul
    0x6F5443: (0xC343, 0),  # Korean hangul
    0x22646B: (0x789A, 0),  # East Asian ideograph
    0x213A28: (0x5A41, 0),  # East Asian ideograph
    0x6F2458: (0x3134, 0),  # Korean hangul
    0x234226: (0x922B, 0),  # East Asian ideograph
    0x27515C: (0x7EBF, 0),  # East Asian ideograph
    0x475222: (0x9957, 0),  # East Asian ideograph
    0x6F246E: (0x3143, 0),  # Korean hangul
    0x335333: (0x80BB, 0),  # East Asian ideograph
    0x6F2470: (0x3146, 0),  # Korean hangul
    0x692471: (0x3091, 0),  # Hiragana letter WE
    0x232472: (0x852F, 0),  # East Asian ideograph
    0x6F2473: (0x3150, 0),  # Korean hangul
    0x224F35: (0x7021, 0),  # East Asian ideograph
    0x6F2474: (0x3151, 0),  # Korean hangul
    0x6F5445: (0xC368, 0),  # Korean hangul
    0x6F5A31: (0xCF08, 0),  # Korean hangul
    0x6F2476: (0x3153, 0),  # Korean hangul
    0x295729: (0x9C87, 0),  # East Asian ideograph
    0x6F4F21: (0xB7FD, 0),  # Korean hangul
    0x232477: (0x84F7, 0),  # East Asian ideograph
    0x274F22: (0x4E07, 0),  # East Asian ideograph
    0x234F23: (0x980E, 0),  # East Asian ideograph
    0x6F4E42: (0xB611, 0),  # Korean hangul
    0x224F24: (0x7020, 0),  # East Asian ideograph
    0x6F5446: (0xC369, 0),  # Korean hangul
    0x6F247A: (0x3157, 0),  # Korean hangul
    0x274F25: (0x53B6, 0),  # East Asian ideograph
    0x4B333E: (0xF92E, 0),  # East Asian ideograph
    0x224F26: (0x7027, 0),  # East Asian ideograph
    0x214F27: (0x79C9, 0),  # East Asian ideograph
    0x22537A: (0x71BF, 0),  # East Asian ideograph
    0x22537C: (0x71B8, 0),  # East Asian ideograph
    0x29247D: (0x835C, 0),  # East Asian ideograph
    0x6F4F28: (0xB80C, 0),  # Korean hangul
    0x212A38: (0xE8E5, 0),  # EACC component character
    0x276775: (0x4F65, 0),  # East Asian ideograph
    0x6F5447: (0xC36C, 0),  # Korean hangul
    0x6F4F2A: (0xB818, 0),  # Korean hangul
    0x23422A: (0x9292, 0),  # East Asian ideograph
    0x2D5D56: (0x920E, 0),  # East Asian ideograph
    0x234F2C: (0x9826, 0),  # East Asian ideograph
    0x6F5D5A: (0xD6FC, 0),  # Korean hangul
    0x234F2D: (0x981E, 0),  # East Asian ideograph
    0x6F7652: (0xE8C4, 0),  # Korean hangul
    0x6F4F2E: (0xB824, 0),  # Korean hangul
    0x2D3C26: (0x5D18, 0),  # East Asian ideograph
    0x6F5448: (0xC370, 0),  # Korean hangul
    0x213E70: (0x60FB, 0),  # East Asian ideograph
    0x224F2F: (0x702E, 0),  # East Asian ideograph
    0x225B21: (0x7489, 0),  # East Asian ideograph
    0x225B22: (0x747C, 0),  # East Asian ideograph
    0x215B23: (0x8E82, 0),  # East Asian ideograph
    0x215B24: (0x8E81, 0),  # East Asian ideograph
    0x215B25: (0x8E87, 0),  # East Asian ideograph
    0x215B26: (0x8E89, 0),  # East Asian ideograph
    0x214F31: (0x79FB, 0),  # East Asian ideograph
    0x225B28: (0x747E, 0),  # East Asian ideograph
    0x275B29: (0x8DC3, 0),  # East Asian ideograph
    0x235B2A: (0x9D52, 0),  # East Asian ideograph
    0x215B2B: (0x8EA1, 0),  # East Asian ideograph
    0x235B2C: (0x9D77, 0),  # East Asian ideograph
    0x224F39: (0x7018, 0),  # East Asian ideograph
    0x215B2E: (0x8EAC, 0),  # East Asian ideograph
    0x215B2F: (0x8EB2, 0),  # East Asian ideograph
    0x225B30: (0x747A, 0),  # East Asian ideograph
    0x215B31: (0x8EC0, 0),  # East Asian ideograph
    0x215B32: (0x8ECA, 0),  # East Asian ideograph
    0x275B33: (0x8F67, 0),  # East Asian ideograph
    0x215B34: (0x8ECD, 0),  # East Asian ideograph
    0x215B35: (0x8ECC, 0),  # East Asian ideograph
    0x215B36: (0x8ED2, 0),  # East Asian ideograph
    0x215B37: (0x8ED4, 0),  # East Asian ideograph
    0x215B38: (0x8EDF, 0),  # East Asian ideograph
    0x215B39: (0x8EDB, 0),  # East Asian ideograph
    0x215B3A: (0x8EFB, 0),  # East Asian ideograph
    0x275B3B: (0x8F74, 0),  # East Asian ideograph
    0x215B3C: (0x8EFC, 0),  # East Asian ideograph
    0x215B3D: (0x8F03, 0),  # East Asian ideograph
    0x225B3E: (0x747D, 0),  # East Asian ideograph
    0x235B3F: (0x9D78, 0),  # East Asian ideograph
    0x215B40: (0x8F0A, 0),  # East Asian ideograph
    0x215B41: (0x8F14, 0),  # East Asian ideograph
    0x235B42: (0x9D7E, 0),  # East Asian ideograph
    0x215B43: (0x8F15, 0),  # East Asian ideograph
    0x215B44: (0x8F13, 0),  # East Asian ideograph
    0x215B45: (0x8F26, 0),  # East Asian ideograph
    0x215B46: (0x8F1B, 0),  # East Asian ideograph
    0x235B47: (0x9D69, 0),  # East Asian ideograph
    0x215B48: (0x8F1D, 0),  # East Asian ideograph
    0x215B49: (0x8F29, 0),  # East Asian ideograph
    0x215B4A: (0x8F2A, 0),  # East Asian ideograph
    0x275B4B: (0x8F8E, 0),  # East Asian ideograph
    0x215B4C: (0x8F3B, 0),  # East Asian ideograph
    0x215B4D: (0x8F2F, 0),  # East Asian ideograph
    0x215B4E: (0x8F38, 0),  # East Asian ideograph
    0x235B4F: (0x9D83, 0),  # East Asian ideograph
    0x215B50: (0x8F3E, 0),  # East Asian ideograph
    0x215B51: (0x8F45, 0),  # East Asian ideograph
    0x215B52: (
        0x8F42,
        0,
    ),  # East Asian ideograph (variant of 4B5B52 which maps to 8F42)
    0x215B53: (0x8F3F, 0),  # East Asian ideograph
    0x225B54: (0x749F, 0),  # East Asian ideograph
    0x225B55: (0x749D, 0),  # East Asian ideograph
    0x215B56: (0x8F54, 0),  # East Asian ideograph
    0x225B57: (0x749E, 0),  # East Asian ideograph
    0x215B58: (0x8F5F, 0),  # East Asian ideograph
    0x215B59: (0x8F61, 0),  # East Asian ideograph
    0x215B5A: (0x8F9B, 0),  # East Asian ideograph
    0x215B5B: (0x8F9C, 0),  # East Asian ideograph
    0x215B5C: (0x8F9F, 0),  # East Asian ideograph
    0x224F3A: (0x7023, 0),  # East Asian ideograph
    0x235B5E: (0x9D92, 0),  # East Asian ideograph
    0x215B5F: (0x8FA6, 0),  # East Asian ideograph
    0x225B60: (0x74B2, 0),  # East Asian ideograph
    0x215B61: (0x8FAF, 0),  # East Asian ideograph
    0x215B62: (0x8FB0, 0),  # East Asian ideograph
    0x215B63: (0x8FB1, 0),  # East Asian ideograph
    0x215B64: (0x8FB2, 0),  # East Asian ideograph
    0x295E6A: (0x9EEA, 0),  # East Asian ideograph
    0x225B66: (0x74B4, 0),  # East Asian ideograph
    0x225B67: (0x74AB, 0),  # East Asian ideograph
    0x215B68: (0x8FC4, 0),  # East Asian ideograph
    0x215B69: (0x5DE1, 0),  # East Asian ideograph
    0x215B6A: (0x8FCE, 0),  # East Asian ideograph
    0x215B6B: (0x8FD1, 0),  # East Asian ideograph
    0x215B6C: (0x8FD4, 0),  # East Asian ideograph
    0x275B6D: (0x8FF0, 0),  # East Asian ideograph
    0x215B6E: (0x8FE6, 0),  # East Asian ideograph
    0x215B6F: (0x8FE2, 0),  # East Asian ideograph
    0x235B70: (0x9D96, 0),  # East Asian ideograph
    0x215B71: (0x8FE5, 0),  # East Asian ideograph
    0x6F544B: (0xC379, 0),  # Korean hangul
    0x215B73: (0x8FEB, 0),  # East Asian ideograph
    0x215B74: (0x9001, 0),  # East Asian ideograph
    0x215B75: (0x9006, 0),  # East Asian ideograph
    0x225B76: (0x74B8, 0),  # East Asian ideograph
    0x215B77: (0x9000, 0),  # East Asian ideograph
    0x6F5B78: (0xD329, 0),  # Korean hangul
    0x235B79: (0x9DC0, 0),  # East Asian ideograph
    0x225B7A: (0x74C0, 0),  # East Asian ideograph
    0x23422E: (0x9207, 0),  # East Asian ideograph
    0x215B7C: (0x9005, 0),  # East Asian ideograph
    0x215B7D: (0x9019, 0),  # East Asian ideograph
    0x215B7E: (0x9023, 0),  # East Asian ideograph
    0x214F40: (0x7A40, 0),  # East Asian ideograph
    0x393C52: (0x8D26, 0),  # East Asian ideograph
    0x224F41: (0x703C, 0),  # East Asian ideograph
    0x213941: (0x596E, 0),  # East Asian ideograph
    0x6F4F42: (0xB8E1, 0),  # Korean hangul
    0x6F544C: (0xC37C, 0),  # Korean hangul
    0x4B4F43: (0x7A32, 0),  # East Asian ideograph
    0x213A31: (0x5A9B, 0),  # East Asian ideograph
    0x224F44: (0x7035, 0),  # East Asian ideograph
    0x213A41: (0x5AFB, 0),  # East Asian ideograph
    0x234F45: (0x9832, 0),  # East Asian ideograph
    0x294331: (0x94F1, 0),  # East Asian ideograph
    0x274F46: (0x7A23, 0),  # East Asian ideograph
    0x6F4F47: (0xB8F8, 0),  # Korean hangul
    0x2D4F48: (0x7A42, 0),  # East Asian ideograph
    0x213A32: (0x5ACC, 0),  # East Asian ideograph
    0x294231: (0x94AF, 0),  # East Asian ideograph
    0x214F49: (0x7A61, 0),  # East Asian ideograph
    0x4C3744: (0x65D9, 0),  # East Asian ideograph
    0x274F4A: (0x79FD, 0),  # East Asian ideograph
    0x214F4B: (0x7A6B, 0),  # East Asian ideograph
    0x227631: (0x8008, 0),  # East Asian ideograph
    0x274F4C: (0x7A33, 0),  # East Asian ideograph
    0x6F544E: (0xC384, 0),  # Korean hangul
    0x6F4F4D: (0xB958, 0),  # Korean hangul
    0x6F5361: (0xC229, 0),  # Korean hangul
    0x213A33: (0x5AC1, 0),  # East Asian ideograph
    0x234F4E: (0x9844, 0),  # East Asian ideograph
    0x4B393A: (0x5F09, 0),  # East Asian ideograph
    0x6F4F4F: (0xB95C, 0),  # Korean hangul
    0x334755: (0x6FEC, 0),  # East Asian ideograph
    0x6F4F50: (0xB960, 0),  # Korean hangul
    0x6F4C69: (0xB2DD, 0),  # Korean hangul
    0x23533E: (0x9A0B, 0),  # East Asian ideograph
    0x224F51: (0x7034, 0),  # East Asian ideograph
    0x274564: (0x69DF, 0),  # East Asian ideograph
    0x6F544F: (0xC388, 0),  # Korean hangul
    0x213E77: (0x611B, 0),  # East Asian ideograph
    0x6F4F52: (0xB96D, 0),  # Korean hangul
    0x213A34: (0x5AC9, 0),  # East Asian ideograph
    0x217E79: (0x5BE0, 0),  # East Asian ideograph
    0x224F53: (0x7039, 0),  # East Asian ideograph
    0x224F54: (0x703A, 0),  # East Asian ideograph
    0x395E6F: (0x7A7D, 0),  # East Asian ideograph
    0x6F4F55: (0xB978, 0),  # Korean hangul
    0x23533F: (0x9A09, 0),  # East Asian ideograph
    0x6F4E44: (0xB618, 0),  # Korean hangul
    0x6F4F56: (0xB97C, 0),  # Korean hangul
    0x6F5450: (0xC399, 0),  # Korean hangul
    0x6F4F57: (0xB984, 0),  # Korean hangul
    0x213A35: (0x5ABE, 0),  # East Asian ideograph
    0x696B27: (0x8977, 0),  # East Asian ideograph
    0x234233: (0x91FE, 0),  # East Asian ideograph
    0x3A2F7C: (0x64C0, 0),  # East Asian ideograph
    0x395A2F: (0x58F2, 0),  # East Asian ideograph
    0x334F59: (0x7A93, 0),  # East Asian ideograph
    0x293C57: (0x8F79, 0),  # East Asian ideograph
    0x6F4F5A: (0xB989, 0),  # Korean hangul
    0x215C21: (0x901F, 0),  # East Asian ideograph
    0x215C22: (0x9017, 0),  # East Asian ideograph
    0x215C23: (0x901D, 0),  # East Asian ideograph
    0x215C24: (0x9010, 0),  # East Asian ideograph
    0x225C25: (0x74BF, 0),  # East Asian ideograph
    0x215C26: (0x900D, 0),  # East Asian ideograph
    0x215C27: (0x901E, 0),  # East Asian ideograph
    0x235C28: (0x9DBB, 0),  # East Asian ideograph
    0x274123: (0x6302, 0),  # East Asian ideograph
    0x215C2A: (0x900F, 0),  # East Asian ideograph
    0x215C2B: (0x9022, 0),  # East Asian ideograph
    0x215C2C: (0x9016, 0),  # East Asian ideograph
    0x215C2D: (0x901B, 0),  # East Asian ideograph
    0x215C2E: (0x9014, 0),  # East Asian ideograph
    0x214F5D: (0x7AA9, 0),  # East Asian ideograph
    0x215C30: (0x9035, 0),  # East Asian ideograph
    0x215C31: (0x9031, 0),  # East Asian ideograph
    0x235C32: (0x9DB9, 0),  # East Asian ideograph
    0x275C33: (0x8FDB, 0),  # East Asian ideograph
    0x275C34: (0x8FD0, 0),  # East Asian ideograph
    0x2D4F5E: (0x7AB0, 0),  # East Asian ideograph
    0x215C36: (0x9053, 0),  # East Asian ideograph
    0x215C37: (0x9042, 0),  # East Asian ideograph
    0x215C38: (0x9050, 0),  # East Asian ideograph
    0x275C39: (0x8FBE, 0),  # East Asian ideograph
    0x275C3A: (0x8FDD, 0),  # East Asian ideograph
    0x274F5F: (0x7A77, 0),  # East Asian ideograph
    0x275C3C: (0x8FC2, 0),  # East Asian ideograph
    0x215C3D: (0x904F, 0),  # East Asian ideograph
    0x235C3E: (0x9DD9, 0),  # East Asian ideograph
    0x215C3F: (0x904D, 0),  # East Asian ideograph
    0x215C40: (0x9051, 0),  # East Asian ideograph
    0x214F60: (0x7ABA, 0),  # East Asian ideograph
    0x215C42: (0x903E, 0),  # East Asian ideograph
    0x215C43: (0x9058, 0),  # East Asian ideograph
    0x275C44: (0x8FDC, 0),  # East Asian ideograph
    0x275C45: (0x900A, 0),  # East Asian ideograph
    0x215C46: (0x9063, 0),  # East Asian ideograph
    0x214F61: (0x7AC5, 0),  # East Asian ideograph
    0x275C48: (0x9012, 0),  # East Asian ideograph
    0x215C49: (0x9069, 0),  # East Asian ideograph
    0x215C4A: (0x906E, 0),  # East Asian ideograph
    0x215C4B: (0x9068, 0),  # East Asian ideograph
    0x215C4C: (0x906D, 0),  # East Asian ideograph
    0x214F62: (0x7AC4, 0),  # East Asian ideograph
    0x215C4E: (0x9074, 0),  # East Asian ideograph
    0x275C4F: (0x9009, 0),  # East Asian ideograph
    0x275C50: (0x8FDF, 0),  # East Asian ideograph
    0x215C51: (0x9077, 0),  # East Asian ideograph
    0x215C52: (0x907C, 0),  # East Asian ideograph
    0x275C53: (0x9057, 0),  # East Asian ideograph
    0x215C54: (0x907F, 0),  # East Asian ideograph
    0x215C55: (0x907D, 0),  # East Asian ideograph
    0x275C56: (0x8FC8, 0),  # East Asian ideograph
    0x235C57: (0x9DF2, 0),  # East Asian ideograph
    0x215C58: (0x9082, 0),  # East Asian ideograph
    0x215C59: (0x9080, 0),  # East Asian ideograph
    0x275C5A: (
        0x8FE9,
        0,
    ),  # East Asian ideograph (variant of 2D5C5A which maps to 8FE9)
    0x275C5B: (0x8FB9, 0),  # East Asian ideograph
    0x275C5C: (0x9026, 0),  # East Asian ideograph
    0x275C5D: (0x903B, 0),  # East Asian ideograph
    0x215C5E: (0x9091, 0),  # East Asian ideograph
    0x215C5F: (0x9095, 0),  # East Asian ideograph
    0x215C60: (0x90A3, 0),  # East Asian ideograph
    0x215C61: (0x90A2, 0),  # East Asian ideograph
    0x215C62: (0x90AA, 0),  # East Asian ideograph
    0x215C63: (0x90A6, 0),  # East Asian ideograph
    0x215C64: (0x90B5, 0),  # East Asian ideograph
    0x215C65: (0x90B1, 0),  # East Asian ideograph
    0x215C66: (0x90B8, 0),  # East Asian ideograph
    0x215C67: (0x90CE, 0),  # East Asian ideograph
    0x215C68: (0x90CA, 0),  # East Asian ideograph
    0x4B5564: (0x77C7, 0),  # East Asian ideograph
    0x235C6A: (0x9DED, 0),  # East Asian ideograph
    0x215C6B: (0x90E8, 0),  # East Asian ideograph
    0x215C6C: (0x90ED, 0),  # East Asian ideograph
    0x275C6D: (0x90AE, 0),  # East Asian ideograph
    0x215C6E: (0x90FD, 0),  # East Asian ideograph
    0x215C6F: (0x9102, 0),  # East Asian ideograph
    0x275C70: (0x4E61, 0),  # East Asian ideograph
    0x275C71: (0x90B9, 0),  # East Asian ideograph
    0x215C72: (0x9119, 0),  # East Asian ideograph
    0x275C73: (0x90D1, 0),  # East Asian ideograph
    0x275C74: (0x90BB, 0),  # East Asian ideograph
    0x275C75: (0x9093, 0),  # East Asian ideograph
    0x215C76: (0x9131, 0),  # East Asian ideograph
    0x214F69: (0x7AED, 0),  # East Asian ideograph
    0x215C78: (0x9149, 0),  # East Asian ideograph
    0x215C79: (0x914B, 0),  # East Asian ideograph
    0x215C7A: (0x914A, 0),  # East Asian ideograph
    0x215C7B: (0x9152, 0),  # East Asian ideograph
    0x215C7C: (0x914D, 0),  # East Asian ideograph
    0x215C7D: (0x914C, 0),  # East Asian ideograph
    0x215C7E: (0x9157, 0),  # East Asian ideograph
    0x6F5454: (0xC3DF, 0),  # Korean hangul
    0x6F5A34: (0xCF13, 0),  # Korean hangul
    0x214F6B: (0x7AF6, 0),  # East Asian ideograph
    0x213A39: (0x5AB3, 0),  # East Asian ideograph
    0x234237: (0x9226, 0),  # East Asian ideograph
    0x6F4F6D: (0xB9D8, 0),  # Korean hangul
    0x695A31: (0x64F6, 0),  # East Asian ideograph
    0x6F4E45: (0xB625, 0),  # Korean hangul
    0x234F6F: (0x9857, 0),  # East Asian ideograph
    0x27456A: (0x6988, 0),  # East Asian ideograph
    0x213E7D: (0x6108, 0),  # East Asian ideograph
    0x395821: (0x97E4, 0),  # East Asian ideograph
    0x274F70: (0x5DF4, 0),  # East Asian ideograph (duplicate simplified)
    0x213A3A: (0x5AE1, 0),  # East Asian ideograph
    0x224F71: (0x7052, 0),  # East Asian ideograph
    0x234F72: (0x9856, 0),  # East Asian ideograph
    0x295E7A: (0x9EFE, 0),  # East Asian ideograph
    0x224F73: (0x705C, 0),  # East Asian ideograph
    0x213F39: (0x6163, 0),  # East Asian ideograph
    0x6F4F74: (0xB9E4, 0),  # Korean hangul
    0x6F5456: (0xC3E8, 0),  # Korean hangul
    0x213E7E: (0x60F1, 0),  # East Asian ideograph
    0x214F75: (0x7B1B, 0),  # East Asian ideograph
    0x213A3B: (0x5AD7, 0),  # East Asian ideograph
    0x284E66: (0x6EE2, 0),  # East Asian ideograph
    0x213A21: (0x5A46, 0),  # East Asian ideograph
    0x234F77: (0x9862, 0),  # East Asian ideograph
    0x275235: (0x7F62, 0),  # East Asian ideograph
    0x224F78: (0x7059, 0),  # East Asian ideograph
    0x213A23: (0x5A6A, 0),  # East Asian ideograph
    0x274F79: (0x7B14, 0),  # East Asian ideograph
    0x213A24: (0x5A36, 0),  # East Asian ideograph
    0x6F5457: (0xC3ED, 0),  # Korean hangul
    0x22427E: (0x6AED, 0),  # East Asian ideograph
    0x214F7B: (0x7B50, 0),  # East Asian ideograph
    0x213A26: (0x5A40, 0),  # East Asian ideograph
    0x695E63: (0x6E82, 0),  # East Asian ideograph
    0x275679: (0x80E1, 0),  # East Asian ideograph (duplicate simplified)
    0x224F7C: (0x7061, 0),  # East Asian ideograph
    0x213A27: (0x5A66, 0),  # East Asian ideograph
    0x224F7D: (0x705D, 0),  # East Asian ideograph
    0x223A28: (0x6705, 0),  # East Asian ideograph
    0x335347: (0x81D9, 0),  # East Asian ideograph
    0x293B4F: (0x8F78, 0),  # East Asian ideograph
    0x234F7E: (0x9868, 0),  # East Asian ideograph
    0x6F4F7B: (0xB9F8, 0),  # Korean hangul
    0x6F5458: (0xC3F4, 0),  # Korean hangul
    0x6F5363: (0xC22D, 0),  # Korean hangul
    0x2D5D68: (0x8021, 0),  # East Asian ideograph
    0x394928: (0x6D5C, 0),  # East Asian ideograph
    0x29366A: (0x8D53, 0),  # East Asian ideograph
    0x227A2C: (0x81B5, 0),  # East Asian ideograph
    0x223173: (0x637F, 0),  # East Asian ideograph
    0x2D5179: (0x7E62, 0),  # East Asian ideograph
    0x213A2E: (0x5A92, 0),  # East Asian ideograph
    0x6F5459: (0xC3F5, 0),  # Korean hangul
    0x2D3A2F: (0x58FB, 0),  # East Asian ideograph
    0x4B3351: (0x5204, 0),  # East Asian ideograph
    0x215D21: (0x9163, 0),  # East Asian ideograph
    0x215D22: (0x9165, 0),  # East Asian ideograph
    0x215D23: (0x916C, 0),  # East Asian ideograph
    0x215D24: (0x9169, 0),  # East Asian ideograph
    0x215D25: (0x916A, 0),  # East Asian ideograph
    0x215D26: (0x9175, 0),  # East Asian ideograph
    0x215D27: (0x9178, 0),  # East Asian ideograph
    0x215D28: (0x9177, 0),  # East Asian ideograph
    0x215D29: (0x9187, 0),  # East Asian ideograph
    0x215D2A: (0x9189, 0),  # East Asian ideograph
    0x215D2B: (0x918B, 0),  # East Asian ideograph
    0x215D2C: (0x9183, 0),  # East Asian ideograph
    0x215D2D: (0x9192, 0),  # East Asian ideograph
    0x215D2E: (0x91A3, 0),  # East Asian ideograph
    0x275D2F: (0x915D, 0),  # East Asian ideograph
    0x215D30: (0x919C, 0),  # East Asian ideograph
    0x275D31: (0x533B, 0),  # East Asian ideograph
    0x225D32: (0x7512, 0),  # East Asian ideograph
    0x215D33: (0x91BA, 0),  # East Asian ideograph
    0x275D34: (0x917F, 0),  # East Asian ideograph
    0x275D35: (0x8845, 0),  # East Asian ideograph
    0x215D36: (0x91C7, 0),  # East Asian ideograph
    0x215D37: (0x91C9, 0),  # East Asian ideograph
    0x215D38: (0x91CB, 0),  # East Asian ideograph
    0x235D39: (0x9E1C, 0),  # East Asian ideograph
    0x235D3A: (0x9E1B, 0),  # East Asian ideograph
    0x215D3B: (0x91CE, 0),  # East Asian ideograph
    0x235D3C: (0x9E75, 0),  # East Asian ideograph
    0x275D3D: (0x5398, 0),  # East Asian ideograph
    0x215D3E: (0x91D1, 0),  # East Asian ideograph
    0x215D3F: (0x91DD, 0),  # East Asian ideograph
    0x215D40: (0x91D8, 0),  # East Asian ideograph
    0x215D41: (0x91D7, 0),  # East Asian ideograph
    0x235D42: (0x9E7A, 0),  # East Asian ideograph
    0x215D43: (0x91F5, 0),  # East Asian ideograph
    0x225D44: (0x7524, 0),  # East Asian ideograph
    0x215D45: (0x91E3, 0),  # East Asian ideograph
    0x215D46: (0x91E7, 0),  # East Asian ideograph
    0x235D47: (0x9E80, 0),  # East Asian ideograph
    0x215D48: (0x920D, 0),  # East Asian ideograph
    0x215D49: (0x9215, 0),  # East Asian ideograph
    0x215D4A: (0x9209, 0),  # East Asian ideograph
    0x275D4B: (0x949E, 0),  # East Asian ideograph
    0x215D4C: (0x921E, 0),  # East Asian ideograph
    0x215D4D: (0x9210, 0),  # East Asian ideograph
    0x2D4C5D: (0x7661, 0),  # East Asian ideograph
    0x225D4F: (0x753F, 0),  # East Asian ideograph
    0x215D50: (0x9238, 0),  # East Asian ideograph
    0x225D51: (0x7540, 0),  # East Asian ideograph
    0x225D52: (0x753E, 0),  # East Asian ideograph
    0x215D53: (0x9240, 0),  # East Asian ideograph
    0x215D54: (0x924B, 0),  # East Asian ideograph
    0x235D55: (0x9E90, 0),  # East Asian ideograph
    0x215D56: (0x9264, 0),  # East Asian ideograph
    0x215D57: (0x9251, 0),  # East Asian ideograph
    0x235D58: (0x9E8C, 0),  # East Asian ideograph
    0x215D59: (0x9278, 0),  # East Asian ideograph
    0x215D5A: (0x9280, 0),  # East Asian ideograph
    0x275D5B: (0x94D0, 0),  # East Asian ideograph
    0x215D5C: (0x9285, 0),  # East Asian ideograph
    0x235D5D: (0x9E9B, 0),  # East Asian ideograph
    0x215D5E: (0x9296, 0),  # East Asian ideograph
    0x225D5F: (0x755F, 0),  # East Asian ideograph
    0x215D60: (0x9293, 0),  # East Asian ideograph
    0x275D61: (0x8854, 0),  # East Asian ideograph
    0x215D62: (0x92C5, 0),  # East Asian ideograph
    0x215D63: (0x92BB, 0),  # East Asian ideograph
    0x275D64: (0x9510, 0),  # East Asian ideograph
    0x275D65: (0x94FA, 0),  # East Asian ideograph
    0x275D66: (0x9500, 0),  # East Asian ideograph
    0x215D67: (0x92C1, 0),  # East Asian ideograph
    0x215D68: (0x92E4, 0),  # East Asian ideograph
    0x215D69: (0x92BC, 0),  # East Asian ideograph
    0x215D6A: (0x92D2, 0),  # East Asian ideograph
    0x225D6B: (0x756C, 0),  # East Asian ideograph
    0x215D6C: (0x9336, 0),  # East Asian ideograph
    0x275D6D: (0x952F, 0),  # East Asian ideograph
    0x215D6E: (0x9333, 0),  # East Asian ideograph
    0x215D6F: (0x932F, 0),  # East Asian ideograph
    0x215D70: (0x9322, 0),  # East Asian ideograph
    0x215D71: (0x92FC, 0),  # East Asian ideograph
    0x215D72: (0x932B, 0),  # East Asian ideograph
    0x215D73: (0x931A, 0),  # East Asian ideograph
    0x215D74: (0x9304, 0),  # East Asian ideograph
    0x213A3E: (0x5AE9, 0),  # East Asian ideograph
    0x275D76: (0x9526, 0),  # East Asian ideograph
    0x275D77: (0x9540, 0),  # East Asian ideograph
    0x275D78: (0x9541, 0),  # East Asian ideograph
    0x235D79: (0x9EAF, 0),  # East Asian ideograph
    0x215D7A: (0x9365, 0),  # East Asian ideograph
    0x213A3F: (0x5AD8, 0),  # East Asian ideograph
    0x215D7C: (0x934B, 0),  # East Asian ideograph
    0x215D7D: (0x9328, 0),  # East Asian ideograph
    0x215D7E: (0x9370, 0),  # East Asian ideograph
    0x4B5E3F: (0x922C, 0),  # East Asian ideograph
    0x213A40: (0x5AE6, 0),  # East Asian ideograph
    0x6F5367: (0xC234, 0),  # Korean hangul
    0x233A41: (0x8E61, 0),  # East Asian ideograph
    0x6F5825: (0xC990, 0),  # Korean hangul
    0x6F545D: (0xC434, 0),  # Korean hangul
    0x284971: (0x6D9E, 0),  # East Asian ideograph
    0x224A32: (0x6DFC, 0),  # East Asian ideograph
    0x227A43: (0x81D0, 0),  # East Asian ideograph
    0x213A44: (0x5B0C, 0),  # East Asian ideograph
    0x29366B: (0x8D55, 0),  # East Asian ideograph
    0x233A45: (0x8E74, 0),  # East Asian ideograph
    0x213A46: (0x5B34, 0),  # East Asian ideograph
    0x213A47: (0x5B1D, 0),  # East Asian ideograph
    0x6F545E: (0xC43C, 0),  # Korean hangul
    0x6F5A36: (0xCF1C, 0),  # Korean hangul
    0x273A48: (0x5AD4, 0),  # East Asian ideograph
    0x213A43: (0x5B0B, 0),  # East Asian ideograph
    0x395829: (0x69FB, 0),  # East Asian ideograph
    0x6F4C3E: (0xB1D0, 0),  # Korean hangul
    0x4B3A49: (0x5B37, 0),  # East Asian ideograph
    0x2D3B54: (0x5C4A, 0),  # East Asian ideograph
    0x6F5923: (0xCC2E, 0),  # Korean hangul
    0x213A4A: (0x5B30, 0),  # East Asian ideograph
    0x287855: (0x80EB, 0),  # East Asian ideograph
    0x233A4B: (0x8E69, 0),  # East Asian ideograph
    0x213A4C: (0x5B40, 0),  # East Asian ideograph
    0x6F545F: (0xC43F, 0),  # Korean hangul
    0x213A4D: (0x5B50, 0),  # East Asian ideograph
    0x213A4E: (0x5B51, 0),  # East Asian ideograph
    0x217A4F: (0x59EE, 0),  # East Asian ideograph
    0x225B3F: (0x7485, 0),  # East Asian ideograph
    0x295E7C: (0x9F0B, 0),  # East Asian ideograph
    0x29456F: (0x9538, 0),  # East Asian ideograph
    0x6F5460: (0xC464, 0),  # Korean hangul
    0x233A52: (0x8E83, 0),  # East Asian ideograph
    0x213A45: (0x5AF5, 0),  # East Asian ideograph
    0x334243: (0x52B9, 0),  # East Asian ideograph
    0x233A53: (0x8E84, 0),  # East Asian ideograph
    0x2D592C: (0x8B01, 0),  # East Asian ideograph
    0x294335: (0x94F5, 0),  # East Asian ideograph
    0x4C3A55: (0x6741, 0),  # East Asian ideograph
    0x4B623B: (0x9D12, 0),  # East Asian ideograph
    0x217A56: (0x59FD, 0),  # East Asian ideograph
    0x6F5461: (0xC465, 0),  # Korean hangul
    0x213A57: (0x5B5F, 0),  # East Asian ideograph
    0x6F5A39: (0xCF2C, 0),  # Korean hangul
    0x213A58: (0x5B63, 0),  # East Asian ideograph
    0x692544: (0x30C4, 0),  # Katakana letter TU
    0x225622: (0x728D, 0),  # East Asian ideograph
    0x215E21: (0x937E, 0),  # East Asian ideograph
    0x275E22: (0x9524, 0),  # East Asian ideograph
    0x275E23: (0x9539, 0),  # East Asian ideograph
    0x215E24: (0x935B, 0),  # East Asian ideograph
    0x275E25: (0x9551, 0),  # East Asian ideograph
    0x215E26: (0x9394, 0),  # East Asian ideograph
    0x275E27: (0x9547, 0),  # East Asian ideograph
    0x275E28: (0x9501, 0),  # East Asian ideograph
    0x215E29: (0x93A2, 0),  # East Asian ideograph
    0x275E2A: (0x954D, 0),  # East Asian ideograph
    0x275E2B: (0x955C, 0),  # East Asian ideograph
    0x275E2C: (0x955D, 0),  # East Asian ideograph
    0x215E2D: (0x93D6, 0),  # East Asian ideograph
    0x275E2E: (0x955E, 0),  # East Asian ideograph
    0x215E2F: (0x93DF, 0),  # East Asian ideograph
    0x275E30: (0x94FF, 0),  # East Asian ideograph
    0x275E31: (0x94FE, 0),  # East Asian ideograph
    0x215E32: (0x93E2, 0),  # East Asian ideograph
    0x215E33: (0x93DC, 0),  # East Asian ideograph
    0x215E34: (0x93E4, 0),  # East Asian ideograph
    0x225E35: (0x7598, 0),  # East Asian ideograph
    0x215E36: (0x93CD, 0),  # East Asian ideograph
    0x235E37: (0x9EC8, 0),  # East Asian ideograph
    0x215E39: (0x9403, 0),  # East Asian ideograph
    0x215E3A: (0x942E, 0),  # East Asian ideograph
    0x225E3B: (0x75A3, 0),  # East Asian ideograph
    0x215E3C: (0x9433, 0),  # East Asian ideograph
    0x215E3D: (0x9435, 0),  # East Asian ideograph
    0x215E3E: (0x943A, 0),  # East Asian ideograph
    0x215E3F: (0x9438, 0),  # East Asian ideograph
    0x215E40: (0x9432, 0),  # East Asian ideograph
    0x223A60: (0x675D, 0),  # East Asian ideograph
    0x215E42: (0x9451, 0),  # East Asian ideograph
    0x215E43: (0x9444, 0),  # East Asian ideograph
    0x215E44: (0x9463, 0),  # East Asian ideograph
    0x215E45: (0x9460, 0),  # East Asian ideograph
    0x215E46: (0x9472, 0),  # East Asian ideograph
    0x215E47: (0x9470, 0),  # East Asian ideograph
    0x215E48: (0x947E, 0),  # East Asian ideograph
    0x215E49: (0x947C, 0),  # East Asian ideograph
    0x235E4A: (0x9ED0, 0),  # East Asian ideograph
    0x215E4B: (0x947F, 0),  # East Asian ideograph
    0x215E4C: (0x9577, 0),  # East Asian ideograph
    0x215E4D: (0x9580, 0),  # East Asian ideograph
    0x215E4E: (0x9582, 0),  # East Asian ideograph
    0x215E4F: (0x9583, 0),  # East Asian ideograph
    0x215E50: (0x9589, 0),  # East Asian ideograph
    0x215E51: (0x9594, 0),  # East Asian ideograph
    0x215E52: (0x958F, 0),  # East Asian ideograph
    0x235E53: (0x9EDA, 0),  # East Asian ideograph
    0x215E54: (0x9591, 0),  # East Asian ideograph
    0x235E55: (0x9EDF, 0),  # East Asian ideograph
    0x215E56: (0x9592, 0),  # East Asian ideograph
    0x215E57: (0x9598, 0),  # East Asian ideograph
    0x215E58: (0x95A1, 0),  # East Asian ideograph
    0x235E59: (0x9EE5, 0),  # East Asian ideograph
    0x215E5A: (0x95A9, 0),  # East Asian ideograph
    0x215E5B: (0x95A3, 0),  # East Asian ideograph
    0x215E5C: (0x95A5, 0),  # East Asian ideograph
    0x215E5D: (0x95A4, 0),  # East Asian ideograph
    0x215E5E: (0x95B1, 0),  # East Asian ideograph
    0x215E5F: (0x95AD, 0),  # East Asian ideograph
    0x235E60: (0x9EEE, 0),  # East Asian ideograph
    0x215E61: (0x95CA, 0),  # East Asian ideograph
    0x215E62: (0x95CB, 0),  # East Asian ideograph
    0x215E63: (0x95CC, 0),  # East Asian ideograph
    0x215E64: (0x95C8, 0),  # East Asian ideograph
    0x215E65: (0x95C6, 0),  # East Asian ideograph
    0x235E66: (0x9EF0, 0),  # East Asian ideograph
    0x215E67: (0x95D6, 0),  # East Asian ideograph
    0x215E68: (0x95D0, 0),  # East Asian ideograph
    0x215E69: (0x95DC, 0),  # East Asian ideograph
    0x215E6A: (0x95E1, 0),  # East Asian ideograph
    0x215E6B: (0x95E2, 0),  # East Asian ideograph
    0x215E6C: (0x961C, 0),  # East Asian ideograph
    0x215E6D: (0x9621, 0),  # East Asian ideograph
    0x215E6E: (0x9632, 0),  # East Asian ideograph
    0x215E6F: (0x9631, 0),  # East Asian ideograph
    0x215E70: (0x962E, 0),  # East Asian ideograph
    0x215E71: (0x962A, 0),  # East Asian ideograph
    0x215E72: (0x9640, 0),  # East Asian ideograph
    0x215E73: (0x963F, 0),  # East Asian ideograph
    0x215E74: (0x963B, 0),  # East Asian ideograph
    0x215E75: (0x9644, 0),  # East Asian ideograph
    0x215E76: (0x9650, 0),  # East Asian ideograph
    0x235E77: (0x9EFC, 0),  # East Asian ideograph
    0x215E78: (0x964B, 0),  # East Asian ideograph
    0x215E79: (0x964D, 0),  # East Asian ideograph
    0x235E7A: (0x9EFD, 0),  # East Asian ideograph
    0x215E7B: (0x9663, 0),  # East Asian ideograph
    0x235E7C: (0x9EFF, 0),  # East Asian ideograph
    0x215E7D: (0x9661, 0),  # East Asian ideograph
    0x225E7E: (0x7603, 0),  # East Asian ideograph
    0x6F5465: (0xC479, 0),  # Korean hangul
    0x223A6B: (0x6763, 0),  # East Asian ideograph
    0x223A6E: (0x6753, 0),  # East Asian ideograph
    0x2D355C: (0x5434, 0),  # East Asian ideograph
    0x213A6F: (0x5B98, 0),  # East Asian ideograph
    0x6F5466: (0xC480, 0),  # Korean hangul
    0x6F5440: (0xC328, 0),  # Korean hangul
    0x293A70: (0x8E9C, 0),  # East Asian ideograph
    0x213A4B: (0x5B38, 0),  # East Asian ideograph
    0x294936: (0x95F3, 0),  # East Asian ideograph
    0x215821: (0x896A, 0),  # East Asian ideograph
    0x233A71: (0x8EA9, 0),  # East Asian ideograph
    0x692524: (0x30A4, 0),  # Katakana letter I
    0x213A72: (0x5BA5, 0),  # East Asian ideograph
    0x6F595F: (0xCE04, 0),  # Korean hangul
    0x2D3B52: (0x6EBA, 0),  # East Asian ideograph
    0x223A75: (0x6793, 0),  # East Asian ideograph
    0x23424A: (0x9216, 0),  # East Asian ideograph
    0x6F2521: (0x315C, 0),  # Korean hangul
    0x4B4767: (
        0x6DB5,
        0,
    ),  # East Asian ideograph (variant of 214767 which maps to 6DB5)
    0x28342C: (0x63BA, 0),  # East Asian ideograph
    0x295A44: (0x9E32, 0),  # East Asian ideograph
    0x223A78: (0x677C, 0),  # East Asian ideograph
    0x692523: (0x30A3, 0),  # Katakana letter small I
    0x292524: (0x848C, 0),  # East Asian ideograph
    0x29322A: (0x8BB5, 0),  # East Asian ideograph
    0x223A7A: (0x679F, 0),  # East Asian ideograph
    0x226065: (0x76A4, 0),  # East Asian ideograph
    0x23424B: (0x9211, 0),  # East Asian ideograph
    0x4D472C: (0x952A, 0),  # East Asian ideograph
    0x4D5934: (0x9CA6, 0),  # East Asian ideograph
    0x213A7C: (0x5BAE, 0),  # East Asian ideograph
    0x692527: (0x30A7, 0),  # Katakana letter small E
    0x213D2E: (0x5EEC, 0),  # East Asian ideograph
    0x233A7D: (0x8EB6, 0),  # East Asian ideograph
    0x692528: (0x30A8, 0),  # Katakana letter E
    0x6F5469: (0xC4D5, 0),  # Korean hangul
    0x69252A: (0x30AA, 0),  # Katakana letter O
    0x283B22: (0x4E2B, 0),  # East Asian ideograph
    0x22652C: (0x7892, 0),  # East Asian ideograph
    0x28342E: (0x63BC, 0),  # East Asian ideograph
    0x235359: (0x9A2F, 0),  # East Asian ideograph
    0x22252D: (0x5D47, 0),  # East Asian ideograph
    0x2D4829: (0x51CF, 0),  # East Asian ideograph
    0x6F5027: (0xBA4B, 0),  # Korean hangul
    0x23252F: (0x84E7, 0),  # East Asian ideograph
    0x215F21: (0x9664, 0),  # East Asian ideograph
    0x215F22: (0x966A, 0),  # East Asian ideograph
    0x215F23: (0x9673, 0),  # East Asian ideograph
    0x215F24: (0x9678, 0),  # East Asian ideograph
    0x215F25: (0x9675, 0),  # East Asian ideograph
    0x215F26: (0x9672, 0),  # East Asian ideograph
    0x215F27: (0x9676, 0),  # East Asian ideograph
    0x215F28: (0x9677, 0),  # East Asian ideograph
    0x215F29: (0x9674, 0),  # East Asian ideograph
    0x215F2A: (0x9670, 0),  # East Asian ideograph
    0x215F2B: (0x968A, 0),  # East Asian ideograph
    0x215F2C: (0x968E, 0),  # East Asian ideograph
    0x215F2D: (0x968B, 0),  # East Asian ideograph
    0x215F2E: (0x967D, 0),  # East Asian ideograph
    0x235F2F: (0x9F0F, 0),  # East Asian ideograph
    0x215F30: (0x9686, 0),  # East Asian ideograph
    0x235F31: (0x9F10, 0),  # East Asian ideograph
    0x235F32: (0x9F12, 0),  # East Asian ideograph
    0x235F33: (0x9F16, 0),  # East Asian ideograph
    0x235F34: (0x9F17, 0),  # East Asian ideograph
    0x215F35: (0x9695, 0),  # East Asian ideograph
    0x215F36: (0x969C, 0),  # East Asian ideograph
    0x235F37: (0x9F1A, 0),  # East Asian ideograph
    0x215F38: (0x96A7, 0),  # East Asian ideograph
    0x215F39: (0x96A8, 0),  # East Asian ideograph
    0x215F3A: (0x96AA, 0),  # East Asian ideograph
    0x215F3B: (0x96B1, 0),  # East Asian ideograph
    0x215F3C: (0x96B4, 0),  # East Asian ideograph
    0x215F3D: (0x96B8, 0),  # East Asian ideograph
    0x225F3E: (0x7625, 0),  # East Asian ideograph
    0x225F3F: (0x761A, 0),  # East Asian ideograph
    0x215F40: (0x96C7, 0),  # East Asian ideograph
    0x215F41: (0x96C6, 0),  # East Asian ideograph
    0x215F42: (0x96C4, 0),  # East Asian ideograph
    0x215F43: (0x96C1, 0),  # East Asian ideograph
    0x215F44: (0x96C5, 0),  # East Asian ideograph
    0x215F45: (0x96CD, 0),  # East Asian ideograph
    0x215F46: (0x96CB, 0),  # East Asian ideograph
    0x215F47: (0x96C9, 0),  # East Asian ideograph
    0x215F48: (0x96CC, 0),  # East Asian ideograph
    0x215F49: (0x96D5, 0),  # East Asian ideograph
    0x215F4A: (0x96D6, 0),  # East Asian ideograph
    0x215F4B: (0x96DC, 0),  # East Asian ideograph
    0x215F4C: (0x96DE, 0),  # East Asian ideograph
    0x215F4D: (0x96DB, 0),  # East Asian ideograph
    0x215F4E: (0x96D9, 0),  # East Asian ideograph
    0x215F4F: (0x96E2, 0),  # East Asian ideograph
    0x225F50: (0x7622, 0),  # East Asian ideograph
    0x225F51: (0x762F, 0),  # East Asian ideograph
    0x215F52: (0x96EA, 0),  # East Asian ideograph
    0x215F53: (0x96EF, 0),  # East Asian ideograph
    0x215F54: (0x96F2, 0),  # East Asian ideograph
    0x215F55: (0x96FB, 0),  # East Asian ideograph
    0x215F56: (0x96F7, 0),  # East Asian ideograph
    0x215F57: (0x96F9, 0),  # East Asian ideograph
    0x215F58: (0x96F6, 0),  # East Asian ideograph
    0x215F59: (0x9700, 0),  # East Asian ideograph
    0x23424F: (0x92A2, 0),  # East Asian ideograph
    0x215F5B: (0x9704, 0),  # East Asian ideograph
    0x215F5C: (0x9709, 0),  # East Asian ideograph
    0x215F5D: (0x9706, 0),  # East Asian ideograph
    0x225F5E: (0x763B, 0),  # East Asian ideograph
    0x215F5F: (0x970E, 0),  # East Asian ideograph
    0x225F60: (0x763C, 0),  # East Asian ideograph
    0x215F61: (0x970F, 0),  # East Asian ideograph
    0x225F62: (0x7635, 0),  # East Asian ideograph
    0x215F63: (0x9713, 0),  # East Asian ideograph
    0x235F64: (0x9F3D, 0),  # East Asian ideograph
    0x215F65: (0x971E, 0),  # East Asian ideograph
    0x215F66: (0x972A, 0),  # East Asian ideograph
    0x225F67: (0x7648, 0),  # East Asian ideograph
    0x225F68: (0x764E, 0),  # East Asian ideograph
    0x235F69: (0x9F41, 0),  # East Asian ideograph
    0x225F6A: (0x7643, 0),  # East Asian ideograph
    0x215F6B: (0x973D, 0),  # East Asian ideograph
    0x215F6C: (0x973E, 0),  # East Asian ideograph
    0x215F6D: (0x9744, 0),  # East Asian ideograph
    0x215F6E: (0x9742, 0),  # East Asian ideograph
    0x225F6F: (0x7649, 0),  # East Asian ideograph
    0x215F70: (0x9751, 0),  # East Asian ideograph
    0x215F71: (0xFA1C, 0),  # East Asian ideograph
    0x215F72: (
        0x975B,
        0,
    ),  # East Asian ideograph (variant of 4B5F72 which maps to 975B)
    0x215F73: (0x975C, 0),  # East Asian ideograph
    0x215F74: (0x975E, 0),  # East Asian ideograph
    0x225F75: (0x7654, 0),  # East Asian ideograph
    0x215F76: (0x9761, 0),  # East Asian ideograph
    0x215F78: (0x9766, 0),  # East Asian ideograph
    0x235F79: (0x9F4E, 0),  # East Asian ideograph
    0x225F7A: (0x765C, 0),  # East Asian ideograph
    0x235F7B: (0x9F4F, 0),  # East Asian ideograph
    0x235F7C: (0x9F54, 0),  # East Asian ideograph
    0x215F7D: (0x977C, 0),  # East Asian ideograph
    0x235F7E: (0x9F55, 0),  # East Asian ideograph
    0x216540: (0x4F66, 0),  # East Asian ideograph
    0x692541: (0x30C1, 0),  # Katakana letter TI
    0x6F5622: (0xC644, 0),  # Korean hangul
    0x6F546E: (0xC500, 0),  # Korean hangul
    0x6F502B: (0xBA54, 0),  # Korean hangul
    0x215829: (0x898F, 0),  # East Asian ideograph
    0x234251: (0x9230, 0),  # East Asian ideograph
    0x225C28: (0x74B5, 0),  # East Asian ideograph
    0x216544: (0x4F67, 0),  # East Asian ideograph
    0x695429: (0x5726, 0),  # East Asian ideograph
    0x6F515C: (0xBD88, 0),  # Korean hangul
    0x292546: (0x8368, 0),  # East Asian ideograph
    0x233145: (0x89DC, 0),  # East Asian ideograph
    0x692547: (0x30C7, 0),  # Katakana letter DE
    0x225C29: (0x74BA, 0),  # East Asian ideograph
    0x213A48: (0x5B2A, 0),  # East Asian ideograph
    0x6F492D: (0xAC85, 0),  # Korean hangul
    0x69254A: (0x30CA, 0),  # Katakana letter NA
    0x29254B: (0x835B, 0),  # East Asian ideograph
    0x2D482F: (0x6E07, 0),  # East Asian ideograph
    0x6F5442: (0xC330, 0),  # Korean hangul
    0x70586F: (0x4EEB, 0),  # East Asian ideograph
    0x274142: (0x6325, 0),  # East Asian ideograph
    0x6F502D: (0xBA58, 0),  # Korean hangul
    0x23254D: (0x8553, 0),  # East Asian ideograph
    0x21654E: (0x4F5A, 0),  # East Asian ideograph
    0x335065: (0x7A45, 0),  # East Asian ideograph
    0x2E3B22: (0x690F, 0),  # East Asian ideograph
    0x224F61: (0x7044, 0),  # East Asian ideograph
    0x692550: (0x30D0, 0),  # Katakana letter BA
    0x6F5C71: (0xD57C, 0),  # Korean hangul
    0x222551: (0x5D8E, 0),  # East Asian ideograph
    0x6F586B: (0xCB58, 0),  # Korean hangul
    0x335834: (0x89E7, 0),  # East Asian ideograph
    0x2D593D: (0x8AE9, 0),  # East Asian ideograph
    0x4B4476: (0x685F, 0),  # East Asian ideograph
    0x692555: (0x30D5, 0),  # Katakana letter HU
    0x216556: (0x4F82, 0),  # East Asian ideograph
    0x6F5A3A: (0xCF2D, 0),  # Korean hangul
    0x6F502F: (0xBA64, 0),  # Korean hangul
    0x692557: (0x30D7, 0),  # Katakana letter PU
    0x294942: (0x9606, 0),  # East Asian ideograph
    0x234255: (0x9248, 0),  # East Asian ideograph
    0x692558: (0x30D8, 0),  # Katakana letter HE
    0x47347B: (0x8C2B, 0),  # East Asian ideograph
    0x6F5262: (0xC0AF, 0),  # Korean hangul
    0x23255A: (0x8546, 0),  # East Asian ideograph
    0x216021: (0x978D, 0),  # East Asian ideograph
    0x226022: (0x7664, 0),  # East Asian ideograph
    0x236023: (0x9F57, 0),  # East Asian ideograph
    0x226024: (0x7659, 0),  # East Asian ideograph
    0x216025: (0x97A0, 0),  # East Asian ideograph
    0x216026: (0x97A3, 0),  # East Asian ideograph
    0x216027: (0x97A6, 0),  # East Asian ideograph
    0x236028: (0x9F60, 0),  # East Asian ideograph
    0x216029: (0x97C3, 0),  # East Asian ideograph
    0x21602A: (0x97C1, 0),  # East Asian ideograph
    0x22602B: (0x765F, 0),  # East Asian ideograph
    0x21602C: (0x97CB, 0),  # East Asian ideograph
    0x21602D: (0x97CC, 0),  # East Asian ideograph
    0x21602E: (0x97D3, 0),  # East Asian ideograph
    0x21602F: (0x97DC, 0),  # East Asian ideograph
    0x216030: (0x97ED, 0),  # East Asian ideograph
    0x216031: (0x97F3, 0),  # East Asian ideograph
    0x226032: (0x7667, 0),  # East Asian ideograph
    0x216033: (0x7ADF, 0),  # East Asian ideograph
    0x216034: (0x97F6, 0),  # East Asian ideograph
    0x226035: (0x766A, 0),  # East Asian ideograph
    0x216036: (
        0x97FF,
        0,
    ),  # East Asian ideograph (variant of 456036 which maps to 97FF)
    0x226037: (0x766D, 0),  # East Asian ideograph
    0x226038: (0x766F, 0),  # East Asian ideograph
    0x216039: (0x9803, 0),  # East Asian ideograph
    0x22603A: (0x7670, 0),  # East Asian ideograph
    0x21603B: (0x9806, 0),  # East Asian ideograph
    0x21603C: (0x9808, 0),  # East Asian ideograph
    0x21603D: (0x9810, 0),  # East Asian ideograph
    0x21603E: (0x980A, 0),  # East Asian ideograph
    0x21603F: (0x9811, 0),  # East Asian ideograph
    0x226040: (0x7676, 0),  # East Asian ideograph
    0x226041: (0x7677, 0),  # East Asian ideograph
    0x216042: (0x980C, 0),  # East Asian ideograph
    0x216043: (0x9817, 0),  # East Asian ideograph
    0x216044: (
        0x9818,
        0,
    ),  # East Asian ideograph (variant of 4B6044 which maps to 9818)
    0x216045: (0x9821, 0),  # East Asian ideograph
    0x216046: (0x982D, 0),  # East Asian ideograph
    0x216047: (0x9830, 0),  # East Asian ideograph
    0x226048: (0x7680, 0),  # East Asian ideograph
    0x21582F: (0x89B2, 0),  # East Asian ideograph
    0x22604A: (0x768B, 0),  # East Asian ideograph
    0x21604B: (0x9837, 0),  # East Asian ideograph
    0x21604C: (0x9824, 0),  # East Asian ideograph
    0x21604D: (0x9846, 0),  # East Asian ideograph
    0x21604E: (0x9854, 0),  # East Asian ideograph
    0x21604F: (0x984D, 0),  # East Asian ideograph
    0x216050: (0x984C, 0),  # East Asian ideograph
    0x216051: (0x984E, 0),  # East Asian ideograph
    0x226052: (0x7695, 0),  # East Asian ideograph
    0x216053: (
        0x985E,
        0,
    ),  # East Asian ideograph (variant of 4B6053 which maps to 985E)
    0x216054: (0x985A, 0),  # East Asian ideograph
    0x226055: (0x656B, 0),  # East Asian ideograph
    0x216056: (0x9867, 0),  # East Asian ideograph
    0x216057: (0x986B, 0),  # East Asian ideograph
    0x216058: (0x986F, 0),  # East Asian ideograph
    0x226059: (0x7699, 0),  # East Asian ideograph
    0x21605A: (0x9870, 0),  # East Asian ideograph
    0x21605B: (0x98A8, 0),  # East Asian ideograph
    0x21605C: (0x98AF, 0),  # East Asian ideograph
    0x22605D: (0x769C, 0),  # East Asian ideograph
    0x21605E: (0x98B3, 0),  # East Asian ideograph
    0x22605F: (0x769D, 0),  # East Asian ideograph
    0x216060: (0x98BA, 0),  # East Asian ideograph
    0x236061: (0x9F93, 0),  # East Asian ideograph
    0x216062: (0x98C4, 0),  # East Asian ideograph
    0x216063: (0x98DB, 0),  # East Asian ideograph
    0x216064: (0x98DF, 0),  # East Asian ideograph
    0x216065: (0x98E2, 0),  # East Asian ideograph
    0x226066: (0x76A5, 0),  # East Asian ideograph
    0x226067: (0x76A6, 0),  # East Asian ideograph
    0x216068: (0x98ED, 0),  # East Asian ideograph
    0x216069: (0x98EA, 0),  # East Asian ideograph
    0x21606A: (0x98EE, 0),  # East Asian ideograph
    0x23606B: (0x9FA0, 0),  # East Asian ideograph
    0x21606C: (0x98FC, 0),  # East Asian ideograph
    0x21606D: (0x98F4, 0),  # East Asian ideograph
    0x21606E: (0x98FD, 0),  # East Asian ideograph
    0x21606F: (0x98FE, 0),  # East Asian ideograph
    0x216070: (0x9903, 0),  # East Asian ideograph
    0x216071: (0x990A, 0),  # East Asian ideograph
    0x236072: (0x9FA4, 0),  # East Asian ideograph
    0x216073: (0x9909, 0),  # East Asian ideograph
    0x226074: (0x76B8, 0),  # East Asian ideograph
    0x216075: (0x9912, 0),  # East Asian ideograph
    0x216076: (0x9918, 0),  # East Asian ideograph
    0x226077: (0x76BD, 0),  # East Asian ideograph
    0x216078: (0x9905, 0),  # East Asian ideograph
    0x216079: (0x9928, 0),  # East Asian ideograph
    0x21607A: (0x991E, 0),  # East Asian ideograph
    0x21607B: (0x991B, 0),  # East Asian ideograph
    0x21607C: (0x9921, 0),  # East Asian ideograph
    0x21607D: (0x9935, 0),  # East Asian ideograph
    0x21607E: (0x993E, 0),  # East Asian ideograph
    0x6F5369: (0xC258, 0),  # Korean hangul
    0x6F5033: (0xBA71, 0),  # Korean hangul
    0x213A5B: (0x5B6B, 0),  # East Asian ideograph
    0x69256B: (0x30EB, 0),  # Katakana letter RU
    0x69256C: (0x30EC, 0),  # Katakana letter RE
    0x293670: (0x8D49, 0),  # East Asian ideograph
    0x69656D: (0x7E83, 0),  # East Asian ideograph
    0x224F67: (0x7047, 0),  # East Asian ideograph
    0x235172: (0x994C, 0),  # East Asian ideograph
    0x69256F: (0x30EF, 0),  # Katakana letter WA
    0x2E4C35: (0x6DE5, 0),  # East Asian ideograph
    0x6F5034: (0xBA74, 0),  # Korean hangul
    0x213A5C: (0x5B70, 0),  # East Asian ideograph
    0x6F5934: (0xCC59, 0),  # Korean hangul
    0x4D4F39: (0x988C, 0),  # East Asian ideograph
    0x292571: (0x835E, 0),  # East Asian ideograph
    0x226573: (0x78E0, 0),  # East Asian ideograph
    0x6F4E4C: (0xB6B1, 0),  # Korean hangul
    0x292574: (0x83B8, 0),  # East Asian ideograph
    0x4B3A47: (0x88CA, 0),  # East Asian ideograph
    0x6F5035: (0xBA78, 0),  # Korean hangul
    0x692575: (0x30F5, 0),  # Katakana letter small KA
    0x294948: (0x960F, 0),  # East Asian ideograph
    0x213378: (0x5275, 0),  # East Asian ideograph
    0x225C32: (0x74CC, 0),  # East Asian ideograph
    0x216576: (0x4F9C, 0),  # East Asian ideograph
    0x215021: (0x7B4D, 0),  # East Asian ideograph
    0x6F5C6C: (0xD56D, 0),  # Korean hangul
    0x232577: (0x858C, 0),  # East Asian ideograph
    0x214B6A: (0x74CA, 0),  # East Asian ideograph
    0x224F69: (0x7049, 0),  # East Asian ideograph
    0x216940: (0x5133, 0),  # East Asian ideograph
    0x692578: (0x309C, 0),  # Katakana-hiragana semi-voiced sound mark
    0x275023: (0x8345, 0),  # East Asian ideograph
    0x2E742E: (0x7516, 0),  # East Asian ideograph
    0x6F5479: (0xC53D, 0),  # Korean hangul
    0x6F5024: (0xBA40, 0),  # Korean hangul
    0x6F5036: (0xBA83, 0),  # Korean hangul
    0x213A5E: (0x5B71, 0),  # East Asian ideograph
    0x294949: (0x9608, 0),  # East Asian ideograph
    0x225025: (0x7066, 0),  # East Asian ideograph
    0x2E257B: (0x5D1F, 0),  # East Asian ideograph
    0x6F5026: (0xBA49, 0),  # Korean hangul
    0x6F4A5F: (0xAECD, 0),  # Korean hangul
    0x225027: (0x7065, 0),  # East Asian ideograph
    0x235369: (0x9A36, 0),  # East Asian ideograph
    0x225028: (0x7068, 0),  # East Asian ideograph
    0x234F26: (0x9816, 0),  # East Asian ideograph
    0x215029: (0x7B95, 0),  # East Asian ideograph
    0x276272: (0x9EE9, 0),  # East Asian ideograph
    0x213A5F: (0x5B75, 0),  # East Asian ideograph
    0x27502A: (0x94B3, 0),  # East Asian ideograph
    0x27502B: (0x7B3A, 0),  # East Asian ideograph
    0x6F502C: (0xBA55, 0),  # Korean hangul
    0x224F6B: (0x7055, 0),  # East Asian ideograph
    0x23536A: (0x9A2E, 0),  # East Asian ideograph
    0x2D502D: (0x7B5D, 0),  # East Asian ideograph
    0x4C4339: (0x69DE, 0),  # East Asian ideograph
    0x6F502E: (0xBA5C, 0),  # Korean hangul
    0x6F5038: (0xBA85, 0),  # Korean hangul
    0x213A60: (0x5B78, 0),  # East Asian ideograph
    0x21502F: (0x7BAD, 0),  # East Asian ideograph
    0x215030: (0x7BC4, 0),  # East Asian ideograph
    0x216122: (0x993D, 0),  # East Asian ideograph
    0x226123: (0x76CB, 0),  # East Asian ideograph
    0x216124: (0x9952, 0),  # East Asian ideograph
    0x216125: (0x9951, 0),  # East Asian ideograph
    0x226126: (0x76CC, 0),  # East Asian ideograph
    0x216127: (0x995E, 0),  # East Asian ideograph
    0x216128: (0x9996, 0),  # East Asian ideograph
    0x216129: (0x9999, 0),  # East Asian ideograph
    0x21612A: (0x99A5, 0),  # East Asian ideograph
    0x21612B: (0x99A8, 0),  # East Asian ideograph
    0x21612C: (0x99AC, 0),  # East Asian ideograph
    0x21612D: (0x99AE, 0),  # East Asian ideograph
    0x21612E: (0x99AD, 0),  # East Asian ideograph
    0x21612F: (0x99B3, 0),  # East Asian ideograph
    0x216130: (0x99B1, 0),  # East Asian ideograph
    0x216131: (0x99B4, 0),  # East Asian ideograph
    0x216132: (0x99C1, 0),  # East Asian ideograph
    0x275033: (0x8282, 0),  # East Asian ideograph
    0x216134: (0x99DD, 0),  # East Asian ideograph
    0x216135: (0x99D5, 0),  # East Asian ideograph
    0x216136: (0x99DF, 0),  # East Asian ideograph
    0x216137: (0x99DB, 0),  # East Asian ideograph
    0x216138: (0x99D2, 0),  # East Asian ideograph
    0x216139: (0x99D9, 0),  # East Asian ideograph
    0x21613A: (0x99D1, 0),  # East Asian ideograph
    0x21613B: (0x99ED, 0),  # East Asian ideograph
    0x21613C: (0x99F1, 0),  # East Asian ideograph
    0x21613D: (0x9A01, 0),  # East Asian ideograph
    0x21613E: (0x99FF, 0),  # East Asian ideograph
    0x21613F: (0x99E2, 0),  # East Asian ideograph
    0x216140: (0x9A0E, 0),  # East Asian ideograph
    0x216141: (0x9A19, 0),  # East Asian ideograph
    0x216142: (0x9A16, 0),  # East Asian ideograph
    0x216143: (0x9A2B, 0),  # East Asian ideograph
    0x226144: (0x76ED, 0),  # East Asian ideograph
    0x216145: (0x9A37, 0),  # East Asian ideograph
    0x216146: (0x9A43, 0),  # East Asian ideograph
    0x216147: (0x9A45, 0),  # East Asian ideograph
    0x226148: (0x76F1, 0),  # East Asian ideograph
    0x216149: (0x9A3E, 0),  # East Asian ideograph
    0x21614A: (0x9A55, 0),  # East Asian ideograph
    0x21614B: (0x9A5A, 0),  # East Asian ideograph
    0x21614C: (0x9A5B, 0),  # East Asian ideograph
    0x21614D: (0x9A57, 0),  # East Asian ideograph
    0x21614E: (0x9A5F, 0),  # East Asian ideograph
    0x22614F: (0x7708, 0),  # East Asian ideograph
    0x226150: (0x7707, 0),  # East Asian ideograph
    0x275038: (0x7BAC, 0),  # East Asian ideograph
    0x216152: (0x9AA8, 0),  # East Asian ideograph
    0x216153: (0x9AAF, 0),  # East Asian ideograph
    0x226154: (0x770A, 0),  # East Asian ideograph
    0x216155: (0x9AB7, 0),  # East Asian ideograph
    0x216156: (0x9AB8, 0),  # East Asian ideograph
    0x215039: (0x7BE4, 0),  # East Asian ideograph
    0x216158: (0x9ACF, 0),  # East Asian ideograph
    0x226159: (0x76FB, 0),  # East Asian ideograph
    0x21615A: (0x9AD4, 0),  # East Asian ideograph
    0x21615B: (0x9AD2, 0),  # East Asian ideograph
    0x21615C: (0x9AD8, 0),  # East Asian ideograph
    0x21615D: (0x9AE5, 0),  # East Asian ideograph
    0x22615E: (0x772B, 0),  # East Asian ideograph
    0x21615F: (0x9AEE, 0),  # East Asian ideograph
    0x216160: (0x9AFB, 0),  # East Asian ideograph
    0x216161: (0x9AED, 0),  # East Asian ideograph
    0x216162: (0x9B03, 0),  # East Asian ideograph
    0x216163: (0x9B06, 0),  # East Asian ideograph
    0x216164: (0x9B0D, 0),  # East Asian ideograph
    0x216165: (0x9B1A, 0),  # East Asian ideograph
    0x216166: (0x9B22, 0),  # East Asian ideograph
    0x216167: (0x9B25, 0),  # East Asian ideograph
    0x216168: (0x9B27, 0),  # East Asian ideograph
    0x27503C: (0x7B5B, 0),  # East Asian ideograph
    0x21616A: (0x9B31, 0),  # East Asian ideograph
    0x21616B: (0x9B32, 0),  # East Asian ideograph
    0x21616C: (0x9B3C, 0),  # East Asian ideograph
    0x21616D: (0x9B41, 0),  # East Asian ideograph
    0x21616E: (0x9B42, 0),  # East Asian ideograph
    0x22616F: (0x7721, 0),  # East Asian ideograph
    0x216170: (0x9B44, 0),  # East Asian ideograph
    0x216171: (0x9B4F, 0),  # East Asian ideograph
    0x216172: (0x9B54, 0),  # East Asian ideograph
    0x216173: (0x9B58, 0),  # East Asian ideograph
    0x216174: (0x9B5A, 0),  # East Asian ideograph
    0x226175: (0x7739, 0),  # East Asian ideograph
    0x226176: (0x772F, 0),  # East Asian ideograph
    0x216177: (0x9B91, 0),  # East Asian ideograph
    0x216178: (0x9BAB, 0),  # East Asian ideograph
    0x216179: (0x9BAE, 0),  # East Asian ideograph
    0x21617A: (0x9BAA, 0),  # East Asian ideograph
    0x21617B: (0x9BCA, 0),  # East Asian ideograph
    0x21617C: (0x9BC9, 0),  # East Asian ideograph
    0x21617D: (0x9BE8, 0),  # East Asian ideograph
    0x21617E: (0x9BE7, 0),  # East Asian ideograph
    0x215040: (0x7BF7, 0),  # East Asian ideograph
    0x275041: (0x7B80, 0),  # East Asian ideograph
    0x225042: (0x7086, 0),  # East Asian ideograph
    0x6F503C: (0xBAAB, 0),  # Korean hangul
    0x29596B: (0x9CA1, 0),  # East Asian ideograph
    0x335F3D: (0x96B7, 0),  # East Asian ideograph
    0x29494F: (0x960A, 0),  # East Asian ideograph
    0x6F5043: (0xBAC3, 0),  # Korean hangul
    0x4B5044: (
        0x7C27,
        0,
    ),  # East Asian ideograph (variant of 215044 which maps to 7C27)
    0x275045: (0x7BAA, 0),  # East Asian ideograph
    0x2E3D73: (0x7A1C, 0),  # East Asian ideograph
    0x275046: (0x7BD1, 0),  # East Asian ideograph
    0x6F5047: (0xBB34, 0),  # Korean hangul
    0x6F503D: (0xBAAC, 0),  # Korean hangul
    0x213A65: (0x5B87, 0),  # East Asian ideograph
    0x294950: (0x960C, 0),  # East Asian ideograph
    0x235048: (0x98B8, 0),  # East Asian ideograph
    0x225C3A: (0x74D4, 0),  # East Asian ideograph
    0x27583A: (0x8BA3, 0),  # East Asian ideograph
    0x225049: (0x7084, 0),  # East Asian ideograph
    0x2D594C: (0x8B72, 0),  # East Asian ideograph
    0x6F5960: (0xCE20, 0),  # Korean hangul
    0x22504A: (0x7081, 0),  # East Asian ideograph
    0x235370: (0x9A41, 0),  # East Asian ideograph
    0x21504B: (0x7C3D, 0),  # East Asian ideograph
    0x4D3032: (0x88AE, 0),  # East Asian ideograph
    0x6F5A3D: (0xCF54, 0),  # Korean hangul
    0x27504C: (0x7BEE, 0),  # East Asian ideograph
    0x274153: (0x6363, 0),  # East Asian ideograph
    0x4D5C6B: (0x9D50, 0),  # East Asian ideograph
    0x213A66: (0x5B88, 0),  # East Asian ideograph
    0x21504D: (0x7C4C, 0),  # East Asian ideograph
    0x234264: (0x925E, 0),  # East Asian ideograph
    0x2D3B77: (0x5CE9, 0),  # East Asian ideograph
    0x21504E: (0x7C4D, 0),  # East Asian ideograph
    0x6F5025: (0xBA48, 0),  # Korean hangul
    0x2D504F: (0x7C58, 0),  # East Asian ideograph
    0x69542A: (0x5737, 0),  # East Asian ideograph
    0x293B59: (0x8F82, 0),  # East Asian ideograph
    0x4B4B2B: (0x7363, 0),  # East Asian ideograph
    0x275050: (0x7B3C, 0),  # East Asian ideograph
    0x275051: (0x7C41, 0),  # East Asian ideograph
    0x6F503F: (0xBAB8, 0),  # Korean hangul
    0x213A67: (0x5B89, 0),  # East Asian ideograph
    0x294952: (0x960D, 0),  # East Asian ideograph
    0x275052: (0x7B7E, 0),  # East Asian ideograph (duplicate simplified)
    0x6F5963: (0xCE35, 0),  # Korean hangul
    0x2D3B78: (0x5CEF, 0),  # East Asian ideograph
    0x275053: (0x7BF1, 0),  # East Asian ideograph
    0x4D594E: (0x9BF5, 0),  # East Asian ideograph
    0x3F614C: (0x99C5, 0),  # East Asian ideograph
    0x275054: (0x7BA9, 0),  # East Asian ideograph
    0x4B6258: (0x68BA, 0),  # East Asian ideograph
    0x275055: (0x5401, 0),  # East Asian ideograph
    0x6F245A: (0x3139, 0),  # Korean hangul
    0x225056: (0x7088, 0),  # East Asian ideograph
    0x6F5040: (0xBAB9, 0),  # Korean hangul
    0x213A68: (0x5B85, 0),  # East Asian ideograph
    0x21583E: (0x8A0C, 0),  # East Asian ideograph
    0x2D3B79: (0x5D8B, 0),  # East Asian ideograph
    0x6F5058: (0xBB88, 0),  # Korean hangul
    0x2D594F: (0x8B83, 0),  # East Asian ideograph
    0x225059: (0x708C, 0),  # East Asian ideograph
    0x224B31: (0x6E5D, 0),  # East Asian ideograph
    0x216221: (0x9C13, 0),  # East Asian ideograph
    0x226222: (0x7725, 0),  # East Asian ideograph
    0x216223: (0x9BFD, 0),  # East Asian ideograph
    0x216224: (0x9C2D, 0),  # East Asian ideograph
    0x216225: (0x9C25, 0),  # East Asian ideograph
    0x226226: (0x7734, 0),  # East Asian ideograph
    0x216227: (0x9C3E, 0),  # East Asian ideograph
    0x216228: (0x9C3B, 0),  # East Asian ideograph
    0x216229: (0x9C54, 0),  # East Asian ideograph
    0x21622A: (0x9C57, 0),  # East Asian ideograph
    0x21622B: (0x9C56, 0),  # East Asian ideograph
    0x21622C: (0x9C49, 0),  # East Asian ideograph
    0x22622D: (0x7747, 0),  # East Asian ideograph
    0x21622E: (0x9C78, 0),  # East Asian ideograph
    0x21622F: (0x9CE5, 0),  # East Asian ideograph
    0x216230: (0x9CE9, 0),  # East Asian ideograph
    0x226231: (0x7745, 0),  # East Asian ideograph
    0x226232: (0x774D, 0),  # East Asian ideograph
    0x216233: (0x9CF3, 0),  # East Asian ideograph
    0x216234: (0x9D06, 0),  # East Asian ideograph
    0x216235: (0x9D09, 0),  # East Asian ideograph
    0x216236: (0x9D15, 0),  # East Asian ideograph
    0x226237: (0x774E, 0),  # East Asian ideograph
    0x216238: (0x9D28, 0),  # East Asian ideograph
    0x216239: (0x9D26, 0),  # East Asian ideograph
    0x22623A: (0x775F, 0),  # East Asian ideograph
    0x21505F: (0x7CBD, 0),  # East Asian ideograph
    0x21623C: (0x9D3B, 0),  # East Asian ideograph
    0x21623D: (0x9D3F, 0),  # East Asian ideograph
    0x22623E: (0x7752, 0),  # East Asian ideograph
    0x21623F: (0x9D51, 0),  # East Asian ideograph
    0x216240: (0x9D60, 0),  # East Asian ideograph
    0x215060: (0x7CB9, 0),  # East Asian ideograph
    0x226242: (0x7758, 0),  # East Asian ideograph
    0x216243: (0x9D72, 0),  # East Asian ideograph
    0x226244: (0x7756, 0),  # East Asian ideograph
    0x226245: (0x775A, 0),  # East Asian ideograph
    0x216246: (0x9DB4, 0),  # East Asian ideograph
    0x216247: (0x9DAF, 0),  # East Asian ideograph
    0x216248: (0x9DC2, 0),  # East Asian ideograph
    0x216249: (0x9DD3, 0),  # East Asian ideograph
    0x21624A: (0x9DD7, 0),  # East Asian ideograph
    0x21624B: (0x9DE5, 0),  # East Asian ideograph
    0x21624C: (0x9DF9, 0),  # East Asian ideograph
    0x215062: (0x7CCA, 0),  # East Asian ideograph
    0x21624E: (0x9E1A, 0),  # East Asian ideograph
    0x22624F: (0x7762, 0),  # East Asian ideograph
    0x216250: (0x9E79, 0),  # East Asian ideograph
    0x216251: (0x9E7D, 0),  # East Asian ideograph
    0x226252: (0x7780, 0),  # East Asian ideograph
    0x216253: (0x9E7F, 0),  # East Asian ideograph
    0x216254: (0x9E82, 0),  # East Asian ideograph
    0x216255: (0x9E8B, 0),  # East Asian ideograph
    0x226256: (0x776F, 0),  # East Asian ideograph
    0x216257: (0x9E92, 0),  # East Asian ideograph
    0x216258: (0x9E93, 0),  # East Asian ideograph
    0x224B33: (0x6E30, 0),  # East Asian ideograph
    0x21625A: (0x9E9F, 0),  # East Asian ideograph
    0x21625B: (0x9EA5, 0),  # East Asian ideograph
    0x21625C: (0x9EA9, 0),  # East Asian ideograph
    0x21625D: (0x9EB4, 0),  # East Asian ideograph
    0x21625E: (0x9EB5, 0),  # East Asian ideograph
    0x22625F: (0x7785, 0),  # East Asian ideograph
    0x216260: (0x9EBC, 0),  # East Asian ideograph
    0x216261: (0x9EBE, 0),  # East Asian ideograph
    0x216262: (0x9EC3, 0),  # East Asian ideograph
    0x216263: (0x9ECD, 0),  # East Asian ideograph
    0x216264: (0x9ECE, 0),  # East Asian ideograph
    0x216265: (0x9ECF, 0),  # East Asian ideograph
    0x226266: (
        0x778B,
        0,
    ),  # East Asian ideograph (variant of 4C6266 which maps to 778B)
    0x216267: (0x58A8, 0),  # East Asian ideograph
    0x216268: (0x9ED8, 0),  # East Asian ideograph
    0x216269: (0x9ED4, 0),  # East Asian ideograph
    0x22626A: (0x778D, 0),  # East Asian ideograph
    0x21626B: (0x9EDC, 0),  # East Asian ideograph
    0x21626C: (0x9EDB, 0),  # East Asian ideograph
    0x21626D: (0x9EDD, 0),  # East Asian ideograph
    0x21626E: (0x9EE0, 0),  # East Asian ideograph
    0x21626F: (0x9EE8, 0),  # East Asian ideograph
    0x216270: (0x9EEF, 0),  # East Asian ideograph
    0x235068: (0x98F1, 0),  # East Asian ideograph
    0x226272: (0x7798, 0),  # East Asian ideograph
    0x226273: (0x7796, 0),  # East Asian ideograph
    0x216274: (0x9F0E, 0),  # East Asian ideograph
    0x226275: (0x77A2, 0),  # East Asian ideograph
    0x226276: (0x7799, 0),  # East Asian ideograph
    0x216277: (0x9F19, 0),  # East Asian ideograph
    0x216278: (0x9F20, 0),  # East Asian ideograph
    0x216279: (0x9F2C, 0),  # East Asian ideograph
    0x22627A: (0x77B5, 0),  # East Asian ideograph
    0x21627B: (0x9F3B, 0),  # East Asian ideograph
    0x21627C: (0x9F3E, 0),  # East Asian ideograph
    0x22627D: (0x77B7, 0),  # East Asian ideograph
    0x21627E: (0x9F4B, 0),  # East Asian ideograph
    0x6F5044: (0xBAFC, 0),  # Korean hangul
    0x27506B: (0x7CAE, 0),  # East Asian ideograph
    0x6F5964: (0xCE58, 0),  # Korean hangul
    0x225C41: (0x74DB, 0),  # East Asian ideograph
    0x236040: (0x9F6F, 0),  # East Asian ideograph
    0x23506C: (0x98EB, 0),  # East Asian ideograph
    0x6F506D: (0xBC14, 0),  # Korean hangul
    0x23315E: (0x89F5, 0),  # East Asian ideograph
    0x6F506E: (0xBC15, 0),  # Korean hangul
    0x4B4049: (0x62D0, 0),  # East Asian ideograph
    0x234F34: (0x982B, 0),  # East Asian ideograph
    0x22506F: (0x70A7, 0),  # East Asian ideograph
    0x27415A: (0x5C4F, 0),  # East Asian ideograph
    0x696273: (0x78B5, 0),  # East Asian ideograph
    0x275070: (0x7EAA, 0),  # East Asian ideograph
    0x215843: (0x8A13, 0),  # East Asian ideograph
    0x225071: (0x70B5, 0),  # East Asian ideograph
    0x275072: (0x7EA2, 0),  # East Asian ideograph
    0x295A65: (0x9E39, 0),  # East Asian ideograph
    0x215073: (0x7D09, 0),  # East Asian ideograph
    0x396179: (0x5C20, 0),  # East Asian ideograph
    0x275074: (0x7EA6, 0),  # East Asian ideograph
    0x27415B: (0x631A, 0),  # East Asian ideograph
    0x6F5046: (0xBB18, 0),  # Korean hangul
    0x275075: (0x7EA5, 0),  # East Asian ideograph
    0x215844: (0x8A2A, 0),  # East Asian ideograph
    0x275076: (0x7EBA, 0),  # East Asian ideograph
    0x213B21: (0x5BC6, 0),  # East Asian ideograph
    0x275077: (0x7EB9, 0),  # East Asian ideograph
    0x213B22: (0x5BC7, 0),  # East Asian ideograph
    0x235379: (0x9A42, 0),  # East Asian ideograph
    0x215078: (0x7D0A, 0),  # East Asian ideograph
    0x6F5729: (0xC7B0, 0),  # Korean hangul
    0x213B23: (0x5BC5, 0),  # East Asian ideograph
    0x6F5C72: (0xD584, 0),  # Korean hangul
    0x6F5079: (0xBC2D, 0),  # Korean hangul
    0x6F536D: (0xC27C, 0),  # Korean hangul
    0x29495A: (0x9612, 0),  # East Asian ideograph
    0x27507A: (0x7EAD, 0),  # East Asian ideograph
    0x213B25: (0x5BC2, 0),  # East Asian ideograph
    0x22507B: (0x70E5, 0),  # East Asian ideograph
    0x213B26: (0x5BBF, 0),  # East Asian ideograph
    0x21507C: (0x7D15, 0),  # East Asian ideograph
    0x224F7B: (0x705E, 0),  # East Asian ideograph
    0x23537A: (0x9A44, 0),  # East Asian ideograph
    0x22507D: (0x70D3, 0),  # East Asian ideograph
    0x234F37: (0x9820, 0),  # East Asian ideograph
    0x27507E: (0x7EBD, 0),  # East Asian ideograph
    0x335276: (0x8061, 0),  # East Asian ideograph
    0x6F5048: (0xBB35, 0),  # Korean hangul
    0x215846: (0x8A1D, 0),  # East Asian ideograph
    0x2D3B2A: (0x5EBD, 0),  # East Asian ideograph
    0x2D5957: (0x7AEA, 0),  # East Asian ideograph
    0x4B386C: (0x5841, 0),  # East Asian ideograph
    0x295A68: (0x9E3A, 0),  # East Asian ideograph
    0x453336: (0x5B82, 0),  # East Asian ideograph
    0x224B39: (0x6E6B, 0),  # East Asian ideograph
    0x213B2D: (0x5BE8, 0),  # East Asian ideograph
    0x273B2E: (0x5BDD, 0),  # East Asian ideograph
    0x6F5049: (0xBB36, 0),  # Korean hangul
    0x213A71: (0x5B9B, 0),  # East Asian ideograph
    0x6F5965: (0xCE59, 0),  # Korean hangul
    0x213B2F: (0x5BE4, 0),  # East Asian ideograph
    0x4B515A: (0x7E01, 0),  # East Asian ideograph
    0x216321: (0x9F52, 0),  # East Asian ideograph
    0x216322: (0x9F5F, 0),  # East Asian ideograph
    0x216323: (0x9F63, 0),  # East Asian ideograph
    0x216324: (
        0x9F61,
        0,
    ),  # East Asian ideograph (variant of 456324 which maps to 9F61)
    0x216325: (0x9F66, 0),  # East Asian ideograph
    0x216326: (0x9F5C, 0),  # East Asian ideograph
    0x233B31: (0x8ECE, 0),  # East Asian ideograph
    0x216328: (0x9F6A, 0),  # East Asian ideograph
    0x216329: (0x9F77, 0),  # East Asian ideograph
    0x21632A: (0x9F72, 0),  # East Asian ideograph
    0x21632B: (0x9F8D, 0),  # East Asian ideograph
    0x22632C: (0x77BC, 0),  # East Asian ideograph
    0x21632D: (0x9F9C, 0),  # East Asian ideograph
    0x216330: (0x8288, 0),  # East Asian ideograph
    0x213B33: (0x5BDF, 0),  # East Asian ideograph
    0x6F504A: (0xBB38, 0),  # Korean hangul
    0x226335: (0x77CD, 0),  # East Asian ideograph
    0x29307D: (0x89CF, 0),  # East Asian ideograph
    0x696733: (0x81A4, 0),  # East Asian ideograph
    0x225C47: (0x74DE, 0),  # East Asian ideograph
    0x6F4C3F: (0xB1D4, 0),  # Korean hangul
    0x213B35: (0x5BEC, 0),  # East Asian ideograph
    0x706340: (0x61B7, 0),  # East Asian ideograph
    0x45462B: (0x7688, 0),  # East Asian ideograph
    0x226345: (0x77DE, 0),  # East Asian ideograph
    0x226346: (0x77DF, 0),  # East Asian ideograph
    0x23537D: (0x9A48, 0),  # East Asian ideograph
    0x224B3B: (0x6E8B, 0),  # East Asian ideograph
    0x213B37: (0x5BEB, 0),  # East Asian ideograph
    0x335738: (0x880F, 0),  # East Asian ideograph
    0x69634E: (0x7A43, 0),  # East Asian ideograph
    0x22634F: (0x77E7, 0),  # East Asian ideograph
    0x274160: (0x63B4, 0),  # East Asian ideograph
    0x226352: (0x77E6, 0),  # East Asian ideograph
    0x226355: (0x77EC, 0),  # East Asian ideograph
    0x273B39: (0x5B9D, 0),  # East Asian ideograph
    0x69254D: (0x30CD, 0),  # Katakana letter NE
    0x226359: (0x77F0, 0),  # East Asian ideograph
    0x22635A: (0x77F1, 0),  # East Asian ideograph
    0x22635C: (0x77F4, 0),  # East Asian ideograph
    0x217B3A: (0x5A38, 0),  # East Asian ideograph
    0x226360: (0x77FC, 0),  # East Asian ideograph
    0x213B3B: (0x5BFA, 0),  # East Asian ideograph
    0x23537E: (0x9A4C, 0),  # East Asian ideograph
    0x226367: (0x77F8, 0),  # East Asian ideograph
    0x226368: (0x77FB, 0),  # East Asian ideograph
    0x277B3C: (0x5A05, 0),  # East Asian ideograph
    0x355739: (0x9C76, 0),  # East Asian ideograph
    0x234944: (0x95AB, 0),  # East Asian ideograph
    0x226370: (0x7809, 0),  # East Asian ideograph
    0x226371: (0x7806, 0),  # East Asian ideograph
    0x226373: (0x7819, 0),  # East Asian ideograph
    0x226374: (0x7811, 0),  # East Asian ideograph
    0x293B3E: (0x8F71, 0),  # East Asian ideograph
    0x4C6376: (0x7839, 0),  # East Asian ideograph
    0x226378: (0x7812, 0),  # East Asian ideograph
    0x223B3F: (0x67A1, 0),  # East Asian ideograph
    0x213B40: (0x5C07, 0),  # East Asian ideograph
    0x4B5E27: (0x93AD, 0),  # East Asian ideograph
    0x273B42: (0x5BFB, 0),  # East Asian ideograph
    0x6F504D: (0xBB3D, 0),  # Korean hangul
    0x6F5935: (0xCC60, 0),  # Korean hangul
    0x294960: (0x9619, 0),  # East Asian ideograph
    0x213B43: (0x5C0D, 0),  # East Asian ideograph
    0x223A31: (0x6710, 0),  # East Asian ideograph
    0x273B44: (0x5BFC, 0),  # East Asian ideograph
    0x224B3E: (0x6E76, 0),  # East Asian ideograph
    0x234F3D: (0x9833, 0),  # East Asian ideograph
    0x2D4850: (0x6EDA, 0),  # East Asian ideograph
    0x293B47: (0x8F77, 0),  # East Asian ideograph
    0x6F504E: (0xBB44, 0),  # Korean hangul
    0x275F39: (0x968F, 0),  # East Asian ideograph
    0x23573F: (0x9BA8, 0),  # East Asian ideograph
    0x274B74: (0x74EF, 0),  # East Asian ideograph
    0x217B48: (0x5A50, 0),  # East Asian ideograph
    0x213B49: (0x5C24, 0),  # East Asian ideograph
    0x234E3B: (0x97C5, 0),  # East Asian ideograph
    0x4B4053: (0x627A, 0),  # East Asian ideograph
    0x213B4B: (0x5C31, 0),  # East Asian ideograph
    0x273B4C: (0x5C34, 0),  # East Asian ideograph
    0x6F504F: (0xBB47, 0),  # Korean hangul
    0x275F3A: (0x9669, 0),  # East Asian ideograph
    0x2D625F: (0x83FB, 0),  # East Asian ideograph
    0x213634: (0x5501, 0),  # East Asian ideograph
    0x213B4E: (0x5C3A, 0),  # East Asian ideograph
    0x394956: (0x792E, 0),  # East Asian ideograph
    0x2D7552: (0x579B, 0),  # East Asian ideograph
    0x213B4F: (0x5C3C, 0),  # East Asian ideograph
    0x69562C: (0x599B, 0),  # East Asian ideograph
    0x294E54: (0x97EA, 0),  # East Asian ideograph
    0x692574: (0x30F4, 0),  # Katakana letter VU
    0x233B51: (0x8EFF, 0),  # East Asian ideograph
    0x6F5050: (0xBB49, 0),  # Korean hangul
    0x275F3B: (0x9690, 0),  # East Asian ideograph
    0x213635: (0x54FC, 0),  # East Asian ideograph
    0x27516C: (0x7F1D, 0),  # East Asian ideograph
    0x4B4537: (0x6804, 0),  # East Asian ideograph
    0x213B54: (0x5C46, 0),  # East Asian ideograph
    0x45304C: (0x69A6, 0),  # East Asian ideograph
    0x234F40: (0x982E, 0),  # East Asian ideograph
    0x2D4853: (0x7001, 0),  # East Asian ideograph
    0x224A3D: (0x6DA4, 0),  # East Asian ideograph
    0x213B56: (0x5C48, 0),  # East Asian ideograph
    0x6F5051: (0xBB4D, 0),  # Korean hangul
    0x275F3C: (0x9647, 0),  # East Asian ideograph
    0x334277: (0x65EF, 0),  # East Asian ideograph
    0x213B58: (0x5C4B, 0),  # East Asian ideograph
    0x213B59: (0x5C4D, 0),  # East Asian ideograph
    0x23316B: (0x89FF, 0),  # East Asian ideograph
    0x213B5A: (0x5C55, 0),  # East Asian ideograph
    0x213B5B: (0x5C51, 0),  # East Asian ideograph
    0x226424: (0x781B, 0),  # East Asian ideograph
    0x216425: (0x5187, 0),  # East Asian ideograph
    0x226426: (0x782C, 0),  # East Asian ideograph
    0x226427: (0x7823, 0),  # East Asian ideograph
    0x226428: (0x782B, 0),  # East Asian ideograph
    0x216429: (0x4E28, 0),  # East Asian ideograph
    0x22642A: (0x7829, 0),  # East Asian ideograph
    0x22642D: (0x7822, 0),  # East Asian ideograph
    0x21642E: (0x4E31, 0),  # East Asian ideograph
    0x2D3748: (0x8B5F, 0),  # East Asian ideograph
    0x226431: (0x7835, 0),  # East Asian ideograph
    0x226432: (0x7833, 0),  # East Asian ideograph
    0x226433: (0x782E, 0),  # East Asian ideograph
    0x216434: (0x4E42, 0),  # East Asian ideograph
    0x226435: (0x7820, 0),  # East Asian ideograph
    0x216437: (0x738D, 0),  # East Asian ideograph
    0x226438: (0x783D, 0),  # East Asian ideograph
    0x22643B: (0x781F, 0),  # East Asian ideograph
    0x21643C: (0x4E5C, 0),  # East Asian ideograph
    0x22643D: (0x7831, 0),  # East Asian ideograph
    0x21643F: (0x6C39, 0),  # East Asian ideograph
    0x274168: (0x6320, 0),  # East Asian ideograph
    0x6F5053: (0xBB50, 0),  # Korean hangul
    0x275F3E: (0x53EA, 0),  # East Asian ideograph (duplicate simplified)
    0x226444: (0x784D, 0),  # East Asian ideograph
    0x216446: (0x4E85, 0),  # East Asian ideograph
    0x273B61: (0x5C42, 0),  # East Asian ideograph
    0x226448: (0x7848, 0),  # East Asian ideograph
    0x226449: (0x7853, 0),  # East Asian ideograph
    0x22644A: (0x7854, 0),  # East Asian ideograph
    0x22644B: (0x7845, 0),  # East Asian ideograph
    0x22644C: (0x7852, 0),  # East Asian ideograph
    0x295938: (0x9CDF, 0),  # East Asian ideograph
    0x22644E: (0x7850, 0),  # East Asian ideograph
    0x22644F: (0x7858, 0),  # East Asian ideograph
    0x216450: (0x4EA0, 0),  # East Asian ideograph
    0x216451: (0x4EA2, 0),  # East Asian ideograph
    0x226452: (0x7847, 0),  # East Asian ideograph
    0x233B63: (0x8F27, 0),  # East Asian ideograph
    0x216455: (
        0x4EB6,
        0,
    ),  # East Asian ideograph (variant of 4B6455 which maps to 4EB6)
    0x226456: (0x784C, 0),  # East Asian ideograph
    0x695630: (0x5CBC, 0),  # East Asian ideograph
    0x216458: (0x4EB9, 0),  # East Asian ideograph
    0x223B64: (0x67B7, 0),  # East Asian ideograph
    0x22645A: (0x7868, 0),  # East Asian ideograph
    0x22645B: (0x786D, 0),  # East Asian ideograph
    0x21645E: (0x4EC9, 0),  # East Asian ideograph
    0x226460: (0x7864, 0),  # East Asian ideograph
    0x226461: (0x785C, 0),  # East Asian ideograph
    0x216462: (0x4ECE, 0),  # East Asian ideograph (not in Unicode)
    0x216463: (0x4EE8, 0),  # East Asian ideograph
    0x215852: (0x8A54, 0),  # East Asian ideograph
    0x213639: (0x54FA, 0),  # East Asian ideograph
    0x226466: (0x786A, 0),  # East Asian ideograph
    0x226469: (0x7886, 0),  # East Asian ideograph
    0x21646B: (0x4EE1, 0),  # East Asian ideograph
    0x22646C: (0x787F, 0),  # East Asian ideograph
    0x22646D: (0x7887, 0),  # East Asian ideograph
    0x213C2A: (0x5D84, 0),  # East Asian ideograph
    0x226470: (0x7894, 0),  # East Asian ideograph
    0x696471: (0x7CC0, 0),  # East Asian ideograph
    0x216472: (0x4F08, 0),  # East Asian ideograph
    0x216473: (0x4F0E, 0),  # East Asian ideograph
    0x696474: (0x7CD8, 0),  # East Asian ideograph
    0x216475: (0x4F03, 0),  # East Asian ideograph
    0x226476: (0x788F, 0),  # East Asian ideograph
    0x234F44: (0x982F, 0),  # East Asian ideograph
    0x6F544A: (0xC378, 0),  # Korean hangul
    0x21647C: (0x4F22, 0),  # East Asian ideograph
    0x22647E: (0x7899, 0),  # East Asian ideograph
    0x213B6B: (0x5CB7, 0),  # East Asian ideograph
    0x225C52: (0x74E7, 0),  # East Asian ideograph
    0x27516D: (0x603B, 0),  # East Asian ideograph
    0x223B6D: (0x6802, 0),  # East Asian ideograph
    0x695632: (0x5CC5, 0),  # East Asian ideograph
    0x213B6E: (0x5CA1, 0),  # East Asian ideograph
    0x4C3A5B: (0x6859, 0),  # East Asian ideograph
    0x213B6F: (0x5CAB, 0),  # East Asian ideograph
    0x6F5056: (0xBB61, 0),  # Korean hangul
    0x294969: (0x961A, 0),  # East Asian ideograph
    0x215854: (0x8A50, 0),  # East Asian ideograph
    0x21363B: (0x54EE, 0),  # East Asian ideograph
    0x21762A: (0x57FB, 0),  # East Asian ideograph
    0x27583F: (0x8BAA, 0),  # East Asian ideograph
    0x213B71: (0x5CB1, 0),  # East Asian ideograph
    0x6F5961: (0xCE21, 0),  # Korean hangul
    0x213B72: (0x5CD9, 0),  # East Asian ideograph
    0x275F2C: (0x9636, 0),  # East Asian ideograph
    0x223B74: (0x67DF, 0),  # East Asian ideograph
    0x6F5057: (0xBB63, 0),  # Korean hangul
    0x233B75: (0x8F17, 0),  # East Asian ideograph
    0x23576B: (0x9BBB, 0),  # East Asian ideograph
    0x213B77: (0x5CE8, 0),  # East Asian ideograph
    0x216622: (0x4FE4, 0),  # East Asian ideograph
    0x6F4E53: (0xB729, 0),  # Korean hangul
    0x223B78: (0x6806, 0),  # East Asian ideograph
    0x223B79: (0x67AE, 0),  # East Asian ideograph
    0x213B7A: (0x5CEA, 0),  # East Asian ideograph
    0x336054: (0x985B, 0),  # East Asian ideograph
    0x213B7B: (0x5D07, 0),  # East Asian ideograph
    0x27527A: (0x804B, 0),  # East Asian ideograph
    0x213B7C: (0x5D06, 0),  # East Asian ideograph
    0x216627: (0x4FC5, 0),  # East Asian ideograph
    0x6F773E: (0xCB4C, 0),  # Korean hangul
    0x692435: (0x3055, 0),  # Hiragana letter SA
    0x233B7D: (0x8F2D, 0),  # East Asian ideograph
    0x455746: (0x672F, 0),  # East Asian ideograph
    0x213B7E: (0x5D16, 0),  # East Asian ideograph
    0x6F5059: (0xBB8C, 0),  # Korean hangul
    0x216629: (0x4FC9, 0),  # East Asian ideograph
    0x4B516A: (0x7EF7, 0),  # East Asian ideograph
    0x6F7737: (0xC5AB, 0),  # Korean hangul
    0x6F5A67: (0xD0A5, 0),  # Korean hangul
    0x6F5D23: (0xD5DD, 0),  # Korean hangul
    0x2D485C: (0x6F44, 0),  # East Asian ideograph
    0x6F505A: (0xBBA4, 0),  # Korean hangul
    0x21363F: (0x54E9, 0),  # East Asian ideograph
    0x22262F: (0x5DAE, 0),  # East Asian ideograph
    0x27516E: (0x7EB5, 0),  # East Asian ideograph
    0x283462: (0x6322, 0),  # East Asian ideograph
    0x334C7B: (0x767A, 0),  # East Asian ideograph
    0x216527: (0x4EF5, 0),  # East Asian ideograph
    0x216528: (0x4F07, 0),  # East Asian ideograph
    0x226529: (0x7893, 0),  # East Asian ideograph
    0x21652A: (0x4F00, 0),  # East Asian ideograph
    0x21652C: (0x4F0B, 0),  # East Asian ideograph
    0x22652D: (0x7896, 0),  # East Asian ideograph
    0x22652F: (0x78B2, 0),  # East Asian ideograph
    0x6F5371: (0xC288, 0),  # Korean hangul
    0x226531: (0x78A1, 0),  # East Asian ideograph
    0x216532: (0x4F3B, 0),  # East Asian ideograph
    0x292633: (0x84E3, 0),  # East Asian ideograph
    0x216536: (0x4F58, 0),  # East Asian ideograph
    0x216537: (0x4F62, 0),  # East Asian ideograph
    0x216539: (0x4F64, 0),  # East Asian ideograph
    0x21653A: (0x4F49, 0),  # East Asian ideograph
    0x22653B: (0x78A4, 0),  # East Asian ideograph
    0x22653E: (0x78B4, 0),  # East Asian ideograph
    0x21653F: (0x4F3E, 0),  # East Asian ideograph
    0x226540: (0x78AD, 0),  # East Asian ideograph
    0x226541: (0x78A3, 0),  # East Asian ideograph
    0x226543: (0x789E, 0),  # East Asian ideograph
    0x226544: (0x78A8, 0),  # East Asian ideograph
    0x232636: (0x857B, 0),  # East Asian ideograph
    0x214B5E: (0x746A, 0),  # East Asian ideograph
    0x226548: (0x78AB, 0),  # East Asian ideograph
    0x234F4B: (0x9847, 0),  # East Asian ideograph
    0x4B6637: (0x4FE3, 0),  # East Asian ideograph
    0x21654D: (0x4F68, 0),  # East Asian ideograph
    0x22654E: (0x78BB, 0),  # East Asian ideograph
    0x21654F: (0x4F5F, 0),  # East Asian ideograph
    0x6F505C: (0xBBC4, 0),  # Korean hangul
    0x29496F: (0x95FC, 0),  # East Asian ideograph
    0x226555: (0x78CC, 0),  # East Asian ideograph
    0x226556: (0x78C9, 0),  # East Asian ideograph
    0x216557: (0x4F7C, 0),  # East Asian ideograph
    0x226558: (0x78D1, 0),  # East Asian ideograph
    0x21655A: (0x4F98, 0),  # East Asian ideograph
    0x21655B: (0x4F92, 0),  # East Asian ideograph
    0x21655C: (0x4F7D, 0),  # East Asian ideograph
    0x22655E: (0x78C8, 0),  # East Asian ideograph
    0x226560: (0x78D4, 0),  # East Asian ideograph
    0x274E3B: (0x781A, 0),  # East Asian ideograph
    0x216562: (0x4F76, 0),  # East Asian ideograph
    0x216564: (0x4FA2, 0),  # East Asian ideograph
    0x4C6565: (0x78B9, 0),  # East Asian ideograph
    0x216566: (0x4F91, 0),  # East Asian ideograph
    0x216567: (0x4F95, 0),  # East Asian ideograph
    0x226568: (0x78DF, 0),  # East Asian ideograph
    0x22656A: (0x78E7, 0),  # East Asian ideograph
    0x21656C: (0x4F4C, 0),  # East Asian ideograph
    0x21656D: (0x4F97, 0),  # East Asian ideograph
    0x22656E: (0x78DB, 0),  # East Asian ideograph
    0x22656F: (0x78E1, 0),  # East Asian ideograph
    0x216570: (0x4F79, 0),  # East Asian ideograph
    0x216571: (0x4F9A, 0),  # East Asian ideograph
    0x216572: (0x4F81, 0),  # East Asian ideograph
    0x216573: (0x4F78, 0),  # East Asian ideograph
    0x225C5A: (0x74F0, 0),  # East Asian ideograph
    0x4B516E: (0x7E26, 0),  # East Asian ideograph
    0x226576: (0x78EE, 0),  # East Asian ideograph
    0x226577: (0x78E3, 0),  # East Asian ideograph
    0x226579: (0x78F2, 0),  # East Asian ideograph
    0x21657B: (0x4F7A, 0),  # East Asian ideograph
    0x21657C: (0x4FCD, 0),  # East Asian ideograph
    0x2D5529: (0x830E, 0),  # East Asian ideograph (variant of 275529)
    0x22657E: (0x7905, 0),  # East Asian ideograph
    0x6F5D27: (0xD5EC, 0),  # Korean hangul
    0x6F505E: (0xBBD0, 0),  # Korean hangul
    0x217A75: (0x5A16, 0),  # East Asian ideograph
    0x224F5D: (0x7043, 0),  # East Asian ideograph
    0x216643: (0x4FB9, 0),  # East Asian ideograph
    0x232644: (0x8597, 0),  # East Asian ideograph
    0x283466: (0x63FF, 0),  # East Asian ideograph
    0x6F5D28: (0xD5F4, 0),  # Korean hangul
    0x287269: (0x7EC9, 0),  # East Asian ideograph
    0x2D3C38: (0x9245, 0),  # East Asian ideograph
    0x216646: (0x501E, 0),  # East Asian ideograph
    0x217E25: (0x5B67, 0),  # East Asian ideograph
    0x6F4B42: (0xB059, 0),  # Korean hangul
    0x6F505F: (0xBBF8, 0),  # Korean hangul
    0x282647: (0x5CBF, 0),  # East Asian ideograph
    0x275F4A: (0x867D, 0),  # East Asian ideograph
    0x225C5C: (0x74EE, 0),  # East Asian ideograph
    0x217633: (0x5800, 0),  # East Asian ideograph
    0x23605B: (0x9F8E, 0),  # East Asian ideograph
    0x276649: (0x4F1C, 0),  # East Asian ideograph
    0x274E3E: (0x7815, 0),  # East Asian ideograph
    0x293866: (0x8DB1, 0),  # East Asian ideograph
    0x29563C: (0x9B49, 0),  # East Asian ideograph
    0x6F5C73: (0xD585, 0),  # Korean hangul
    0x4B3C21: (0x5D5C, 0),  # East Asian ideograph
    0x21664C: (0x5007, 0),  # East Asian ideograph
    0x21664D: (0x5013, 0),  # East Asian ideograph
    0x23264E: (0x8586, 0),  # East Asian ideograph
    0x6F5D2A: (0xD5F7, 0),  # Korean hangul
    0x222650: (0x5DDB, 0),  # East Asian ideograph
    0x22606A: (0x76AA, 0),  # East Asian ideograph
    0x292651: (0x84DF, 0),  # East Asian ideograph
    0x275F4C: (0x9E21, 0),  # East Asian ideograph
    0x696466: (0x7CAD, 0),  # East Asian ideograph
    0x217635: (0x57EC, 0),  # East Asian ideograph
    0x6F5264: (0xC0B3, 0),  # Korean hangul
    0x393770: (0x56F2, 0),  # East Asian ideograph
    0x2D552D: (0x8358, 0),  # East Asian ideograph
    0x6F5D2B: (0xD5F9, 0),  # Korean hangul
    0x4B4066: (0x62F4, 0),  # East Asian ideograph
    0x286655: (0x783B, 0),  # East Asian ideograph
    0x4B3C23: (0x5CE5, 0),  # East Asian ideograph
    0x274177: (0x631E, 0),  # East Asian ideograph
    0x222656: (0x5DE4, 0),  # East Asian ideograph
    0x217636: (0x5807, 0),  # East Asian ideograph
    0x292658: (0x83B6, 0),  # East Asian ideograph
    0x282659: (0x5DEF, 0),  # East Asian ideograph
    0x692432: (0x3052, 0),  # Hiragana letter GE
    0x276068: (0x996C, 0),  # East Asian ideograph
    0x706D3B: (0x7818, 0),  # East Asian ideograph
    0x226621: (0x78F9, 0),  # East Asian ideograph
    0x226622: (0x78FD, 0),  # East Asian ideograph
    0x6F5063: (0xBC00, 0),  # Korean hangul
    0x216626: (0x4FB7, 0),  # East Asian ideograph
    0x226627: (0x78FE, 0),  # East Asian ideograph
    0x226629: (0x78FB, 0),  # East Asian ideograph
    0x21662A: (0x4FE5, 0),  # East Asian ideograph
    0x22662B: (0x7904, 0),  # East Asian ideograph
    0x21662C: (0x4FE7, 0),  # East Asian ideograph
    0x22662E: (0x7912, 0),  # East Asian ideograph
    0x226632: (0x790C, 0),  # East Asian ideograph
    0x216633: (0x4FDC, 0),  # East Asian ideograph
    0x226634: (0x7913, 0),  # East Asian ideograph
    0x216635: (0x4FD4, 0),  # East Asian ideograph
    0x216637: (0x4FC1, 0),  # East Asian ideograph
    0x21663B: (0x4FDB, 0),  # East Asian ideograph
    0x21663E: (0x4FC6, 0),  # East Asian ideograph
    0x706640: (0x80EC, 0),  # East Asian ideograph
    0x6F5064: (0xBC08, 0),  # Korean hangul
    0x226643: (0x791E, 0),  # East Asian ideograph
    0x6F4C21: (0xB128, 0),  # Korean hangul
    0x226646: (0x7922, 0),  # East Asian ideograph
    0x292661: (0x8360, 0),  # East Asian ideograph
    0x216648: (0x503F, 0),  # East Asian ideograph
    0x216649: (0x5005, 0),  # East Asian ideograph
    0x4D5973: (0x51EB, 0),  # East Asian ideograph
    0x22664C: (0x7924, 0),  # East Asian ideograph
    0x22664D: (0x7927, 0),  # East Asian ideograph
    0x21664E: (0x5022, 0),  # East Asian ideograph
    0x226650: (0x7929, 0),  # East Asian ideograph
    0x216652: (0x4FF5, 0),  # East Asian ideograph
    0x6F2463: (0x314D, 0),  # Korean hangul
    0x226655: (0x7931, 0),  # East Asian ideograph
    0x393428: (0x5227, 0),  # East Asian ideograph
    0x276235: (0x9E26, 0),  # East Asian ideograph
    0x216659: (0x4FF4, 0),  # East Asian ideograph
    0x21665B: (0x5037, 0),  # East Asian ideograph
    0x22665D: (0x7934, 0),  # East Asian ideograph
    0x21665E: (0x502E, 0),  # East Asian ideograph
    0x6F5065: (0xBC09, 0),  # Korean hangul
    0x226660: (0x7936, 0),  # East Asian ideograph
    0x216661: (0x4FF6, 0),  # East Asian ideograph
    0x216662: (0x501C, 0),  # East Asian ideograph
    0x6F4C22: (0xB12C, 0),  # Korean hangul
    0x226665: (0x793D, 0),  # East Asian ideograph
    0x216666: (0x502C, 0),  # East Asian ideograph
    0x226667: (0x7942, 0),  # East Asian ideograph
    0x226668: (0x793F, 0),  # East Asian ideograph
    0x216669: (0x5010, 0),  # East Asian ideograph
    0x22666A: (0x794A, 0),  # East Asian ideograph
    0x22666B: (0x794D, 0),  # East Asian ideograph
    0x292668: (0x8369, 0),  # East Asian ideograph
    0x226675: (0x7946, 0),  # East Asian ideograph
    0x226677: (0x7958, 0),  # East Asian ideograph
    0x216679: (0x503D, 0),  # East Asian ideograph
    0x22667A: (0x795C, 0),  # East Asian ideograph
    0x22667B: (0x794F, 0),  # East Asian ideograph
    0x22667C: (0x7953, 0),  # East Asian ideograph
    0x22667D: (0x7953, 0),  # Unrelated variant of EACC 22667C which maps to 7953
    0x6F4C23: (0xB134, 0),  # Korean hangul
    0x225C63: (0x74F8, 0),  # East Asian ideograph
    0x236062: (0x9F95, 0),  # East Asian ideograph
    0x2D336B: (0x5C05, 0),  # East Asian ideograph
    0x213F71: (0x6233, 0),  # East Asian ideograph
    0x6F5D30: (0xD610, 0),  # Korean hangul
    0x224B57: (0x6EA8, 0),  # East Asian ideograph
    0x27627D: (0x9F50, 0),  # East Asian ideograph
    0x6F5D77: (0xD774, 0),  # Korean hangul
    0x213B2E: (0x5BE2, 0),  # East Asian ideograph
    0x6F4C24: (0xB135, 0),  # Korean hangul
    0x21763B: (0x580F, 0),  # East Asian ideograph
    0x227A3A: (0x81CA, 0),  # East Asian ideograph
    0x232672: (0x85BF, 0),  # East Asian ideograph
    0x6F5528: (0xC557, 0),  # Korean hangul
    0x6F5068: (0xBC0D, 0),  # Korean hangul
    0x6F4C25: (0xB137, 0),  # Korean hangul
    0x295A48: (0x9E31, 0),  # East Asian ideograph
    0x395A36: (0x983C, 0),  # East Asian ideograph
    0x6F4939: (0xACA1, 0),  # Korean hangul
    0x275121: (0x7EB1, 0),  # East Asian ideograph
    0x222677: (0x5E12, 0),  # East Asian ideograph
    0x225122: (0x70DD, 0),  # East Asian ideograph
    0x225123: (0x70E1, 0),  # East Asian ideograph
    0x27417E: (0x62E9, 0),  # East Asian ideograph
    0x226679: (0x795B, 0),  # East Asian ideograph
    0x275F54: (0x4E91, 0),  # East Asian ideograph
    0x235124: (0x9907, 0),  # East Asian ideograph
    0x6F4C26: (0xB140, 0),  # Korean hangul
    0x225C66: (0x74FB, 0),  # East Asian ideograph
    0x275125: (0x7EB7, 0),  # East Asian ideograph
    0x4B3869: (0x5727, 0),  # East Asian ideograph
    0x235C22: (0x9DC7, 0),  # East Asian ideograph
    0x225126: (0x70E3, 0),  # East Asian ideograph
    0x6F5D33: (0xD614, 0),  # Korean hangul
    0x6F5127: (0xBC85, 0),  # Korean hangul
    0x235128: (0x9902, 0),  # East Asian ideograph
    0x6F5374: (0xC298, 0),  # Korean hangul
    0x6F506A: (0xBC11, 0),  # Korean hangul
    0x275129: (0x624E, 0),  # East Asian ideograph
    0x277D2B: (0x5A06, 0),  # East Asian ideograph
    0x225C67: (0x74FF, 0),  # East Asian ideograph
    0x27512A: (0x7ECD, 0),  # East Asian ideograph
    0x21512B: (0x7D44, 0),  # East Asian ideograph
    0x6F4F31: (0xB82C, 0),  # Korean hangul
    0x27413F: (0x626C, 0),  # East Asian ideograph
    0x6F5D34: (0xD615, 0),  # Korean hangul
    0x27512C: (0x7EC6, 0),  # East Asian ideograph
    0x27512D: (0x7EC5, 0),  # East Asian ideograph
    0x4C7328: (
        0x5FAD,
        0,
    ),  # East Asian ideograph (variant of 2E7328 which maps to 5FAD)
    0x22512E: (0x70D1, 0),  # East Asian ideograph
    0x215869: (0x8AAA, 0),  # East Asian ideograph
    0x21512F: (0x7D40, 0),  # East Asian ideograph
    0x215130: (0x7D42, 0),  # East Asian ideograph
    0x216722: (0x506F, 0),  # East Asian ideograph
    0x216723: (0x5050, 0),  # East Asian ideograph
    0x216725: (0x5070, 0),  # East Asian ideograph
    0x215131: (0x7D71, 0),  # East Asian ideograph
    0x216729: (0x5053, 0),  # East Asian ideograph
    0x21672A: (0x506A, 0),  # East Asian ideograph
    0x21672C: (0x5056, 0),  # East Asian ideograph
    0x215132: (0x7D5E, 0),  # East Asian ideograph
    0x226730: (0x7972, 0),  # East Asian ideograph
    0x216731: (0x506D, 0),  # East Asian ideograph
    0x275133: (0x7ED2, 0),  # East Asian ideograph
    0x6F4C29: (0xB150, 0),  # Korean hangul
    0x216738: (0x505D, 0),  # East Asian ideograph
    0x215134: (0x7D50, 0),  # East Asian ideograph
    0x21673B: (0x5058, 0),  # East Asian ideograph
    0x21673C: (0x5072, 0),  # East Asian ideograph
    0x22673E: (0x797C, 0),  # East Asian ideograph
    0x3F6179: (0x5C1F, 0),  # East Asian ideograph
    0x216741: (0x5041, 0),  # East Asian ideograph
    0x6F5D36: (0xD638, 0),  # Korean hangul
    0x275136: (0x7EDA, 0),  # East Asian ideograph
    0x216746: (0x5015, 0),  # East Asian ideograph
    0x293430: (0x8BB4, 0),  # East Asian ideograph
    0x216748: (0x507A, 0),  # East Asian ideograph
    0x21674A: (0x506C, 0),  # East Asian ideograph
    0x275137: (0x7EDD, 0),  # East Asian ideograph
    0x21674D: (0x506B, 0),  # East Asian ideograph
    0x21674E: (0x5094, 0),  # East Asian ideograph
    0x22674F: (0x798B, 0),  # East Asian ideograph
    0x216750: (0x509E, 0),  # East Asian ideograph
    0x235138: (0x9915, 0),  # East Asian ideograph
    0x216752: (0x509B, 0),  # East Asian ideograph
    0x216753: (0x509A, 0),  # East Asian ideograph
    0x226754: (0x7994, 0),  # East Asian ideograph
    0x226755: (0x7993, 0),  # East Asian ideograph
    0x215139: (0x7D66, 0),  # East Asian ideograph
    0x21675A: (0x508C, 0),  # East Asian ideograph
    0x21675C: (0x5088, 0),  # East Asian ideograph
    0x23513A: (0x9924, 0),  # East Asian ideograph
    0x22675F: (0x79A1, 0),  # East Asian ideograph
    0x226760: (0x799B, 0),  # East Asian ideograph
    0x226761: (0x79A3, 0),  # East Asian ideograph
    0x216762: (0x508E, 0),  # East Asian ideograph
    0x23513B: (0x991F, 0),  # East Asian ideograph
    0x224B5E: (0x6E8E, 0),  # East Asian ideograph
    0x216767: (0x50A6, 0),  # East Asian ideograph
    0x274C76: (0x763E, 0),  # East Asian ideograph
    0x21513C: (0x7D93, 0),  # East Asian ideograph
    0x21676A: (0x5092, 0),  # East Asian ideograph
    0x21676C: (0x509C, 0),  # East Asian ideograph
    0x2D442D: (0x6780, 0),  # East Asian ideograph
    0x22676E: (0x79A9, 0),  # East Asian ideograph
    0x27513D: (0x6346, 0),  # East Asian ideograph
    0x226770: (0x79AB, 0),  # East Asian ideograph
    0x216771: (0x50C7, 0),  # East Asian ideograph
    0x216775: (0x50C9, 0),  # East Asian ideograph
    0x22677A: (0x79B3, 0),  # East Asian ideograph
    0x22513F: (0x70FA, 0),  # East Asian ideograph
    0x21677C: (0x50B4, 0),  # East Asian ideograph
    0x6F5D38: (0xD63C, 0),  # Korean hangul
    0x212A23: (0xE8D2, 0),  # EACC component character
    0x215140: (0x7D81, 0),  # East Asian ideograph
    0x334F5E: (0x7A91, 0),  # East Asian ideograph
    0x215141: (0x7D9C, 0),  # East Asian ideograph
    0x6F5375: (0xC29B, 0),  # Korean hangul
    0x213538: (0x53F0, 0),  # East Asian ideograph (duplicate simplified)
    0x6F506F: (0xBC16, 0),  # Korean hangul
    0x215142: (0x7DBB, 0),  # East Asian ideograph
    0x6F4C2C: (0xB154, 0),  # Korean hangul
    0x284140: (0x6861, 0),  # East Asian ideograph
    0x235143: (0x9929, 0),  # East Asian ideograph
    0x2D3765: (0x8086, 0),  # East Asian ideograph
    0x215144: (0x7DCA, 0),  # East Asian ideograph
    0x6F5D39: (0xD640, 0),  # Korean hangul
    0x215145: (0x7DBE, 0),  # East Asian ideograph
    0x224B60: (0x6ED9, 0),  # East Asian ideograph
    0x215146: (0x7DB4, 0),  # East Asian ideograph
    0x2E2D79: (0x6128, 0),  # East Asian ideograph
    0x4B5724: (0x86CD, 0),  # East Asian ideograph
    0x235147: (0x991A, 0),  # East Asian ideograph
    0x275242: (0x4E49, 0),  # East Asian ideograph
    0x6F4C2D: (0xB155, 0),  # Korean hangul
    0x6F5C48: (0xD46F, 0),  # Korean hangul
    0x215148: (0x7DB2, 0),  # East Asian ideograph
    0x215149: (0x7DB1, 0),  # East Asian ideograph
    0x6F5D3A: (0xD648, 0),  # Korean hangul
    0x21514A: (0x7DBD, 0),  # East Asian ideograph
    0x224B61: (0x6EBD, 0),  # East Asian ideograph
    0x234F60: (0x9852, 0),  # East Asian ideograph
    0x4B3C32: (0x5DD3, 0),  # East Asian ideograph
    0x6F5071: (0xBC1B, 0),  # Korean hangul
    0x22514C: (0x7103, 0),  # East Asian ideograph
    0x21586F: (0x8AA3, 0),  # East Asian ideograph
    0x21514D: (0x7DA2, 0),  # East Asian ideograph
    0x22582B: (0x736B, 0),  # East Asian ideograph
    0x4B615F: (0x9AEA, 0),  # East Asian ideograph
    0x21514E: (0x7DAD, 0),  # East Asian ideograph
    0x2D3324: (0x634C, 0),  # East Asian ideograph
    0x6F5D3B: (0xD649, 0),  # Korean hangul
    0x21514F: (0x7DBF, 0),  # East Asian ideograph
    0x2D356A: (0x8A36, 0),  # East Asian ideograph
    0x215150: (0x7DB8, 0),  # East Asian ideograph
    0x6F5072: (0xBC1C, 0),  # Korean hangul
    0x215151: (0x7DC7, 0),  # East Asian ideograph
    0x22482D: (0x6CF2, 0),  # East Asian ideograph
    0x275152: (0x7F14, 0),  # East Asian ideograph
    0x6F493B: (0xACA9, 0),  # Korean hangul
    0x2D3768: (0x56EC, 0),  # East Asian ideograph
    0x215153: (0x7DEF, 0),  # East Asian ideograph
    0x294346: (0x94D1, 0),  # East Asian ideograph
    0x2F5D3C: (0x6EF7, 0),  # East Asian ideograph
    0x215154: (
        0x7DF4,
        0,
    ),  # East Asian ideograph (variant of 4B5154 which maps to 7DF4)
    0x224B63: (0x6EC1, 0),  # East Asian ideograph
    0x234F62: (0x984B, 0),  # East Asian ideograph
    0x235155: (0x9932, 0),  # East Asian ideograph
    0x6F5073: (0xBC1D, 0),  # Korean hangul
    0x225156: (0x7112, 0),  # East Asian ideograph
    0x6F4C30: (0xB178, 0),  # Korean hangul
    0x69675C: (0x825D, 0),  # East Asian ideograph
    0x215157: (0x7DEC, 0),  # East Asian ideograph
    0x234179: (0x91E9, 0),  # East Asian ideograph
    0x215158: (0x7DDD, 0),  # East Asian ideograph
    0x213E37: (0x6012, 0),  # East Asian ideograph
    0x6F5D3D: (0xD64D, 0),  # Korean hangul
    0x215159: (0x7DE9, 0),  # East Asian ideograph
    0x21515A: (0x7DE3, 0),  # East Asian ideograph
    0x213539: (0x53E5, 0),  # East Asian ideograph
    0x6F5074: (0xBC1F, 0),  # Korean hangul
    0x216822: (0x50C2, 0),  # East Asian ideograph
    0x27515B: (0x7F16, 0),  # East Asian ideograph
    0x226825: (0x79BC, 0),  # East Asian ideograph
    0x225C71: (0x7505, 0),  # East Asian ideograph
    0x226828: (0x79C6, 0),  # East Asian ideograph
    0x22515C: (0x710C, 0),  # East Asian ideograph
    0x22682A: (0x79C8, 0),  # East Asian ideograph
    0x21682C: (0x50BA, 0),  # East Asian ideograph
    0x22682D: (0x79D4, 0),  # East Asian ideograph
    0x21682E: (0x50CD, 0),  # East Asian ideograph
    0x21515D: (0x7D9E, 0),  # East Asian ideograph
    0x6F4F33: (0xB835, 0),  # Korean hangul
    0x226832: (0x79D6, 0),  # East Asian ideograph
    0x216834: (0x50EF, 0),  # East Asian ideograph
    0x21515E: (0x7DDE, 0),  # East Asian ideograph
    0x293438: (0x8C29, 0),  # East Asian ideograph
    0x21683A: (0x50F4, 0),  # East Asian ideograph
    0x21515F: (0x7E11, 0),  # East Asian ideograph
    0x21683C: (0x50DD, 0),  # East Asian ideograph
    0x22683D: (0x79EC, 0),  # East Asian ideograph
    0x22683E: (
        0x79EB,
        0,
    ),  # East Asian ideograph (variant of 4C683E which maps to 79EB)
    0x6F5075: (0xBC24, 0),  # Korean hangul
    0x215160: (0x7E0A, 0),  # East Asian ideograph
    0x226842: (0x79E1, 0),  # East Asian ideograph
    0x6F4C32: (0xB17A, 0),  # Korean hangul
    0x226844: (0x79DD, 0),  # East Asian ideograph
    0x226845: (0x79ED, 0),  # East Asian ideograph
    0x216846: (0x50D9, 0),  # East Asian ideograph
    0x215161: (0x7E08, 0),  # East Asian ideograph
    0x226848: (0x79F8, 0),  # East Asian ideograph
    0x215162: (0x7E1B, 0),  # East Asian ideograph
    0x2E684E: (0x8020, 0),  # East Asian ideograph
    0x22684F: (0x7A02, 0),  # East Asian ideograph
    0x226850: (0x7A0A, 0),  # East Asian ideograph
    0x6F5D3F: (0xD654, 0),  # Korean hangul
    0x6F5625: (0xC651, 0),  # Korean hangul
    0x275163: (0x81F4, 0),  # East Asian ideograph
    0x226854: (0x7A09, 0),  # East Asian ideograph
    0x216855: (0x50EC, 0),  # East Asian ideograph
    0x4B442D: (0x67A9, 0),  # East Asian ideograph
    0x215164: (0x7E23, 0),  # East Asian ideograph
    0x21685B: (0x510E, 0),  # East Asian ideograph
    0x22685C: (0x7A03, 0),  # East Asian ideograph
    0x6F5076: (0xBC25, 0),  # Korean hangul
    0x275165: (0x7F29, 0),  # East Asian ideograph
    0x226861: (0x7A0C, 0),  # East Asian ideograph
    0x293160: (0x89EF, 0),  # East Asian ideograph
    0x225166: (0x7113, 0),  # East Asian ideograph
    0x216866: (0x5107, 0),  # East Asian ideograph
    0x216867: (0x510F, 0),  # East Asian ideograph
    0x216868: (0x50FE, 0),  # East Asian ideograph
    0x216869: (0x510B, 0),  # East Asian ideograph
    0x21686A: (0x50FD, 0),  # East Asian ideograph
    0x22686B: (0x7A11, 0),  # East Asian ideograph
    0x22686C: (0x7A18, 0),  # East Asian ideograph
    0x21686D: (0x5101, 0),  # East Asian ideograph
    0x234E43: (0x97C9, 0),  # East Asian ideograph
    0x22686F: (
        0x7A19,
        0,
    ),  # East Asian ideograph (variant of 2E686F which maps to 7A19)
    0x6F5D40: (0xD655, 0),  # Korean hangul
    0x226871: (0x7A1E, 0),  # East Asian ideograph
    0x216872: (0x5113, 0),  # East Asian ideograph
    0x234F66: (0x983F, 0),  # East Asian ideograph
    0x226876: (0x7A17, 0),  # East Asian ideograph
    0x275169: (0x7F27, 0),  # East Asian ideograph
    0x216878: (0x511A, 0),  # East Asian ideograph
    0x216879: (0x9797, 0),  # East Asian ideograph
    0x6F5077: (0xBC27, 0),  # Korean hangul
    0x21516A: (0x7E43, 0),  # East Asian ideograph
    0x21687E: (0x5126, 0),  # East Asian ideograph
    0x6F4C34: (0xB180, 0),  # Korean hangul
    0x223A5B: (0x6745, 0),  # East Asian ideograph
    0x33516B: (0x7DD0, 0),  # East Asian ideograph
    0x4C735D: (0x7D4B, 0),  # East Asian ideograph
    0x22516C: (0x711E, 0),  # East Asian ideograph
    0x2E3729: (0x65B5, 0),  # East Asian ideograph
    0x6F5D41: (0xD658, 0),  # Korean hangul
    0x21516D: (0x7E3D, 0),  # East Asian ideograph
    0x6F5451: (0xC3D8, 0),  # Korean hangul
    0x22516E: (0x7120, 0),  # East Asian ideograph
    0x2D4437: (0x67FE, 0),  # East Asian ideograph
    0x21516F: (0x7E45, 0),  # East Asian ideograph
    0x6F4C35: (0xB188, 0),  # Korean hangul
    0x215170: (0x7E55, 0),  # East Asian ideograph
    0x275174: (0x7F2D, 0),  # East Asian ideograph
    0x235171: (0x994D, 0),  # East Asian ideograph
    0x473539: (0x8B9E, 0),  # East Asian ideograph
    0x29426D: (0x94CD, 0),  # East Asian ideograph
    0x275172: (0x7EE3, 0),  # East Asian ideograph
    0x224B69: (0x6EBB, 0),  # East Asian ideograph
    0x275173: (0x7ED5, 0),  # East Asian ideograph
    0x6F5B23: (0xD0F0, 0),  # Korean hangul
    0x215174: (0x7E5A, 0),  # East Asian ideograph
    0x6F4C36: (0xB189, 0),  # Korean hangul
    0x225175: (0x712D, 0),  # East Asian ideograph
    0x2D376F: (0x5700, 0),  # East Asian ideograph
    0x275176: (0x7EF3, 0),  # East Asian ideograph
    0x213C21: (0x5D0E, 0),  # East Asian ideograph
    0x275177: (0x8327, 0),  # East Asian ideograph
    0x2D3C22: (0x5D10, 0),  # East Asian ideograph
    0x275178: (0x7ECE, 0),  # East Asian ideograph
    0x223C23: (0x67C2, 0),  # East Asian ideograph
    0x6F507A: (0xBC30, 0),  # Korean hangul
    0x275179: (0x7ED8, 0),  # East Asian ideograph
    0x215878: (0x8AD2, 0),  # East Asian ideograph
    0x225C77: (0x7503, 0),  # East Asian ideograph
    0x27517A: (0x8FAB, 0),  # East Asian ideograph
    0x217C25: (0x5A9E, 0),  # East Asian ideograph
    0x45465B: (0x6C2F, 0),  # East Asian ideograph
    0x21517B: (0x7E7D, 0),  # East Asian ideograph
    0x223C26: (0x67CA, 0),  # East Asian ideograph
    0x274E59: (0x7840, 0),  # East Asian ideograph
    0x6F5D44: (0xD667, 0),  # Korean hangul
    0x6F517C: (0xBE61, 0),  # Korean hangul
    0x213C27: (0x5D4C, 0),  # East Asian ideograph
    0x234F6A: (0x985C, 0),  # East Asian ideograph
    0x27517D: (0x7EE7, 0),  # East Asian ideograph
    0x223C28: (0x67CE, 0),  # East Asian ideograph
    0x2D443A: (0x6942, 0),  # East Asian ideograph
    0x23517E: (0x9955, 0),  # East Asian ideograph
    0x213B32: (0x5BE7, 0),  # East Asian ideograph
    0x213C29: (0x5D69, 0),  # East Asian ideograph
    0x223C2A: (0x67F2, 0),  # East Asian ideograph
    0x275E3E: (0x94DB, 0),  # East Asian ideograph
    0x2D5547: (0x837D, 0),  # East Asian ideograph
    0x223C2B: (0x67C3, 0),  # East Asian ideograph
    0x6F5D45: (0xD669, 0),  # Korean hangul
    0x234F6B: (0x9859, 0),  # East Asian ideograph
    0x223C2D: (0x67DD, 0),  # East Asian ideograph
    0x6F507C: (0xBC34, 0),  # Korean hangul
    0x275F67: (0x96FE, 0),  # East Asian ideograph
    0x213C2E: (0x5DBD, 0),  # East Asian ideograph
    0x6F4D43: (0xB3D0, 0),  # Korean hangul
    0x233E5F: (0x90AD, 0),  # East Asian ideograph
    0x213C2F: (
        0x5DBA,
        0,
    ),  # East Asian ideograph (variant of 4B3C2F which maps to 5DBA)
    0x6F493D: (0xACAC, 0),  # Korean hangul
    0x233C30: (0x8F46, 0),  # East Asian ideograph
    0x226922: (0x7A2C, 0),  # East Asian ideograph
    0x6F5D46: (0xD670, 0),  # Korean hangul
    0x233C31: (0x8F4A, 0),  # East Asian ideograph
    0x216929: (0x5124, 0),  # East Asian ideograph
    0x6F5452: (0xC3D9, 0),  # Korean hangul
    0x21692B: (0x5129, 0),  # East Asian ideograph
    0x213C32: (0x5DD4, 0),  # East Asian ideograph
    0x6F507D: (0xBC37, 0),  # Korean hangul
    0x216930: (0x5131, 0),  # East Asian ideograph
    0x273C33: (0x5CA9, 0),  # East Asian ideograph
    0x29454D: (0x9534, 0),  # East Asian ideograph
    0x275175: (0x7CFB, 0),  # East Asian ideograph (duplicate simplified)
    0x226939: (0x7A48, 0),  # East Asian ideograph
    0x22693D: (0x7A4B, 0),  # East Asian ideograph
    0x22693E: (0x7A47, 0),  # East Asian ideograph
    0x22693F: (0x7A44, 0),  # East Asian ideograph
    0x274E5C: (0x77FE, 0),  # East Asian ideograph
    0x6F5D47: (0xD671, 0),  # Korean hangul
    0x216944: (0x513A, 0),  # East Asian ideograph
    0x213C36: (0x5DE2, 0),  # East Asian ideograph
    0x696946: (0x8630, 0),  # East Asian ideograph
    0x216947: (0x5139, 0),  # East Asian ideograph
    0x216948: (0x513B, 0),  # East Asian ideograph
    0x213C37: (0x5DE5, 0),  # East Asian ideograph
    0x22694D: (0x7A5F, 0),  # East Asian ideograph
    0x22694F: (0x7A60, 0),  # East Asian ideograph
    0x216951: (0x5159, 0),  # East Asian ideograph
    0x216952: (0x515B, 0),  # East Asian ideograph
    0x213663: (0x55AA, 0),  # East Asian ideograph
    0x29454E: (0x9545, 0),  # East Asian ideograph
    0x216955: (0x515D, 0),  # East Asian ideograph
    0x216956: (0x515E, 0),  # East Asian ideograph
    0x225838: (0x737E, 0),  # East Asian ideograph
    0x216958: (0x515F, 0),  # East Asian ideograph
    0x216959: (0x5161, 0),  # East Asian ideograph
    0x69695B: (0x86AB, 0),  # East Asian ideograph
    0x21695C: (0x5163, 0),  # East Asian ideograph
    0x6F4F35: (0xB838, 0),  # Korean hangul
    0x274E5D: (0x783A, 0),  # East Asian ideograph
    0x22695F: (0x7A70, 0),  # East Asian ideograph
    0x6F5D48: (0xD683, 0),  # Korean hangul
    0x696962: (0x86EF, 0),  # East Asian ideograph
    0x213C3B: (0x5DEB, 0),  # East Asian ideograph
    0x226966: (0x7A75, 0),  # East Asian ideograph
    0x216967: (0x5182, 0),  # East Asian ideograph
    0x216969: (0x5184, 0),  # East Asian ideograph
    0x22696B: (0x7A80, 0),  # East Asian ideograph
    0x21696E: (0x518F, 0),  # East Asian ideograph
    0x213C3D: (0x5DF1, 0),  # East Asian ideograph
    0x216970: (0x5194, 0),  # East Asian ideograph
    0x216971: (0x5193, 0),  # East Asian ideograph
    0x2E403D: (0x6AC1, 0),  # East Asian ideograph
    0x216975: (0x5196, 0),  # East Asian ideograph
    0x226978: (0x7A8A, 0),  # East Asian ideograph
    0x22697A: (0x7A94, 0),  # East Asian ideograph
    0x21697B: (0x51A1, 0),  # East Asian ideograph
    0x21697C: (0x51A3, 0),  # East Asian ideograph
    0x22697E: (0x68A5, 0),  # East Asian ideograph
    0x213C40: (0x5DF4, 0),  # East Asian ideograph
    0x223C41: (0x6832, 0),  # East Asian ideograph
    0x213C42: (0x5DFD, 0),  # East Asian ideograph
    0x275B28: (0x8E0C, 0),  # East Asian ideograph
    0x213C43: (0x5DFE, 0),  # East Asian ideograph
    0x275E3F: (0x94CE, 0),  # East Asian ideograph
    0x213C44: (0x5E02, 0),  # East Asian ideograph
    0x6F5471: (0xC510, 0),  # Korean hangul
    0x29565D: (0x9C82, 0),  # East Asian ideograph
    0x217C45: (0x5AB7, 0),  # East Asian ideograph
    0x2D4440: (0x6822, 0),  # East Asian ideograph
    0x223C47: (0x682B, 0),  # East Asian ideograph
    0x294551: (0x9517, 0),  # East Asian ideograph
    0x223C48: (0x682D, 0),  # East Asian ideograph
    0x6F493E: (0xACAF, 0),  # Korean hangul
    0x235C3A: (0x9DDF, 0),  # East Asian ideograph
    0x233C49: (0x8F57, 0),  # East Asian ideograph
    0x6F5D4B: (0xD68D, 0),  # Korean hangul
    0x213C4A: (0x5E16, 0),  # East Asian ideograph
    0x334F71: (0x54B2, 0),  # East Asian ideograph
    0x213C4B: (0x5E15, 0),  # East Asian ideograph
    0x275F6D: (0x972D, 0),  # East Asian ideograph
    0x213C4C: (0x5E1B, 0),  # East Asian ideograph
    0x4B3321: (0x5185, 0),  # East Asian ideograph
    0x233C4D: (0x8F5C, 0),  # East Asian ideograph
    0x213C4E: (0x5E1D, 0),  # East Asian ideograph
    0x284F7D: (0x704F, 0),  # East Asian ideograph
    0x29426F: (0x94BD, 0),  # East Asian ideograph
    0x223C4F: (0x6844, 0),  # East Asian ideograph
    0x4B5E5D: (0x95D4, 0),  # East Asian ideograph
    0x224730: (0x6C78, 0),  # East Asian ideograph
    0x6F5379: (0xC2A8, 0),  # Korean hangul
    0x217C50: (0x5ABA, 0),  # East Asian ideograph
    0x275F6E: (0x96F3, 0),  # East Asian ideograph
    0x213C51: (0x5E2B, 0),  # East Asian ideograph
    0x6F5B26: (0xD131, 0),  # Korean hangul
    0x213668: (0x55AE, 0),  # East Asian ideograph
    0x232635: (0x8598, 0),  # East Asian ideograph
    0x213C52: (0x5E33, 0),  # East Asian ideograph
    0x233C53: (0x8F5D, 0),  # East Asian ideograph
    0x6F5D4D: (0xD6A1, 0),  # Korean hangul
    0x224731: (0x6C74, 0),  # East Asian ideograph
    0x213C55: (0x5E37, 0),  # East Asian ideograph
    0x275F6F: (0x7075, 0),  # East Asian ideograph
    0x213C56: (0x5E45, 0),  # East Asian ideograph
    0x6F4C41: (0xB1E8, 0),  # Korean hangul
    0x275B2C: (0x8E8F, 0),  # East Asian ideograph
    0x213226: (0x5000, 0),  # East Asian ideograph
    0x223C58: (0x6834, 0),  # East Asian ideograph
    0x334F37: (0x5EE9, 0),  # East Asian ideograph
    0x695D36: (0x6B1F, 0),  # East Asian ideograph
    0x223C59: (0x6812, 0),  # East Asian ideograph
    0x224732: (0x6C86, 0),  # East Asian ideograph
    0x213C5A: (0x5E5B, 0),  # East Asian ideograph
    0x216A22: (0x51AA, 0),  # East Asian ideograph
    0x216A23: (0x51AB, 0),  # East Asian ideograph
    0x6F4C42: (0xB1FD, 0),  # Korean hangul
    0x216A26: (0x51B1, 0),  # East Asian ideograph
    0x29233C: (0x836D, 0),  # East Asian ideograph
    0x226A28: (0x7AA3, 0),  # East Asian ideograph
    0x213227: (0x4FEE, 0),  # East Asian ideograph
    0x226A2B: (0x7A9E, 0),  # East Asian ideograph
    0x226A2C: (0x7AA7, 0),  # East Asian ideograph
    0x226A2E: (0x7AA8, 0),  # East Asian ideograph
    0x46284C: (0x5ED0, 0),  # East Asian ideograph
    0x226A31: (0x7AAC, 0),  # East Asian ideograph
    0x6F5D4F: (0xD6C4, 0),  # Korean hangul
    0x216A35: (0x51BC, 0),  # East Asian ideograph
    0x226A36: (0x7AB3, 0),  # East Asian ideograph
    0x226A3A: (0x7ABD, 0),  # East Asian ideograph
    0x2D3C5F: (0x6A66, 0),  # East Asian ideograph
    0x226A3C: (0x7AB6, 0),  # East Asian ideograph
    0x226A3D: (0x7AB8, 0),  # East Asian ideograph
    0x226A3E: (0x7AB5, 0),  # East Asian ideograph
    0x226A3F: (0x7ABB, 0),  # East Asian ideograph
    0x213C60: (0x5E5F, 0),  # East Asian ideograph
    0x6F4C43: (0xB204, 0),  # Korean hangul
    0x216A43: (0x51CA, 0),  # East Asian ideograph
    0x216A46: (0x51C7, 0),  # East Asian ideograph
    0x213C61: (0x5E6B, 0),  # East Asian ideograph
    0x226A49: (0x7ACD, 0),  # East Asian ideograph
    0x226A4B: (0x7ACF, 0),  # East Asian ideograph
    0x216A4E: (0x51D1, 0),  # East Asian ideograph
    0x216A4F: (0x51D0, 0),  # East Asian ideograph
    0x287271: (0x7EA4, 0),  # East Asian ideograph (duplicate simplified)
    0x226A51: (0x7AD3, 0),  # East Asian ideograph
    0x226A52: (0x7AD4, 0),  # East Asian ideograph
    0x216A54: (0x51D3, 0),  # East Asian ideograph
    0x226A55: (0x7ADA, 0),  # East Asian ideograph
    0x226A5A: (0x7AE1, 0),  # East Asian ideograph
    0x226A5E: (0x7AE6, 0),  # East Asian ideograph
    0x233C65: (0x8FA4, 0),  # East Asian ideograph
    0x277D48: (0x5AD2, 0),  # East Asian ideograph
    0x696A61: (0x88C3, 0),  # East Asian ideograph
    0x21765B: (0x57DD, 0),  # East Asian ideograph
    0x216A63: (0x51D9, 0),  # East Asian ideograph
    0x226A66: (0x7AEB, 0),  # East Asian ideograph
    0x216A68: (0x51E2, 0),  # East Asian ideograph
    0x226A6B: (0x7AF0, 0),  # East Asian ideograph
    0x696A6D: (0x8904, 0),  # East Asian ideograph
    0x6F5D51: (0xD6C8, 0),  # Korean hangul
    0x213C68: (0x5E7B, 0),  # East Asian ideograph
    0x216A73: (0x5160, 0),  # East Asian ideograph
    0x226A76: (0x7AF5, 0),  # East Asian ideograph
    0x213C69: (0x5E7C, 0),  # East Asian ideograph
    0x216A78: (0x51F5, 0),  # East Asian ideograph
    0x216A79: (0x51F7, 0),  # East Asian ideograph
    0x226A7C: (0x7AFE, 0),  # East Asian ideograph
    0x2D3C6A: (0x51FC, 0),  # East Asian ideograph
    0x273C6B: (0x51E0, 0),  # East Asian ideograph
    0x4B4D56: (0x8846, 0),  # East Asian ideograph
    0x2D5554: (0x855A, 0),  # East Asian ideograph
    0x213C6C: (0x5E8F, 0),  # East Asian ideograph
    0x6F5D52: (0xD6CC, 0),  # Korean hangul
    0x233C6D: (0x8FB7, 0),  # East Asian ideograph
    0x295222: (0x98E8, 0),  # East Asian ideograph
    0x234B35: (0x96A9, 0),  # East Asian ideograph
    0x227333: (0x7E50, 0),  # East Asian ideograph
    0x6F4C46: (0xB20B, 0),  # Korean hangul
    0x275B31: (0x8EAF, 0),  # East Asian ideograph
    0x213C70: (0x5E97, 0),  # East Asian ideograph
    0x22326A: (0x63F9, 0),  # East Asian ideograph
    0x223C71: (0x689B, 0),  # East Asian ideograph
    0x6F5D53: (0xD6D1, 0),  # Korean hangul
    0x213C72: (0x5E9C, 0),  # East Asian ideograph
    0x29344D: (0x8C2E, 0),  # East Asian ideograph
    0x6F5972: (0xCE7C, 0),  # Korean hangul
    0x223C74: (0x68B6, 0),  # East Asian ideograph
    0x6F4C47: (0xB20C, 0),  # Korean hangul
    0x275B32: (0x8F66, 0),  # East Asian ideograph
    0x213C75: (0x5EA6, 0),  # East Asian ideograph
    0x223C76: (0x6882, 0),  # East Asian ideograph
    0x226721: (0x7951, 0),  # East Asian ideograph
    0x6F5D54: (0xD6D4, 0),  # Korean hangul
    0x273C77: (0x5750, 0),  # East Asian ideograph
    0x23595C: (0x9C6F, 0),  # East Asian ideograph
    0x234B37: (0x96AE, 0),  # East Asian ideograph
    0x226723: (0x7954, 0),  # East Asian ideograph
    0x28232B: (0x5C66, 0),  # East Asian ideograph
    0x232724: (0x8624, 0),  # East Asian ideograph
    0x223C7A: (0x6890, 0),  # East Asian ideograph
    0x4B4D59: (
        0x775B,
        0,
    ),  # East Asian ideograph (variant of 214D59 which maps to 775B)
    0x2F317D: (0x8A7E, 0),  # East Asian ideograph
    0x213C7B: (0x5EB6, 0),  # East Asian ideograph
    0x6F5D55: (0xD6D7, 0),  # Korean hangul
    0x275D67: (0x94DD, 0),  # East Asian ideograph
    0x217C7C: (0x5AEB, 0),  # East Asian ideograph
    0x2D462C: (0x6B7A, 0),  # East Asian ideograph
    0x224739: (0x6C67, 0),  # East Asian ideograph
    0x233C7D: (0x8FCD, 0),  # East Asian ideograph
    0x4B5A23: (0x621D, 0),  # East Asian ideograph
    0x213C7E: (0x5EC1, 0),  # East Asian ideograph
    0x2D4756: (0x6F94, 0),  # East Asian ideograph
    0x275B34: (0x519B, 0),  # East Asian ideograph
    0x4B5C47: (0x9059, 0),  # East Asian ideograph
    0x22672A: (0x7967, 0),  # East Asian ideograph
    0x235C45: (0x9DD6, 0),  # East Asian ideograph
    0x6F4866: (0xAC10, 0),  # Korean hangul
    0x6F5B27: (0xD134, 0),  # Korean hangul
    0x4C6266: (0x778B, 0),  # East Asian ideograph
    0x22672D: (0x796B, 0),  # East Asian ideograph
    0x2D6222: (0x9C0C, 0),  # East Asian ideograph
    0x6F4C4A: (0xB215, 0),  # Korean hangul
    0x275B35: (0x8F68, 0),  # East Asian ideograph
    0x6F4F38: (0xB85C, 0),  # Korean hangul
    0x33476F: (0x6D44, 0),  # East Asian ideograph
    0x6F5D57: (0xD6E4, 0),  # Korean hangul
    0x216B24: (0x5213, 0),  # East Asian ideograph
    0x216B26: (0x5216, 0),  # East Asian ideograph
    0x226B27: (0x7B39, 0),  # East Asian ideograph
    0x22473B: (0x6C84, 0),  # East Asian ideograph
    0x216B2A: (0x521C, 0),  # East Asian ideograph
    0x226B2D: (0x7B0F, 0),  # East Asian ideograph
    0x226B2E: (0x7B08, 0),  # East Asian ideograph
    0x275F79: (0x9765, 0),  # East Asian ideograph
    0x6F4C4B: (0xB217, 0),  # Korean hangul
    0x226B33: (0x7B0A, 0),  # East Asian ideograph
    0x29455E: (0x94E1, 0),  # East Asian ideograph
    0x226B35: (0x7B35, 0),  # East Asian ideograph
    0x226B36: (0x7B25, 0),  # East Asian ideograph
    0x216B37: (0x5232, 0),  # East Asian ideograph
    0x226B39: (0x7B38, 0),  # East Asian ideograph
    0x226B3B: (0x7B3B, 0),  # East Asian ideograph
    0x216B3E: (0x5244, 0),  # East Asian ideograph
    0x226B3F: (0x7B24, 0),  # East Asian ideograph
    0x226B40: (0x7B33, 0),  # East Asian ideograph
    0x226B42: (0x7B2A, 0),  # East Asian ideograph
    0x216B43: (0x5249, 0),  # East Asian ideograph
    0x226B44: (0x7B18, 0),  # East Asian ideograph
    0x282736: (0x5E0F, 0),  # East Asian ideograph
    0x226B47: (0x7B31, 0),  # East Asian ideograph
    0x234B3B: (0x96B0, 0),  # East Asian ideograph
    0x226B4A: (0x7B2B, 0),  # East Asian ideograph
    0x216B4B: (0x525A, 0),  # East Asian ideograph
    0x216B4C: (0x5252, 0),  # East Asian ideograph
    0x226B4D: (0x7B1F, 0),  # East Asian ideograph
    0x213B36: (0x5BE9, 0),  # East Asian ideograph
    0x216B50: (0x525F, 0),  # East Asian ideograph
    0x226B52: (0x7B4A, 0),  # East Asian ideograph
    0x226B53: (0x7B59, 0),  # East Asian ideograph (not in Unicode)
    0x226B54: (
        0x7B04,
        0,
    ),  # East Asian ideograph (variant of 2E6B54 which maps to 7B04)
    0x226B55: (0x7B47, 0),  # East Asian ideograph
    0x216739: (0x5048, 0),  # East Asian ideograph
    0x226B59: (0x7B58, 0),  # East Asian ideograph
    0x226B5B: (0x7B6C, 0),  # East Asian ideograph
    0x696B5C: (0x8ADA, 0),  # East Asian ideograph
    0x216B5E: (0x5268, 0),  # East Asian ideograph
    0x216B5F: (0x7B9A, 0),  # East Asian ideograph
    0x226B60: (0x7B48, 0),  # East Asian ideograph
    0x226B61: (0x7B45, 0),  # East Asian ideograph
    0x226B62: (0x7B4C, 0),  # East Asian ideograph
    0x226B63: (0x7B4E, 0),  # East Asian ideograph
    0x234B3C: (0x96B2, 0),  # East Asian ideograph
    0x226B68: (0x7B66, 0),  # East Asian ideograph
    0x706B6A: (0x8159, 0),  # East Asian ideograph
    0x216B6B: (0x5278, 0),  # East Asian ideograph
    0x226B6C: (0x7B64, 0),  # East Asian ideograph
    0x226B6E: (0x7B69, 0),  # East Asian ideograph
    0x275B38: (0x8F6F, 0),  # East Asian ideograph
    0x226B70: (0x7B6D, 0),  # East Asian ideograph
    0x226B74: (0x7B62, 0),  # East Asian ideograph
    0x226B75: (0x7B6E, 0),  # East Asian ideograph
    0x226B76: (0x7B74, 0),  # East Asian ideograph
    0x233A30: (0x8E50, 0),  # East Asian ideograph
    0x216B79: (0x528C, 0),  # East Asian ideograph
    0x216B7A: (0x528A, 0),  # East Asian ideograph
    0x226B7B: (0x7B6F, 0),  # East Asian ideograph
    0x216B7C: (0x5290, 0),  # East Asian ideograph
    0x226B7E: (0x7B65, 0),  # East Asian ideograph
    0x4B3A2F: (0x805F, 0),  # East Asian ideograph
    0x275B39: (0x8F6D, 0),  # East Asian ideograph
    0x6F4867: (0xAC11, 0),  # Korean hangul
    0x27457A: (0x6B20, 0),  # East Asian ideograph (duplicate simplified)
    0x222969: (0x5F54, 0),  # East Asian ideograph
    0x4B3C53: (0x5E2F, 0),  # East Asian ideograph
    0x234B3E: (0x96B3, 0),  # East Asian ideograph
    0x4C6564: (0x78D9, 0),  # East Asian ideograph
    0x282747: (0x5E3B, 0),  # East Asian ideograph
    0x22584C: (0x7393, 0),  # East Asian ideograph
    0x6F4F39: (0xB85D, 0),  # Korean hangul
    0x2F5D5C: (0x730A, 0),  # East Asian ideograph
    0x294944: (0x9603, 0),  # East Asian ideograph
    0x22674A: (0x7998, 0),  # East Asian ideograph
    0x33306C: (0x8B90, 0),  # East Asian ideograph
    0x21674B: (0x505F, 0),  # East Asian ideograph
    0x273D65: (0x540E, 0),  # East Asian ideograph
    0x6F4C50: (0xB25C, 0),  # Korean hangul
    0x27583B: (0x8BA6, 0),  # East Asian ideograph
    0x213235: (0x5074, 0),  # East Asian ideograph
    0x22674D: (0x7999, 0),  # East Asian ideograph
    0x22674E: (0x7995, 0),  # East Asian ideograph
    0x6F5D5D: (0xD711, 0),  # Korean hangul
    0x226750: (0x7996, 0),  # East Asian ideograph
    0x333051: (0x8CB3, 0),  # East Asian ideograph
    0x2D6229: (0x9C53, 0),  # East Asian ideograph
    0x6F4C51: (0xB260, 0),  # Korean hangul
    0x275B3C: (0x8F76, 0),  # East Asian ideograph
    0x294564: (0x9536, 0),  # East Asian ideograph
    0x292752: (0x830F, 0),  # East Asian ideograph
    0x233A34: (0x8E5C, 0),  # East Asian ideograph
    0x6F5A29: (0xCEF5, 0),  # Korean hangul
    0x6F5D5E: (0xD718, 0),  # Korean hangul
    0x274A30: (0x70DB, 0),  # East Asian ideograph
    0x292577: (0x8297, 0),  # East Asian ideograph
    0x4B4A62: (0x72A0, 0),  # East Asian ideograph
    0x273D67: (0x5F84, 0),  # East Asian ideograph
    0x6F4C52: (0xB268, 0),  # Korean hangul
    0x275B3D: (0x8F83, 0),  # East Asian ideograph
    0x217669: (0x5819, 0),  # East Asian ideograph
    0x223636: (0x6549, 0),  # East Asian ideograph
    0x2D5561: (0x76D6, 0),  # East Asian ideograph
    0x6F5D5F: (0xD719, 0),  # Korean hangul
    0x274A31: (0x707F, 0),  # East Asian ideograph
    0x293459: (0x8C2F, 0),  # East Asian ideograph
    0x284E30: (0x6E11, 0),  # East Asian ideograph
    0x29584B: (0x9CBD, 0),  # East Asian ideograph
    0x6F584A: (0xCA0B, 0),  # Korean hangul
    0x34715A: (0x7E1A, 0),  # East Asian ideograph
    0x216C21: (0x5293, 0),  # East Asian ideograph
    0x6F4C53: (0xB269, 0),  # Korean hangul
    0x275B3E: (0x8F7C, 0),  # East Asian ideograph
    0x226C26: (0x7B71, 0),  # East Asian ideograph
    0x226C27: (0x7B70, 0),  # East Asian ideograph
    0x216C29: (0x5298, 0),  # East Asian ideograph
    0x235C4F: (0x9DE9, 0),  # East Asian ideograph
    0x216C2B: (0x529A, 0),  # East Asian ideograph
    0x216C2C: (0x5299, 0),  # East Asian ideograph
    0x226C2D: (0x7B9C, 0),  # East Asian ideograph
    0x216C2E: (0x52A6, 0),  # East Asian ideograph
    0x22275D: (0x5E68, 0),  # East Asian ideograph
    0x212A2B: (0xE8D9, 0),  # EACC component character
    0x216C31: (0x52AD, 0),  # East Asian ideograph
    0x226C33: (0x7B92, 0),  # East Asian ideograph
    0x226C34: (0x7B91, 0),  # East Asian ideograph
    0x226C35: (0x7B90, 0),  # East Asian ideograph
    0x216C37: (0x52BB, 0),  # East Asian ideograph
    0x226C38: (0x7BA3, 0),  # East Asian ideograph
    0x226C3A: (0x7B8D, 0),  # East Asian ideograph
    0x28275F: (0x5E31, 0),  # East Asian ideograph
    0x216C3C: (0x52CA, 0),  # East Asian ideograph
    0x216C3D: (0x52CD, 0),  # East Asian ideograph
    0x2E6C3E: (0x7B59, 0),  # East Asian ideograph
    0x2D622C: (0x9F08, 0),  # East Asian ideograph
    0x216C40: (0x52D0, 0),  # East Asian ideograph
    0x226C41: (0x7B85, 0),  # East Asian ideograph
    0x706C42: (0x70BB, 0),  # East Asian ideograph
    0x226C43: (0x7B8E, 0),  # East Asian ideograph
    0x226C44: (0x7B98, 0),  # East Asian ideograph
    0x213239: (0x504C, 0),  # East Asian ideograph
    0x226C46: (0x7B86, 0),  # East Asian ideograph
    0x226C48: (0x7B99, 0),  # East Asian ideograph
    0x6F4F3A: (0xB860, 0),  # Korean hangul
    0x216C4C: (0x52E3, 0),  # East Asian ideograph
    0x216C4E: (0x52E1, 0),  # East Asian ideograph
    0x6F5D61: (0xD720, 0),  # Korean hangul
    0x216C50: (0x55E7, 0),  # East Asian ideograph
    0x226C52: (0x7BB2, 0),  # East Asian ideograph
    0x216C53: (0x52E9, 0),  # East Asian ideograph
    0x6F5623: (0xC648, 0),  # Korean hangul
    0x226C58: (0x7BCB, 0),  # East Asian ideograph
    0x226C59: (0x7BB8, 0),  # East Asian ideograph
    0x226C5A: (0x7BCF, 0),  # East Asian ideograph
    0x226C5C: (0x7BD0, 0),  # East Asian ideograph
    0x216C5E: (0x52F7, 0),  # East Asian ideograph
    0x292765: (0x82C8, 0),  # East Asian ideograph
    0x226C60: (0x7BBE, 0),  # East Asian ideograph
    0x216C61: (0x52F9, 0),  # East Asian ideograph
    0x216C62: (0x52FA, 0),  # East Asian ideograph
    0x216C64: (0x52FC, 0),  # East Asian ideograph
    0x216C69: (0x5307, 0),  # East Asian ideograph
    0x216C6A: (0x5303, 0),  # East Asian ideograph
    0x216C6B: (0x5306, 0),  # East Asian ideograph (not in Unicode)
    0x6F5D62: (0xD728, 0),  # Korean hangul
    0x216C6E: (0x530A, 0),  # East Asian ideograph
    0x226C6F: (0x7BCC, 0),  # East Asian ideograph
    0x216560: (0x4F80, 0),  # East Asian ideograph
    0x216C77: (0x5311, 0),  # East Asian ideograph
    0x213F6A: (0x6221, 0),  # East Asian ideograph
    0x6F5975: (0xCE87, 0),  # Korean hangul
    0x216C7B: (0x6706, 0),  # East Asian ideograph
    0x234767: (0x93F5, 0),  # East Asian ideograph
    0x21323B: (0x500F, 0),  # East Asian ideograph
    0x343E38: (0x7BDA, 0),  # East Asian ideograph
    0x4B6167: (0x95D8, 0),  # East Asian ideograph
    0x6F5D63: (0xD729, 0),  # Korean hangul
    0x6F5532: (0xC571, 0),  # Korean hangul
    0x216561: (0x4F74, 0),  # East Asian ideograph
    0x4B5A31: (0x8CCE, 0),  # East Asian ideograph
    0x6F4C57: (0xB290, 0),  # Korean hangul
    0x275B42: (0x8F84, 0),  # East Asian ideograph
    0x333E7D: (0x7652, 0),  # East Asian ideograph
    0x4B4925: (
        0x6FB3,
        0,
    ),  # East Asian ideograph (variant of 214925 which maps to 6FB3)
    0x226771: (0x79A8, 0),  # East Asian ideograph
    0x225A7E: (0x7488, 0),  # East Asian ideograph
    0x6F5921: (0xCC29, 0),  # Korean hangul
    0x692577: (0x309B, 0),  # Katakana-hiragana voiced sound mark
    0x224B26: (0x6E31, 0),  # East Asian ideograph
    0x6F5A3E: (0xCF55, 0),  # Korean hangul
    0x6F4C58: (0xB291, 0),  # Korean hangul
    0x275B43: (0x8F7B, 0),  # East Asian ideograph
    0x226775: (0x79B0, 0),  # East Asian ideograph
    0x233A3B: (0x8E67, 0),  # East Asian ideograph
    0x275221: (0x7EED, 0),  # East Asian ideograph
    0x6F5922: (0xCC2C, 0),  # Korean hangul
    0x215222: (0x7E93, 0),  # East Asian ideograph
    0x234B48: (0x96B9, 0),  # East Asian ideograph
    0x4D445B: (
        0x9306,
        0,
    ),  # East Asian ideograph (variant of 23445B which maps to 9306)
    0x275223: (0x7EA4, 0),  # East Asian ideograph
    0x275224: (0x7F06, 0),  # East Asian ideograph
    0x21323E: (0x50A2, 0),  # East Asian ideograph
    0x6F4F3B: (0xB864, 0),  # Korean hangul
    0x2D334F: (0x5202, 0),  # East Asian ideograph
    0x21677B: (0x50CA, 0),  # East Asian ideograph
    0x4B4B2C: (0x731F, 0),  # East Asian ideograph
    0x213933: (0x5944, 0),  # East Asian ideograph
    0x27677C: (0x4F1B, 0),  # East Asian ideograph
    0x4C6022: (0x7596, 0),  # East Asian ideograph
    0x225227: (0x7139, 0),  # East Asian ideograph
    0x4B3C5E: (0x5E64, 0),  # East Asian ideograph
    0x234B49: (0x96BC, 0),  # East Asian ideograph
    0x215228: (0x7F3D, 0),  # East Asian ideograph
    0x6F4C5A: (0xB298, 0),  # Korean hangul
    0x275B45: (0x8F87, 0),  # East Asian ideograph
    0x215229: (0x7F44, 0),  # East Asian ideograph
    0x22363E: (0x6554, 0),  # East Asian ideograph
    0x23522B: (0x995F, 0),  # East Asian ideograph
    0x6F5924: (0xCC2F, 0),  # Korean hangul
    0x22522C: (0x713B, 0),  # East Asian ideograph
    0x516122: (0x9988, 0),  # East Asian ideograph
    0x6F522D: (0xBE90, 0),  # Korean hangul
    0x6F4C5B: (0xB299, 0),  # Korean hangul
    0x22522E: (0x711C, 0),  # East Asian ideograph
    0x213240: (0x5099, 0),  # East Asian ideograph
    0x23522F: (0x9997, 0),  # East Asian ideograph
    0x225B59: (0x74A0, 0),  # East Asian ideograph
    0x4B6168: (0x9599, 0),  # East Asian ideograph
    0x235230: (0x9998, 0),  # East Asian ideograph
    0x226D22: (0x7BDD, 0),  # East Asian ideograph
    0x216D23: (0x531A, 0),  # East Asian ideograph
    0x226D24: (0x7BE5, 0),  # East Asian ideograph
    0x216D25: (0x531F, 0),  # East Asian ideograph
    0x215231: (0x7F69, 0),  # East Asian ideograph
    0x226D29: (0x7BE8, 0),  # East Asian ideograph
    0x277267: (0x5452, 0),  # East Asian ideograph
    0x225232: (0x713D, 0),  # East Asian ideograph
    0x226D2E: (0x7BF9, 0),  # East Asian ideograph
    0x226D2F: (0x7BD4, 0),  # East Asian ideograph
    0x6F4C5C: (0xB2A0, 0),  # Korean hangul
    0x226D32: (0x7BDF, 0),  # East Asian ideograph
    0x275233: (0x7F5A, 0),  # East Asian ideograph
    0x226D35: (0x7BD8, 0),  # East Asian ideograph
    0x216D36: (0x5335, 0),  # East Asian ideograph
    0x226D37: (0x7BEA, 0),  # Unrelated variant of EACC 3A6A7C which maps to 7BEA
    0x213C2D: (0x5DBC, 0),  # East Asian ideograph
    0x275234: (0x9A82, 0),  # East Asian ideograph
    0x216D3A: (0x5338, 0),  # East Asian ideograph
    0x226D3B: (0x7C06, 0),  # East Asian ideograph
    0x226D3E: (0x7BF0, 0),  # East Asian ideograph
    0x275D6B: (0x952D, 0),  # East Asian ideograph
    0x696D40: (0x8EC5, 0),  # East Asian ideograph
    0x226D41: (0x7C0F, 0),  # East Asian ideograph
    0x216D42: (0x534D, 0),  # East Asian ideograph
    0x6F5926: (0xCC38, 0),  # Korean hangul
    0x706D45: (0x783C, 0),  # East Asian ideograph
    0x226D46: (0x7C0B, 0),  # East Asian ideograph
    0x222534: (0x5D74, 0),  # East Asian ideograph
    0x275237: (0x7F57, 0),  # East Asian ideograph
    0x216D4C: (0x5363, 0),  # East Asian ideograph
    0x2D6235: (0x9D76, 0),  # East Asian ideograph
    0x216D4E: (0x5365, 0),  # East Asian ideograph (not in Unicode)
    0x226D4F: (0x7BF4, 0),  # East Asian ideograph
    0x215238: (0x7F88, 0),  # East Asian ideograph
    0x216D53: (0x536C, 0),  # East Asian ideograph
    0x226D54: (0x7BF3, 0),  # East Asian ideograph
    0x216D57: (0x5372, 0),  # East Asian ideograph
    0x216D58: (0x537A, 0),  # East Asian ideograph
    0x4B492B: (0x6FEB, 0),  # East Asian ideograph
    0x226D5A: (0x7C09, 0),  # East Asian ideograph
    0x226D5B: (0x7C03, 0),  # East Asian ideograph
    0x226D5C: (0x7BFC, 0),  # East Asian ideograph
    0x216D5D: (0x5380, 0),  # East Asian ideograph
    0x226D5F: (0x7C1C, 0),  # East Asian ideograph
    0x226D61: (0x7C26, 0),  # East Asian ideograph
    0x226D62: (0x7C28, 0),  # East Asian ideograph
    0x22523B: (0x7129, 0),  # East Asian ideograph
    0x216D64: (0x538E, 0),  # East Asian ideograph
    0x233D3F: (0x9004, 0),  # East Asian ideograph
    0x226D66: (0x7C1F, 0),  # East Asian ideograph
    0x216D67: (0x5394, 0),  # East Asian ideograph
    0x226D68: (0x7C2F, 0),  # East Asian ideograph
    0x23523C: (0x99A1, 0),  # East Asian ideograph
    0x6F4C5E: (0xB2A5, 0),  # Korean hangul
    0x216D6D: (0x5399, 0),  # East Asian ideograph
    0x6F523D: (0xBF18, 0),  # Korean hangul
    0x285F48: (0x7617, 0),  # East Asian ideograph
    0x213243: (0x5096, 0),  # East Asian ideograph
    0x216D74: (0x8652, 0),  # East Asian ideograph
    0x226D75: (0x7C30, 0),  # East Asian ideograph
    0x6F4F3C: (0xB86C, 0),  # Korean hangul
    0x216D7A: (0x53A4, 0),  # East Asian ideograph
    0x216D7B: (0x53AB, 0),  # East Asian ideograph
    0x2D5941: (0x5629, 0),  # East Asian ideograph
    0x6F5928: (0xCC3B, 0),  # Korean hangul
    0x2D5240: (0x7FA1, 0),  # East Asian ideograph
    0x235241: (0x99A9, 0),  # East Asian ideograph
    0x6F4C5F: (0xB2A6, 0),  # Korean hangul
    0x215242: (0x7FA9, 0),  # East Asian ideograph
    0x283D30: (0x67A7, 0),  # East Asian ideograph
    0x235C5B: (0x9DF8, 0),  # East Asian ideograph
    0x225243: (0x712E, 0),  # East Asian ideograph
    0x6F5244: (0xBF51, 0),  # Korean hangul
    0x6F5929: (0xCC3C, 0),  # Korean hangul
    0x226969: (0x7A78, 0),  # East Asian ideograph
    0x6F523B: (0xBF08, 0),  # Korean hangul
    0x28337B: (0x62A0, 0),  # East Asian ideograph
    0x6F4C60: (0xB2AA, 0),  # Korean hangul
    0x4B5247: (0x7FAE, 0),  # East Asian ideograph
    0x334256: (0x6B5B, 0),  # East Asian ideograph
    0x22585D: (0x73A5, 0),  # East Asian ideograph
    0x235C5C: (0x9DFC, 0),  # East Asian ideograph
    0x225248: (0x7177, 0),  # East Asian ideograph
    0x233A43: (0x8E5D, 0),  # East Asian ideograph
    0x4B492E: (0x6E0B, 0),  # East Asian ideograph
    0x234E4C: (0x97CD, 0),  # East Asian ideograph
    0x2D7345: (0x56D3, 0),  # East Asian ideograph
    0x215249: (0x7FBF, 0),  # East Asian ideograph
    0x284E3E: (0x6CF6, 0),  # East Asian ideograph
    0x212A3A: (0xE8E7, 0),  # EACC component character
    0x2D524A: (0x7FC4, 0),  # East Asian ideograph
    0x39483B: (0x9061, 0),  # East Asian ideograph
    0x276029: (0x9791, 0),  # East Asian ideograph
    0x6F524B: (0xBFD0, 0),  # Korean hangul
    0x2E337B: (0x630E, 0),  # East Asian ideograph
    0x6F4C61: (0xB2AC, 0),  # Korean hangul
    0x6F524C: (0xBFD4, 0),  # Korean hangul
    0x27524D: (0x4E60, 0),  # East Asian ideograph
    0x233A44: (0x8E75, 0),  # East Asian ideograph
    0x23524E: (0x99BC, 0),  # East Asian ideograph
    0x293468: (0x8C35, 0),  # East Asian ideograph
    0x6F545A: (0xC410, 0),  # Korean hangul
    0x23524F: (0x99C3, 0),  # East Asian ideograph
    0x6F5250: (0xC058, 0),  # Korean hangul
    0x6F4C62: (0xB2C8, 0),  # Korean hangul
    0x275B4D: (0x8F91, 0),  # East Asian ideograph
    0x275251: (0x7FC6, 0),  # East Asian ideograph
    0x213247: (0x50B5, 0),  # East Asian ideograph
    0x4B4D73: (0x66B8, 0),  # East Asian ideograph
    0x225252: (0x7152, 0),  # East Asian ideograph
    0x235253: (0x99B9, 0),  # East Asian ideograph
    0x6F592C: (0xCC3F, 0),  # Korean hangul
    0x215254: (0x7FE9, 0),  # East Asian ideograph
    0x274D3A: (0x76CF, 0),  # East Asian ideograph
    0x225255: (0x715D, 0),  # East Asian ideograph
    0x6F4C63: (0xB2C9, 0),  # Korean hangul
    0x225256: (0x7141, 0),  # East Asian ideograph
    0x227636: (0x800F, 0),  # East Asian ideograph
    0x4B4931: (0x6E16, 0),  # East Asian ideograph
    0x4D3359: (0x56AF, 0),  # East Asian ideograph
    0x275258: (0x7FD8, 0),  # East Asian ideograph
    0x21656E: (0x4F94, 0),  # East Asian ideograph
    0x284E41: (0x6F4B, 0),  # East Asian ideograph
    0x225259: (0x7175, 0),  # East Asian ideograph
    0x692546: (0x30C6, 0),  # Katakana letter TE
    0x22525A: (0x7173, 0),  # East Asian ideograph
    0x6F4C64: (0xB2CC, 0),  # Korean hangul
    0x275B4F: (0x8F96, 0),  # East Asian ideograph
    0x33525B: (0x71FF, 0),  # East Asian ideograph
    0x226E27: (0x7C35, 0),  # East Asian ideograph
    0x23347B: (0x8B7E, 0),  # East Asian ideograph
    0x21525C: (0x8001, 0),  # East Asian ideograph
    0x226E2A: (0x7C40, 0),  # East Asian ideograph
    0x2D5573: (0x83D4, 0),  # East Asian ideograph
    0x216E2C: (0x53B5, 0),  # East Asian ideograph
    0x216E2E: (0x53B9, 0),  # East Asian ideograph
    0x22525D: (0x715A, 0),  # East Asian ideograph
    0x226E30: (0x7C39, 0),  # East Asian ideograph
    0x6F592E: (0xCC45, 0),  # Korean hangul
    0x226E34: (0x7C3B, 0),  # East Asian ideograph
    0x226E35: (0x7C34, 0),  # East Asian ideograph
    0x6F5426: (0xC2E3, 0),  # Korean hangul
    0x226E3B: (0x7C42, 0),  # East Asian ideograph
    0x216E3E: (0x53D0, 0),  # East Asian ideograph
    0x70727D: (0x87A8, 0),  # East Asian ideograph
    0x275B50: (0x8F97, 0),  # East Asian ideograph
    0x225260: (0x714B, 0),  # East Asian ideograph
    0x4C6E42: (0x7C31, 0),  # East Asian ideograph
    0x21324A: (0x50BE, 0),  # East Asian ideograph
    0x225862: (0x73A2, 0),  # East Asian ideograph
    0x226E46: (0x7C4E, 0),  # East Asian ideograph
    0x235261: (0x99D3, 0),  # East Asian ideograph
    0x216E48: (0x53DA, 0),  # East Asian ideograph
    0x4D5574: (0x9B2E, 0),  # East Asian ideograph
    0x275E47: (0x94A5, 0),  # East Asian ideograph
    0x225262: (0x7147, 0),  # East Asian ideograph
    0x6F592F: (0xCC48, 0),  # Korean hangul
    0x235263: (0x99D4, 0),  # East Asian ideograph
    0x226E54: (0x7C5D, 0),  # East Asian ideograph
    0x226E56: (0x7C5C, 0),  # East Asian ideograph
    0x226E57: (0x7C5A, 0),  # East Asian ideograph
    0x226E58: (0x7C5B, 0),  # East Asian ideograph
    0x226E59: (0x7C59, 0),  # East Asian ideograph
    0x226E5B: (0x7C5E, 0),  # East Asian ideograph
    0x226E5C: (0x7C67, 0),  # East Asian ideograph
    0x6F4C66: (0xB2D8, 0),  # Korean hangul
    0x226E5E: (0x7C63, 0),  # East Asian ideograph
    0x235265: (0x99C9, 0),  # East Asian ideograph
    0x226E61: (0x7C68, 0),  # East Asian ideograph
    0x226E62: (0x7C65, 0),  # East Asian ideograph
    0x2D3132: (0x4ECF, 0),  # East Asian ideograph
    0x225266: (0x7171, 0),  # East Asian ideograph
    0x216E68: (0x5406, 0),  # East Asian ideograph
    0x286E69: (0x7C16, 0),  # East Asian ideograph
    0x225267: (0x715F, 0),  # East Asian ideograph
    0x216E6C: (0x544C, 0),  # East Asian ideograph
    0x216E6D: (0x5445, 0),  # East Asian ideograph
    0x226E6F: (0x7C6F, 0),  # East Asian ideograph
    0x216E70: (0x5432, 0),  # East Asian ideograph
    0x226970: (0x7A85, 0),  # East Asian ideograph
    0x226E75: (0x7C75, 0),  # East Asian ideograph
    0x216E76: (0x5421, 0),  # East Asian ideograph
    0x215269: (0x8033, 0),  # East Asian ideograph
    0x216E78: (0x5430, 0),  # East Asian ideograph
    0x226E79: (0x7C7E, 0),  # East Asian ideograph
    0x226E7A: (0x7C78, 0),  # East Asian ideograph
    0x6F4C67: (0xB2D9, 0),  # Korean hangul
    0x275B52: (0x6BC2, 0),  # East Asian ideograph
    0x226E7D: (0x7C7D, 0),  # East Asian ideograph
    0x27517E: (0x7F20, 0),  # East Asian ideograph
    0x692560: (0x30E0, 0),  # Katakana letter MU
    0x215022: (0x7B4F, 0),  # East Asian ideograph
    0x6F5323: (0xC11E, 0),  # Korean hangul
    0x225421: (0x71DD, 0),  # East Asian ideograph
    0x6F486C: (0xAC16, 0),  # Korean hangul
    0x2D526C: (0x8EAD, 0),  # East Asian ideograph
    0x274A46: (0x5899, 0),  # East Asian ideograph
    0x6F5931: (0xCC54, 0),  # Korean hangul
    0x225F5F: (0x7630, 0),  # East Asian ideograph
    0x6F5B2D: (0xD145, 0),  # Korean hangul
    0x22253F: (0x5D75, 0),  # East Asian ideograph
    0x234B57: (0x96D2, 0),  # East Asian ideograph
    0x69654F: (0x7E05, 0),  # East Asian ideograph
    0x4B526E: (
        0x8046,
        0,
    ),  # East Asian ideograph (variant of 21526E which maps to 8046)
    0x6F4C68: (0xB2DB, 0),  # Korean hangul
    0x27526F: (0x5723, 0),  # East Asian ideograph
    0x22763B: (0x801F, 0),  # East Asian ideograph
    0x225422: (0x71C0, 0),  # East Asian ideograph
    0x335821: (0x97C8, 0),  # East Asian ideograph
    0x275271: (0x95FB, 0),  # East Asian ideograph
    0x6F5932: (0xCC55, 0),  # Korean hangul
    0x6F5272: (0xC0D0, 0),  # Korean hangul
    0x2D446B: (0x6936, 0),  # East Asian ideograph
    0x2D6241: (0x9D5E, 0),  # East Asian ideograph
    0x21346A: (0x536F, 0),  # East Asian ideograph
    0x275B54: (0x8F99, 0),  # East Asian ideograph
    0x235274: (0x99EC, 0),  # East Asian ideograph
    0x2E625F: (0x77C1, 0),  # East Asian ideograph
    0x275275: (0x8038, 0),  # East Asian ideograph
    0x4B4937: (0x56A0, 0),  # East Asian ideograph
    0x225276: (0x7172, 0),  # East Asian ideograph
    0x223D21: (0x6872, 0),  # East Asian ideograph
    0x6F5933: (0xCC58, 0),  # Korean hangul
    0x29486F: (0x9569, 0),  # East Asian ideograph
    0x275277: (0x8054, 0),  # East Asian ideograph
    0x223D22: (0x689C, 0),  # East Asian ideograph
    0x275278: (0x804C, 0),  # East Asian ideograph
    0x6F5979: (0xCE94, 0),  # Korean hangul
    0x2F3C2D: (0x8F3C, 0),  # East Asian ideograph
    0x6F4C6A: (0xB2E2, 0),  # Korean hangul
    0x275B55: (0x8F6C, 0),  # East Asian ideograph
    0x215279: (0x8076, 0),  # East Asian ideograph
    0x2E7D24: (0x83F0, 0),  # East Asian ideograph
    0x225867: (0x73B6, 0),  # East Asian ideograph
    0x235D66: (0x9E9E, 0),  # East Asian ideograph
    0x21527A: (0x807E, 0),  # East Asian ideograph
    0x213D25: (0x5ED3, 0),  # East Asian ideograph
    0x275E48: (0x92AE, 0),  # East Asian ideograph
    0x235823: (0x9BD5, 0),  # East Asian ideograph
    0x21527B: (0x807D, 0),  # East Asian ideograph
    0x217D26: (0x5AFF, 0),  # East Asian ideograph
    0x287061: (0x7EC0, 0),  # East Asian ideograph
    0x23527C: (0x99EA, 0),  # East Asian ideograph
    0x213D27: (0x5EE2, 0),  # East Asian ideograph
    0x284668: (0x6C29, 0),  # East Asian ideograph
    0x6F527D: (0xC0F7, 0),  # Korean hangul
    0x333D28: (0x53A8, 0),  # East Asian ideograph
    0x275B56: (0x8F9A, 0),  # East Asian ideograph
    0x6F527E: (0xC0F9, 0),  # Korean hangul
    0x2D3D29: (0x53AE, 0),  # East Asian ideograph
    0x33417E: (0x629E, 0),  # East Asian ideograph
    0x213D2A: (
        0x5EE3,
        0,
    ),  # East Asian ideograph (variant of 4B3D2A which maps to 5EE3)
    0x287279: (0x7F25, 0),  # East Asian ideograph
    0x294568: (0x9518, 0),  # East Asian ideograph
    0x213D2B: (0x5EDF, 0),  # East Asian ideograph
    0x287062: (0x7EC1, 0),  # East Asian ideograph
    0x6F545C: (0xC430, 0),  # Korean hangul
    0x226975: (0x7A86, 0),  # East Asian ideograph
    0x22475C: (0x6CA0, 0),  # East Asian ideograph
    0x216133: (0x99D0, 0),  # East Asian ideograph
    0x226532: (0x78B6, 0),  # East Asian ideograph
    0x213D2D: (0x9F90, 0),  # East Asian ideograph
    0x275B57: (0x8F7F, 0),  # East Asian ideograph
    0x223D2E: (0x68A9, 0),  # East Asian ideograph
    0x213D2F: (0x5EF3, 0),  # East Asian ideograph
    0x212A30: (0xE8DE, 0),  # EACC component character
    0x6F5D79: (0xD789, 0),  # Korean hangul
    0x226F21: (0x7C81, 0),  # East Asian ideograph
    0x216577: (0x4F90, 0),  # East Asian ideograph
    0x216F24: (0x542A, 0),  # East Asian ideograph
    0x33314C: (0x5FA0, 0),  # East Asian ideograph
    0x216F26: (0x5422, 0),  # East Asian ideograph
    0x274D3C: (0x5C3D, 0),  # East Asian ideograph
    0x226F28: (0x7C8E, 0),  # East Asian ideograph
    0x226F29: (0x7C91, 0),  # East Asian ideograph
    0x226F2A: (0x7C83, 0),  # East Asian ideograph
    0x226F2C: (0x7C8D, 0),  # East Asian ideograph
    0x213D32: (0x5EF6, 0),  # East Asian ideograph
    0x216F2E: (0x545F, 0),  # East Asian ideograph
    0x216F2F: (0x549C, 0),  # East Asian ideograph
    0x27393F: (0x5941, 0),  # East Asian ideograph
    0x223D33: (0x68A0, 0),  # East Asian ideograph
    0x213252: (0x50D6, 0),  # East Asian ideograph
    0x216F35: (0x5488, 0),  # East Asian ideograph
    0x216F37: (0x547F, 0),  # East Asian ideograph
    0x216F39: (0x5482, 0),  # East Asian ideograph
    0x226F3A: (0x7C99, 0),  # East Asian ideograph
    0x226F3B: (0x7C98, 0),  # East Asian ideograph
    0x6F5D7A: (0xD78C, 0),  # Korean hangul
    0x226F3E: (0x7C9C, 0),  # East Asian ideograph
    0x226F40: (0x7C95, 0),  # East Asian ideograph
    0x6F5937: (0xCC70, 0),  # Korean hangul
    0x226F42: (0x7CA7, 0),  # East Asian ideograph
    0x226F43: (0x7CA2, 0),  # East Asian ideograph
    0x226F45: (0x7C9E, 0),  # East Asian ideograph
    0x226F46: (0x7CA9, 0),  # East Asian ideograph
    0x6F5939: (0xCC98, 0),  # Korean hangul
    0x226F48: (0x7CA8, 0),  # East Asian ideograph
    0x226F49: (0x7CA1, 0),  # East Asian ideograph
    0x226F4A: (0x7CAC, 0),  # East Asian ideograph
    0x216F4B: (0x5474, 0),  # East Asian ideograph
    0x226F4C: (0x7CA6, 0),  # East Asian ideograph
    0x6F4C6E: (0xB2E5, 0),  # Korean hangul
    0x216F52: (0x5466, 0),  # East Asian ideograph
    0x216F53: (0x5464, 0),  # East Asian ideograph
    0x226F54: (0x7CB2, 0),  # East Asian ideograph
    0x216F55: (0x54A4, 0),  # East Asian ideograph
    0x213D39: (0x5F0F, 0),  # East Asian ideograph
    0x226F58: (0x7CBB, 0),  # East Asian ideograph
    0x226F59: (0x7CBF, 0),  # East Asian ideograph
    0x216F5A: (0x54AD, 0),  # East Asian ideograph
    0x216F5B: (0x54BA, 0),  # East Asian ideograph
    0x216F5C: (0x54CF, 0),  # East Asian ideograph
    0x696F5D: (0x9596, 0),  # East Asian ideograph
    0x226F5E: (0x7CBA, 0),  # East Asian ideograph
    0x226F5F: (0x7CBC, 0),  # East Asian ideograph
    0x216F60: (0x54A5, 0),  # East Asian ideograph
    0x216F63: (0x54A7, 0),  # East Asian ideograph
    0x226F64: (0x7CC2, 0),  # East Asian ideograph
    0x216F66: (0x54A2, 0),  # East Asian ideograph
    0x216F67: (0x5472, 0),  # East Asian ideograph
    0x216F68: (0x5470, 0),  # East Asian ideograph
    0x216F69: (0x54BC, 0),  # East Asian ideograph
    0x216F6A: (0x54B7, 0),  # East Asian ideograph
    0x216F6B: (0x54DE, 0),  # East Asian ideograph
    0x216F6C: (0x54D6, 0),  # East Asian ideograph
    0x226F6D: (0x7CCC, 0),  # East Asian ideograph
    0x226F6F: (0x7CC9, 0),  # East Asian ideograph
    0x226F71: (0x7CD2, 0),  # East Asian ideograph
    0x6F4A22: (0xADC0, 0),  # Korean hangul
    0x29442D: (0x94A1, 0),  # East Asian ideograph
    0x216F74: (0x54C6, 0),  # East Asian ideograph
    0x225429: (0x71CB, 0),  # East Asian ideograph
    0x226F77: (0x7CE1, 0),  # East Asian ideograph
    0x6F5D7C: (0xD798, 0),  # Korean hangul
    0x33467A: (0x6CA1, 0),  # East Asian ideograph
    0x223D3F: (0x6877, 0),  # East Asian ideograph
    0x216F7C: (0x54E2, 0),  # East Asian ideograph
    0x216F7D: (0x5507, 0),  # East Asian ideograph
    0x233D40: (0x9008, 0),  # East Asian ideograph
    0x233D59: (0x9036, 0),  # East Asian ideograph
    0x277D74: (0x5A08, 0),  # East Asian ideograph
    0x333D42: (0x7D43, 0),  # East Asian ideograph
    0x213A63: (0x5B7F, 0),  # East Asian ideograph
    0x213D43: (0x5F27, 0),  # East Asian ideograph
    0x2D3366: (0x5234, 0),  # East Asian ideograph
    0x6F5D7D: (0xD799, 0),  # Korean hangul
    0x223D44: (0x688E, 0),  # East Asian ideograph
    0x6F593A: (0xCC99, 0),  # Korean hangul
    0x233D45: (0x900B, 0),  # East Asian ideograph
    0x277030: (0x5457, 0),  # East Asian ideograph
    0x697023: (0x9666, 0),  # East Asian ideograph
    0x6F4A64: (0xAEDC, 0),  # Korean hangul
    0x213D47: (0x5F35, 0),  # East Asian ideograph
    0x235C6D: (0x9DEE, 0),  # East Asian ideograph
    0x233D48: (0x900C, 0),  # East Asian ideograph
    0x6F5D7E: (0xD79B, 0),  # Korean hangul
    0x213D49: (0x5F3C, 0),  # East Asian ideograph
    0x6F593B: (0xCC9C, 0),  # Korean hangul
    0x394944: (0x6B12, 0),  # East Asian ideograph
    0x6F5B2F: (0xD14D, 0),  # Korean hangul
    0x224762: (0x6CEB, 0),  # East Asian ideograph
    0x4B3B52: (0x8132, 0),  # East Asian ideograph
    0x2D4474: (
        0x690D,
        0,
    ),  # East Asian ideograph (variant of 214474 which maps to 690D)
    0x273D4B: (0x5F39, 0),  # East Asian ideograph
    0x2D4031: (0x64A6, 0),  # East Asian ideograph
    0x6F5A32: (0xCF10, 0),  # Korean hangul
    0x213D4C: (0x5F4C, 0),  # East Asian ideograph
    0x213D4D: (0x5F4E, 0),  # East Asian ideograph
    0x4B4940: (0x6F45, 0),  # East Asian ideograph
    0x23582B: (0x9BF1, 0),  # East Asian ideograph
    0x6F5D25: (0xD5E5, 0),  # Korean hangul
    0x213D4E: (0x5F57, 0),  # East Asian ideograph
    0x6F5030: (0xBA65, 0),  # Korean hangul
    0x224763: (0x6CEE, 0),  # East Asian ideograph
    0x226539: (0x78B7, 0),  # East Asian ideograph
    0x213D50: (0x5F5D, 0),  # East Asian ideograph
    0x6F4C73: (0xB2ED, 0),  # Korean hangul
    0x223D51: (0x6917, 0),  # East Asian ideograph
    0x225870: (0x73C8, 0),  # East Asian ideograph
    0x217247: (0x5642, 0),  # East Asian ideograph
    0x4B6247: (0x9D2C, 0),  # East Asian ideograph
    0x217D52: (0x5B2C, 0),  # East Asian ideograph
    0x23582C: (0x9BE1, 0),  # East Asian ideograph
    0x213D53: (0x5F65, 0),  # East Asian ideograph
    0x28706A: (0x7ED0, 0),  # East Asian ideograph
    0x294871: (0x954A, 0),  # East Asian ideograph
    0x6F5D78: (0xD788, 0),  # Korean hangul
    0x224764: (0x6CC0, 0),  # East Asian ideograph
    0x6F597B: (0xCEA0, 0),  # Korean hangul
    0x275B5F: (0x529E, 0),  # East Asian ideograph
    0x285F5E: (0x7618, 0),  # East Asian ideograph
    0x223D56: (0x690B, 0),  # East Asian ideograph
    0x213259: (0x5100, 0),  # East Asian ideograph
    0x233D57: (0x9034, 0),  # East Asian ideograph
    0x455122: (0x7D0D, 0),  # East Asian ideograph
    0x23582D: (0x9BDB, 0),  # East Asian ideograph
    0x233D58: (0x902F, 0),  # East Asian ideograph
    0x6F593E: (0xCCA9, 0),  # Korean hangul
    0x223D59: (0x6904, 0),  # East Asian ideograph
    0x6F5B45: (0xD230, 0),  # Korean hangul
    0x234B64: (0x96DF, 0),  # East Asian ideograph
    0x6F4C75: (0xB2F3, 0),  # Korean hangul
    0x275B60: (0x8F9E, 0),  # East Asian ideograph
    0x227022: (0x7CDD, 0),  # East Asian ideograph
    0x217023: (0x5517, 0),  # East Asian ideograph
    0x217024: (0x54FD, 0),  # East Asian ideograph
    0x217025: (0x54E7, 0),  # East Asian ideograph
    0x217027: (0x54F3, 0),  # East Asian ideograph
    0x227028: (0x7CED, 0),  # East Asian ideograph
    0x213D5C: (0x5F80, 0),  # East Asian ideograph
    0x21702A: (0x54E4, 0),  # East Asian ideograph
    0x21702B: (0x550A, 0),  # East Asian ideograph
    0x21702D: (0x54FF, 0),  # East Asian ideograph
    0x21702E: (0x5518, 0),  # East Asian ideograph
    0x223D5D: (0x6929, 0),  # East Asian ideograph
    0x227030: (0x7CF2, 0),  # East Asian ideograph
    0x6F593F: (0xCCAB, 0),  # Korean hangul
    0x217032: (0x54EF, 0),  # East Asian ideograph
    0x217034: (0x5508, 0),  # East Asian ideograph
    0x227035: (0x7CF4, 0),  # East Asian ideograph
    0x217038: (0x54F6, 0),  # East Asian ideograph
    0x227039: (0x7CF6, 0),  # East Asian ideograph
    0x6F4C76: (0xB2F4, 0),  # Korean hangul
    0x21703E: (0x550E, 0),  # East Asian ideograph
    0x275B61: (0x8FA9, 0),  # East Asian ideograph
    0x4B5C50: (0x9045, 0),  # East Asian ideograph
    0x692563: (0x30E3, 0),  # Katakana letter small YA
    0x21325B: (0x50FB, 0),  # East Asian ideograph
    0x217044: (0x5523, 0),  # East Asian ideograph
    0x227045: (0x7D08, 0),  # East Asian ideograph
    0x217046: (0x550F, 0),  # East Asian ideograph
    0x217047: (0x5511, 0),  # East Asian ideograph
    0x23582F: (0x9BE2, 0),  # East Asian ideograph
    0x22704A: (0x7D13, 0),  # East Asian ideograph
    0x21704B: (0x5575, 0),  # East Asian ideograph
    0x21704D: (0x5573, 0),  # East Asian ideograph
    0x21704E: (0x554C, 0),  # East Asian ideograph
    0x21704F: (0x5576, 0),  # East Asian ideograph
    0x217050: (0x554D, 0),  # East Asian ideograph
    0x217051: (0x555A, 0),  # East Asian ideograph
    0x227052: (0x7D1D, 0),  # East Asian ideograph
    0x217053: (0x553C, 0),  # East Asian ideograph
    0x217055: (0x5550, 0),  # East Asian ideograph
    0x217057: (0x5539, 0),  # East Asian ideograph
    0x217058: (0x5548, 0),  # East Asian ideograph
    0x217059: (0x552D, 0),  # East Asian ideograph
    0x21705A: (0x5551, 0),  # East Asian ideograph
    0x6F4C77: (0xB2F5, 0),  # Korean hangul
    0x21705D: (0x552A, 0),  # East Asian ideograph
    0x213D65: (0x5F8C, 0),  # East Asian ideograph
    0x217060: (0x5562, 0),  # East Asian ideograph
    0x217061: (0x5536, 0),  # East Asian ideograph
    0x227062: (0x7D32, 0),  # East Asian ideograph
    0x217064: (0x5549, 0),  # East Asian ideograph
    0x227065: (0x7D31, 0),  # East Asian ideograph
    0x335830: (0x658D, 0),  # East Asian ideograph
    0x227068: (0x7D45, 0),  # East Asian ideograph
    0x21706A: (0x5540, 0),  # East Asian ideograph
    0x21706B: (0x5535, 0),  # East Asian ideograph
    0x22706C: (0x7D29, 0),  # East Asian ideograph
    0x6F5941: (0xCCB4, 0),  # Korean hangul
    0x22706F: (0x7D41, 0),  # East Asian ideograph
    0x217070: (0x5545, 0),  # East Asian ideograph
    0x227071: (0x7D3E, 0),  # East Asian ideograph
    0x234B67: (0x96DD, 0),  # East Asian ideograph
    0x213D69: (0x5F98, 0),  # East Asian ideograph
    0x217079: (0x553F, 0),  # East Asian ideograph
    0x22707A: (0x7D5C, 0),  # East Asian ideograph
    0x21707B: (0x5541, 0),  # East Asian ideograph
    0x22707C: (0x7D53, 0),  # East Asian ideograph
    0x21707D: (0x5565, 0),  # East Asian ideograph
    0x22707E: (0x7D5A, 0),  # East Asian ideograph
    0x275779: (0x891B, 0),  # East Asian ideograph
    0x225432: (0x71EB, 0),  # East Asian ideograph
    0x235831: (0x9BF0, 0),  # East Asian ideograph
    0x213D6C: (0x5F9E, 0),  # East Asian ideograph
    0x6F5942: (0xCCB5, 0),  # Korean hangul
    0x213F27: (0x614D, 0),  # East Asian ideograph
    0x213B3F: (0x5C08, 0),  # East Asian ideograph
    0x283D6E: (0x67A8, 0),  # East Asian ideograph
    0x2D6251: (0x5869, 0),  # East Asian ideograph
    0x6F4C79: (0xB2F9, 0),  # Korean hangul
    0x275B64: (0x519C, 0),  # East Asian ideograph
    0x273D6F: (0x590D, 0),  # East Asian ideograph
    0x21325E: (0x5102, 0),  # East Asian ideograph
    0x6F4A24: (0xADC8, 0),  # Korean hangul
    0x4B4947: (0x7AC3, 0),  # East Asian ideograph
    0x6F5943: (0xCCB8, 0),  # Korean hangul
    0x213F28: (0x614B, 0),  # East Asian ideograph
    0x213D73: (0x5FAE, 0),  # East Asian ideograph
    0x2D6252: (0x78B1, 0),  # East Asian ideograph
    0x295A59: (0x9E38, 0),  # East Asian ideograph
    0x277328: (0x54DC, 0),  # East Asian ideograph
    0x213D74: (0x5FB9, 0),  # East Asian ideograph
    0x21325F: (0x510D, 0),  # East Asian ideograph
    0x285B21: (0x740F, 0),  # East Asian ideograph
    0x233A5D: (0x8E94, 0),  # East Asian ideograph
    0x213D75: (0x5FB7, 0),  # East Asian ideograph
    0x275D71: (0x94A2, 0),  # East Asian ideograph
    0x217D76: (0x5B4B, 0),  # East Asian ideograph
    0x6F5023: (0xBA3C, 0),  # Korean hangul
    0x226822: (0x79B8, 0),  # East Asian ideograph
    0x223D78: (0x68FD, 0),  # East Asian ideograph
    0x226823: (0x79BA, 0),  # East Asian ideograph
    0x213D79: (0x5FC5, 0),  # East Asian ideograph
    0x4B7E6A: (
        0x5BC3,
        0,
    ),  # East Asian ideograph (variant of 217E6A which maps to 5BC3)
    0x223F3E: (0x696F, 0),  # East Asian ideograph
    0x212A33: (0xE8E0, 0),  # EACC component character
    0x223D7B: (0x68F3, 0),  # East Asian ideograph
    0x6F5945: (0xCCC7, 0),  # Korean hangul
    0x6F5B31: (0xD154, 0),  # Korean hangul
    0x213D7C: (0x5FCC, 0),  # East Asian ideograph
    0x27493C: (0x6FD2, 0),  # East Asian ideograph
    0x213261: (0x5109, 0),  # East Asian ideograph
    0x233A5F: (0x8E92, 0),  # East Asian ideograph
    0x29282A: (0x8539, 0),  # East Asian ideograph
    0x29494D: (0x9609, 0),  # East Asian ideograph
    0x6F5342: (0xC190, 0),  # Korean hangul
    0x696D3F: (0x8EBE, 0),  # East Asian ideograph
    0x213F2B: (0x6134, 0),  # East Asian ideograph
    0x334729: (0x6E2B, 0),  # East Asian ideograph
    0x6F4C7D: (0xB300, 0),  # Korean hangul
    0x2F2A64: (0x87B5, 0),  # East Asian ideograph
    0x22682E: (0x79D5, 0),  # East Asian ideograph
    0x287431: (0x575B, 0),  # East Asian ideograph (duplicate simplified)
    0x275E60: (0x960E, 0),  # East Asian ideograph
    0x233A60: (0x8E93, 0),  # East Asian ideograph
    0x22282F: (0x5EA4, 0),  # East Asian ideograph
    0x227122: (0x7D70, 0),  # East Asian ideograph
    0x217123: (0x5591, 0),  # East Asian ideograph
    0x697124: (0x98AA, 0),  # East Asian ideograph
    0x217125: (0x5577, 0),  # East Asian ideograph
    0x217126: (0x55A8, 0),  # East Asian ideograph
    0x217127: (0x55AD, 0),  # East Asian ideograph
    0x227129: (0x7D67, 0),  # East Asian ideograph
    0x21712A: (0x5605, 0),  # East Asian ideograph
    0x22712B: (0x7D6A, 0),  # East Asian ideograph
    0x22712C: (0x7D6B, 0),  # East Asian ideograph
    0x216832: (0x50D4, 0),  # East Asian ideograph
    0x21712F: (0x5586, 0),  # East Asian ideograph
    0x227130: (0x7D73, 0),  # East Asian ideograph
    0x227134: (0x7D4E, 0),  # East Asian ideograph
    0x217136: (0x55B4, 0),  # East Asian ideograph
    0x227137: (0x7D8B, 0),  # East Asian ideograph
    0x227139: (0x7D88, 0),  # East Asian ideograph
    0x22713B: (0x7D85, 0),  # East Asian ideograph
    0x2D514A: (0x6DD6, 0),  # East Asian ideograph
    0x22713D: (0x7D8E, 0),  # East Asian ideograph
    0x216835: (0x50E6, 0),  # East Asian ideograph
    0x6F5948: (0xCD08, 0),  # Korean hangul
    0x227142: (0x7D7F, 0),  # East Asian ideograph
    0x217143: (
        0x55E2,
        0,
    ),  # East Asian ideograph (variant of 2D7143 which maps to 55E2)
    0x227144: (0x7D86, 0),  # East Asian ideograph
    0x217145: (0x558E, 0),  # East Asian ideograph
    0x217147: (0x55B5, 0),  # East Asian ideograph
    0x227148: (0x7D8D, 0),  # East Asian ideograph
    0x217149: (0x558F, 0),  # East Asian ideograph
    0x21714B: (0x5559, 0),  # East Asian ideograph
    0x22714D: (0x7D83, 0),  # East Asian ideograph
    0x22714F: (0x7D7D, 0),  # East Asian ideograph
    0x217150: (0x55A4, 0),  # East Asian ideograph
    0x217151: (0x5592, 0),  # East Asian ideograph
    0x217152: (0x5599, 0),  # East Asian ideograph
    0x227154: (0x7D7B, 0),  # East Asian ideograph
    0x233A62: (0x8E90, 0),  # East Asian ideograph
    0x217156: (0x55F4, 0),  # East Asian ideograph
    0x227158: (0x7D7A, 0),  # East Asian ideograph
    0x227159: (0x7D96, 0),  # East Asian ideograph
    0x22715A: (0x7D5B, 0),  # East Asian ideograph
    0x22715B: (0x7D8C, 0),  # East Asian ideograph
    0x21715C: (0x55DE, 0),  # East Asian ideograph
    0x21715D: (0x55D9, 0),  # East Asian ideograph
    0x21715E: (0x55C3, 0),  # East Asian ideograph
    0x21715F: (0x55C9, 0),  # East Asian ideograph
    0x217161: (0x55CA, 0),  # East Asian ideograph
    0x227162: (0x7DAE, 0),  # East Asian ideograph
    0x21683B: (0x50CE, 0),  # East Asian ideograph
    0x217164: (0x55D4, 0),  # East Asian ideograph
    0x217165: (0x55C4, 0),  # East Asian ideograph
    0x227167: (0x7DCB, 0),  # East Asian ideograph
    0x227169: (0x7DAA, 0),  # East Asian ideograph
    0x22716A: (0x7DCE, 0),  # East Asian ideograph
    0x22716B: (0x7DC9, 0),  # East Asian ideograph
    0x692565: (0x30E5, 0),  # Katakana letter small YU
    0x22716E: (0x7DC5, 0),  # East Asian ideograph
    0x22716F: (0x7DA6, 0),  # East Asian ideograph
    0x217170: (0x55D2, 0),  # East Asian ideograph
    0x223664: (0x6585, 0),  # East Asian ideograph
    0x277C36: (0x59AB, 0),  # East Asian ideograph
    0x22543A: (0x71F5, 0),  # East Asian ideograph
    0x227174: (0x7DC4, 0),  # East Asian ideograph
    0x217175: (0x55E5, 0),  # East Asian ideograph
    0x6F4871: (0xAC1C, 0),  # Korean hangul
    0x217177: (0x55D6, 0),  # East Asian ideograph
    0x227178: (0x7DAC, 0),  # East Asian ideograph
    0x217179: (0x55F2, 0),  # East Asian ideograph
    0x6F5C77: (0xD590, 0),  # Korean hangul
    0x2E717C: (0x7D63, 0),  # East Asian ideograph
    0x22717D: (0x7DB9, 0),  # East Asian ideograph
    0x21717E: (0x5627, 0),  # East Asian ideograph
    0x292840: (0x84E0, 0),  # East Asian ideograph
    0x235F5F: (0x9F37, 0),  # East Asian ideograph
    0x216841: (0x50F3, 0),  # East Asian ideograph
    0x216842: (0x50E8, 0),  # East Asian ideograph
    0x217255: (0x5635, 0),  # East Asian ideograph
    0x2D514D: (0x7D2C, 0),  # East Asian ideograph
    0x216844: (0x50F0, 0),  # East Asian ideograph
    0x6F594B: (0xCD10, 0),  # Korean hangul
    0x224772: (0x6CF5, 0),  # East Asian ideograph
    0x6F4E69: (0xB78D, 0),  # Korean hangul
    0x23307D: (0x89AF, 0),  # East Asian ideograph
    0x295B35: (0x9E2B, 0),  # East Asian ideograph
    0x4B7874: (0x590A, 0),  # East Asian ideograph
    0x23284C: (0x8645, 0),  # East Asian ideograph
    0x6F4A26: (0xADD1, 0),  # Korean hangul
    0x22543D: (0x71F3, 0),  # East Asian ideograph
    0x234E53: (0x97D8, 0),  # East Asian ideograph
    0x69684D: (0x8422, 0),  # East Asian ideograph
    0x333623: (0x9F69, 0),  # East Asian ideograph
    0x225B61: (0x74B1, 0),  # East Asian ideograph
    0x6F553B: (0xC58C, 0),  # Korean hangul
    0x706D3F: (0x781C, 0),  # East Asian ideograph
    0x4B587A: (0x8ACB, 0),  # East Asian ideograph
    0x6F7723: (0xE8CA, 0),  # Korean hangul
    0x213F32: (0x615D, 0),  # East Asian ideograph
    0x234730: (0x93E6, 0),  # East Asian ideograph
    0x222851: (0x5ECC, 0),  # East Asian ideograph
    0x6F594E: (0xCD1B, 0),  # Korean hangul
    0x284E62: (0x6F4D, 0),  # East Asian ideograph
    0x6F5732: (0xC7CC, 0),  # Korean hangul
    0x6F5328: (0xC126, 0),  # Korean hangul
    0x213F33: (0x6182, 0),  # East Asian ideograph
    0x285F6F: (0x7605, 0),  # East Asian ideograph
    0x6F4A3D: (0xAE43, 0),  # Korean hangul
    0x6F4E25: (0xB545, 0),  # Korean hangul
    0x295F2B: (0x9F0D, 0),  # East Asian ideograph
    0x212A35: (0xE8E2, 0),  # EACC component character
    0x6F594F: (0xCD1D, 0),  # Korean hangul
    0x6F5B33: (0xD15D, 0),  # Korean hangul
    0x274621: (0x6B22, 0),  # East Asian ideograph
    0x232859: (0x864D, 0),  # East Asian ideograph
    0x224333: (0x6ADF, 0),  # East Asian ideograph
    0x234732: (0x940B, 0),  # East Asian ideograph
    0x21797C: (0x5997, 0),  # East Asian ideograph
    0x23285A: (0x8653, 0),  # East Asian ideograph
    0x6F4E43: (0xB614, 0),  # Korean hangul
    0x227222: (0x7D9F, 0),  # East Asian ideograph
    0x217224: (0x55FB, 0),  # East Asian ideograph
    0x217225: (0x5612, 0),  # East Asian ideograph
    0x217227: (0x55F8, 0),  # East Asian ideograph
    0x217228: (0x560F, 0),  # East Asian ideograph
    0x227229: (0x7DE1, 0),  # East Asian ideograph
    0x22722A: (0x7DD9, 0),  # East Asian ideograph
    0x22722B: (0x7DE4, 0),  # East Asian ideograph
    0x6F4F44: (0xB8E9, 0),  # Korean hangul
    0x21722E: (0x561E, 0),  # East Asian ideograph
    0x217539: (0x5790, 0),  # East Asian ideograph
    0x227231: (0x7DD7, 0),  # East Asian ideograph
    0x295263: (0x9A75, 0),  # East Asian ideograph
    0x217234: (0x561C, 0),  # East Asian ideograph
    0x217235: (0x5610, 0),  # East Asian ideograph
    0x217236: (0x5601, 0),  # East Asian ideograph
    0x217238: (0x5613, 0),  # East Asian ideograph
    0x217239: (0x55F6, 0),  # East Asian ideograph
    0x22723A: (0x7E06, 0),  # East Asian ideograph
    0x21685F: (0x5105, 0),  # East Asian ideograph
    0x21723C: (0x5602, 0),  # East Asian ideograph
    0x22723E: (0x7DE6, 0),  # East Asian ideograph
    0x697240: (0x9BB4, 0),  # East Asian ideograph
    0x217242: (0x561D, 0),  # East Asian ideograph
    0x27577C: (0x88C6, 0),  # East Asian ideograph
    0x217244: (0x55FF, 0),  # East Asian ideograph
    0x697245: (0x9BCF, 0),  # East Asian ideograph
    0x227246: (0x7DDC, 0),  # East Asian ideograph
    0x216861: (0x50FC, 0),  # East Asian ideograph
    0x217248: (0x564C, 0),  # East Asian ideograph
    0x227249: (0x7DE5, 0),  # East Asian ideograph
    0x22724B: (0x7DF5, 0),  # East Asian ideograph
    0x6F4E6A: (0xB78F, 0),  # Korean hangul
    0x295021: (0x98A2, 0),  # East Asian ideograph
    0x2E7328: (0x5FAD, 0),  # East Asian ideograph
    0x227250: (0x7E17, 0),  # East Asian ideograph
    0x227251: (0x7E1E, 0),  # East Asian ideograph
    0x227252: (0x7E21, 0),  # East Asian ideograph
    0x227253: (0x7E0B, 0),  # East Asian ideograph
    0x224335: (0x6ADE, 0),  # East Asian ideograph
    0x227256: (0x7E22, 0),  # East Asian ideograph
    0x217257: (0x5649, 0),  # East Asian ideograph
    0x217258: (0x5641, 0),  # East Asian ideograph
    0x2D5124: (0x5E0B, 0),  # East Asian ideograph
    0x22725B: (0x7E20, 0),  # East Asian ideograph
    0x21725C: (0x5658, 0),  # East Asian ideograph
    0x22725D: (0x7E1D, 0),  # East Asian ideograph
    0x21725E: (0x5654, 0),  # East Asian ideograph
    0x216865: (0x5106, 0),  # East Asian ideograph
    0x217260: (0x562A, 0),  # East Asian ideograph
    0x217261: (0x563D, 0),  # East Asian ideograph
    0x217264: (0x562C, 0),  # East Asian ideograph
    0x227265: (0x7E15, 0),  # East Asian ideograph
    0x6F5474: (0xC52C, 0),  # Korean hangul
    0x217267: (0x5638, 0),  # East Asian ideograph
    0x4D5154: (0x9942, 0),  # East Asian ideograph
    0x217269: (0x564D, 0),  # East Asian ideograph
    0x22726A: (0x7E0F, 0),  # East Asian ideograph
    0x21726B: (0x562B, 0),  # East Asian ideograph
    0x21726C: (0x564F, 0),  # East Asian ideograph
    0x22726D: (0x7E3B, 0),  # East Asian ideograph
    0x21726E: (0x5670, 0),  # East Asian ideograph
    0x21726F: (0x565F, 0),  # East Asian ideograph
    0x217270: (0x567C, 0),  # East Asian ideograph
    0x227271: (0x7E34, 0),  # East Asian ideograph
    0x227272: (0x7E2D, 0),  # East Asian ideograph
    0x227273: (0x7E2F, 0),  # East Asian ideograph
    0x227275: (0x7E36, 0),  # East Asian ideograph
    0x227277: (0x7E3A, 0),  # East Asian ideograph
    0x217278: (0x5676, 0),  # East Asian ideograph
    0x227279: (0x7E39, 0),  # East Asian ideograph
    0x21727A: (0x5666, 0),  # East Asian ideograph
    0x21727B: (0x5673, 0),  # East Asian ideograph
    0x21727C: (0x566D, 0),  # East Asian ideograph
    0x22727D: (0x7E44, 0),  # East Asian ideograph
    0x21727E: (0x5672, 0),  # East Asian ideograph
    0x33537D: (0x9AD5, 0),  # East Asian ideograph
    0x4B3E7E: (0x60A9, 0),  # East Asian ideograph
    0x6F5953: (0xCD94, 0),  # Korean hangul
    0x6F7729: (0xAE0E, 0),  # Korean hangul
    0x224B30: (0x6E36, 0),  # East Asian ideograph
    0x2D6262: (0x9EC4, 0),  # East Asian ideograph
    0x2D4049: (0x67B4, 0),  # East Asian ideograph
    0x4B5C54: (0x8F9F, 0),  # East Asian ideograph (duplicate simplified)
    0x2E686F: (0x7A19, 0),  # East Asian ideograph
    0x6F4873: (0xAC20, 0),  # Korean hangul
    0x33362A: (0x9B28, 0),  # East Asian ideograph
    0x216871: (0x5115, 0),  # East Asian ideograph
    0x6F5954: (0xCD95, 0),  # Korean hangul
    0x6F5B34: (0xD15F, 0),  # Korean hangul
    0x234B7A: (0x96F5, 0),  # East Asian ideograph
    0x6F4F45: (0xB8EC, 0),  # Korean hangul
    0x6F5031: (0xBA67, 0),  # Korean hangul
    0x6F5955: (0xCD98, 0),  # Korean hangul
    0x215321: (0x8085, 0),  # East Asian ideograph
    0x6F772B: (0xAE11, 0),  # Korean hangul
    0x213F3A: (0x615F, 0),  # East Asian ideograph
    0x6F5322: (0xC11D, 0),  # Korean hangul
    0x225323: (0x7192, 0),  # East Asian ideograph
    0x2D5E21: (0x9418, 0),  # East Asian ideograph
    0x29415C: (0x917E, 0),  # East Asian ideograph
    0x215324: (0x808B, 0),  # East Asian ideograph
    0x6F5325: (0xC123, 0),  # Korean hangul
    0x224539: (0x6BAB, 0),  # East Asian ideograph
    0x6F5956: (0xCD9C, 0),  # Korean hangul
    0x695326: (0x54D8, 0),  # East Asian ideograph
    0x22477D: (0x6CC2, 0),  # East Asian ideograph
    0x23287C: (0x866F, 0),  # East Asian ideograph
    0x6F5327: (0xC125, 0),  # Korean hangul
    0x275E35: (0x9558, 0),  # East Asian ideograph
    0x2D404C: (0x6283, 0),  # East Asian ideograph
    0x6F4B6B: (0xB0E0, 0),  # Korean hangul
    0x275735: (0x8681, 0),  # East Asian ideograph
    0x6F4A28: (0xADDC, 0),  # Korean hangul
    0x235329: (0x99F8, 0),  # East Asian ideograph
    0x225447: (0x71E0, 0),  # East Asian ideograph
    0x23532A: (0x99F4, 0),  # East Asian ideograph
    0x6F5957: (0xCDA4, 0),  # Korean hangul
    0x21532B: (0x8096, 0),  # East Asian ideograph
    0x276842: (0x507E, 0),  # East Asian ideograph
    0x274629: (0x5C81, 0),  # East Asian ideograph
    0x213F3C: (0x617E, 0),  # East Asian ideograph
    0x21532C: (0x80B2, 0),  # East Asian ideograph
    0x6F5235: (0xBED8, 0),  # Korean hangul
    0x6F532D: (0xC12F, 0),  # Korean hangul
    0x213273: (0x5147, 0),  # East Asian ideograph
    0x6F532E: (0xC130, 0),  # Korean hangul
    0x275D75: (0x9525, 0),  # East Asian ideograph
    0x216F43: (0x546B, 0),  # East Asian ideograph
    0x6F5958: (0xCDA5, 0),  # Korean hangul
    0x215330: (0x80A2, 0),  # East Asian ideograph
    0x27462A: (0x5386, 0),  # East Asian ideograph
    0x217325: (0x5693, 0),  # East Asian ideograph
    0x227326: (0x7E3F, 0),  # East Asian ideograph
    0x215331: (0x80AB, 0),  # East Asian ideograph
    0x227328: (0x7E47, 0),  # East Asian ideograph
    0x225332: (0x7185, 0),  # East Asian ideograph
    0x22732F: (0x7E51, 0),  # East Asian ideograph
    0x217332: (0x56BA, 0),  # East Asian ideograph
    0x215333: (0x80AF, 0),  # East Asian ideograph
    0x227334: (0x7E67, 0),  # East Asian ideograph
    0x217335: (0x5684, 0),  # East Asian ideograph
    0x217336: (0x5691, 0),  # East Asian ideograph
    0x227337: (0x7E56, 0),  # East Asian ideograph
    0x6F5334: (0xC140, 0),  # Korean hangul
    0x21733E: (0x569E, 0),  # East Asian ideograph
    0x6F5335: (0xC148, 0),  # Korean hangul
    0x27462B: (0x5F52, 0),  # East Asian ideograph
    0x217342: (0x569A, 0),  # East Asian ideograph
    0x213F3E: (0x61B2, 0),  # East Asian ideograph
    0x225336: (0x717C, 0),  # East Asian ideograph
    0x227348: (0x7E68, 0),  # East Asian ideograph
    0x227349: (0x7E6E, 0),  # East Asian ideograph
    0x21734B: (0x56AD, 0),  # East Asian ideograph
    0x21734C: (0x56A6, 0),  # East Asian ideograph
    0x22734E: (0x7E70, 0),  # East Asian ideograph
    0x6F4E66: (0xB780, 0),  # Korean hangul
    0x227351: (0x7E6F, 0),  # East Asian ideograph
    0x227352: (0x7E73, 0),  # East Asian ideograph
    0x217353: (0x56B2, 0),  # East Asian ideograph
    0x235849: (0x9C0A, 0),  # East Asian ideograph
    0x225339: (0x7198, 0),  # East Asian ideograph
    0x227358: (0x7E7B, 0),  # East Asian ideograph
    0x227359: (0x7E7E, 0),  # East Asian ideograph
    0x21735A: (0x56B3, 0),  # East Asian ideograph
    0x22735B: (0x7E81, 0),  # East Asian ideograph
    0x6F595A: (0xCDA9, 0),  # Korean hangul
    0x22735D: (0x7E8A, 0),  # East Asian ideograph
    0x22735E: (0x7E87, 0),  # East Asian ideograph
    0x6F7730: (0xAF50, 0),  # Korean hangul
    0x227360: (0x7E88, 0),  # East Asian ideograph
    0x217362: (0x56CF, 0),  # East Asian ideograph
    0x4B533B: (0x695C, 0),  # East Asian ideograph
    0x227364: (0x7E86, 0),  # East Asian ideograph
    0x23473D: (0x93FB, 0),  # East Asian ideograph
    0x217367: (0x56CD, 0),  # East Asian ideograph
    0x22533C: (0x7197, 0),  # East Asian ideograph
    0x22736A: (0x7E91, 0),  # East Asian ideograph
    0x21736B: (0x56D7, 0),  # East Asian ideograph
    0x22736D: (0x7E94, 0),  # East Asian ideograph
    0x70736E: (0x7BA2, 0),  # East Asian ideograph
    0x23533D: (0x9A0F, 0),  # East Asian ideograph
    0x227370: (0x7E9B, 0),  # East Asian ideograph
    0x227371: (0x7E9A, 0),  # East Asian ideograph
    0x22544B: (0x720C, 0),  # East Asian ideograph
    0x227373: (0x7E99, 0),  # East Asian ideograph
    0x227374: (0x7E98, 0),  # East Asian ideograph
    0x22533E: (0x71B5, 0),  # East Asian ideograph
    0x217376: (0x56EE, 0),  # East Asian ideograph
    0x217377: (0x56E7, 0),  # East Asian ideograph
    0x217379: (0x56FB, 0),  # East Asian ideograph
    0x22533F: (0x71A9, 0),  # East Asian ideograph
    0x21737E: (0x56F7, 0),  # East Asian ideograph
    0x222569: (0x5D97, 0),  # East Asian ideograph
    0x295340: (0x9A92, 0),  # East Asian ideograph
    0x4B3853: (0x586D, 0),  # East Asian ideograph (not in Unicode)
    0x4B5629: (0x85CD, 0),  # East Asian ideograph
    0x6F5341: (0xC18E, 0),  # Korean hangul
    0x6F4A29: (0xADE0, 0),  # Korean hangul
    0x225342: (0x71A5, 0),  # East Asian ideograph
    0x334260: (0x89D4, 0),  # East Asian ideograph
    0x275E50: (0x95ED, 0),  # East Asian ideograph
    0x23584B: (0x9C08, 0),  # East Asian ideograph
    0x2E3936: (0x66CD, 0),  # East Asian ideograph
    0x6F595C: (0xCDC4, 0),  # Korean hangul
    0x235344: (0x9A04, 0),  # East Asian ideograph
    0x6F7732: (0xB060, 0),  # Korean hangul
    0x235345: (0x9A11, 0),  # East Asian ideograph
    0x275B7E: (0x8FDE, 0),  # East Asian ideograph
    0x2D5E28: (0x93C1, 0),  # East Asian ideograph
    0x213A6A: (0x5B8B, 0),  # East Asian ideograph
    0x235347: (0x9A05, 0),  # East Asian ideograph
    0x4B4874: (0x6FF3, 0),  # East Asian ideograph
    0x23584C: (0x9C14, 0),  # East Asian ideograph
    0x215348: (0x80FD, 0),  # East Asian ideograph
    0x6F5349: (0xC1A8, 0),  # Korean hangul
    0x705D5C: (0x8488, 0),  # East Asian ideograph
    0x6F7733: (0xB9C4, 0),  # Korean hangul
    0x224B32: (0x6E72, 0),  # East Asian ideograph
    0x6F5128: (0xBC88, 0),  # Korean hangul
    0x22655A: (0x78D8, 0),  # East Asian ideograph
    0x27534A: (0x8090, 0),  # East Asian ideograph
    0x226D4B: (0x7C0C, 0),  # East Asian ideograph
    0x334740: (0x6D1A, 0),  # East Asian ideograph
    0x4B562B: (0x8535, 0),  # East Asian ideograph
    0x2D534B: (0x80F7, 0),  # East Asian ideograph
    0x27573C: (0x86CE, 0),  # East Asian ideograph
    0x21534C: (0x810A, 0),  # East Asian ideograph
    0x23584D: (0x9C04, 0),  # East Asian ideograph
    0x23534D: (0x9A22, 0),  # East Asian ideograph
    0x6F595E: (0xCDE8, 0),  # Korean hangul
    0x22534E: (0x71AF, 0),  # East Asian ideograph
    0x6F5B36: (0xD161, 0),  # Korean hangul
    0x6F7734: (0xC54D, 0),  # Korean hangul
    0x23534F: (0x9A20, 0),  # East Asian ideograph
    0x6F5350: (0xC1E4, 0),  # Korean hangul
    0x21327A: (0x5152, 0),  # East Asian ideograph
    0x2D6134: (0x99DE, 0),  # East Asian ideograph
    0x233A78: (0x8EB3, 0),  # East Asian ideograph
    0x4C6F7B: (0x7CE8, 0),  # East Asian ideograph
    0x235352: (0x9A27, 0),  # East Asian ideograph
    0x6F5343: (0xC194, 0),  # Korean hangul
    0x6F5353: (0xC1F1, 0),  # Korean hangul
    0x6F7735: (0xC54F, 0),  # Korean hangul
    0x213F44: (0x619A, 0),  # East Asian ideograph
    0x6F5354: (0xC1F3, 0),  # Korean hangul
    0x4C7C45: (0x82AE, 0),  # East Asian ideograph
    0x225355: (0x719A, 0),  # East Asian ideograph
    0x4D4832: (0x953F, 0),  # East Asian ideograph
    0x27573E: (0x8721, 0),  # East Asian ideograph
    0x22367A: (0x65A0, 0),  # East Asian ideograph
    0x223237: (0x63B1, 0),  # East Asian ideograph
    0x6F5629: (0xC65C, 0),  # Korean hangul
    0x225357: (0x71B3, 0),  # East Asian ideograph
    0x27407B: (0x5377, 0),  # East Asian ideograph
    0x275358: (0x80BE, 0),  # East Asian ideograph
    0x213F45: (0x61A9, 0),  # East Asian ideograph
    0x215359: (0x8139, 0),  # East Asian ideograph
    0x2D416E: (0x6534, 0),  # East Asian ideograph
    0x23535A: (0x9A38, 0),  # East Asian ideograph
    0x217421: (0x56F9, 0),  # East Asian ideograph
    0x6F4A2A: (0xADE4, 0),  # Korean hangul
    0x294435: (0x950A, 0),  # East Asian ideograph
    0x217424: (0x56FF, 0),  # East Asian ideograph
    0x227425: (0x7F43, 0),  # East Asian ideograph
    0x275E51: (0x95F5, 0),  # East Asian ideograph
    0x217427: (0x5705, 0),  # East Asian ideograph
    0x227428: (0x7F45, 0),  # East Asian ideograph
    0x217429: (0x5702, 0),  # East Asian ideograph
    0x22742B: (0x7F4B, 0),  # East Asian ideograph
    0x21742C: (0x570A, 0),  # East Asian ideograph
    0x21742D: (0x5709, 0),  # East Asian ideograph
    0x22742E: (0x7F4C, 0),  # East Asian ideograph
    0x22742F: (0x7F4D, 0),  # East Asian ideograph
    0x217430: (0x570C, 0),  # East Asian ideograph
    0x217431: (0x5715, 0),  # East Asian ideograph
    0x227432: (0x7F4F, 0),  # East Asian ideograph
    0x213F46: (0x6194, 0),  # East Asian ideograph
    0x27535E: (0x80A0, 0),  # East Asian ideograph
    0x224345: (0x6AE8, 0),  # East Asian ideograph
    0x217437: (0x571C, 0),  # East Asian ideograph
    0x4B423A: (0x64B9, 0),  # East Asian ideograph
    0x217439: (0x571D, 0),  # East Asian ideograph
    0x21743A: (0x571E, 0),  # East Asian ideograph
    0x6F535F: (0xC220, 0),  # Korean hangul
    0x22743E: (0x7F60, 0),  # East Asian ideograph
    0x22743F: (0x7F61, 0),  # East Asian ideograph
    0x235360: (0x9A2D, 0),  # East Asian ideograph
    0x217442: (0x572E, 0),  # East Asian ideograph
    0x227443: (0x7F5D, 0),  # East Asian ideograph
    0x227445: (0x7F5B, 0),  # East Asian ideograph
    0x235361: (0x9A35, 0),  # East Asian ideograph
    0x217448: (0x5738, 0),  # East Asian ideograph
    0x21744C: (0x572A, 0),  # East Asian ideograph
    0x215362: (0x816B, 0),  # East Asian ideograph
    0x6F4B43: (0xB05D, 0),  # Korean hangul
    0x227450: (0x7F65, 0),  # East Asian ideograph
    0x227451: (0x7F66, 0),  # East Asian ideograph
    0x213F47: (0x618A, 0),  # East Asian ideograph
    0x227453: (0x7F6D, 0),  # East Asian ideograph
    0x227454: (0x7F6B, 0),  # East Asian ideograph
    0x227455: (0x7F67, 0),  # East Asian ideograph
    0x227457: (0x7F68, 0),  # East Asian ideograph
    0x235364: (0x9A32, 0),  # East Asian ideograph
    0x21327E: (0x5165, 0),  # East Asian ideograph
    0x22745E: (0x7F71, 0),  # East Asian ideograph
    0x275365: (0x8111, 0),  # East Asian ideograph
    0x227460: (0x7F73, 0),  # East Asian ideograph
    0x227463: (0x7F76, 0),  # East Asian ideograph
    0x6F5022: (0xBA39, 0),  # Korean hangul
    0x217465: (0x5745, 0),  # East Asian ideograph
    0x6F572F: (0xC7C1, 0),  # Korean hangul
    0x217468: (0x574B, 0),  # East Asian ideograph
    0x217469: (0x574C, 0),  # East Asian ideograph
    0x21746A: (0x573F, 0),  # East Asian ideograph
    0x215367: (0x818F, 0),  # East Asian ideograph
    0x22746C: (0x7F7D, 0),  # East Asian ideograph
    0x6F7739: (0xC61C, 0),  # Korean hangul
    0x217470: (0x5768, 0),  # East Asian ideograph
    0x6F5368: (0xC250, 0),  # Korean hangul
    0x227472: (0x7F86, 0),  # East Asian ideograph
    0x6F4F25: (0xB807, 0),  # Korean hangul
    0x217475: (0x578A, 0),  # East Asian ideograph
    0x225369: (0x71C7, 0),  # East Asian ideograph
    0x345175: (0x7162, 0),  # East Asian ideograph
    0x217479: (0x5774, 0),  # East Asian ideograph
    0x21747A: (0x5767, 0),  # East Asian ideograph
    0x22536A: (0x71B7, 0),  # East Asian ideograph
    0x22747E: (0x7F96, 0),  # East Asian ideograph
    0x6F536B: (0xC270, 0),  # Korean hangul
    0x27536C: (0x80F6, 0),  # East Asian ideograph
    0x274636: (0x6B93, 0),  # East Asian ideograph
    0x6F5521: (0xC549, 0),  # Korean hangul
    0x21536D: (0x819B, 0),  # East Asian ideograph
    0x224348: (0x6AF5, 0),  # East Asian ideograph
    0x4B5632: (0x7C54, 0),  # East Asian ideograph
    0x27536E: (0x80A4, 0),  # East Asian ideograph
    0x454F45: (0x9896, 0),  # East Asian ideograph
    0x22536F: (0x71CF, 0),  # East Asian ideograph
    0x4C5541: (0x4E2C, 0),  # East Asian ideograph
    0x225370: (0x71D6, 0),  # East Asian ideograph
    0x213031: (0x4E1E, 0),  # East Asian ideograph
    0x215371: (0x81A9, 0),  # East Asian ideograph
    0x274637: (0x6BA1, 0),  # East Asian ideograph
    0x6F5522: (0xC54A, 0),  # Korean hangul
    0x213F4A: (0x61C9, 0),  # East Asian ideograph
    0x217463: (0x5749, 0),  # East Asian ideograph
    0x6F5373: (0xC290, 0),  # Korean hangul
    0x335172: (0x7D89, 0),  # East Asian ideograph
    0x212A29: (0xE8D7, 0),  # EACC component character
    0x6F4A2B: (0xADEC, 0),  # Korean hangul
    0x235374: (0x9A3B, 0),  # East Asian ideograph
    0x4B496A: (0x932C, 0),  # East Asian ideograph
    0x225375: (0x71C2, 0),  # East Asian ideograph
    0x6F5376: (0xC29D, 0),  # Korean hangul
    0x233E21: (0x9070, 0),  # East Asian ideograph
    0x213F4B: (0x6190, 0),  # East Asian ideograph
    0x225377: (0x71C5, 0),  # East Asian ideograph
    0x4B385E: (0x5897, 0),  # East Asian ideograph
    0x234749: (0x93FA, 0),  # East Asian ideograph
    0x2D6275: (0x76B7, 0),  # East Asian ideograph
    0x215378: (0x81BF, 0),  # East Asian ideograph
    0x216431: (0x4E36, 0),  # East Asian ideograph
    0x215379: (0x81BD, 0),  # East Asian ideograph
    0x223E24: (0x6919, 0),  # East Asian ideograph
    0x4B496B: (0x83F8, 0),  # East Asian ideograph
    0x21537A: (0x81C9, 0),  # East Asian ideograph
    0x213E25: (0x5FFD, 0),  # East Asian ideograph
    0x21537B: (0x81BE, 0),  # East Asian ideograph
    0x39304C: (0x4E81, 0),  # East Asian ideograph
    0x213E26: (0x5FDD, 0),  # East Asian ideograph
    0x23603F: (0x9F6E, 0),  # East Asian ideograph
    0x27537C: (0x8110, 0),  # East Asian ideograph
    0x33474A: (0x6D1F, 0),  # East Asian ideograph
    0x21537D: (0x81CF, 0),  # East Asian ideograph
    0x213E28: (0x5FFF, 0),  # East Asian ideograph
    0x275746: (0x672E, 0),  # East Asian ideograph
    0x21537E: (0x81D8, 0),  # East Asian ideograph
    0x6F4E26: (0xB54B, 0),  # Korean hangul
    0x227042: (0x7D06, 0),  # East Asian ideograph
    0x294471: (0x951D, 0),  # East Asian ideograph
    0x233E2A: (0x907B, 0),  # East Asian ideograph
    0x6F5968: (0xCE61, 0),  # Korean hangul
    0x6F5B38: (0xD1A0, 0),  # Korean hangul
    0x213E2B: (0x602A, 0),  # East Asian ideograph
    0x213E2C: (0x602F, 0),  # East Asian ideograph
    0x6F585B: (0xCACC, 0),  # Korean hangul
    0x213E2D: (0x6016, 0),  # East Asian ideograph
    0x213E2F: (0x600F, 0),  # East Asian ideograph
    0x6F5969: (0xCE68, 0),  # Korean hangul
    0x227523: (0x7F97, 0),  # East Asian ideograph
    0x227524: (0x7F95, 0),  # East Asian ideograph
    0x51456D: (0x822E, 0),  # East Asian ideograph
    0x217526: (0x5770, 0),  # East Asian ideograph
    0x217528: (0x5771, 0),  # East Asian ideograph
    0x21752A: (0x576E, 0),  # East Asian ideograph
    0x22752C: (0x7FA2, 0),  # East Asian ideograph
    0x21752D: (0x5776, 0),  # East Asian ideograph
    0x21752E: (0x5789, 0),  # East Asian ideograph
    0x217530: (0x577F, 0),  # East Asian ideograph
    0x217531: (0x5775, 0),  # East Asian ideograph
    0x217532: (0x577B, 0),  # East Asian ideograph
    0x227533: (0x7FA7, 0),  # East Asian ideograph
    0x217535: (0x5773, 0),  # East Asian ideograph
    0x223241: (0x636D, 0),  # East Asian ideograph
    0x217538: (0x579F, 0),  # East Asian ideograph
    0x233E34: (0x9083, 0),  # East Asian ideograph
    0x21753A: (0x5793, 0),  # East Asian ideograph
    0x22753B: (0x7FB0, 0),  # East Asian ideograph
    0x22753C: (0x7FAD, 0),  # East Asian ideograph
    0x6F596A: (0xCE69, 0),  # Korean hangul
    0x22753F: (0x7FB1, 0),  # East Asian ideograph
    0x227540: (0x7FB4, 0),  # East Asian ideograph
    0x6F5527: (0xC555, 0),  # Korean hangul
    0x227542: (0x7FB5, 0),  # East Asian ideograph
    0x217543: (0x579A, 0),  # East Asian ideograph
    0x217545: (0x5794, 0),  # East Asian ideograph
    0x217547: (0x57A4, 0),  # East Asian ideograph
    0x217548: (0x5799, 0),  # East Asian ideograph
    0x217549: (0x578C, 0),  # East Asian ideograph
    0x22754A: (0x7FBC, 0),  # East Asian ideograph
    0x21754B: (0x5797, 0),  # East Asian ideograph
    0x22754C: (0x7FBE, 0),  # East Asian ideograph
    0x275749: (0x536B, 0),  # East Asian ideograph
    0x227551: (0x7FC3, 0),  # East Asian ideograph
    0x217552: (0x579C, 0),  # East Asian ideograph
    0x217554: (0x57A7, 0),  # East Asian ideograph
    0x227557: (0x7FCA, 0),  # East Asian ideograph
    0x217559: (0x3013, 0),  # East Asian ideograph (not found in unified han)
    0x21755B: (0x5795, 0),  # East Asian ideograph
    0x213E3A: (0x6068, 0),  # East Asian ideograph
    0x21755F: (0x57B8, 0),  # East Asian ideograph
    0x217560: (0x57C7, 0),  # East Asian ideograph
    0x227567: (0x7FDB, 0),  # East Asian ideograph
    0x227568: (0x7FE3, 0),  # East Asian ideograph
    0x2D3E3C: (0x803B, 0),  # East Asian ideograph
    0x21756A: (0x5809, 0),  # East Asian ideograph
    0x22756C: (0x7FE6, 0),  # East Asian ideograph
    0x22756F: (0x7FE5, 0),  # East Asian ideograph
    0x22545C: (0x5911, 0),  # East Asian ideograph
    0x217571: (0x57DB, 0),  # East Asian ideograph
    0x227572: (0x7FEC, 0),  # East Asian ideograph
    0x227573: (0x7FEB, 0),  # East Asian ideograph
    0x273B60: (0x5C61, 0),  # East Asian ideograph
    0x213E3E: (0x606D, 0),  # East Asian ideograph
    0x227577: (0x7FEF, 0),  # East Asian ideograph
    0x6F596C: (0xCE6D, 0),  # Korean hangul
    0x22757A: (0x7FEE, 0),  # East Asian ideograph
    0x233E3F: (0x9099, 0),  # East Asian ideograph
    0x28632C: (0x7751, 0),  # East Asian ideograph
    0x293066: (0x89C7, 0),  # East Asian ideograph
    0x21757E: (0x57C6, 0),  # East Asian ideograph
    0x233E40: (0x9097, 0),  # East Asian ideograph
    0x4B563A: (
        0x82A6,
        0,
    ),  # East Asian ideograph (variant of 27563A which maps to 82A6)
    0x4B3421: (0x5263, 0),  # East Asian ideograph
    0x275936: (0x8C23, 0),  # East Asian ideograph
    0x213E41: (0x604D, 0),  # East Asian ideograph
    0x6F4860: (0xAC01, 0),  # Korean hangul
    0x4C695F: (0x7A63, 0),  # East Asian ideograph
    0x213E42: (0x606B, 0),  # East Asian ideograph
    0x395F49: (0x5F6B, 0),  # East Asian ideograph
    0x23585C: (0x9C09, 0),  # East Asian ideograph
    0x233643: (0x8C9F, 0),  # East Asian ideograph
    0x213E43: (0x6069, 0),  # East Asian ideograph
    0x6F5B39: (0xD1A1, 0),  # Korean hangul
    0x223E44: (0x6911, 0),  # East Asian ideograph
    0x6F552A: (0xC559, 0),  # Korean hangul
    0x4B5A7E: (0x5C69, 0),  # East Asian ideograph
    0x213E46: (0x606A, 0),  # East Asian ideograph
    0x6F4861: (0xAC02, 0),  # Korean hangul
    0x223E47: (0x68EF, 0),  # East Asian ideograph
    0x22545E: (0x720A, 0),  # East Asian ideograph
    0x6F4F4A: (0xB8FD, 0),  # Korean hangul
    0x213E48: (0x6070, 0),  # East Asian ideograph
    0x213E49: (0x6055, 0),  # East Asian ideograph
    0x274640: (0x6BB4, 0),  # East Asian ideograph
    0x234751: (0x9427, 0),  # East Asian ideograph
    0x33433E: (0x95C7, 0),  # East Asian ideograph
    0x213E4B: (0x60A6, 0),  # East Asian ideograph
    0x4D4835: (0x954C, 0),  # East Asian ideograph
    0x2D3C21: (0x57FC, 0),  # East Asian ideograph
    0x275F2E: (0x9633, 0),  # East Asian ideograph
    0x393E4C: (0x6142, 0),  # East Asian ideograph
    0x4B4973: (0x7115, 0),  # East Asian ideograph
    0x213E4D: (0x609F, 0),  # East Asian ideograph
    0x27407E: (0x626A, 0),  # East Asian ideograph
    0x6F596F: (0xCE74, 0),  # Korean hangul
    0x6F552C: (0xC55F, 0),  # Korean hangul
    0x697058: (0x9779, 0),  # East Asian ideograph
    0x275E36: (0x9559, 0),  # East Asian ideograph
    0x2D627E: (0x658B, 0),  # East Asian ideograph
    0x213B48: (0x5C1A, 0),  # East Asian ideograph
    0x2D5E3B: (0x92B9, 0),  # East Asian ideograph
    0x6F4863: (0xAC07, 0),  # Korean hangul
    0x6F4A2D: (0xADF9, 0),  # Korean hangul
    0x393078: (0x9AE3, 0),  # East Asian ideograph
    0x227E51: (0x8423, 0),  # East Asian ideograph
    0x225460: (0x7217, 0),  # East Asian ideograph
    0x223247: (0x63D3, 0),  # East Asian ideograph
    0x213E52: (0x60A3, 0),  # East Asian ideograph
    0x6F5970: (0xCE75, 0),  # Korean hangul
    0x6F5542: (0xC598, 0),  # Korean hangul
    0x223E53: (0x6974, 0),  # East Asian ideograph
    0x6F552D: (0xC560, 0),  # Korean hangul
    0x213E54: (0x6094, 0),  # East Asian ideograph
    0x2D4066: (0x63CE, 0),  # East Asian ideograph
    0x216433: (0x4E3F, 0),  # East Asian ideograph
    0x6F4864: (0xAC08, 0),  # Korean hangul
    0x4B4975: (0x6427, 0),  # East Asian ideograph
    0x275D7A: (0x9532, 0),  # East Asian ideograph
    0x213E57: (0x60B4, 0),  # East Asian ideograph
    0x395D23: (0x91BB, 0),  # East Asian ideograph
    0x4B517E: (0x7E92, 0),  # East Asian ideograph
    0x6F5971: (0xCE78, 0),  # Korean hangul
    0x223E58: (0x6962, 0),  # East Asian ideograph
    0x224B36: (0x6E39, 0),  # East Asian ideograph
    0x6F5468: (0xC4D4, 0),  # Korean hangul
    0x213E59: (0x60CB, 0),  # East Asian ideograph
    0x4B563F: (0x6A98, 0),  # East Asian ideograph
    0x2D4067: (0x62CF, 0),  # East Asian ideograph
    0x6F4865: (0xAC09, 0),  # Korean hangul
    0x6F7621: (0x3181, 0),  # Korean hangul
    0x217622: (0x57C4, 0),  # East Asian ideograph
    0x233E5B: (0x90B6, 0),  # East Asian ideograph
    0x6F7624: (0xE8B0, 0),  # Korean hangul
    0x6F7625: (0xE8B1, 0),  # Korean hangul
    0x4B4556: (0x6A2A, 0),  # East Asian ideograph
    0x217627: (0x70FE, 0),  # East Asian ideograph
    0x227629: (0x7FFD, 0),  # East Asian ideograph
    0x22762A: (0x7FFE, 0),  # East Asian ideograph
    0x21762B: (0x5803, 0),  # East Asian ideograph
    0x22762C: (0x7FFF, 0),  # East Asian ideograph
    0x21762D: (0x57E6, 0),  # East Asian ideograph
    0x22762E: (0x8004, 0),  # East Asian ideograph
    0x233E5D: (0x90B0, 0),  # East Asian ideograph
    0x29332C: (0x8BFC, 0),  # East Asian ideograph
    0x217631: (0x57ED, 0),  # East Asian ideograph
    0x227633: (0x800B, 0),  # East Asian ideograph
    0x227634: (0x800E, 0),  # East Asian ideograph
    0x227635: (0x8011, 0),  # East Asian ideograph
    0x234755: (0x9409, 0),  # East Asian ideograph
    0x227637: (0x8014, 0),  # East Asian ideograph
    0x277638: (0x57AD, 0),  # East Asian ideograph
    0x227639: (0x8016, 0),  # East Asian ideograph
    0x223E5F: (0x6957, 0),  # East Asian ideograph
    0x21763D: (0x57F4, 0),  # East Asian ideograph
    0x22763E: (0x801D, 0),  # East Asian ideograph
    0x294179: (0x9492, 0),  # East Asian ideograph
    0x217640: (0x580D, 0),  # East Asian ideograph
    0x223E60: (0x693F, 0),  # East Asian ideograph
    0x6F7642: (0xE8B4, 0),  # Korean hangul
    0x217643: (0x57EF, 0),  # East Asian ideograph
    0x6F7644: (0xE8B6, 0),  # Korean hangul
    0x6F7645: (0xE8B7, 0),  # Korean hangul
    0x6F4F4B: (0xB904, 0),  # Korean hangul
    0x273E61: (0x6076, 0),  # East Asian ideograph
    0x217648: (0x5801, 0),  # East Asian ideograph
    0x217649: (0x5812, 0),  # East Asian ideograph
    0x6F764A: (0xE8BC, 0),  # Korean hangul
    0x22764B: (0x8025, 0),  # East Asian ideograph
    0x22764C: (0x8026, 0),  # East Asian ideograph
    0x22764D: (0x802A, 0),  # East Asian ideograph
    0x22764E: (0x8029, 0),  # East Asian ideograph
    0x22764F: (0x8028, 0),  # East Asian ideograph
    0x217650: (0x580C, 0),  # East Asian ideograph
    0x217651: (0x5813, 0),  # East Asian ideograph
    0x217652: (0x57F0, 0),  # East Asian ideograph
    0x6F7653: (0xE8C5, 0),  # Korean hangul
    0x6F7654: (0xE8C6, 0),  # Korean hangul
    0x287655: (0x8027, 0),  # East Asian ideograph
    0x217656: (0x580B, 0),  # East Asian ideograph
    0x6F7657: (0xE8C9, 0),  # Korean hangul
    0x217658: (0x57F3, 0),  # East Asian ideograph
    0x217659: (0x5804, 0),  # East Asian ideograph
    0x21765A: (0x57CF, 0),  # East Asian ideograph
    0x22765B: (0x8030, 0),  # East Asian ideograph
    0x22765D: (0x8031, 0),  # East Asian ideograph
    0x21765F: (0x5847, 0),  # East Asian ideograph
    0x227660: (0x8035, 0),  # East Asian ideograph
    0x225021: (0x9E02, 0),  # East Asian ideograph
    0x4D2F5D: (
        0x8941,
        0,
    ),  # East Asian ideograph (variant of 232F5D which maps to 8941)
    0x217667: (0x581B, 0),  # East Asian ideograph
    0x227669: (0x8039, 0),  # East Asian ideograph
    0x21766A: (0x5833, 0),  # East Asian ideograph
    0x22766B: (0x8041, 0),  # East Asian ideograph
    0x21766C: (0x581E, 0),  # East Asian ideograph
    0x21766D: (0x583F, 0),  # East Asian ideograph
    0x213F59: (0x61FE, 0),  # East Asian ideograph
    0x227670: (0x8043, 0),  # East Asian ideograph
    0x213E68: (0x60B8, 0),  # East Asian ideograph
    0x217676: (0x5828, 0),  # East Asian ideograph
    0x213E69: (0x60DA, 0),  # East Asian ideograph
    0x217678: (0x582E, 0),  # East Asian ideograph
    0x6F4868: (0xAC12, 0),  # Korean hangul
    0x21767A: (0x581D, 0),  # East Asian ideograph
    0x22767B: (0x8052, 0),  # East Asian ideograph
    0x233E6A: (0x90BD, 0),  # East Asian ideograph
    0x22767E: (0x8062, 0),  # East Asian ideograph
    0x225B69: (0x74AA, 0),  # East Asian ideograph
    0x213E6B: (0x610F, 0),  # East Asian ideograph
    0x2D4D34: (0x76C7, 0),  # East Asian ideograph
    0x4B4046: (0x629C, 0),  # East Asian ideograph
    0x213E6C: (0x611C, 0),  # East Asian ideograph
    0x29306F: (0x89CB, 0),  # East Asian ideograph
    0x213F5A: (0x61FF, 0),  # East Asian ideograph
    0x224832: (0x6CD2, 0),  # East Asian ideograph
    0x234D62: (0x979C, 0),  # East Asian ideograph
    0x6F773D: (0xC733, 0),  # Korean hangul
    0x2D4844: (0x6FD5, 0),  # East Asian ideograph
    0x2D4461: (0x6746, 0),  # East Asian ideograph
    0x213E6E: (0x611F, 0),  # East Asian ideograph
    0x6F4869: (0xAC13, 0),  # Korean hangul
    0x39417C: (0x62E0, 0),  # East Asian ideograph
    0x213E6F: (0x60F0, 0),  # East Asian ideograph
    0x225466: (0x7215, 0),  # East Asian ideograph
    0x22723C: (0x7DF2, 0),  # East Asian ideograph
    0x223E70: (0x696A, 0),  # East Asian ideograph
    0x6F5976: (0xCE89, 0),  # Korean hangul
    0x213E71: (0x60FA, 0),  # East Asian ideograph
    0x224B37: (0x6E71, 0),  # East Asian ideograph
    0x213E72: (0x611A, 0),  # East Asian ideograph
    0x234759: (0x9404, 0),  # East Asian ideograph
    0x333D48: (0x5F3A, 0),  # East Asian ideograph
    0x213E73: (0x6115, 0),  # East Asian ideograph
    0x6F486A: (0xAC14, 0),  # Korean hangul
    0x212A3D: (0xE8EA, 0),  # EACC component character
    0x235866: (0x9C1C, 0),  # East Asian ideograph
    0x233E75: (0x90C7, 0),  # East Asian ideograph
    0x456064: (0x9963, 0),  # East Asian ideograph
    0x6F5977: (0xCE90, 0),  # Korean hangul
    0x6F5B3B: (0xD1A8, 0),  # Korean hangul
    0x2D3B7B: (0x5D08, 0),  # East Asian ideograph
    0x222921: (0x5EF1, 0),  # East Asian ideograph
    0x213F5C: (0x6200, 0),  # East Asian ideograph
    0x697060: (0x9790, 0),  # East Asian ideograph
    0x4B506C: (0x7CAB, 0),  # East Asian ideograph
    0x215D32: (0x91AC, 0),  # East Asian ideograph
    0x225347: (0x71B2, 0),  # East Asian ideograph
    0x213E78: (0x610E, 0),  # East Asian ideograph
    0x2D5E43: (0x92F3, 0),  # East Asian ideograph
    0x6F486B: (0xAC15, 0),  # Korean hangul
    0x213E79: (0x6100, 0),  # East Asian ideograph
    0x23364E: (0x8CB0, 0),  # East Asian ideograph
    0x213E7A: (0x6101, 0),  # East Asian ideograph
    0x4D2925: (0x8770, 0),  # East Asian ideograph
    0x6F5344: (0xC19C, 0),  # Korean hangul
    0x6F5978: (0xCE91, 0),  # Korean hangul
    0x213E7B: (0x60F6, 0),  # East Asian ideograph
    0x6F5535: (0xC575, 0),  # Korean hangul
    0x4B3870: (0x58CC, 0),  # East Asian ideograph
    0x232927: (0x867C, 0),  # East Asian ideograph
    0x223E7D: (0x6980, 0),  # East Asian ideograph
    0x28736D: (0x624D, 0),  # East Asian ideograph
    0x275E62: (0x9615, 0),  # East Asian ideograph
    0x223E7E: (0x6933, 0),  # East Asian ideograph
    0x225469: (0x7213, 0),  # East Asian ideograph
    0x6F4935: (0xAC94, 0),  # Korean hangul
    0x6F4E72: (0xB7A8, 0),  # Korean hangul
    0x2D4D38: (0x76D7, 0),  # East Asian ideograph
    0x6F5536: (0xC57C, 0),  # Korean hangul
    0x4B3871: (0x57BB, 0),  # East Asian ideograph
    0x4B5647: (0x51E6, 0),  # East Asian ideograph
    0x6F486D: (0xAC17, 0),  # Korean hangul
    0x2D5434: (0x64E7, 0),  # East Asian ideograph
    0x234E5C: (0x97DE, 0),  # East Asian ideograph
    0x225B6A: (0x7490, 0),  # East Asian ideograph
    0x23292F: (0x86A8, 0),  # East Asian ideograph
    0x6F597A: (0xCE98, 0),  # Korean hangul
    0x4B5221: (0x7D9A, 0),  # East Asian ideograph
    0x217721: (0x5848, 0),  # East Asian ideograph
    0x6F7722: (0xAD7B, 0),  # Korean hangul
    0x217723: (0x5818, 0),  # East Asian ideograph
    0x6F7724: (0xAD89, 0),  # Korean hangul
    0x6F7725: (0xAD9D, 0),  # Korean hangul
    0x217726: (0x57F5, 0),  # East Asian ideograph
    0x4B5D36: (0x91C6, 0),  # East Asian ideograph
    0x227728: (0x8063, 0),  # East Asian ideograph
    0x21315B: (0x4FBF, 0),  # East Asian ideograph
    0x6F772A: (0xAE0F, 0),  # Korean hangul
    0x21772B: (0x5820, 0),  # East Asian ideograph
    0x6F772C: (0xAE14, 0),  # Korean hangul
    0x6F486E: (0xAC19, 0),  # Korean hangul
    0x6F772E: (0xAEED, 0),  # Korean hangul
    0x6F772F: (0xAF09, 0),  # Korean hangul
    0x217730: (0x584E, 0),  # East Asian ideograph
    0x6F7731: (0xAFBF, 0),  # Korean hangul
    0x227732: (0x806C, 0),  # East Asian ideograph
    0x217733: (0x585D, 0),  # East Asian ideograph
    0x6F4926: (0xAC78, 0),  # Korean hangul
    0x217735: (0x5859, 0),  # East Asian ideograph
    0x6F7736: (0xC552, 0),  # Korean hangul
    0x217737: (0x584B, 0),  # East Asian ideograph
    0x6F7738: (0xC5B1, 0),  # Korean hangul
    0x227739: (0x8075, 0),  # East Asian ideograph
    0x6F773A: (0xC61D, 0),  # Korean hangul
    0x2D3876: (0x58F7, 0),  # East Asian ideograph
    0x6F773C: (0xE8CB, 0),  # Korean hangul
    0x21773D: (0x5865, 0),  # East Asian ideograph
    0x22773E: (0x807B, 0),  # East Asian ideograph
    0x22773F: (0x8079, 0),  # East Asian ideograph
    0x217740: (0x586C, 0),  # East Asian ideograph
    0x213F60: (0x620D, 0),  # East Asian ideograph
    0x217742: (0x5852, 0),  # East Asian ideograph
    0x33475E: (0x6FB9, 0),  # East Asian ideograph
    0x217745: (0x5864, 0),  # East Asian ideograph
    0x227747: (0x808A, 0),  # East Asian ideograph
    0x217748: (0x584F, 0),  # East Asian ideograph
    0x227749: (0x808E, 0),  # East Asian ideograph
    0x213533: (0x53FC, 0),  # East Asian ideograph
    0x6F486F: (0xAC1A, 0),  # Korean hangul
    0x21774D: (0x584D, 0),  # East Asian ideograph
    0x22774E: (0x809F, 0),  # East Asian ideograph
    0x6F5730: (0xC7C8, 0),  # Korean hangul
    0x225029: (0x7054, 0),  # East Asian ideograph
    0x232939: (0x8698, 0),  # East Asian ideograph
    0x217758: (0x5892, 0),  # East Asian ideograph
    0x6F597C: (0xCEA1, 0),  # Korean hangul
    0x21775A: (0x588E, 0),  # East Asian ideograph
    0x22775C: (0x670A, 0),  # East Asian ideograph
    0x70775D: (0x9B0F, 0),  # East Asian ideograph
    0x282632: (0x5D58, 0),  # East Asian ideograph
    0x21775F: (0x5840, 0),  # East Asian ideograph
    0x227760: (0x80A7, 0),  # East Asian ideograph
    0x227761: (0x80B0, 0),  # East Asian ideograph
    0x33475F: (0x60BD, 0),  # East Asian ideograph
    0x21576C: (0x88FD, 0),  # East Asian ideograph
    0x217765: (0x5890, 0),  # East Asian ideograph
    0x217768: (0x5898, 0),  # East Asian ideograph
    0x227769: (0x80B5, 0),  # East Asian ideograph
    0x22776A: (0x80A6, 0),  # East Asian ideograph
    0x21776B: (0x587D, 0),  # East Asian ideograph
    0x6F5C36: (0xD3B8, 0),  # Korean hangul
    0x21776F: (0x587F, 0),  # East Asian ideograph
    0x217770: (0x5881, 0),  # East Asian ideograph
    0x707771: (0x9EE2, 0),  # East Asian ideograph (Version J extension)
    0x227773: (0x80E0, 0),  # East Asian ideograph
    0x21693E: (0x5135, 0),  # East Asian ideograph
    0x235B26: (0x9D5A, 0),  # East Asian ideograph
    0x6F597D: (0xCEA3, 0),  # Korean hangul
    0x213D62: (0x5F8B, 0),  # East Asian ideograph
    0x22777B: (0x80DF, 0),  # East Asian ideograph
    0x22777D: (0x80C2, 0),  # East Asian ideograph
    0x21777E: (0x58A1, 0),  # East Asian ideograph
    0x226940: (0x7A5C, 0),  # East Asian ideograph
    0x4B7421: (0xF9A9, 0),  # East Asian ideograph
    0x4C433F: (0x6A65, 0),  # East Asian ideograph
    0x6F4D21: (0xB304, 0),  # Korean hangul
    0x45606B: (0x98F0, 0),  # East Asian ideograph
    0x27482D: (0x6C64, 0),  # East Asian ideograph
    0x293B6B: (0x8F8B, 0),  # East Asian ideograph
    0x276944: (0x50A9, 0),  # East Asian ideograph
    0x213F63: (0x6212, 0),  # East Asian ideograph
    0x2D5E4A: (0x945A, 0),  # East Asian ideograph
    0x6F4A30: (0xAE00, 0),  # Korean hangul
    0x275E57: (0x95F8, 0),  # East Asian ideograph
    0x6F5321: (0xC11C, 0),  # Korean hangul
    0x276948: (0x50A5, 0),  # East Asian ideograph
    0x6F553C: (0xC58D, 0),  # Korean hangul
    0x213F64: (0x6211, 0),  # East Asian ideograph
    0x215D3A: (0x91CD, 0),  # East Asian ideograph
    0x234762: (0x9423, 0),  # East Asian ideograph
    0x23294B: (0x86BF, 0),  # East Asian ideograph
    0x6F4956: (0xACF6, 0),  # Korean hangul
    0x6F4B41: (0xB057, 0),  # Korean hangul
    0x292C5D: (0x867F, 0),  # East Asian ideograph
    0x4B3435: (0x52B4, 0),  # East Asian ideograph
    0x6F4E27: (0xB54C, 0),  # Korean hangul
    0x222951: (0x5F33, 0),  # East Asian ideograph
    0x223258: (0x63E6, 0),  # East Asian ideograph
    0x235870: (0x9C2E, 0),  # East Asian ideograph
    0x227247: (0x7DF1, 0),  # East Asian ideograph
    0x6F5B3D: (0xD1B1, 0),  # Korean hangul
    0x6F553E: (0xC590, 0),  # Korean hangul
    0x213F66: (0x6215, 0),  # East Asian ideograph
    0x2D3539: (0x52FE, 0),  # East Asian ideograph
    0x22613B: (0x76E6, 0),  # East Asian ideograph
    0x4B3436: (0x52F2, 0),  # East Asian ideograph
    0x6F4E6C: (0xB791, 0),  # Korean hangul
    0x23517A: (0x9958, 0),  # East Asian ideograph
    0x214C30: (0x755A, 0),  # East Asian ideograph
    0x226957: (0x7A6E, 0),  # East Asian ideograph
    0x222958: (0x5F38, 0),  # East Asian ideograph
    0x2D424F: (0x555F, 0),  # East Asian ideograph
    0x215D3D: (0x91D0, 0),  # East Asian ideograph
    0x22613C: (0x76E9, 0),  # East Asian ideograph
    0x334342: (0x7156, 0),  # East Asian ideograph
    0x513D67: (0x8FF3, 0),  # East Asian ideograph
    0x217824: (0x58B1, 0),  # East Asian ideograph
    0x227827: (0x80D9, 0),  # East Asian ideograph
    0x4B4544: (0x69D8, 0),  # East Asian ideograph
    0x4C695C: (0x7A06, 0),  # East Asian ideograph
    0x22782A: (0x80DD, 0),  # East Asian ideograph
    0x21782B: (0x58AD, 0),  # East Asian ideograph
    0x22782D: (0x80CF, 0),  # East Asian ideograph
    0x21782E: (0x58A0, 0),  # East Asian ideograph
    0x22782F: (0x80CD, 0),  # East Asian ideograph
    0x227830: (0x80D7, 0),  # East Asian ideograph
    0x213F68: (0x621A, 0),  # East Asian ideograph
    0x217832: (0x58A6, 0),  # East Asian ideograph
    0x227833: (0x80F2, 0),  # East Asian ideograph
    0x227834: (0x80FA, 0),  # East Asian ideograph
    0x227838: (0x80FE, 0),  # East Asian ideograph
    0x21783A: (0x58C8, 0),  # East Asian ideograph
    0x2D3C36: (0x5DE3, 0),  # East Asian ideograph
    0x22783C: (0x8103, 0),  # East Asian ideograph
    0x275762: (0x8865, 0),  # East Asian ideograph
    0x227840: (0x80F9, 0),  # East Asian ideograph
    0x217841: (0x58BC, 0),  # East Asian ideograph
    0x227842: (0x80D4, 0),  # East Asian ideograph
    0x33365A: (0x5405, 0),  # East Asian ideograph
    0x4B4545: (0x6982, 0),  # East Asian ideograph
    0x217849: (0x58BF, 0),  # East Asian ideograph
    0x22784B: (0x8118, 0),  # East Asian ideograph
    0x21784C: (0x58BA, 0),  # East Asian ideograph
    0x222962: (0x5F4D, 0),  # East Asian ideograph
    0x6F5541: (0xC597, 0),  # Korean hangul
    0x227850: (0x8130, 0),  # East Asian ideograph
    0x232963: (0x86B4, 0),  # East Asian ideograph
    0x227854: (0x8124, 0),  # East Asian ideograph
    0x227855: (0x811B, 0),  # East Asian ideograph
    0x217856: (0x58CE, 0),  # East Asian ideograph
    0x2D5E50: (0x9587, 0),  # East Asian ideograph
    0x6F4878: (0xAC2F, 0),  # Korean hangul
    0x21785A: (0x58E0, 0),  # East Asian ideograph
    0x21785E: (0x58DA, 0),  # East Asian ideograph
    0x227860: (0x812A, 0),  # East Asian ideograph
    0x227861: (0x811E, 0),  # East Asian ideograph
    0x294362: (0x94EA, 0),  # East Asian ideograph
    0x227864: (0x8121, 0),  # East Asian ideograph
    0x212321: (0x3000, 0),  # Ideographic space per ANSI Z39.64
    0x227866: (0x8117, 0),  # East Asian ideograph
    0x227869: (0x813A, 0),  # East Asian ideograph
    0x22786A: (0x815A, 0),  # East Asian ideograph
    0x21786C: (0x58FC, 0),  # East Asian ideograph
    0x22786D: (0x8148, 0),  # East Asian ideograph
    0x28786E: (0x80E8, 0),  # East Asian ideograph
    0x4B387D: (0x591B, 0),  # East Asian ideograph
    0x217870: (0x5902, 0),  # East Asian ideograph
    0x213B27: (0x5BCC, 0),  # East Asian ideograph
    0x217873: (0x5906, 0),  # East Asian ideograph
    0x217874: (0x6535, 0),  # East Asian ideograph
    0x227877: (0x814C, 0),  # East Asian ideograph
    0x21787A: (0x5910, 0),  # East Asian ideograph
    0x21787C: (0x8641, 0),  # East Asian ideograph
    0x22787D: (0x8141, 0),  # East Asian ideograph
    0x22325D: (0x63F6, 0),  # East Asian ideograph
    0x214C34: (0x7570, 0),  # East Asian ideograph
    0x343A5B: (0x572C, 0),  # East Asian ideograph
    0x2E735D: (0x7D56, 0),  # East Asian ideograph
    0x276871: (0x4FAA, 0),  # East Asian ideograph
    0x6F5543: (0xC59C, 0),  # Korean hangul
    0x696464: (0x7C90, 0),  # East Asian ideograph
    0x213B28: (0x5BD2, 0),  # East Asian ideograph
    0x234326: (0x924C, 0),  # East Asian ideograph
    0x275765: (0x88C5, 0),  # East Asian ideograph
    0x23296F: (0x86E9, 0),  # East Asian ideograph
    0x22325E: (0x63F2, 0),  # East Asian ideograph
    0x214C35: (0x7565, 0),  # East Asian ideograph
    0x6F557C: (0xC63A, 0),  # Korean hangul
    0x235433: (0x9A64, 0),  # East Asian ideograph
    0x222971: (0x5F61, 0),  # East Asian ideograph
    0x6F5544: (0xC5B4, 0),  # Korean hangul
    0x2D5E24: (0x7145, 0),  # East Asian ideograph
    0x23476A: (0x9407, 0),  # East Asian ideograph
    0x4B403D: (0x62DD, 0),  # East Asian ideograph
    0x6F487B: (0xAC38, 0),  # Korean hangul
    0x2D4D65: (0x53E1, 0),  # East Asian ideograph
    0x232974: (0x86D5, 0),  # East Asian ideograph
    0x22325F: (0x63F8, 0),  # East Asian ideograph
    0x23365E: (0x8CD8, 0),  # East Asian ideograph
    0x235434: (0x9A66, 0),  # East Asian ideograph
    0x275421: (0x80EA, 0),  # East Asian ideograph
    0x275E37: (0x9535, 0),  # East Asian ideograph
    0x215422: (0x81DF, 0),  # East Asian ideograph
    0x6F5862: (0xCB10, 0),  # Korean hangul
    0x6F487C: (0xAC39, 0),  # Korean hangul
    0x6F4A32: (0xAE08, 0),  # Korean hangul
    0x6F5423: (0xC2DC, 0),  # Korean hangul
    0x27623F: (0x9E43, 0),  # East Asian ideograph
    0x275E59: (0x95FA, 0),  # East Asian ideograph
    0x215424: (0x81E5, 0),  # East Asian ideograph
    0x23365F: (0x8CD5, 0),  # East Asian ideograph
    0x456076: (0x9980, 0),  # East Asian ideograph
    0x215425: (0x81E8, 0),  # East Asian ideograph
    0x6F5B48: (0xD23D, 0),  # Korean hangul
    0x275142: (0x7EFD, 0),  # East Asian ideograph
    0x225426: (0x71D4, 0),  # East Asian ideograph
    0x235427: (0x9A4A, 0),  # East Asian ideograph
    0x6F487D: (0xAC40, 0),  # Korean hangul
    0x4B5428: (
        0x81ED,
        0,
    ),  # East Asian ideograph (variant of 215428 which maps to 81ED)
    0x235879: (0x9C24, 0),  # East Asian ideograph
    0x6F5C6A: (0xD56B, 0),  # Korean hangul
    0x23542A: (0x9A58, 0),  # East Asian ideograph
    0x6F546D: (0xC4F8, 0),  # Korean hangul
    0x6F5547: (0xC5B8, 0),  # Korean hangul
    0x27542B: (0x53F0, 0),  # East Asian ideograph
    0x333D4C: (0x7030, 0),  # East Asian ideograph
    0x23542C: (0x9A56, 0),  # East Asian ideograph
    0x6F542D: (0xC2F6, 0),  # Korean hangul
    0x293D4E: (0x8FF8, 0),  # East Asian ideograph
    0x28352A: (0x6448, 0),  # East Asian ideograph
    0x47577A: (
        0x9BD6,
        0,
    ),  # East Asian ideograph (variant of 23577A which maps to 9BD6)
    0x6F5B3F: (0xD1B5, 0),  # Korean hangul
    0x6F5430: (0xC2F8, 0),  # Korean hangul
    0x227925: (0x814D, 0),  # East Asian ideograph
    0x6F5431: (0xC2F9, 0),  # Korean hangul
    0x217928: (0x592C, 0),  # East Asian ideograph
    0x21792B: (0x592F, 0),  # East Asian ideograph
    0x275432: (0x4E0E, 0),  # East Asian ideograph
    0x22792E: (0x6720, 0),  # East Asian ideograph
    0x21507D: (0x7D14, 0),  # East Asian ideograph
    0x217930: (0x593C, 0),  # East Asian ideograph
    0x395F68: (0x8987, 0),  # East Asian ideograph
    0x227932: (0x8160, 0),  # East Asian ideograph
    0x215433: (0x8208, 0),  # East Asian ideograph
    0x225039: (0x7074, 0),  # East Asian ideograph
    0x217938: (0x594D, 0),  # East Asian ideograph
    0x215434: (0x8209, 0),  # East Asian ideograph
    0x22793B: (0x8169, 0),  # East Asian ideograph
    0x22793C: (0x817C, 0),  # East Asian ideograph
    0x275435: (0x65E7, 0),  # East Asian ideograph
    0x294E5C: (0x97EB, 0),  # East Asian ideograph
    0x227941: (0x8161, 0),  # East Asian ideograph
    0x6F5A65: (0xD081, 0),  # Korean hangul
    0x217943: (0x5953, 0),  # East Asian ideograph
    0x225436: (0x71E8, 0),  # East Asian ideograph
    0x227946: (0x8176, 0),  # East Asian ideograph
    0x227947: (0x8174, 0),  # East Asian ideograph
    0x227948: (0x8167, 0),  # East Asian ideograph
    0x334633: (
        0x6B8B,
        0,
    ),  # East Asian ideograph (variant of 274633 which maps to 6B8B)
    0x22794B: (0x816F, 0),  # East Asian ideograph
    0x22794D: (0x8182, 0),  # East Asian ideograph
    0x4C794E: (0x80B7, 0),  # East Asian ideograph
    0x21794F: (0x5961, 0),  # East Asian ideograph
    0x227951: (0x818B, 0),  # East Asian ideograph
    0x227952: (0x8186, 0),  # East Asian ideograph
    0x217954: (0x596C, 0),  # East Asian ideograph
    0x217955: (0x596D, 0),  # East Asian ideograph
    0x274830: (0x6D4B, 0),  # East Asian ideograph
    0x4B6324: (0x9F62, 0),  # East Asian ideograph
    0x227959: (0x8183, 0),  # East Asian ideograph
    0x21543A: (0x8214, 0),  # East Asian ideograph
    0x334770: (0x5A6C, 0),  # East Asian ideograph
    0x69543B: (0x57B0, 0),  # East Asian ideograph
    0x217965: (0x597C, 0),  # East Asian ideograph
    0x6F4A33: (0xAE09, 0),  # Korean hangul
    0x217969: (0x59A7, 0),  # East Asian ideograph
    0x22796A: (0x819F, 0),  # East Asian ideograph
    0x22796B: (0x81A3, 0),  # East Asian ideograph
    0x287941: (0x8136, 0),  # East Asian ideograph
    0x21796F: (0x599A, 0),  # East Asian ideograph
    0x227970: (0x8198, 0),  # East Asian ideograph
    0x22503B: (0x707A, 0),  # East Asian ideograph
    0x335E3D: (0x9244, 0),  # East Asian ideograph
    0x227975: (0x8195, 0),  # East Asian ideograph
    0x227977: (0x8197, 0),  # East Asian ideograph
    0x22543F: (0x71E1, 0),  # East Asian ideograph
    0x22797C: (0x81AA, 0),  # East Asian ideograph
    0x224372: (0x6B1E, 0),  # East Asian ideograph
    0x22797E: (0x6725, 0),  # East Asian ideograph
    0x213B30: (0x5BDE, 0),  # East Asian ideograph
    0x2D5440: (0x6841, 0),  # East Asian ideograph
    0x6F4862: (0xAC04, 0),  # Korean hangul
    0x215441: (0x822B, 0),  # East Asian ideograph
    0x275068: (0x7CAA, 0),  # East Asian ideograph
    0x695442: (0x57D6, 0),  # East Asian ideograph
    0x227255: (0x7E12, 0),  # East Asian ideograph
    0x235443: (0x9AB1, 0),  # East Asian ideograph
    0x294E79: (0x9878, 0),  # East Asian ideograph
    0x6F5444: (0xC345, 0),  # Korean hangul
    0x213B31: (0x5BE6, 0),  # East Asian ideograph
    0x235445: (0x9AB3, 0),  # East Asian ideograph
    0x33432F: (0x664B, 0),  # East Asian ideograph
    0x225651: (0x72C6, 0),  # East Asian ideograph
    0x2D5446: (0x8229, 0),  # East Asian ideograph
    0x216E57: (0x53FB, 0),  # East Asian ideograph
    0x214C3E: (0x758F, 0),  # East Asian ideograph
    0x276329: (0x9F8C, 0),  # East Asian ideograph
    0x6F554D: (0xC5C4, 0),  # Korean hangul
    0x235449: (0x9AB6, 0),  # East Asian ideograph
    0x227427: (0x7F46, 0),  # East Asian ideograph
    0x224A62: (0x6E4B, 0),  # East Asian ideograph
    0x27544A: (0x8231, 0),  # East Asian ideograph
    0x294161: (0x9487, 0),  # East Asian ideograph
    0x27544B: (0x8230, 0),  # East Asian ideograph
    0x283955: (0x6619, 0),  # East Asian ideograph
    0x23544C: (0x9ABB, 0),  # East Asian ideograph
    0x233667: (0x8CE8, 0),  # East Asian ideograph
    0x4D2F7A: (0x891D, 0),  # East Asian ideograph
    0x6F5345: (0xC19D, 0),  # Korean hangul
    0x6F544D: (0xC37D, 0),  # Korean hangul
    0x235871: (0x9C28, 0),  # East Asian ideograph
    0x6F554E: (0xC5C5, 0),  # Korean hangul
    0x27544E: (0x8270, 0),  # East Asian ideograph
    0x234774: (0x943F, 0),  # East Asian ideograph
    0x22544F: (0x71FC, 0),  # East Asian ideograph
    0x235450: (0x9ABA, 0),  # East Asian ideograph
    0x695451: (0x58B9, 0),  # East Asian ideograph
    0x233668: (0x8CE9, 0),  # East Asian ideograph
    0x4B4553: (0x6955, 0),  # East Asian ideograph
    0x6F4E77: (0xB7B4, 0),  # Korean hangul
    0x274831: (0x6DA1, 0),  # East Asian ideograph
    0x233225: (0x8A22, 0),  # East Asian ideograph
    0x6F554F: (0xC5C6, 0),  # Korean hangul
    0x6F5453: (0xC3DC, 0),  # Korean hangul
    0x235454: (0x9ABD, 0),  # East Asian ideograph
    0x2E6C26: (0x7BE0, 0),  # East Asian ideograph
    0x6F4A34: (0xAE0B, 0),  # Korean hangul
    0x6F5455: (0xC3E0, 0),  # Korean hangul
    0x225456: (0x71F9, 0),  # East Asian ideograph
    0x225040: (0x7093, 0),  # East Asian ideograph
    0x23543F: (0x9AAD, 0),  # East Asian ideograph
    0x235457: (0x9AC1, 0),  # East Asian ideograph
    0x6F5550: (0xC5C7, 0),  # Korean hangul
    0x275458: (0x5DF4, 0),  # East Asian ideograph (duplicate simplified)
    0x274222: (0x62C5, 0),  # East Asian ideograph
    0x4B3B22: (0x51A6, 0),  # East Asian ideograph
    0x235459: (0x9AC0, 0),  # East Asian ideograph
    0x22572C: (0x72FB, 0),  # East Asian ideograph
    0x23545A: (0x9AC2, 0),  # East Asian ideograph
    0x217A21: (0x5990, 0),  # East Asian ideograph
    0x22545B: (0x720E, 0),  # East Asian ideograph
    0x217A24: (0x59C5, 0),  # East Asian ideograph
    0x217A25: (0x59B5, 0),  # East Asian ideograph
    0x217A28: (0x59CF, 0),  # East Asian ideograph
    0x21545C: (0x82BB, 0),  # East Asian ideograph
    0x217A2A: (0x59BA, 0),  # East Asian ideograph
    0x3F377B: (0x784E, 0),  # East Asian ideograph (Version J extension)
    0x217A2C: (0x59B8, 0),  # East Asian ideograph
    0x6F546F: (0xC501, 0),  # Korean hangul
    0x227A2E: (0x81B0, 0),  # East Asian ideograph
    0x227A2F: (0x81B4, 0),  # East Asian ideograph
    0x215D4F: (0x9237, 0),  # East Asian ideograph
    0x227A33: (0x81B7, 0),  # East Asian ideograph
    0x217A35: (0x59B2, 0),  # East Asian ideograph
    0x227A37: (0x81BB, 0),  # East Asian ideograph
    0x227A38: (0x81C1, 0),  # East Asian ideograph
    0x227A39: (0x81CC, 0),  # East Asian ideograph
    0x217A3A: (0x59B7, 0),  # East Asian ideograph
    0x227A3B: (0x81C4, 0),  # East Asian ideograph
    0x217A3E: (0x59C1, 0),  # East Asian ideograph
    0x227A40: (0x81D1, 0),  # East Asian ideograph
    0x227A41: (0x81CE, 0),  # East Asian ideograph
    0x217A43: (0x59F9, 0),  # East Asian ideograph
    0x217A44: (0x59F8, 0),  # East Asian ideograph
    0x212A43: (0xE8F0, 0),  # EACC component character
    0x225461: (0x7207, 0),  # East Asian ideograph
    0x227A4B: (0x81DB, 0),  # East Asian ideograph
    0x6F5552: (0xC5C9, 0),  # Korean hangul
    0x6F5462: (0xC468, 0),  # Korean hangul
    0x227A4F: (0x81DD, 0),  # East Asian ideograph
    0x217A50: (0x59F1, 0),  # East Asian ideograph
    0x217A51: (0x5A00, 0),  # East Asian ideograph
    0x217A52: (0x59DE, 0),  # East Asian ideograph
    0x227A53: (0x81DE, 0),  # East Asian ideograph
    0x227A56: (0x81E0, 0),  # East Asian ideograph
    0x227A57: (0x81E2, 0),  # East Asian ideograph
    0x6F5464: (0xC474, 0),  # Korean hangul
    0x227A5B: (0x81E7, 0),  # East Asian ideograph
    0x217A5D: (0x59F6, 0),  # East Asian ideograph
    0x217A5E: (0x59DD, 0),  # East Asian ideograph
    0x217A5F: (0x59FA, 0),  # East Asian ideograph
    0x227A60: (0x81EF, 0),  # East Asian ideograph
    0x217A61: (0x59E4, 0),  # East Asian ideograph
    0x227A65: (0x81F2, 0),  # East Asian ideograph
    0x227A68: (0x81F6, 0),  # East Asian ideograph
    0x6F5553: (0xC5CA, 0),  # Korean hangul
    0x6F5467: (0xC494, 0),  # Korean hangul
    0x274225: (0x6324, 0),  # East Asian ideograph
    0x217A6E: (0x5A2A, 0),  # East Asian ideograph
    0x213B38: (0x5BF5, 0),  # East Asian ideograph
    0x227A70: (0x8201, 0),  # East Asian ideograph
    0x2D5468: (0x6959, 0),  # East Asian ideograph
    0x227A72: (0x8201, 0),  # East Asian ideograph (not in Unicode)
    0x227A74: (0x8203, 0),  # East Asian ideograph
    0x227A75: (0x8204, 0),  # East Asian ideograph
    0x2D3C49: (0x83F7, 0),  # East Asian ideograph
    0x227A77: (0x820B, 0),  # East Asian ideograph
    0x217A78: (0x5A09, 0),  # East Asian ideograph
    0x23546A: (0x9AD1, 0),  # East Asian ideograph
    0x217A7E: (0x5A12, 0),  # East Asian ideograph
    0x6F4E78: (0xB7B5, 0),  # Korean hangul
    0x6F546B: (0xC4F1, 0),  # Korean hangul
    0x6F5554: (0xC5CC, 0),  # Korean hangul
    0x6F546C: (0xC4F4, 0),  # Korean hangul
    0x274226: (0x62E7, 0),  # East Asian ideograph
    0x213B39: (0x5BF6, 0),  # East Asian ideograph
    0x21546D: (0x82D3, 0),  # East Asian ideograph
    0x234337: (0x927C, 0),  # East Asian ideograph
    0x22546E: (0x7218, 0),  # East Asian ideograph
    0x28395C: (0x6654, 0),  # East Asian ideograph
    0x2D546F: (0x83C0, 0),  # East Asian ideograph
    0x22725E: (0x7E09, 0),  # East Asian ideograph
    0x4B4559: (0x9792, 0),  # East Asian ideograph
    0x6F5470: (0xC50C, 0),  # Korean hangul
    0x4B5227: (0x6B20, 0),  # East Asian ideograph
    0x6F5555: (0xC5CE, 0),  # Korean hangul
    0x225471: (0x720B, 0),  # East Asian ideograph
    0x33477B: (0x904A, 0),  # East Asian ideograph
    0x235472: (0x9ADC, 0),  # East Asian ideograph
    0x4B5223: (0x7E4A, 0),  # East Asian ideograph
    0x275777: (0x4EB5, 0),  # East Asian ideograph
    0x215474: (0x834A, 0),  # East Asian ideograph
    0x22725F: (0x7E1F, 0),  # East Asian ideograph
    0x23366F: (0x8CEB, 0),  # East Asian ideograph
    0x335445: (0x67C1, 0),  # East Asian ideograph
    0x6F5475: (0xC530, 0),  # Korean hangul
    0x6F5556: (0xC5D0, 0),  # Korean hangul
    0x235476: (0x9AE0, 0),  # East Asian ideograph
    0x274228: (0x62DF, 0),  # East Asian ideograph
    0x23477C: (0x943D, 0),  # East Asian ideograph
    0x215477: (0x8350, 0),  # East Asian ideograph
    0x27593F: (0x8BC1, 0),  # East Asian ideograph
    0x233F22: (0x90DD, 0),  # East Asian ideograph
    0x6F5478: (0xC53B, 0),  # Korean hangul
    0x293F23: (0x90CF, 0),  # East Asian ideograph
    0x6F5827: (0xC999, 0),  # Korean hangul
    0x225479: (0x721A, 0),  # East Asian ideograph
    0x233670: (0x8CDA, 0),  # East Asian ideograph
    0x212A44: (0xE8F1, 0),  # EACC component character
    0x335446: (0x8221, 0),  # East Asian ideograph
    0x22437E: (0x6B2C, 0),  # East Asian ideograph
    0x4B5154: (0x7DF4, 0),  # East Asian ideograph
    0x6F547C: (0xC544, 0),  # Korean hangul
    0x233F27: (0x90D8, 0),  # East Asian ideograph
    0x6F5B6D: (0xD30D, 0),  # Korean hangul
    0x22547D: (0x721F, 0),  # East Asian ideograph
    0x273F28: (0x6001, 0),  # East Asian ideograph
    0x223272: (0x63EB, 0),  # East Asian ideograph
    0x6F4F53: (0xB974, 0),  # Korean hangul
    0x213F29: (0x613E, 0),  # East Asian ideograph
    0x225048: (0x7096, 0),  # East Asian ideograph (not in Unicode)
    0x6F5624: (0xC650, 0),  # Korean hangul
    0x213F2A: (0x6127, 0),  # East Asian ideograph
    0x27422A: (0x6269, 0),  # East Asian ideograph
    0x213C2B: (0x5D87, 0),  # East Asian ideograph
    0x213F2C: (0x6147, 0),  # East Asian ideograph
    0x275F37: (0x9645, 0),  # East Asian ideograph
    0x223F2D: (0x6985, 0),  # East Asian ideograph
    0x273F2E: (0x5E86, 0),  # East Asian ideograph
    0x6F4E79: (0xB7C9, 0),  # Korean hangul
    0x274833: (0x6D51, 0),  # East Asian ideograph
    0x213F2F: (0x6167, 0),  # East Asian ideograph
    0x6F5559: (0xC5D8, 0),  # Korean hangul
    0x27422B: (0x63B7, 0),  # East Asian ideograph
    0x2E624F: (0x772D, 0),  # East Asian ideograph
    0x227B27: (0x821D, 0),  # East Asian ideograph
    0x227B29: (0x8220, 0),  # East Asian ideograph
    0x6F4A36: (0xAE30, 0),  # Korean hangul
    0x217B2C: (0x5A60, 0),  # East Asian ideograph
    0x223F32: (0x693D, 0),  # East Asian ideograph
    0x227B2E: (0x822D, 0),  # East Asian ideograph
    0x227B2F: (0x822F, 0),  # East Asian ideograph
    0x6F5477: (0xC539, 0),  # Korean hangul
    0x217B31: (0x5A67, 0),  # East Asian ideograph
    0x227B32: (0x8238, 0),  # East Asian ideograph
    0x273F33: (0x5FE7, 0),  # East Asian ideograph
    0x227B34: (0x823A, 0),  # East Asian ideograph
    0x227B35: (0x8233, 0),  # East Asian ideograph
    0x227B36: (0x8234, 0),  # East Asian ideograph
    0x213F34: (0x617C, 0),  # East Asian ideograph
    0x227B3A: (0x8232, 0),  # East Asian ideograph
    0x217B3B: (0x5A5E, 0),  # East Asian ideograph
    0x217B3C: (0x5A6D, 0),  # East Asian ideograph
    0x217B3D: (0x5A35, 0),  # East Asian ideograph
    0x217B3E: (0x5A55, 0),  # East Asian ideograph
    0x27422C: (0x64B5, 0),  # East Asian ideograph
    0x215D58: (
        0x9234,
        0,
    ),  # East Asian ideograph (variant of 4B5D58 which maps to 9234)
    0x217B41: (0x5A2C, 0),  # East Asian ideograph
    0x227B42: (0x8248, 0),  # East Asian ideograph
    0x227B43: (0x8249, 0),  # East Asian ideograph
    0x227B45: (0x8244, 0),  # East Asian ideograph
    0x227B47: (0x8240, 0),  # East Asian ideograph
    0x227B48: (0x8241, 0),  # East Asian ideograph
    0x217B49: (0x5A65, 0),  # East Asian ideograph
    0x227B4A: (0x8245, 0),  # East Asian ideograph
    0x227B4B: (0x824B, 0),  # East Asian ideograph
    0x334E37: (0x784E, 0),  # East Asian ideograph
    0x227B50: (0x824F, 0),  # East Asian ideograph
    0x213F38: (0x6158, 0),  # East Asian ideograph
    0x217B52: (0x5A64, 0),  # East Asian ideograph
    0x227B53: (0x824E, 0),  # East Asian ideograph
    0x227B56: (0x8256, 0),  # East Asian ideograph
    0x227B57: (0x8257, 0),  # East Asian ideograph
    0x2D6B33: (0x5231, 0),  # East Asian ideograph (not in Unicode)
    0x6F555B: (0xC5E1, 0),  # Korean hangul
    0x223F3A: (0x6934, 0),  # East Asian ideograph
    0x227B5E: (0x825A, 0),  # East Asian ideograph
    0x227B62: (0x825F, 0),  # East Asian ideograph
    0x223F3B: (0x6969, 0),  # East Asian ideograph
    0x217B65: (0x5A8A, 0),  # East Asian ideograph
    0x227B67: (0x8262, 0),  # East Asian ideograph
    0x217B69: (0x5ACF, 0),  # East Asian ideograph
    0x217B6A: (0x5A7A, 0),  # East Asian ideograph
    0x227B6B: (0x8268, 0),  # East Asian ideograph
    0x227B6F: (0x826D, 0),  # East Asian ideograph
    0x217B71: (0x5A9F, 0),  # East Asian ideograph
    0x273F3E: (0x5BAA, 0),  # East Asian ideograph
    0x227B77: (0x8278, 0),  # East Asian ideograph
    0x213F3F: (0x6191, 0),  # East Asian ideograph
    0x227B7D: (0x827F, 0),  # East Asian ideograph
    0x23433F: (0x928D, 0),  # East Asian ideograph
    0x213F41: (0x61AB, 0),  # East Asian ideograph
    0x23486C: (0x946F, 0),  # East Asian ideograph
    0x295F7C: (0x9F80, 0),  # East Asian ideograph
    0x6F4F54: (0xB975, 0),  # Korean hangul
    0x213F42: (0x61A4, 0),  # East Asian ideograph
    0x453D53: (0x5F66, 0),  # East Asian ideograph
    0x4B4561: (0x691C, 0),  # East Asian ideograph
    0x4B5061: (0x7CBE, 0),  # East Asian ideograph
    0x2D4D5F: (0x7741, 0),  # East Asian ideograph
    0x6F555D: (0xC5E5, 0),  # Korean hangul
    0x27422F: (0x64DE, 0),  # East Asian ideograph
    0x6F5A69: (0xD0AC, 0),  # Korean hangul
    0x213B42: (0x5C0B, 0),  # East Asian ideograph
    0x294666: (0x933E, 0),  # East Asian ideograph
    0x223F45: (0x69A0, 0),  # East Asian ideograph
    0x234340: (0x92EE, 0),  # East Asian ideograph
    0x4B522B: (0x7F36, 0),  # East Asian ideograph
    0x6F5C50: (0xD48D, 0),  # Korean hangul
    0x223F46: (0x69B1, 0),  # East Asian ideograph
    0x23553C: (0x9B08, 0),  # East Asian ideograph
    0x233F47: (0x90FE, 0),  # East Asian ideograph
    0x295031: (0x98A7, 0),  # East Asian ideograph
    0x213F48: (0x61B6, 0),  # East Asian ideograph
    0x6F555E: (0xC5EC, 0),  # Korean hangul
    0x213F49: (0x61CD, 0),  # East Asian ideograph
    0x213B52: (0x5C3F, 0),  # East Asian ideograph
    0x233F4A: (0x90FF, 0),  # East Asian ideograph
    0x6F4A37: (0xAE31, 0),  # Korean hangul
    0x273F4B: (0x601C, 0),  # East Asian ideograph
    0x213F4C: (0x61BE, 0),  # East Asian ideograph
    0x516A26: (0x51B4, 0),  # East Asian ideograph
    0x4D4D61: (0x7EF1, 0),  # East Asian ideograph
    0x6F5B49: (0xD23F, 0),  # Korean hangul
    0x275143: (0x7EFE, 0),  # East Asian ideograph
    0x274231: (0x62E2, 0),  # East Asian ideograph
    0x295940: (0x9CBC, 0),  # East Asian ideograph
    0x213B44: (0x5C0E, 0),  # East Asian ideograph
    0x234A21: (0x9627, 0),  # East Asian ideograph
    0x223F50: (0x69CE, 0),  # East Asian ideograph
    0x22327A: (0x63DC, 0),  # East Asian ideograph
    0x227269: (0x7E10, 0),  # East Asian ideograph
    0x6F5472: (0xC528, 0),  # Korean hangul
    0x4B3F53: (0x61F2, 0),  # East Asian ideograph
    0x4B5671: (
        0x873B,
        0,
    ),  # East Asian ideograph (variant of 215671 which maps to 873B)
    0x223F44: (0x698A, 0),  # East Asian ideograph
    0x213F54: (0x61F7, 0),  # East Asian ideograph
    0x234343: (0x927A, 0),  # East Asian ideograph
    0x213F55: (0x61F6, 0),  # East Asian ideograph
    0x27414F: (0x635F, 0),  # East Asian ideograph
    0x22327B: (0x63D7, 0),  # East Asian ideograph
    0x213F56: (0x61F8, 0),  # East Asian ideograph
    0x223F51: (0x69CA, 0),  # East Asian ideograph
    0x233237: (0x8A57, 0),  # East Asian ideograph
    0x213F57: (0x61F5, 0),  # East Asian ideograph
    0x6F5561: (0xC5F0, 0),  # Korean hangul
    0x21355B: (0x5436, 0),  # East Asian ideograph
    0x233F58: (0x9111, 0),  # East Asian ideograph
    0x215D5F: (0x927B, 0),  # East Asian ideograph
    0x224A66: (0x6E62, 0),  # East Asian ideograph
    0x223F59: (0x698D, 0),  # East Asian ideograph
    0x223F5A: (0x6991, 0),  # East Asian ideograph
    0x217C21: (0x5AA6, 0),  # East Asian ideograph
    0x217C22: (0x5A8C, 0),  # East Asian ideograph
    0x213F5B: (0x61FC, 0),  # East Asian ideograph
    0x227C24: (0x828E, 0),  # East Asian ideograph
    0x227C25: (0x8291, 0),  # East Asian ideograph
    0x217C26: (0x5AA2, 0),  # East Asian ideograph
    0x227C27: (0x828F, 0),  # East Asian ideograph
    0x227C28: (0x8284, 0),  # East Asian ideograph
    0x273F5C: (0x604B, 0),  # East Asian ideograph
    0x227C2D: (0x8283, 0),  # East Asian ideograph
    0x227C2E: (0x828A, 0),  # East Asian ideograph
    0x213F5D: (0x6208, 0),  # East Asian ideograph
    0x225138: (0x70CB, 0),  # East Asian ideograph
    0x274C78: (0x762B, 0),  # East Asian ideograph
    0x227C34: (0x82A7, 0),  # East Asian ideograph
    0x217C35: (0x5A95, 0),  # East Asian ideograph
    0x217C36: (0x5AAF, 0),  # East Asian ideograph
    0x227C38: (0x82AB, 0),  # East Asian ideograph
    0x217C39: (0x5AC8, 0),  # East Asian ideograph
    0x227C3A: (0x82B0, 0),  # East Asian ideograph
    0x227C3C: (0x82A4, 0),  # East Asian ideograph
    0x217C3E: (0x5AB5, 0),  # East Asian ideograph
    0x227C3F: (0x829A, 0),  # East Asian ideograph
    0x233F60: (0x910B, 0),  # East Asian ideograph
    0x227C42: (0x82A3, 0),  # East Asian ideograph
    0x6F4E7B: (0xB7ED, 0),  # Korean hangul
    0x227C44: (0x82B7, 0),  # East Asian ideograph
    0x227C45: (
        0x82AE,
        0,
    ),  # East Asian ideograph (variant of 4C7C45 which maps to 82AE)
    0x227C46: (0x82A9, 0),  # East Asian ideograph
    0x213F61: (0x620C, 0),  # East Asian ideograph
    0x217C49: (0x5AD1, 0),  # East Asian ideograph
    0x217C4A: (0x5A90, 0),  # East Asian ideograph
    0x6F5563: (0xC5F6, 0),  # Korean hangul
    0x227C4C: (0x82A8, 0),  # East Asian ideograph
    0x213F62: (0x6210, 0),  # East Asian ideograph
    0x227C4E: (0x82B4, 0),  # East Asian ideograph
    0x217C4F: (0x5AB8, 0),  # East Asian ideograph
    0x227C50: (0x82A1, 0),  # East Asian ideograph
    0x226160: (0x770E, 0),  # East Asian ideograph
    0x217C52: (0x5AAA, 0),  # East Asian ideograph
    0x227C53: (0x82AA, 0),  # East Asian ideograph
    0x227C55: (0x82D9, 0),  # East Asian ideograph
    0x227C57: (0x82FE, 0),  # East Asian ideograph
    0x2D3224: (0x7B87, 0),  # East Asian ideograph
    0x217C59: (0x5AD3, 0),  # East Asian ideograph
    0x227C5A: (0x82E0, 0),  # East Asian ideograph
    0x217C5B: (0x5AB1, 0),  # East Asian ideograph
    0x227C5C: (0x8300, 0),  # East Asian ideograph
    0x227C5F: (0x82EA, 0),  # East Asian ideograph
    0x227C60: (0x82F7, 0),  # East Asian ideograph
    0x227C62: (0x82EF, 0),  # East Asian ideograph
    0x227C63: (0x833A, 0),  # East Asian ideograph
    0x227C64: (0x82E4, 0),  # East Asian ideograph
    0x227C65: (0x82D5, 0),  # East Asian ideograph
    0x227C67: (0x8307, 0),  # East Asian ideograph
    0x227C68: (0x82FA, 0),  # East Asian ideograph
    0x227C69: (0x82F4, 0),  # East Asian ideograph
    0x227C6A: (0x82E2, 0),  # East Asian ideograph
    0x213F67: (0x621B, 0),  # East Asian ideograph
    0x227C6D: (0x82D2, 0),  # East Asian ideograph
    0x217C6E: (0x5AE0, 0),  # East Asian ideograph
    0x227C71: (0x82EB, 0),  # East Asian ideograph
    0x227C72: (0x82D8, 0),  # East Asian ideograph
    0x227C73: (0x82E1, 0),  # East Asian ideograph
    0x227C75: (0x82F6, 0),  # East Asian ideograph
    0x28602B: (0x762A, 0),  # East Asian ideograph
    0x227C7B: (0x8310, 0),  # East Asian ideograph
    0x227C7C: (0x82F3, 0),  # East Asian ideograph
    0x233F6A: (0x911E, 0),  # East Asian ideograph
    0x4B4569: (0x6A71, 0),  # East Asian ideograph
    0x23323B: (0x8A58, 0),  # East Asian ideograph
    0x6F5473: (0xC529, 0),  # Korean hangul
    0x274237: (0x631B, 0),  # East Asian ideograph
    0x6F5122: (0xBC41, 0),  # Korean hangul
    0x226162: (0x771B, 0),  # East Asian ideograph
    0x213F6D: (0x622E, 0),  # East Asian ideograph
    0x213F6E: (0x6230, 0),  # East Asian ideograph
    0x4B5973: (0x8D2E, 0),  # East Asian ideograph
    0x275344: (0x80C1, 0),  # East Asian ideograph
    0x213F6F: (0x6232, 0),  # East Asian ideograph
    0x23323C: (0x8A52, 0),  # East Asian ideograph
    0x6F5566: (0xC5FD, 0),  # Korean hangul
    0x21355C: (0x5433, 0),  # East Asian ideograph
    0x274238: (0x644A, 0),  # East Asian ideograph
    0x6F5123: (0xBC43, 0),  # Korean hangul
    0x226163: (0x7724, 0),  # East Asian ideograph
    0x213F72: (0x6236, 0),  # East Asian ideograph
    0x234349: (0x92AA, 0),  # East Asian ideograph
    0x6F4C38: (0xB18D, 0),  # Korean hangul
    0x22557C: (0x728B, 0),  # East Asian ideograph
    0x213F74: (0x623E, 0),  # East Asian ideograph
    0x225057: (0x7098, 0),  # East Asian ideograph
    0x235B2F: (0x9D7A, 0),  # East Asian ideograph
    0x213F75: (0x6240, 0),  # East Asian ideograph
    0x29325D: (0x8BD4, 0),  # East Asian ideograph
    0x2D3F76: (0x78A5, 0),  # East Asian ideograph
    0x6F5A6B: (0xD0B5, 0),  # Korean hangul
    0x6F5124: (0xBC44, 0),  # Korean hangul
    0x213B4C: (0x5C37, 0),  # East Asian ideograph
    0x223F77: (0x69BE, 0),  # East Asian ideograph
    0x4B6A22: (0x7F83, 0),  # East Asian ideograph
    0x213F78: (0x6248, 0),  # East Asian ideograph
    0x222A23: (0x5F82, 0),  # East Asian ideograph
    0x233F79: (0x912B, 0),  # East Asian ideograph
    0x4B456C: (0x6ADB, 0),  # East Asian ideograph (variant of 21456C)
    0x2D602D: (0x976D, 0),  # East Asian ideograph
    0x213F7A: (0x624B, 0),  # East Asian ideograph
    0x212A25: (0xE8D4, 0),  # EACC component character
    0x6F5568: (0xC5FF, 0),  # Korean hangul
    0x294E7B: (0x9883, 0),  # East Asian ideograph
    0x4B6A26: (0x6C8D, 0),  # East Asian ideograph
    0x6F4A39: (0xAE37, 0),  # Korean hangul
    0x2D5A34: (0x8CAD, 0),  # East Asian ideograph
    0x393D6F: (0x8907, 0),  # East Asian ideograph
    0x213F7E: (0x6254, 0),  # East Asian ideograph
    0x6F5A70: (0xD0C0, 0),  # Korean hangul
    0x4B456D: (0x823B, 0),  # East Asian ideograph
    0x2D403F: (0x6255, 0),  # East Asian ideograph
    0x695F70: (0x7195, 0),  # East Asian ideograph
    0x27423B: (0x63FD, 0),  # East Asian ideograph
    0x6F5126: (0xBC84, 0),  # Korean hangul
    0x225731: (0x731D, 0),  # East Asian ideograph
    0x213A7A: (0x5BB5, 0),  # East Asian ideograph
    0x696A2C: (0x87D0, 0),  # East Asian ideograph
    0x2E5A78: (0x74A2, 0),  # East Asian ideograph
    0x277954: (0x5956, 0),  # East Asian ideograph
    0x212A2E: (0xE8DC, 0),  # EACC component character
    0x333240: (0x4FFB, 0),  # East Asian ideograph
    0x232A2F: (0x86FA, 0),  # East Asian ideograph
    0x227D21: (0x830C, 0),  # East Asian ideograph
    0x227D22: (0x82FB, 0),  # East Asian ideograph
    0x227D24: (0x82FD, 0),  # East Asian ideograph
    0x215925: (0x8AE6, 0),  # East Asian ideograph
    0x227D26: (0x8333, 0),  # East Asian ideograph
    0x4B5238: (0x7F87, 0),  # East Asian ideograph
    0x227D29: (0x8328, 0),  # East Asian ideograph
    0x217D2A: (0x5AFD, 0),  # East Asian ideograph
    0x217D2B: (0x5B08, 0),  # East Asian ideograph
    0x212A32: (0xE8DF, 0),  # EACC component character
    0x227D2E: (0x8351, 0),  # East Asian ideograph
    0x214C5C: (0x75F1, 0),  # East Asian ideograph
    0x6F5C7B: (0xD5CC, 0),  # Korean hangul
    0x4B456F: (0x685C, 0),  # East Asian ideograph
    0x227D35: (0x831B, 0),  # East Asian ideograph
    0x217D38: (0x5B03, 0),  # East Asian ideograph
    0x222A34: (0x3013, 0),  # East Asian ideograph (not found in unified han)
    0x227D3B: (0x8356, 0),  # East Asian ideograph
    0x217D3D: (0x5B17, 0),  # East Asian ideograph
    0x217D3E: (0x5B16, 0),  # East Asian ideograph
    0x227D3F: (0x8322, 0),  # East Asian ideograph
    0x227D40: (0x832C, 0),  # East Asian ideograph
    0x212A36: (0xE8E3, 0),  # EACC component character
    0x217D47: (0x5B1B, 0),  # East Asian ideograph
    0x227D48: (0x833C, 0),  # East Asian ideograph
    0x227D4A: (0x834D, 0),  # East Asian ideograph
    0x334F3A: (0x7A49, 0),  # East Asian ideograph
    0x227D4D: (
        0x8343,
        0,
    ),  # East Asian ideograph (variant of 4C7D4D which maps to 8343)
    0x22505C: (0x70B7, 0),  # East Asian ideograph
    0x4B4570: (0x6A29, 0),  # East Asian ideograph
    0x227D52: (0x832F, 0),  # East Asian ideograph
    0x227D53: (0x8348, 0),  # East Asian ideograph
    0x227D54: (0x8312, 0),  # East Asian ideograph
    0x227D56: (0x8316, 0),  # East Asian ideograph
    0x212A39: (0xE8E6, 0),  # EACC component character
    0x227D58: (0x831A, 0),  # East Asian ideograph
    0x217D59: (0x5B32, 0),  # East Asian ideograph
    0x2E6F43: (0x9908, 0),  # East Asian ideograph
    0x6F5A6C: (0xD0B7, 0),  # Korean hangul
    0x6F5129: (0xBC8B, 0),  # Korean hangul
    0x213B51: (0x5C41, 0),  # East Asian ideograph
    0x227D5F: (0x8347, 0),  # East Asian ideograph
    0x227D62: (0x83A8, 0),  # East Asian ideograph
    0x217D63: (0x5B3F, 0),  # East Asian ideograph
    0x4B3021: (0x58F1, 0),  # East Asian ideograph
    0x227D67: (0x83AD, 0),  # East Asian ideograph
    0x6F5121: (0xBC40, 0),  # Korean hangul
    0x286A3C: (0x7AAD, 0),  # East Asian ideograph
    0x4C7D6A: (0x8323, 0),  # East Asian ideograph
    0x227D6D: (0x8373, 0),  # East Asian ideograph
    0x217D6E: (0x5B45, 0),  # East Asian ideograph
    0x6F4E7D: (0xB7F4, 0),  # Korean hangul
    0x227D72: (0x83B0, 0),  # East Asian ideograph
    0x217D74: (0x5B4C, 0),  # East Asian ideograph
    0x212A3E: (0xE8EB, 0),  # EACC component character
    0x227D76: (0x831D, 0),  # East Asian ideograph
    0x6F556D: (0xC608, 0),  # Korean hangul
    0x282868: (0x5E91, 0),  # East Asian ideograph
    0x227D7A: (0x838F, 0),  # East Asian ideograph
    0x6F512A: (0xBC8C, 0),  # Korean hangul
    0x227D7C: (0x8395, 0),  # East Asian ideograph
    0x227D7E: (0x8375, 0),  # East Asian ideograph
    0x215928: (0x8AF1, 0),  # East Asian ideograph
    0x234350: (0x92A6, 0),  # East Asian ideograph
    0x51384D: (0x51C3, 0),  # East Asian ideograph
    0x69545C: (0x58D7, 0),  # East Asian ideograph
    0x212A41: (0xE8EE, 0),  # EACC component character
    0x275E61: (0x9614, 0),  # East Asian ideograph
    0x212A46: (0x3013, 0),  # Ideographic geta symbol
    0x212A42: (0xE8EF, 0),  # EACC component character
    0x23545D: (0x9AC8, 0),  # East Asian ideograph
    0x226A43: (0x7ABF, 0),  # East Asian ideograph
    0x6F556E: (0xC60C, 0),  # Korean hangul
    0x6F512B: (0xBC94, 0),  # Korean hangul
    0x22315C: (0x634B, 0),  # East Asian ideograph
    0x212A45: (0xE8F2, 0),  # EACC component character
    0x6F5574: (0xC62C, 0),  # Korean hangul
    0x2D314C: (0x5008, 0),  # East Asian ideograph
    0x27534D: (0x8109, 0),  # East Asian ideograph
    0x273B6E: (0x5188, 0),  # East Asian ideograph
    0x214C60: (0x760D, 0),  # East Asian ideograph
    0x2D4D71: (0x7719, 0),  # East Asian ideograph
    0x213E6A: (0x60DF, 0),  # East Asian ideograph
    0x6F5C21: (0xD33D, 0),  # Korean hangul
    0x2D3C61: (0x5E47, 0),  # East Asian ideograph
    0x234667: (0x93E7, 0),  # East Asian ideograph
    0x6F512C: (0xBC95, 0),  # Korean hangul
    0x21592A: (0x8ADC, 0),  # East Asian ideograph
    0x2D3C65: (0x79CA, 0),  # East Asian ideograph
    0x6F4E29: (0xB550, 0),  # Korean hangul
    0x393E47: (0x8CC9, 0),  # East Asian ideograph
    0x6F5032: (0xBA70, 0),  # Korean hangul
    0x2F386F: (0x8DD7, 0),  # East Asian ideograph
    0x214C61: (0x7627, 0),  # East Asian ideograph
    0x6F2464: (0x314E, 0),  # Korean hangul
    0x6F5B47: (0xD23C, 0),  # Korean hangul
    0x6F512D: (0xBC97, 0),  # Korean hangul
    0x6F516E: (0xBE45, 0),  # Korean hangul
    0x226A4F: (0x7AD1, 0),  # East Asian ideograph
    0x4B3974: (0x5B22, 0),  # East Asian ideograph
    0x3F5564: (0x61DE, 0),  # East Asian ideograph
    0x214C62: (0x7613, 0),  # East Asian ideograph
    0x4B6130: (0x99C4, 0),  # East Asian ideograph
    0x6F5571: (0xC624, 0),  # Korean hangul
    0x6F512E: (0xBC98, 0),  # Korean hangul
    0x284642: (0x6BF5, 0),  # East Asian ideograph
    0x226A54: (0x7AD5, 0),  # East Asian ideograph
    0x2D5A3D: (0x8CDB, 0),  # East Asian ideograph
    0x225C50: (0x74E4, 0),  # East Asian ideograph
    0x225062: (0x70A1, 0),  # East Asian ideograph
    0x335461: (0x6CD6, 0),  # East Asian ideograph
    0x213041: (0x4E4D, 0),  # East Asian ideograph
    0x6F5572: (0xC625, 0),  # Korean hangul
    0x6F512F: (0xBC99, 0),  # Korean hangul
    0x234355: (0x929A, 0),  # East Asian ideograph
    0x6F4A3B: (0xAE40, 0),  # Korean hangul
    0x217E59: (0x5BC1, 0),  # East Asian ideograph
    0x2F2A5A: (0x868B, 0),  # Unrelated variant of EACC 23293D which maps to 868B
    0x22714B: (0x7D9B, 0),  # East Asian ideograph
    0x227E21: (0x837F, 0),  # East Asian ideograph
    0x227E22: (0x8399, 0),  # East Asian ideograph
    0x225063: (0x70A3, 0),  # East Asian ideograph
    0x217E24: (0x5B65, 0),  # East Asian ideograph
    0x227E25: (0x8387, 0),  # East Asian ideograph
    0x227E26: (0x83B9, 0),  # East Asian ideograph
    0x217E27: (0x5C58, 0),  # East Asian ideograph (not in Unicode)
    0x217E28: (0x5B6C, 0),  # East Asian ideograph
    0x217E2A: (0x5B6E, 0),  # East Asian ideograph
    0x227E2B: (0x83A9, 0),  # East Asian ideograph
    0x227E2F: (0x839B, 0),  # East Asian ideograph
    0x217E30: (0x5B7B, 0),  # East Asian ideograph
    0x217E31: (0x5B7C, 0),  # East Asian ideograph
    0x217E32: (0x5B80, 0),  # East Asian ideograph
    0x227E33: (0x83AA, 0),  # East Asian ideograph
    0x217E34: (0x5B84, 0),  # East Asian ideograph
    0x217E35: (0x5B82, 0),  # East Asian ideograph (not in Unicode)
    0x227E37: (0x839C, 0),  # East Asian ideograph
    0x227E38: (0x839F, 0),  # East Asian ideograph
    0x222A5F: (0x5FD1, 0),  # East Asian ideograph
    0x217E40: (0x5B95, 0),  # East Asian ideograph
    0x227E41: (0x83CF, 0),  # East Asian ideograph
    0x227E43: (0x83F9, 0),  # East Asian ideograph
    0x2F445F: (0x941A, 0),  # East Asian ideograph
    0x227E45: (0x8421, 0),  # East Asian ideograph
    0x6F5476: (0xC538, 0),  # Korean hangul
    0x217E49: (0x5BAC, 0),  # East Asian ideograph
    0x6F5131: (0xBCA0, 0),  # Korean hangul
    0x294A44: (0x9655, 0),  # East Asian ideograph
    0x21592F: (0x8AF7, 0),  # East Asian ideograph
    0x227E52: (0x83EA, 0),  # East Asian ideograph
    0x227E53: (0x8413, 0),  # East Asian ideograph
    0x217E55: (0x5BB7, 0),  # East Asian ideograph
    0x227E56: (0x83FC, 0),  # East Asian ideograph
    0x227E57: (0x83F6, 0),  # East Asian ideograph
    0x227E59: (0x8410, 0),  # East Asian ideograph
    0x227E5A: (0x83E1, 0),  # East Asian ideograph
    0x217E5B: (0x3761, 0),  # East Asian ideograph (not found in unified han)
    0x227E60: (0x83C6, 0),  # East Asian ideograph
    0x227E61: (0x8407, 0),  # East Asian ideograph
    0x227E63: (0x83EB, 0),  # East Asian ideograph
    0x216A66: (0x51DF, 0),  # East Asian ideograph
    0x6F5575: (0xC62D, 0),  # Korean hangul
    0x217E68: (0x5BD4, 0),  # East Asian ideograph
    0x217E6A: (0x5BC3, 0),  # East Asian ideograph
    0x227E6B: (0x83E2, 0),  # East Asian ideograph
    0x227E6D: (0x8401, 0),  # East Asian ideograph
    0x217E6E: (0x5BD6, 0),  # East Asian ideograph
    0x234358: (0x92AB, 0),  # East Asian ideograph
    0x227E71: (0x83D8, 0),  # East Asian ideograph
    0x227E72: (0x83E5, 0),  # East Asian ideograph
    0x227E74: (0x8418, 0),  # East Asian ideograph
    0x217E75: (0x5BD7, 0),  # East Asian ideograph
    0x227E79: (0x83CE, 0),  # East Asian ideograph
    0x227E7B: (0x83D3, 0),  # East Asian ideograph
    0x295B52: (0x9E4E, 0),  # East Asian ideograph
    0x227E7D: (0x83D6, 0),  # East Asian ideograph
    0x217E7E: (0x5BEA, 0),  # East Asian ideograph
    0x6F5576: (0xC62E, 0),  # Korean hangul
    0x6F5133: (0xBCA4, 0),  # Korean hangul
    0x294A46: (0x9649, 0),  # East Asian ideograph
    0x275F3D: (0x96B6, 0),  # East Asian ideograph
    0x4B6260: (0x9EBD, 0),  # East Asian ideograph
    0x227E6A: (0x83BF, 0),  # East Asian ideograph
    0x2D6030: (0x97EE, 0),  # East Asian ideograph
    0x235466: (0x9AD0, 0),  # East Asian ideograph
    0x22454D: (0x6996, 0),  # East Asian ideograph
    0x6F5577: (0xC633, 0),  # Korean hangul
    0x6F5134: (0xBCA7, 0),  # Korean hangul
    0x213B5C: (0x5C50, 0),  # East Asian ideograph
    0x215932: (0x8B19, 0),  # East Asian ideograph
    0x6F4A3C: (0xAE41, 0),  # Korean hangul
    0x2D3C6D: (0x8298, 0),  # East Asian ideograph (duplicate simplified)
    0x222A73: (0x5FF8, 0),  # East Asian ideograph
    0x225068: (0x7551, 0),  # East Asian ideograph
    0x6F5551: (0xC5C8, 0),  # Korean hangul
    0x6F5135: (0xBCA8, 0),  # Korean hangul
    0x215521: (0x5179, 0),  # East Asian ideograph
    0x223F5C: (0x69AA, 0),  # East Asian ideograph
    0x275274: (0x58F0, 0),  # East Asian ideograph
    0x2D3C6E: (0x7240, 0),  # East Asian ideograph
    0x6F5523: (0xC54C, 0),  # Korean hangul
    0x6F5524: (0xC54E, 0),  # Korean hangul
    0x23324F: (0x8A7F, 0),  # East Asian ideograph
    0x233E37: (0x9088, 0),  # East Asian ideograph
    0x4C4446: (0x6B4E, 0),  # East Asian ideograph
    0x6F5525: (0xC553, 0),  # Korean hangul
    0x232A7B: (0x877B, 0),  # East Asian ideograph
    0x6F5526: (0xC554, 0),  # Korean hangul
    0x3A6A7C: (0x7BEA, 0),  # East Asian ideograph
    0x235527: (0x9AEB, 0),  # East Asian ideograph
    0x22763D: (0x801E, 0),  # East Asian ideograph
    0x235528: (0x9AF2, 0),  # East Asian ideograph
    0x215529: (0x8396, 0),  # East Asian ideograph
    0x233250: (0x8A86, 0),  # East Asian ideograph
    0x225424: (0x71C1, 0),  # East Asian ideograph
    0x21552A: (0x83A7, 0),  # East Asian ideograph
    0x6F5137: (0xBCB1, 0),  # Korean hangul
    0x213B5F: (0x5C5C, 0),  # East Asian ideograph
    0x6F552B: (0xC55E, 0),  # Korean hangul
    0x295F7B: (0x9F51, 0),  # East Asian ideograph
    0x2D3C70: (0x576B, 0),  # East Asian ideograph
    0x27552D: (0x5E84, 0),  # East Asian ideograph
    0x2D552E: (0x82FA, 0),  # East Asian ideograph (variant of 227C68)
    0x23316E: (0x8A04, 0),  # East Asian ideograph
    0x2D493A: (0x702C, 0),  # East Asian ideograph
    0x215D79: (0x9375, 0),  # East Asian ideograph
    0x28464C: (0x6BE1, 0),  # East Asian ideograph
    0x213B60: (0x5C62, 0),  # East Asian ideograph
    0x6F5531: (0xC570, 0),  # Korean hangul
    0x293726: (0x8D5C, 0),  # East Asian ideograph
    0x235532: (0x9AF9, 0),  # East Asian ideograph
    0x6F5533: (0xC573, 0),  # Korean hangul
    0x6F5534: (0xC574, 0),  # Korean hangul
    0x2F3363: (0x8B1A, 0),  # East Asian ideograph
    0x6F5139: (0xBCB5, 0),  # Korean hangul
    0x235535: (0x9AFD, 0),  # East Asian ideograph
    0x4B3474: (
        0x537F,
        0,
    ),  # East Asian ideograph (variant of 213474 which maps to 537F)
    0x6F582F: (0xC9D0, 0),  # Korean hangul
    0x22385A: (0x6678, 0),  # East Asian ideograph
    0x235536: (0x9B01, 0),  # East Asian ideograph
    0x2D5A48: (0x8D71, 0),  # East Asian ideograph
    0x295B59: (0x9E5C, 0),  # East Asian ideograph
    0x235538: (0x9B02, 0),  # East Asian ideograph
    0x6F5539: (0xC584, 0),  # Korean hangul
    0x6F513A: (0xBCBC, 0),  # Korean hangul
    0x4B553A: (
        0x83C1,
        0,
    ),  # East Asian ideograph (variant of 21553A which maps to 83C1)
    0x23553B: (0x9B00, 0),  # East Asian ideograph
    0x2D3830: (0x573B, 0),  # East Asian ideograph
    0x27553C: (0x534E, 0),  # East Asian ideograph
    0x283542: (0x64B7, 0),  # East Asian ideograph
    0x287531: (0x7F9F, 0),  # East Asian ideograph
    0x33502A: (0x9257, 0),  # East Asian ideograph
    0x23553E: (0x9B04, 0),  # East Asian ideograph
    0x6F513B: (0xBCBD, 0),  # Korean hangul
    0x213B63: (0x5C6C, 0),  # East Asian ideograph
    0x22565B: (0x72C1, 0),  # East Asian ideograph
    0x275947: (0x8C34, 0),  # East Asian ideograph
    0x223442: (0x648F, 0),  # East Asian ideograph
    0x213E3F: (0x6062, 0),  # East Asian ideograph
    0x3F4472: (0x7881, 0),  # East Asian ideograph
    0x215541: (0x840A, 0),  # East Asian ideograph
    0x4B5542: (0x8420, 0),  # East Asian ideograph
    0x33502B: (0x724B, 0),  # East Asian ideograph
    0x235543: (0x9B0B, 0),  # East Asian ideograph
    0x6F4B2B: (0xAFCE, 0),  # Korean hangul
    0x2E4D3D: (0x6D38, 0),  # East Asian ideograph
    0x696A5E: (0x88B0, 0),  # East Asian ideograph
    0x227431: (0x7F4E, 0),  # East Asian ideograph
    0x213561: (0x543B, 0),  # East Asian ideograph
    0x225D39: (0x7517, 0),  # East Asian ideograph
    0x6F5545: (0xC5B5, 0),  # Korean hangul
    0x6F5546: (0xC5B6, 0),  # Korean hangul
    0x6F4F5B: (0xB98E, 0),  # Korean hangul
    0x295B5C: (0x9E5B, 0),  # East Asian ideograph
    0x225070: (0x79CC, 0),  # East Asian ideograph
    0x235547: (0x9B0E, 0),  # East Asian ideograph
    0x233256: (0x8A61, 0),  # East Asian ideograph
    0x6F5548: (0xC5B9, 0),  # Korean hangul
    0x274252: (0x654C, 0),  # East Asian ideograph
    0x6F513D: (0xBCC4, 0),  # Korean hangul
    0x284651: (0x6C07, 0),  # East Asian ideograph
    0x6F5549: (0xC5BA, 0),  # Korean hangul
    0x213722: (0x55C6, 0),  # East Asian ideograph
    0x233C2D: (0x8F40, 0),  # East Asian ideograph
    0x6F554A: (0xC5BB, 0),  # Korean hangul
    0x6F554B: (0xC5BC, 0),  # Korean hangul
    0x28575E: (0x72B8, 0),  # East Asian ideograph
    0x227849: (0x811D, 0),  # East Asian ideograph
    0x393944: (0x59B3, 0),  # East Asian ideograph
    0x6F554C: (0xC5BD, 0),  # Korean hangul
    0x355E76: (0x82BE, 0),  # East Asian ideograph
    0x27554D: (0x82C7, 0),  # East Asian ideograph
    0x6F513E: (0xBCCC, 0),  # Korean hangul
    0x23554E: (0x9B11, 0),  # East Asian ideograph
    0x223F65: (0x699E, 0),  # East Asian ideograph
    0x4B5959: (0x8273, 0),  # East Asian ideograph
    0x21554F: (0x8449, 0),  # East Asian ideograph
    0x2D5550: (0x585F, 0),  # East Asian ideograph
    0x28575F: (0x72F2, 0),  # East Asian ideograph
    0x283546: (0x6445, 0),  # East Asian ideograph
    0x225072: (0x70BF, 0),  # East Asian ideograph
    0x215551: (0x846B, 0),  # East Asian ideograph
    0x233258: (0x8A3E, 0),  # East Asian ideograph
    0x225552: (0x7253, 0),  # East Asian ideograph
    0x274254: (0x6570, 0),  # East Asian ideograph
    0x6F513F: (0xBCCD, 0),  # Korean hangul
    0x225553: (0x7255, 0),  # East Asian ideograph
    0x275276: (0x806A, 0),  # East Asian ideograph
    0x6F7726: (0xADB9, 0),  # Korean hangul
    0x235554: (0x9B18, 0),  # East Asian ideograph
    0x6F585A: (0xCAC4, 0),  # Korean hangul
    0x333F22: (
        0x6168,
        0,
    ),  # East Asian ideograph (variant of 213F22 which maps to 6168)
    0x275555: (0x83B4, 0),  # East Asian ideograph
}
CHARSET_70 = {  # Superscripts
    0x28: (0x207D, 0),  # SUPERSCRIPT OPENING PARENTHESIS / SUPERSCRIPT LEFT PARENTHESIS
    0x29: (
        0x207E,
        0,
    ),  # SUPERSCRIPT CLOSING PARENTHESIS / SUPERSCRIPT RIGHT PARENTHESIS
    0x2B: (0x207A, 0),  # SUPERSCRIPT PLUS SIGN
    0x2D: (0x207B, 0),  # SUPERSCRIPT HYPHEN-MINUS / SUPERSCRIPT MINUS
    0x30: (0x2070, 0),  # SUPERSCRIPT DIGIT ZERO
    0x31: (0xB9, 0),  # SUPERSCRIPT DIGIT ONE
    0x32: (0xB2, 0),  # SUPERSCRIPT DIGIT TWO
    0x33: (0xB3, 0),  # SUPERSCRIPT DIGIT THREE
    0x34: (0x2074, 0),  # SUPERSCRIPT DIGIT FOUR
    0x35: (0x2075, 0),  # SUPERSCRIPT DIGIT FIVE
    0x36: (0x2076, 0),  # SUPERSCRIPT DIGIT SIX
    0x37: (0x2077, 0),  # SUPERSCRIPT DIGIT SEVEN
    0x38: (0x2078, 0),  # SUPERSCRIPT DIGIT EIGHT
    0x39: (0x2079, 0),  # SUPERSCRIPT DIGIT NINE
}
CHARSET_51 = {  # Extended Cyrillic
    0xC0: (
        0x491,
        0,
    ),  # LOWERCASE GE WITH UPTURN / CYRILLIC SMALL LETTER GHE WITH UPTURN
    0xC1: (0x452, 0),  # LOWERCASE DJE / CYRILLIC SMALL LETTER DJE (Serbian)
    0xC2: (0x453, 0),  # CYRILLIC SMALL LETTER GJE
    0xC3: (0x454, 0),  # LOWERCASE E / CYRILLIC SMALL LETTER UKRAINIAN IE
    0xC4: (0x451, 0),  # CYRILLIC SMALL LETTER IO
    0xC5: (0x455, 0),  # CYRILLIC SMALL LETTER DZE
    0xC6: (0x456, 0),  # LOWERCASE I / CYRILLIC SMALL LETTER BYELORUSSIAN-UKRANIAN I
    0xC7: (0x457, 0),  # LOWERCASE YI / CYRILLIC SMALL LETTER YI (Ukrainian)
    0xC8: (0x458, 0),  # CYRILLIC SMALL LETTER JE
    0xC9: (0x459, 0),  # CYRILLIC SMALL LETTER LJE
    0xCA: (0x45A, 0),  # CYRILLIC SMALL LETTER NJE
    0xCB: (0x45B, 0),  # LOWERCASE TSHE / CYRILLIC SMALL LETTER TSHE (Serbian)
    0xCC: (0x45C, 0),  # CYRILLIC SMALL LETTER KJE
    0xCD: (
        0x45E,
        0,
    ),  # LOWERCASE SHORT U / CYRILLIC SMALL LETTER SHORT U (Byelorussian)
    0xCE: (0x45F, 0),  # CYRILLIC SMALL LETTER DZHE
    0xD0: (0x463, 0),  # CYRILLIC SMALL LETTER YAT
    0xD1: (0x473, 0),  # CYRILLIC SMALL LETTER FITA
    0xD2: (0x475, 0),  # CYRILLIC SMALL LETTER IZHITSA
    0xD3: (0x46B, 0),  # CYRILLIC SMALL LETTER BIG YUS
    0xDB: (0x5B, 0),  # OPENING SQUARE BRACKET / LEFT SQUARE BRACKET
    0xDD: (0x5D, 0),  # CLOSING SQUARE BRACKET / RIGHT SQUARE BRACKET
    0xDF: (0x5F, 0),  # SPACING UNDERSCORE / LOW LINE
    0xE0: (
        0x490,
        0,
    ),  # UPPERCASE GE WITH UPTURN / CYRILLIC CAPITAL LETTER GHE WITH UPTURN
    0xE1: (0x402, 0),  # UPPERCASE DJE / CYRILLIC CAPITAL LETTER DJE (Serbian)
    0xE2: (0x403, 0),  # CYRILLIC CAPITAL LETTER GJE
    0xE3: (0x404, 0),  # UPPERCASE E / CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0xE4: (0x401, 0),  # CYRILLIC CAPITAL LETTER IO
    0xE5: (0x405, 0),  # CYRILLIC CAPITAL LETTER DZE
    0xE6: (0x406, 0),  # UPPERCASE I / CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRANIAN I
    0xE7: (0x407, 0),  # UPPERCASE YI / CYRILLIC CAPITAL LETTER YI (Ukrainian)
    0xE8: (0x408, 0),  # CYRILLIC CAPITAL LETTER JE
    0xE9: (0x409, 0),  # CYRILLIC CAPITAL LETTER LJE
    0xEA: (0x40A, 0),  # CYRILLIC CAPITAL LETTER NJE
    0xEB: (0x40B, 0),  # UPPERCASE TSHE / CYRILLIC CAPITAL LETTER TSHE (Serbian)
    0xEC: (0x40C, 0),  # CYRILLIC CAPITAL LETTER KJE
    0xED: (
        0x40E,
        0,
    ),  # UPPERCASE SHORT U / CYRILLIC CAPITAL LETTER SHORT U (Byelorussian)
    0xEE: (0x40F, 0),  # CYRILLIC CAPITAL LETTER DZHE
    0xEF: (0x42A, 0),  # CYRILLIC CAPITAL LETTER HARD SIGN
    0xF0: (0x462, 0),  # CYRILLIC CAPITAL LETTER YAT
    0xF1: (0x472, 0),  # CYRILLIC CAPITAL LETTER FITA
    0xF2: (0x474, 0),  # CYRILLIC CAPITAL LETTER IZHITSA
    0xF3: (0x46A, 0),  # CYRILLIC CAPITAL LETTER BIG YUS
}
CHARSET_53 = {  # Basic Greek
    0x21: (0x300, 1),  # COMBINING GRAVE ACCENT
    0x22: (0x301, 1),  # COMBINING ACUTE ACCENT
    0x23: (0x308, 1),  # COMBINING DIAERESIS
    0x24: (0x342, 1),  # COMBINING GREEK PERISPOMENI / CIRCUMFLEX
    0x25: (0x313, 1),  # COMBINING COMMA ABOVE / SMOOTH BREATHING
    0x26: (0x314, 1),  # COMBINING REVERSED COMMA ABOVE / ROUGH BREATHING
    0x27: (0x345, 1),  # COMBINING GREEK YPOGEGRAMMENI / IOTA SUBSCRIPT
    0x30: (0xAB, 0),  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x31: (0xBB, 0),  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x32: (0x201C, 0),  # LEFT DOUBLE QUOTATION MARK
    0x33: (0x201D, 0),  # RIGHT DOUBLE QUOTATION MARK
    0x34: (0x374, 0),  # GREEK NUMERAL SIGN / UPPER PRIME
    0x35: (0x375, 0),  # GREEK LOWER NUMERAL SIGN / LOWER PRIME
    0x3B: (0x387, 0),  # GREEK ANO TELEIA / RAISED DOT, GREEK SEMICOLON
    0x3F: (0x37E, 0),  # GREEK QUESTION MARK
    0x41: (0x391, 0),  # GREEK CAPITAL LETTER ALPHA
    0x42: (0x392, 0),  # GREEK CAPITAL LETTER BETA
    0x44: (0x393, 0),  # GREEK CAPITAL LETTER GAMMA
    0x45: (0x394, 0),  # GREEK CAPITAL LETTER DELTA
    0x46: (0x395, 0),  # GREEK CAPITAL LETTER EPSILON
    0x47: (0x3DA, 0),  # GREEK LETTER STIGMA
    0x48: (0x3DC, 0),  # GREEK LETTER DIGAMMA
    0x49: (0x396, 0),  # GREEK CAPITAL LETTER ZETA
    0x4A: (0x397, 0),  # GREEK CAPITAL LETTER ETA
    0x4B: (0x398, 0),  # GREEK CAPITAL LETTER THETA
    0x4C: (0x399, 0),  # GREEK CAPITAL LETTER IOTA
    0x4D: (0x39A, 0),  # GREEK CAPITAL LETTER KAPPA
    0x4E: (0x39B, 0),  # GREEK CAPITAL LETTER LAMDA
    0x4F: (0x39C, 0),  # GREEK CAPITAL LETTER MU
    0x50: (0x39D, 0),  # GREEK CAPITAL LETTER NU
    0x51: (0x39E, 0),  # GREEK CAPITAL LETTER XI
    0x52: (0x39F, 0),  # GREEK CAPITAL LETTER OMICRON
    0x53: (0x3A0, 0),  # GREEK CAPITAL LETTER PI
    0x54: (0x3DE, 0),  # GREEK LETTER KOPPA
    0x55: (0x3A1, 0),  # GREEK CAPITAL LETTER RHO
    0x56: (0x3A3, 0),  # GREEK CAPITAL LETTER SIGMA
    0x58: (0x3A4, 0),  # GREEK CAPITAL LETTER TAU
    0x59: (0x3A5, 0),  # GREEK CAPITAL LETTER UPSILON
    0x5A: (0x3A6, 0),  # GREEK CAPITAL LETTER PHI
    0x5B: (0x3A7, 0),  # GREEK CAPITAL LETTER CHI
    0x5C: (0x3A8, 0),  # GREEK CAPITAL LETTER PSI
    0x5D: (0x3A9, 0),  # GREEK CAPITAL LETTER OMEGA
    0x5E: (0x3E0, 0),  # GREEK LETTER SAMPI
    0x61: (0x3B1, 0),  # GREEK SMALL LETTER ALPHA
    0x62: (0x3B2, 0),  # GREEK SMALL LETTER BETA / SMALL LETTER BETA BEGINNING OF WORD
    0x63: (0x3D0, 0),  # GREEK BETA SYMBOL / SMALL LETTER BETA MIDDLE OF WORD
    0x64: (0x3B3, 0),  # GREEK SMALL LETTER GAMMA
    0x65: (0x3B4, 0),  # GREEK SMALL LETTER DELTA
    0x66: (0x3B5, 0),  # GREEK SMALL LETTER EPSILON
    0x67: (0x3DB, 0),  # GREEK SMALL LETTER STIGMA
    0x68: (0x3DD, 0),  # GREEK SMALL LETTER DIGAMMA
    0x69: (0x3B6, 0),  # GREEK SMALL LETTER ZETA
    0x6A: (0x3B7, 0),  # GREEK SMALL LETTER ETA
    0x6B: (0x3B8, 0),  # GREEK SMALL LETTER THETA
    0x6C: (0x3B9, 0),  # GREEK SMALL LETTER IOTA
    0x6D: (0x3BA, 0),  # GREEK SMALL LETTER KAPPA
    0x6E: (0x3BB, 0),  # GREEK SMALL LETTER LAMDA
    0x6F: (0x3BC, 0),  # GREEK SMALL LETTER MU
    0x70: (0x3BD, 0),  # GREEK SMALL LETTER NU
    0x71: (0x3BE, 0),  # GREEK SMALL LETTER XI
    0x72: (0x3BF, 0),  # GREEK SMALL LETTER OMICRON
    0x73: (0x3C0, 0),  # GREEK SMALL LETTER PI
    0x74: (0x3DF, 0),  # GREEK SMALL LETTER KOPPA
    0x75: (0x3C1, 0),  # GREEK SMALL LETTER RHO
    0x76: (0x3C3, 0),  # GREEK SMALL LETTER SIGMA
    0x77: (0x3C2, 0),  # GREEK SMALL LETTER FINAL SIGMA / SMALL LETTER SIGMA END OF WORD
    0x78: (0x3C4, 0),  # GREEK SMALL LETTER TAU
    0x79: (0x3C5, 0),  # GREEK SMALL LETTER UPSILON
    0x7A: (0x3C6, 0),  # GREEK SMALL LETTER PHI
    0x7B: (0x3C7, 0),  # GREEK SMALL LETTER CHI
    0x7C: (0x3C8, 0),  # GREEK SMALL LETTER PSI
    0x7D: (0x3C9, 0),  # GREEK SMALL LETTER OMEGA
    0x7E: (0x3E1, 0),  # GREEK SMALL LETTER SAMPI
}
CHARSET_42 = {  # Basic Latin (ASCII)
    0x1B: (0x1B, 0),  # ESCAPE (Unlikely to occur in UCS/Unicode)
    0x1D: (0x1D, 0),  # RECORD TERMINATOR / GROUP SEPARATOR
    0x1E: (0x1E, 0),  # FIELD TERMINATOR / RECORD SEPARATOR
    0x1F: (0x1F, 0),  # SUBFIELD DELIMITER / UNIT SEPARATOR
    0x20: (0x20, 0),  # SPACE, BLANK / SPACE
    0x21: (0x21, 0),  # EXCLAMATION MARK
    0x22: (0x22, 0),  # QUOTATION MARK
    0x23: (0x23, 0),  # NUMBER SIGN
    0x24: (0x24, 0),  # DOLLAR SIGN
    0x25: (0x25, 0),  # PERCENT SIGN
    0x26: (0x26, 0),  # AMPERSAND
    0x27: (0x27, 0),  # APOSTROPHE
    0x28: (0x28, 0),  # OPENING PARENTHESIS / LEFT PARENTHESIS
    0x29: (0x29, 0),  # CLOSING PARENTHESIS / CLOSING PARENTHESIS
    0x2A: (0x2A, 0),  # ASTERISK
    0x2B: (0x2B, 0),  # PLUS SIGN
    0x2C: (0x2C, 0),  # COMMA
    0x2D: (0x2D, 0),  # HYPHEN-MINUS
    0x2E: (0x2E, 0),  # PERIOD, DECIMAL POINT / FULL STOP
    0x2F: (0x2F, 0),  # SLASH / SOLIDUS
    0x30: (0x30, 0),  # DIGIT ZERO
    0x31: (0x31, 0),  # DIGIT ONE
    0x32: (0x32, 0),  # DIGIT TWO
    0x33: (0x33, 0),  # DIGIT THREE
    0x34: (0x34, 0),  # DIGIT FOUR
    0x35: (0x35, 0),  # DIGIT FIVE
    0x36: (0x36, 0),  # DIGIT SIX
    0x37: (0x37, 0),  # DIGIT SEVEN
    0x38: (0x38, 0),  # DIGIT EIGHT
    0x39: (0x39, 0),  # DIGIT NINE
    0x3A: (0x3A, 0),  # COLON
    0x3B: (0x3B, 0),  # SEMICOLON
    0x3C: (0x3C, 0),  # LESS-THAN SIGN
    0x3D: (0x3D, 0),  # EQUALS SIGN
    0x3E: (0x3E, 0),  # GREATER-THAN SIGN
    0x3F: (0x3F, 0),  # QUESTION MARK
    0x40: (0x40, 0),  # COMMERCIAL AT
    0x41: (0x41, 0),  # LATIN CAPITAL LETTER A
    0x42: (0x42, 0),  # LATIN CAPITAL LETTER B
    0x43: (0x43, 0),  # LATIN CAPITAL LETTER C
    0x44: (0x44, 0),  # LATIN CAPITAL LETTER D
    0x45: (0x45, 0),  # LATIN CAPITAL LETTER E
    0x46: (0x46, 0),  # LATIN CAPITAL LETTER F
    0x47: (0x47, 0),  # LATIN CAPITAL LETTER G
    0x48: (0x48, 0),  # LATIN CAPITAL LETTER H
    0x49: (0x49, 0),  # LATIN CAPITAL LETTER I
    0x4A: (0x4A, 0),  # LATIN CAPITAL LETTER J
    0x4B: (0x4B, 0),  # LATIN CAPITAL LETTER K
    0x4C: (0x4C, 0),  # LATIN CAPITAL LETTER L
    0x4D: (0x4D, 0),  # LATIN CAPITAL LETTER M
    0x4E: (0x4E, 0),  # LATIN CAPITAL LETTER N
    0x4F: (0x4F, 0),  # LATIN CAPITAL LETTER O
    0x50: (0x50, 0),  # LATIN CAPITAL LETTER P
    0x51: (0x51, 0),  # LATIN CAPITAL LETTER Q
    0x52: (0x52, 0),  # LATIN CAPITAL LETTER R
    0x53: (0x53, 0),  # LATIN CAPITAL LETTER S
    0x54: (0x54, 0),  # LATIN CAPITAL LETTER T
    0x55: (0x55, 0),  # LATIN CAPITAL LETTER U
    0x56: (0x56, 0),  # LATIN CAPITAL LETTER V
    0x57: (0x57, 0),  # LATIN CAPITAL LETTER W
    0x58: (0x58, 0),  # LATIN CAPITAL LETTER X
    0x59: (0x59, 0),  # LATIN CAPITAL LETTER Y
    0x5A: (0x5A, 0),  # LATIN CAPITAL LETTER Z
    0x5B: (0x5B, 0),  # OPENING SQUARE BRACKET / LEFT SQUARE BRACKET
    0x5C: (0x5C, 0),  # REVERSE SLASH / REVERSE SOLIDUS
    0x5D: (0x5D, 0),  # CLOSING SQUARE BRACKET / RIGHT SQUARE BRACKET
    0x5E: (0x5E, 0),  # SPACING CIRCUMFLEX / CIRCUMFLEX ACCENT
    0x5F: (0x5F, 0),  # SPACING UNDERSCORE / LOW LINE
    0x60: (0x60, 0),  # SPACING GRAVE / GRAVE ACCENT
    0x61: (0x61, 0),  # LATIN SMALL LETTER A
    0x62: (0x62, 0),  # LATIN SMALL LETTER B
    0x63: (0x63, 0),  # LATIN SMALL LETTER C
    0x64: (0x64, 0),  # LATIN SMALL LETTER D
    0x65: (0x65, 0),  # LATIN SMALL LETTER E
    0x66: (0x66, 0),  # LATIN SMALL LETTER F
    0x67: (0x67, 0),  # LATIN SMALL LETTER G
    0x68: (0x68, 0),  # LATIN SMALL LETTER H
    0x69: (0x69, 0),  # LATIN SMALL LETTER I
    0x6A: (0x6A, 0),  # LATIN SMALL LETTER J
    0x6B: (0x6B, 0),  # LATIN SMALL LETTER K
    0x6C: (0x6C, 0),  # LATIN SMALL LETTER L
    0x6D: (0x6D, 0),  # LATIN SMALL LETTER M
    0x6E: (0x6E, 0),  # LATIN SMALL LETTER N
    0x6F: (0x6F, 0),  # LATIN SMALL LETTER O
    0x70: (0x70, 0),  # LATIN SMALL LETTER P
    0x71: (0x71, 0),  # LATIN SMALL LETTER Q
    0x72: (0x72, 0),  # LATIN SMALL LETTER R
    0x73: (0x73, 0),  # LATIN SMALL LETTER S
    0x74: (0x74, 0),  # LATIN SMALL LETTER T
    0x75: (0x75, 0),  # LATIN SMALL LETTER U
    0x76: (0x76, 0),  # LATIN SMALL LETTER V
    0x77: (0x77, 0),  # LATIN SMALL LETTER W
    0x78: (0x78, 0),  # LATIN SMALL LETTER X
    0x79: (0x79, 0),  # LATIN SMALL LETTER Y
    0x7A: (0x7A, 0),  # LATIN SMALL LETTER Z
    0x7B: (0x7B, 0),  # OPENING CURLY BRACKET / LEFT CURLY BRACKET
    0x7C: (0x7C, 0),  # VERTICAL BAR (FILL) / VERTICAL LINE
    0x7D: (0x7D, 0),  # CLOSING CURLY BRACKET / RIGHT CURLY BRACKET
    0x7E: (0x7E, 0),  # SPACING TILDE / TILDE
}
CHARSET_62 = {  # Subscripts
    0x28: (0x208D, 0),  # SUBSCRIPT OPENING PARENTHESIS / SUBSCRIPT LEFT PARENTHESIS
    0x29: (0x208E, 0),  # SUBSCRIPT CLOSING PARENTHESIS / SUBSCRIPT RIGHT PARENTHESIS
    0x2B: (0x208A, 0),  # SUBSCRIPT PLUS SIGN
    0x2D: (0x208B, 0),  # SUBSCRIPT HYPHEN-MINUS / SUBSCRIPT MINUS
    0x30: (0x2080, 0),  # SUBSCRIPT DIGIT ZERO
    0x31: (0x2081, 0),  # SUBSCRIPT DIGIT ONE
    0x32: (0x2082, 0),  # SUBSCRIPT DIGIT TWO
    0x33: (0x2083, 0),  # SUBSCRIPT DIGIT THREE
    0x34: (0x2084, 0),  # SUBSCRIPT DIGIT FOUR
    0x35: (0x2085, 0),  # SUBSCRIPT DIGIT FIVE
    0x36: (0x2086, 0),  # SUBSCRIPT DIGIT SIX
    0x37: (0x2087, 0),  # SUBSCRIPT DIGIT SEVEN
    0x38: (0x2088, 0),  # SUBSCRIPT DIGIT EIGHT
    0x39: (0x2089, 0),  # SUBSCRIPT DIGIT NINE
}
CHARSET_67 = {  # Greek Symbols
    0x61: (0x3B1, 0),  # GREEK SMALL LETTER ALPHA
    0x62: (0x3B2, 0),  # GREEK SMALL LETTER BETA
    0x63: (0x3B3, 0),  # GREEK SMALL LETTER GAMMA
}
CHARSET_4E = {  # Basic Cyrillic
    0x21: (0x21, 0),  # EXCLAMATION MARK
    0x22: (0x22, 0),  # QUOTATION MARK
    0x23: (0x23, 0),  # NUMBER SIGN
    0x24: (0x24, 0),  # DOLLAR SIGN
    0x25: (0x25, 0),  # PERCENT SIGN
    0x26: (0x26, 0),  # AMPERSAND
    0x27: (0x27, 0),  # APOSTROPHE
    0x28: (0x28, 0),  # OPENING PARENTHESIS / LEFT PARENTHESIS
    0x29: (0x29, 0),  # CLOSING PARENTHESIS / RIGHT PARENTHESIS
    0x2A: (0x2A, 0),  # ASTERISK
    0x2B: (0x2B, 0),  # PLUS SIGN
    0x2C: (0x2C, 0),  # COMMA
    0x2D: (0x2D, 0),  # HYPHEN-MINUS
    0x2E: (0x2E, 0),  # PERIOD, DECIMAL POINT / FULL STOP
    0x2F: (0x2F, 0),  # SLASH / SOLIDUS
    0x30: (0x30, 0),  # DIGIT ZERO
    0x31: (0x31, 0),  # DIGIT ONE
    0x32: (0x32, 0),  # DIGIT TWO
    0x33: (0x33, 0),  # DIGIT THREE
    0x34: (0x34, 0),  # DIGIT FOUR
    0x35: (0x35, 0),  # DIGIT FIVE
    0x36: (0x36, 0),  # DIGIT SIX
    0x37: (0x37, 0),  # DIGIT SEVEN
    0x38: (0x38, 0),  # DIGIT EIGHT
    0x39: (0x39, 0),  # DIGIT NINE
    0x3A: (0x3A, 0),  # COLON
    0x3B: (0x3B, 0),  # SEMICOLON
    0x3C: (0x3C, 0),  # LESS-THAN SIGN
    0x3D: (0x3D, 0),  # EQUALS SIGN
    0x3E: (0x3E, 0),  # GREATER-THAN SIGN
    0x3F: (0x3F, 0),  # QUESTION MARK
    0x40: (0x44E, 0),  # LOWERCASE IU / CYRILLIC SMALL LETTER YU
    0x41: (0x430, 0),  # CYRILLIC SMALL LETTER A
    0x42: (0x431, 0),  # CYRILLIC SMALL LETTER BE
    0x43: (0x446, 0),  # CYRILLIC SMALL LETTER TSE
    0x44: (0x434, 0),  # CYRILLIC SMALL LETTER DE
    0x45: (0x435, 0),  # CYRILLIC SMALL LETTER IE
    0x46: (0x444, 0),  # CYRILLIC SMALL LETTER EF
    0x47: (0x433, 0),  # LOWERCASE GE / CYRILLIC SMALL LETTER GHE
    0x48: (0x445, 0),  # LOWERCASE KHA / CYRILLIC SMALL LETTER HA
    0x49: (0x438, 0),  # LOWERCASE II / CYRILLIC SMALL LETTER I
    0x4A: (0x439, 0),  # LOWERCASE SHORT II / CYRILLIC SMALL LETTER SHORT I
    0x4B: (0x43A, 0),  # CYRILLIC SMALL LETTER KA
    0x4C: (0x43B, 0),  # CYRILLIC SMALL LETTER EL
    0x4D: (0x43C, 0),  # CYRILLIC SMALL LETTER EM
    0x4E: (0x43D, 0),  # CYRILLIC SMALL LETTER EN
    0x4F: (0x43E, 0),  # CYRILLIC SMALL LETTER O
    0x50: (0x43F, 0),  # CYRILLIC SMALL LETTER PE
    0x51: (0x44F, 0),  # LOWERCASE IA / CYRILLIC SMALL LETTER YA
    0x52: (0x440, 0),  # CYRILLIC SMALL LETTER ER
    0x53: (0x441, 0),  # CYRILLIC SMALL LETTER ES
    0x54: (0x442, 0),  # CYRILLIC SMALL LETTER TE
    0x55: (0x443, 0),  # CYRILLIC SMALL LETTER U
    0x56: (0x436, 0),  # CYRILLIC SMALL LETTER ZHE
    0x57: (0x432, 0),  # CYRILLIC SMALL LETTER VE
    0x58: (0x44C, 0),  # CYRILLIC SMALL LETTER SOFT SIGN
    0x59: (0x44B, 0),  # LOWERCASE YERI / CYRILLIC SMALL LETTER YERI
    0x5A: (0x437, 0),  # CYRILLIC SMALL LETTER ZE
    0x5B: (0x448, 0),  # CYRILLIC SMALL LETTER SHA
    0x5C: (0x44D, 0),  # LOWERCASE REVERSED E / CYRILLIC SMALL LETTER E
    0x5D: (0x449, 0),  # CYRILLIC SMALL LETTER SHCHA
    0x5E: (0x447, 0),  # CYRILLIC SMALL LETTER CHE
    0x5F: (0x44A, 0),  # CYRILLIC SMALL LETTER HARD SIGN
    0x60: (0x42E, 0),  # UPPERCASE IU / CYRILLIC CAPITAL LETTER YU
    0x61: (0x410, 0),  # CYRILLIC CAPITAL LETTER A
    0x62: (0x411, 0),  # CYRILLIC CAPITAL LETTER BE
    0x63: (0x426, 0),  # CYRILLIC CAPITAL LETTER TSE
    0x64: (0x414, 0),  # CYRILLIC CAPITAL LETTER DE
    0x65: (0x415, 0),  # CYRILLIC CAPITAL LETTER IE
    0x66: (0x424, 0),  # CYRILLIC CAPITAL LETTER EF
    0x67: (0x413, 0),  # UPPERCASE GE / CYRILLIC CAPITAL LETTER GHE
    0x68: (0x425, 0),  # UPPERCASE KHA / CYRILLIC CAPITAL LETTER HA
    0x69: (0x418, 0),  # UPPERCASE II / CYRILLIC CAPITAL LETTER I
    0x6A: (0x419, 0),  # UPPERCASE SHORT II / CYRILLIC CAPITAL LETTER SHORT I
    0x6B: (0x41A, 0),  # CYRILLIC CAPITAL LETTER KA
    0x6C: (0x41B, 0),  # CYRILLIC CAPITAL LETTER EL
    0x6D: (0x41C, 0),  # CYRILLIC CAPITAL LETTER EM
    0x6E: (0x41D, 0),  # CYRILLIC CAPITAL LETTER EN
    0x6F: (0x41E, 0),  # CYRILLIC CAPITAL LETTER O
    0x70: (0x41F, 0),  # CYRILLIC CAPITAL LETTER PE
    0x71: (0x42F, 0),  # UPPERCASE IA / CYRILLIC CAPITAL LETTER YA
    0x72: (0x420, 0),  # CYRILLIC CAPITAL LETTER ER
    0x73: (0x421, 0),  # CYRILLIC CAPITAL LETTER ES
    0x74: (0x422, 0),  # CYRILLIC CAPITAL LETTER TE
    0x75: (0x423, 0),  # CYRILLIC CAPITAL LETTER U
    0x76: (0x416, 0),  # CYRILLIC CAPITAL LETTER ZHE
    0x77: (0x412, 0),  # CYRILLIC CAPITAL LETTER VE
    0x78: (0x42C, 0),  # CYRILLIC CAPITAL LETTER SOFT SIGN
    0x79: (0x42B, 0),  # UPPERCASE YERI / CYRILLIC CAPITAL LETTER YERI
    0x7A: (0x417, 0),  # CYRILLIC CAPITAL LETTER ZE
    0x7B: (0x428, 0),  # CYRILLIC CAPITAL LETTER SHA
    0x7C: (0x42D, 0),  # CYRILLIC CAPITAL LETTER E
    0x7D: (0x429, 0),  # CYRILLIC CAPITAL LETTER SHCHA
    0x7E: (0x427, 0),  # CYRILLIC CAPITAL LETTER CHE
}
CODESETS = {
    0x34: CHARSET_34,
    0x45: CHARSET_45,
    0x33: CHARSET_33,
    0x32: CHARSET_32,
    0x31: CHARSET_31,
    0x70: CHARSET_70,
    0x51: CHARSET_51,
    0x53: CHARSET_53,
    0x42: CHARSET_42,
    0x62: CHARSET_62,
    0x67: CHARSET_67,
    0x4E: CHARSET_4E,
}

# ODD_MAP for odd characters (all from III for now)
ODD_MAP = {
    0x21203D: 0x2026,  # HORIZONTAL ELLIPSIS
    0x212040: 0x201C,  # LEFT DOUBLE QUOTATION MARK
    0x7F2014: 0x2014,  # EM DASH
    0x7F2019: 0x2019,  # RIGHT SINGLE QUOTATION MARK
    0x7F2020: 0x201D,  # RIGHT DOUBLE QUOTATION MARK
    0x7F2122: 0x2122,  # TRADE MARK SIGN
}
