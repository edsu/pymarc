```
_|_|_|    _|    _|  _|_|_|  _|_|      _|_|_|  _|  _|_|    _|_|_|
_|    _|  _|    _|  _|    _|    _|  _|    _|  _|_|      _|
_|    _|  _|    _|  _|    _|    _|  _|    _|  _|        _|
_|_|_|      _|_|_|  _|    _|    _|    _|_|_|  _|          _|_|_|
_|              _|
_|          _|_|
```

[![Build Status](https://travis-ci.org/edsu/pymarc.svg)](http://travis-ci.org/edsu/pymarc)

pymarc é uma biblioteca de python para trabalhar com dados bibliográficos codificaos
[MARC21](https://en.wikipedia.org/wiki/MARC_standards). Isto deve funcionar no python 2.x e 3.x. Fornece uma API para a leitura, escrita e modificação de registros MARC. Ela foi projetada principalmente para ser uma medida de emergência na obtenção dos dados ativos do MARC em outra representação mais segura. Porém, ao longo dos anos, foi utilizado para criar e modificar registros MARC, uma vez que apesar de [diversas chamadas](https://web.archive.org/web/20170731163019/http://www.marc-must-die.info/index.php/Main_Page) para que ele moorra como um formato, MARC parece estar vivendo muito feliz como um zumbi.

Abaixo estão alguns exemplos comuns de como você pode querer usar o pymarc. E se você se deparar com um exemplo que  acha que deveria estar por aqui, por facor envie uma pull request.

### Instalação

Você provavelmente vai querer usar o pip para instalar o pymarc:

    pip install pymarc

Se você quiser baixar e instalar a versão mais recente, precisará do git:

    git clone git://github.com/edsu/pymarc.git

Você também vai precisar do [setuptools](https://pypi.python.org/pypi/setuptools#installation-instructions). Após ter a fonte e o setuptools, execute o pymarc test suite para garantirque as tudo está em ordem com a distribuição:

    python setup.py test

E então instale:

    python setup.py install

### Leitura

Na maioria das vezes, você terá alguns dados MARC e desejará extrair dados a partir dele. Aqui está um exemplo de leitura de um lote de registros e print do título. Se estiver curioso, este exemplo usa o arquivo de lote disponível aqui no repositório pymarc:

```python
from pymarc import MARCReader
with open('test/marc.dat', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.title())
```
```
The pragmatic programmer : from journeyman to master /
Programming Python /
Learning Python /
Python cookbook /
Python programming for the absolute beginner /
Web programming : techniques for integrating Python, Linux, Apache, and MySQL /
Python programming on Win32 /
Python programming : an introduction to computer science /
Python Web programming /
Core python programming /
Python and Tkinter programming /
Game programming with Python, Lua, and Ruby /
Python programming patterns /
Python programming with the Java class libraries : a tutorial for building Web
and Enterprise applications /
Learn to program using Python : a tutorial for hobbyists, self-starters, and all
who want to learn the art of computer programming /
Programming with Python /
BSD Sockets programming from a multi-language perspective /
Design patterns : elements of reusable object-oriented software /
Introduction to algorithms /
ANSI Common Lisp /
```

Um objeto `pymarc.Record` tem alguns métodos úteis como `title` para obter o título de um registro bibliográfico, outros inclusos:`author`, `isbn`, `subjects`, `location`, `notes`, `physicaldescription`, `publisher`, `pubyear`. Mas realmente, para trabalhar com dados MARC você precisa enteder as tags de campo numérico e os códigos de subcampo que são usados para designar vários bits de informação. Há muito mais escondido em um registro MARC do que esses métodos fornecem acesso. Por exemplo, o método `title` extrai as informações do campo `245`, subcampos `a` e `b`. Você pode acessar o campo `245a`assim:

```python
print(record['245']['a'])
```

Alguns campos, como assuntos, podem se repetir. Em casos como este, vocẽ vai querer usar `get_fields` para obter todos eles commo objetos `pymarc.Field`, que então você pode interagir mais:

```python
for f in record.get_fields('650'):
    print(f)
```

Se você é novo nos campos MARC  [Understanding MARC](http://www.loc.gov/marc/umb/) é um bom começo, e a paǵina [MARC 21 Formats](http://www.loc.gov/marc/marcdocz.html) na Biblioteca do Congresso é uma boa referência, uma vez que você entende o básico.

### Escrita

Aqui está um exemplo de como criar um registro, e escrevê-lo em um arquivo.

```python
from pymarc import Record, Field
record = Record()
record.add_field(
    Field(
        tag = '245',
        indicators = ['0','1'],
        subfields = [
            'a', 'The pragmatic programmer : ',
            'b', 'from journeyman to master /',
            'c', 'Andrew Hunt, David Thomas.'
        ]))
with open('file.dat', 'wb') as out:
    out.write(record.as_marc())
```

### Atualização

A atualização funciona da mesma forma, você lê, modifica e então escreve novamente.

```python
from pymarc import MARCReader
with open('test/marc.dat', 'rb') as fh:
    reader = MARCReader(fh)
    record = next(reader)
    record['245']['a'] = 'The Zombie Programmer'
with open('file.dat', 'wb') as out:
    out.write(record.as_marc())
```


### JSON e XML

Se você estiver usando os dados do MARC pouco e distribuindo-s, poderá deixar outros desenvolvedores um pouco felizes usando as serializações JSON ou XML. O benefício em usar XML ou JSON é que a codificação de caracteres UTF8 é usada, ao invés da codificação MARC8 frustrantemente arcaica. Eles também poderão usar ferramentas de leitura/gravação pdrão JSON e XML para obter os dados desejdos, em vez de alguma biblioteca de processamento MARC, como pymarc.

O suporte pymarc para JSON e XML é atualmente um pouco desequilibrado e ad hoc. Pymarc permite que você leia XML de várias maneiras, mas não o escreva. Por outro lado, pymarc permite que você escreva JSON, mas não o leia. Parte da razão para esse desalinhamento é que a funcionalidade foi adicionada para resolver uma necessidade particular em um tempo particular. Se estiver interessado em fornecer uma solução mais holística, as PRs (com testes de unidade) são bem vindos.

**XML**

Para o parse de um arquivo de registros você pode:

```python

from pymarc import parse_xml_to_array

records = parse_xml_to_array('test/batch.xml')
```

Se você tem um arquivo XML grande e prefere não lê-lo todo em memória, você pode:

```python

from pymarc import map_xml

def print_title(r):
    print(r.title())

map_xml(print_title, 'test/batch.xml')
```

Além disso, se preferir, pode passar um arquivo como objeto, além do caminho para *map_xml* e *parse_xml_to_array*:

```python
records = parse_xml_to_array(open('test/batch.xml'))
```

**JSON**

O suporte para JSON é razoavelmente mínimo, em que você poode chamar o método `pymarc.Record.as_json()` para retornar o JSON para um determinado registro MARC.

```python
from pymarc import MARCReader

with open('test/one.dat','rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.as_json(indent=2))
```

```javascript
{
  "leader": "01060cam  22002894a 4500",
  "fields": [
    {
      "001": "11778504"
    }, 
    {
      "010": {
        "ind1": " ", 
        "subfields": [
          {
            "a": "   99043581 "
          }
        ], 
        "ind2": " "
      }
    }, 
    {
      "100": {
        "ind1": "1", 
        "subfields": [
          {
            "a": "Hunt, Andrew,"
          }, 
          {
            "d": "1964-"
          }
        ], 
        "ind2": " "
      }
    }, 
    {
      "245": {
        "ind1": "1", 
        "subfields": [
          {
            "a": "The pragmatic programmer :"
          }, 
          {
            "b": "from journeyman to master /"
          }, 
          {
            "c": "Andrew Hunt, David Thomas."
          }
        ], 
        "ind2": "4"
      }
    }, 
    {
      "260": {
        "ind1": " ", 
        "subfields": [
          {
            "a": "Reading, Mass :"
          }, 
          {
            "b": "Addison-Wesley,"
          }, 
          {
            "c": "2000."
          }
        ], 
        "ind2": " "
      }
    }, 
    {
      "300": {
        "ind1": " ", 
        "subfields": [
          {
            "a": "xxiv, 321 p. ;"
          }, 
          {
            "c": "24 cm."
          }
        ], 
        "ind2": " "
      }
    }, 
    {
      "504": {
        "ind1": " ", 
        "subfields": [
          {
            "a": "Includes bibliographical references."
          }
        ], 
        "ind2": " "
      }
    }, 
    {
      "650": {
        "ind1": " ", 
        "subfields": [
          {
            "a": "Computer programming."
          }
        ], 
        "ind2": "0"
      }
    }, 
    {
      "700": {
        "ind1": "1", 
        "subfields": [
          {
            "a": "Thomas, David,"
          }, 
          {
            "d": "1956-"
          }
        ], 
        "ind2": " "
      }
    }
  ]
}
```

Se você deseja analisar um arquivo de registros MARCJSON, você pode:

```python
from pymarc import parse_json_to_array

records = parse_json_to_array(open('test/batch.json'))

print(records[0])
```

```
=LDR  00925njm  22002777a 4500
=001  5637241
=003  DLC
=005  19920826084036.0
=007  sdubumennmplu
=008  910926s1957\\\\nyuuun\\\\\\\\\\\\\\eng\\
=010  \\$a   91758335 
=028  00$a1259$bAtlantic
=040  \\$aDLC$cDLC
=050  00$aAtlantic 1259
=245  04$aThe Great Ray Charles$h[sound recording].
=260  \\$aNew York, N.Y. :$bAtlantic,$c[1957?]
=300  \\$a1 sound disc :$banalog, 33 1/3 rpm ;$c12 in.
=511  0\$aRay Charles, piano & celeste.
=505  0\$aThe Ray -- My melancholy baby -- Black coffee -- There's no you -- Doodlin' -- Sweet sixteen bars -- I surrender dear -- Undecided.
=500  \\$aBrief record.
=650  \0$aJazz$y1951-1960.
=650  \0$aPiano with jazz ensemble.
=700  1\$aCharles, Ray,$d1930-$4prf
```

Suporte
-------

Os desenvolvedores pymarc incentivam você a participar do [pymarc Google Group](http://groups.google.com/group/pymarc) se precisar de ajuda.  Além disso, sinte-se à vontade para usar o [issue tracking](https://github.com/edsu/pymarc/issues) no Github para submeter novos recursos ou relatórios de bugs. Se você tiver um comichão, copie-a e envie PRs no [Github](http://github.com/edsu/pymarc).

Se você iniciou a trabalhar com MARC, pode sentir que precisa de apoio moral além de técnico. O canal [#code4lib](irc://freenode.net/code4lib) em [Freenode](http://freenode.net) é um bom lugar para ambos.

