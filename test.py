import pymarc

r = pymarc.MARCReader(file('trouble1251.dat'), file_encoding='cp1251')
for x in r:
    print x
