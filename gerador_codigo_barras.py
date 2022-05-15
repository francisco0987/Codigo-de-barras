from barcode import EAN13
from barcode.writer import ImageWriter

codigo_barra = EAN13('551745511111', writer=ImageWriter())
codigo_barra.save('codigo-barra')
