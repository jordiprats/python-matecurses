from random import randrange
from fpdf import FPDF
from math import gcd

import random
import click

@click.group()
def matecursa():
  pass

#
# sumes
#

@click.command()
@click.option('--file', default='sumes.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def sumes(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    if disable_total_operacions:
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min, max)
          if min_segona_unitat:
            min_segon_numero=min_segona_unitat
          else:
            min_segon_numero=min
          if max_segona_unitat:
            max_segon_numero=max_segona_unitat
          else:
            max_segon_numero=max
          segon_numero = randrange(min_segon_numero, max_segon_numero)
          operacio = str(primer_numero*multiplicador)+' + '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')


#
# enters (sumes i restes tipus -2 + 12)
#

@click.command()
@click.option('--file', default='enters_sumes_restes.pdf', help='output file')
@click.option('--pages', default=20, help='number of pages')
@click.option('--min', default=-20, help='min int')
@click.option('--max', default=20, help='max int')
def enters_sumes_restes(file, pages, min, max):
  pdf = FPDF(orientation='P', unit='mm', format='A4')

  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )

    pdf.set_font('helvetica', '', 15.0)

    anterior_operacio = ''
    operacio = ''

    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5 + (linea*17))

        while anterior_operacio == operacio:
          a = randrange(min, max)
          b = randrange(min, max)

          operador = random.choice(['+', '-'])

          # format amb parèntesis si és negatiu
          def fmt(n):
            return f"({n})" if n < 0 else str(n)

          operacio = f"{fmt(a)} {operador} {fmt(b)} ="

        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio

  pdf.output(file,'F')

@click.command()
@click.option('--file', default='sumes_hortizontal.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min1', default=100, help='min int')
@click.option('--max1', default=900, help='max int')
@click.option('--min2', default=100, help='min int')
@click.option('--max2', default=300, help='max int')
@click.option('--min3', default=10, help='min int')
@click.option('--max3', default=100, help='max int')
@click.option('--disable-marge-calculs', is_flag=True, default=False, help='deixa marge per calcul')
def sumes_horitzontal(file, pages, min1, max1, min2, max2, min3, max3, disable_marge_calculs):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 18.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 2):
      if disable_marge_calculs:
        range_files = range(0,4)
      else:
        range_files = range(0,11)
      for linea in range_files:
        if disable_marge_calculs:
          pdf.set_xy(10.0 + (columna*100), 32.5+ (linea*22*3))
        else:
          pdf.set_xy(10.0 + (columna*100), 40 + (linea*20))
        while anterior_operacio == operacio:
          print('range: '+str(min1)+'-'+str(max1))
          primer_numero = randrange(min1, max1)
          segon_numero = randrange(min2, max2)
          tercer_numero = randrange(min3, max3)
          operacio = str(primer_numero)+' + '+str(segon_numero)+' + '+str(tercer_numero)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
  pdf.output(file,'F')

#
# restes
#

@click.command()
@click.option('--file', default='restes.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min', default=1, help='max int')
@click.option('--max', default=5, help='max int')
@click.option('--multiplicador', default=1, help='multiplicador')
def restes(file, pages, min, max, multiplicador):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 25.0)
    pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min+1, max)
          if min==primer_numero:
            segon_numero = min
          else:
            segon_numero = randrange(min, primer_numero)
          operacio = str(primer_numero*multiplicador)+' - '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='restes_vertical.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min', default=100, help='max int')
@click.option('--max', default=999, help='max int')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def restes_vertical(file, pages, min, max, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    if not disable_total_operacions:
      pdf.set_xy(5.0, 276)
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 3):
      for linea in range(0,5):
        primer_numero = randrange(int(max/4), max)
        segon_numero = randrange(min, primer_numero)
        pdf.set_xy(30.0 + (columna*65), 47.5+ (((linea*2)-0.4)*25))
        pdf.cell(w=0,h=0, txt=str(primer_numero), ln=0 )
        pdf.set_xy(30.0 + ((columna*65)-5), 47.5+ ((linea*2)*25))
        pdf.set_font('helvetica', '', 30.0)
        pdf.cell(w=0,h=0, txt="-", ln=0 )
        pdf.set_font('helvetica', '', 20.0)
        pdf.set_xy(30.0 + (columna*65), 47.5+ ((linea*2)*25))
        pdf.cell(w=0,h=0, txt=str(segon_numero), ln=0 )
        pdf.set_line_width(0.5)
        pdf.line(
              20.0 + (columna*65), 52.5+ ((linea*2)*25), 
              45.0 + (columna*65), 52.5+ ((linea*2)*25)
            )
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

#
# multiplicacions
#

@click.command()
@click.option('--file', default='multiplicacions.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
@click.option('--disable-total-operacions', is_flag=True, default=False, help='Elimina missatge de total de operacions')
def multiplicacions(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    if not disable_total_operacions:
      pdf.set_xy(5.0, 276)
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min, max)
          if min_segona_unitat:
            min_segon_numero=min_segona_unitat
          else:
            min_segon_numero=min
          if max_segona_unitat:
            max_segon_numero=max_segona_unitat
          else:
            max_segon_numero=max
          segon_numero = randrange(min_segon_numero, max_segon_numero)
          operacio = str(primer_numero*multiplicador)+' x '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='taules_multiplicar.pdf', help='output file')
@click.option('--min', default=2, help='min int')
@click.option('--max', default=30, help='max int')
def taules_multiplicar(file, min, max):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(min, int((max/2))):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 20.0)
    for columna in range(0, 2):
      for linea in range(1,11):
        pdf.set_xy(10.0 + (columna*100), 40.5+ (linea*17))
        pdf.cell(w=0,h=0, txt=str(linea)+' x '+str(((pagina*2))+columna)+' = ', ln=0 )
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='multiplicacions_vertical.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min-factor1', default=1000, help='max int')
@click.option('--max-factor1', default=9999, help='max int')
@click.option('--min-factor2', default=10, help='max int')
@click.option('--max-factor2', default=99, help='max int')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def multiplicacions_vertical(file, pages, min_factor1, max_factor1, min_factor2, max_factor2, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    if not disable_total_operacions:
      pdf.set_xy(5.0, 276)
      pdf.set_font('Courier', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('Courier', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 3):
      for linea in range(0,4):
        primer_numero = randrange(int(min_factor1), max_factor1)
        segon_numero = randrange(int(min_factor2), max_factor2)
        pdf.set_xy(27.0 + (columna*65), 47.5+ (((linea*2.5)-0.4)*25))
        pdf.cell(w=0,h=0, txt=str(primer_numero), ln=0 )
        pdf.set_xy(25.0 + ((columna*65)-5), 47.5+ ((linea*2.5)*25))
        pdf.set_font('helvetica', '', 15.0)
        pdf.cell(w=0,h=0, txt="x", ln=0 )
        pdf.set_font('Courier', '', 20.0)
        pdf.set_xy(27.0 + (columna*65), 47.5+ ((linea*2.5)*25))
        pdf.cell(w=0,h=0, txt="  "+str(segon_numero), ln=0 )
        pdf.set_line_width(0.5)
        pdf.line(
              20.0 + (columna*65), 52.5+ ((linea*2.5)*25), 
              45.0 + (columna*65), 52.5+ ((linea*2.5)*25)
            )
  pdf.output(file,'F')

#
# divisions
#

@click.command()
@click.option('--file', default='divisions_hortizontal.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min-dividend', default=1000, help='min dividend')
@click.option('--max-dividend', default=9999, help='max dividend')
@click.option('--min-divisor', default=2, help='min divisor')
@click.option('--max-divisor', default=9, help='max divisor')
@click.option('--disable-marge-calculs', is_flag=True, default=True, help='deixa marge per calcul')
def divisions(file, pages, min_dividend, max_dividend, min_divisor, max_divisor, disable_marge_calculs):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 18.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 2):
      if disable_marge_calculs:
        range_files = range(0,4)
      else:
        range_files = range(0,11)
      for linea in range_files:
        if disable_marge_calculs:
          pdf.set_xy(10.0 + (columna*100), 32.5+ (linea*22*3))
        else:
          pdf.set_xy(10.0 + (columna*100), 40 + (linea*20))
        while anterior_operacio == operacio:
          dividend = randrange(min_dividend, max_dividend)
          divisor = randrange(min_divisor, max_divisor)
          if disable_marge_calculs:
            operacio = str(dividend)+'   '+str(divisor)
            pdf.cell(w=0,h=0, txt=operacio, ln=0 )
            pdf.set_line_width(0.5)
            pdf.line(
                  29.0 + (columna*100), 37 + (linea*22*3), 
                  45.0 + (columna*100), 37 + (linea*22*3)
                )
            pdf.line(
                  29.0 + (columna*100), 37 + (linea*22*3), 
                  29.0 + (columna*100), 28 + (linea*22*3)
                )
          else:
            operacio = str(dividend)+' / '+str(divisor)
            pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
  pdf.output(file,'F')


#
# fraccions (1r ESO)
#
# Tipus d'operacions:
#   - simplificació de fraccions
#   - comparació de fraccions (>, <)
#   - suma i resta de fraccions (denominador comú i diferent)
#   - multiplicació i divisió de fraccions
#   - fracció d'un nombre enter
#   - mix de totes
#

# ─────────────────────────────────────────────────────────────
#  FRACCIONS  (1r ESO)
#  Estil Col·legi Lestonnac:
#    1. Operacions combinades (·, :, +, –, parèntesis)
#    2. Simplificació fins a irreductible
#    3. Fracció d'un enter
#    4. Fracció de fracció d'un enter
# ─────────────────────────────────────────────────────────────

def _gcd(a, b):
  a, b = abs(a), abs(b)
  while b:
    a, b = b, a % b
  return a

def _lcm(a, b):
  return abs(a * b) // _gcd(a, b)

# ── Constants de dibuix ───────────────────────────────────────
# y_mid és el centre de la línia de fracció
# El numerador es col·loca N_OFF mm per sobre, el denominador D_OFF mm per sota

FONT_F   = 11    # mida font fracció (num/den)
FONT_OP  = 12    # mida font operadors, enters i parèntesis

FRAC_W   = 10.0  # amplada caixa fracció (mm)
N_OFF    = 5.5   # distància de y_mid al top del numerador (mm)
D_OFF    = 1.0   # distància de y_mid al top del denominador (mm)
FRAC_H   = 4.5   # alçada de la cell del num/den (prou per FONT_F=11)

OP_W     = 6.0   # amplada operador 1 caràcter
DE_W     = 8.0   # amplada "de"
PAR_W    = 4.0   # amplada parèntesi
ENTER_W  = 9.0   # amplada nombre enter

GAP      = 2.0   # espai extra entre elements


def _draw_frac(pdf, x, y_mid, num, den):
  """Dibuixa num/den centrat verticalment a y_mid. Retorna x final."""
  pdf.set_font('helvetica', '', FONT_F)
  # numerador
  pdf.set_xy(x, y_mid - N_OFF)
  pdf.cell(FRAC_W, FRAC_H, str(num), align='C', ln=0)
  # línia de fracció
  pdf.set_line_width(0.35)
  pdf.line(x + 0.8, y_mid, x + FRAC_W - 0.8, y_mid)
  # denominador
  pdf.set_xy(x, y_mid + D_OFF)
  pdf.cell(FRAC_W, FRAC_H, str(den), align='C', ln=0)
  return x + FRAC_W


def _draw_op(pdf, x, y_mid, op_txt):
  """Dibuixa un operador/text alineat verticalment al centre. Retorna x final."""
  pdf.set_font('helvetica', '', FONT_OP)
  w = DE_W if len(op_txt) > 1 else OP_W
  # centrar verticalment: cell height = FONT_OP * 0.35mm ≈ alçada lletra
  h = FONT_OP * 0.35
  pdf.set_xy(x, y_mid - h / 2)
  pdf.cell(w, h, op_txt, align='C', ln=0)
  return x + w


def _draw_enter(pdf, x, y_mid, n):
  """Dibuixa un nombre enter alineat al centre. Retorna x final."""
  s = str(n)
  w = max(ENTER_W, len(s) * 3.8)
  pdf.set_font('helvetica', '', FONT_OP)
  h = FONT_OP * 0.35
  pdf.set_xy(x, y_mid - h / 2)
  pdf.cell(w, h, s, align='C', ln=0)
  return x + w


def _draw_par(pdf, x, y_mid, s):
  """Dibuixa un parèntesi. Retorna x final."""
  pdf.set_font('helvetica', '', FONT_OP + 3)
  h = (FONT_OP + 3) * 0.35
  pdf.set_xy(x, y_mid - h)
  pdf.cell(PAR_W, h * 2, s, align='C', ln=0)
  return x + PAR_W


def _gap(x, mm=GAP):
  return x + mm

# ── Generadors d'operacions ───────────────────────────────────

DENS_PETITS = [2, 3, 4, 5, 6, 8]

def _frac():
  d = random.choice(DENS_PETITS)
  n = randrange(1, d)
  return n, d


def gen_operacio_combinada():
  """
  Genera una llista de tokens que representa una operació combinada
  de 3–5 fraccions amb operadors ·, :, +, – i parèntesis opcionals.
  Cada token és un dict:
    {'type': 'frac', 'n': ..., 'd': ...}
    {'type': 'op',   'val': '+'/'-'/'·'/':'}
    {'type': 'par',  'val': '('/')'}
    {'type': 'eq'}
  """
  # Escollim un patró
  patrons = [
    # a · b + c : d
    lambda: [F(), OP('·'), F(), OP('+'), F(), OP(':'), F()],
    # a – b · c + d
    lambda: [F(), OP('-'), F(), OP('·'), F(), OP('+'), F()],
    # (a + b) · c – d
    lambda: [PAR('('), F(), OP('+'), F(), PAR(')'), OP('·'), F(), OP('-'), F()],
    # a + (b – c) · d
    lambda: [F(), OP('+'), PAR('('), F(), OP('-'), F(), PAR(')'), OP('·'), F()],
    # (a + b) : (c – d)   — evitem d>c
    lambda: _patro_par_div(),
    # a · b – c · d
    lambda: [F(), OP('·'), F(), OP('-'), F(), OP('·'), F()],
    # a + b – c + d – e
    lambda: [F(), OP('+'), F(), OP('-'), F(), OP('+'), F(), OP('-'), F()],
    # (a + b) · (c + d)
    lambda: [PAR('('), F(), OP('+'), F(), PAR(')'), OP('·'), PAR('('), F(), OP('+'), F(), PAR(')')],
  ]
  tokens = random.choice(patrons)()
  tokens.append({'type': 'eq'})
  return tokens


def _patro_par_div():
  a, b, c, d = _frac(), _frac(), _frac(), _frac()
  # assegurem que no hi hagi fracció impossible (denominador ≠ 0 sempre ok)
  return [PAR('('), {'type':'frac','n':a[0],'d':a[1]}, OP('+'),
          {'type':'frac','n':b[0],'d':b[1]}, PAR(')'), OP(':'),
          PAR('('), {'type':'frac','n':c[0],'d':c[1]}, OP('-'),
          {'type':'frac','n':d[0],'d':d[1]}, PAR(')')]

def F():
  n, d = _frac()
  return {'type': 'frac', 'n': n, 'd': d}

def OP(v):
  return {'type': 'op', 'val': v}

def PAR(v):
  return {'type': 'par', 'val': v}


def _draw_tokens(pdf, tokens, x, y_mid):
  """Dibuixa la llista de tokens a partir de (x, y_mid). Retorna x final."""
  for tok in tokens:
    x = _gap(x, 1)
    t = tok['type']
    if t == 'frac':
      x = _draw_frac(pdf, x, y_mid, tok['n'], tok['d'])
    elif t == 'op':
      x = _gap(x, 1)
      x = _draw_op(pdf, x, y_mid, tok['val'])
    elif t == 'par':
      x = _draw_par(pdf, x, y_mid, tok['val'])
    elif t == 'eq':
      x = _gap(x, 1)
      x = _draw_op(pdf, x, y_mid, '=')
    x = _gap(x, 1)
  return x


def _token_width(tokens):
  """Estimació amplada en mm d'una llista de tokens."""
  w = 0
  for tok in tokens:
    t = tok['type']
    if t == 'frac':   w += FRAC_W + GAP * 2
    elif t == 'op':   w += OP_W + GAP * 2
    elif t == 'par':  w += PAR_W + 1
    elif t == 'eq':   w += OP_W + GAP * 2
  return w


# ── Seccions del full ─────────────────────────────────────────

def _seccio_operacions_combinades(pdf, y0, n_ex=14):
  """Dibuixa n_ex operacions combinades. Retorna y final."""
  pdf.set_font('helvetica', 'B', 11)
  pdf.set_xy(10, y0)
  pdf.cell(0, 0, '1.  Realitza les seg\u00fcents operacions combinades:', ln=0)
  y = y0 + 7
  lletres = 'abcdefghijklmnopqrstuvwxyz'
  pas = 18  # mm entre exercicis — prou per num+linia+den

  for i in range(n_ex):
    tokens = gen_operacio_combinada()
    for _ in range(8):
      if _token_width(tokens) < 168:
        break
      tokens = gen_operacio_combinada()

    y_mid = y + 7   # centre de la línia de fracció dins cada fila
    pdf.set_font('helvetica', '', FONT_OP)
    pdf.set_xy(10, y_mid - 2)
    pdf.cell(8, 0, f'{lletres[i]}.', ln=0)
    _draw_tokens(pdf, tokens, 19, y_mid)
    y += pas

  return y


def _seccio_simplificacio(pdf, y0, n_ex=9):
  """Simplifica fraccions grans. 3 columnes. Retorna y final."""
  pdf.set_font('helvetica', 'B', 11)
  pdf.set_xy(10, y0)
  pdf.cell(0, 0, '2.  Simplifica aquestes fraccions fins a la irreductible:', ln=0)
  y0 += 8

  def gen_simp():
    n_base = randrange(1, 40)
    d_base = randrange(n_base + 1, n_base + 50)
    factor = random.choice([2, 3, 4, 5, 6, 10, 20, 25])
    return n_base * factor, d_base * factor

  lletres = 'abcdefghi'
  cols = 3
  files = (n_ex + cols - 1) // cols
  col_w = 65
  pas_y = 18  # espai entre files

  for fila in range(files):
    for col in range(cols):
      idx = col * files + fila
      if idx >= n_ex:
        continue
      n, d = gen_simp()
      x = 14 + col * col_w
      y_mid = y0 + fila * pas_y + 7
      # lletra
      pdf.set_font('helvetica', '', FONT_OP)
      pdf.set_xy(x - 8, y_mid - 2)
      pdf.cell(7, 0, f'{lletres[idx]}.', ln=0, align='R')
      # fracció
      xf = _draw_frac(pdf, x, y_mid, n, d)
      xf = _gap(xf, 3)
      _draw_op(pdf, xf, y_mid, '=')

  return y0 + files * pas_y + 2


def _seccio_fraccio_enter(pdf, y0, n_ex=6):
  """Fracció d'un enter. 2 columnes. Retorna y final."""
  pdf.set_font('helvetica', 'B', 11)
  pdf.set_xy(10, y0)
  pdf.cell(0, 0, '3.  Calcula:', ln=0)
  y0 += 8

  lletres = 'abcdef'
  cols = 2
  files = (n_ex + 1) // 2
  col_w = 97
  pas_y = 17

  for i in range(n_ex):
    col = i % cols
    fila = i // cols
    d = random.choice(DENS_PETITS)
    n = randrange(1, d)
    multiplo = randrange(1, 8)
    enter = d * multiplo

    x = 14 + col * col_w
    y_mid = y0 + fila * pas_y + 7
    pdf.set_font('helvetica', '', FONT_OP)
    pdf.set_xy(x - 8, y_mid - 2)
    pdf.cell(7, 0, f'{lletres[i]}.', ln=0, align='R')
    xf = _draw_frac(pdf, x, y_mid, n, d)
    xf = _gap(xf, 3)
    xf = _draw_op(pdf, xf, y_mid, 'de')
    xf = _gap(xf, 3)
    xf = _draw_enter(pdf, xf, y_mid, enter)
    xf = _gap(xf, 3)
    _draw_op(pdf, xf, y_mid, '=')

  return y0 + files * pas_y + 2


def _seccio_fraccio_de_fraccio(pdf, y0, n_ex=6):
  """Fracció de fracció d'un enter. 2 columnes. Retorna y final."""
  pdf.set_font('helvetica', 'B', 11)
  pdf.set_xy(10, y0)
  pdf.cell(0, 0, '4.  Calcula:', ln=0)
  y0 += 8

  lletres = 'abcdef'
  cols = 2
  files = (n_ex + 1) // 2
  col_w = 97
  pas_y = 17

  for i in range(n_ex):
    col = i % cols
    fila = i // cols
    d1 = random.choice(DENS_PETITS)
    n1 = randrange(1, d1)
    d2 = random.choice(DENS_PETITS)
    n2 = randrange(1, d2)
    multiplo = randrange(1, 5)
    enter = d1 * d2 * multiplo

    x = 14 + col * col_w
    y_mid = y0 + fila * pas_y + 7
    pdf.set_font('helvetica', '', FONT_OP)
    pdf.set_xy(x - 8, y_mid - 2)
    pdf.cell(7, 0, f'{lletres[i]}.', ln=0, align='R')
    xf = _draw_frac(pdf, x, y_mid, n1, d1)
    xf = _gap(xf, 3)
    xf = _draw_op(pdf, xf, y_mid, 'de')
    xf = _gap(xf, 3)
    xf = _draw_frac(pdf, xf, y_mid, n2, d2)
    xf = _gap(xf, 3)
    xf = _draw_op(pdf, xf, y_mid, 'de')
    xf = _gap(xf, 3)
    xf = _draw_enter(pdf, xf, y_mid, enter)
    xf = _gap(xf, 3)
    _draw_op(pdf, xf, y_mid, '=')

  return y0 + files * pas_y + 2


# ── Comandament principal ─────────────────────────────────────

@click.command()
@click.option('--file', default='fraccions.pdf', help='fitxer de sortida')
@click.option('--pages', default=5, help='nombre de fulls')
@click.option('--mode',
              type=click.Choice(['combinades', 'simplificacio',
                                 'fraccio_enter', 'fraccio_de_fraccio', 'mix']),
              default='mix',
              help='Tipus: combinades | simplificacio | fraccio_enter | fraccio_de_fraccio | mix')
def fraccions(file, pages, mode):
  """
  Genera fulls d'exercicis de fraccions estil 1r ESO (Col·legi Lestonnac).

  Modes:
    mix              - Les 4 seccions en un sol full (per defecte)
    combinades       - Només operacions combinades (·, :, +, –, parèntesis)
    simplificacio    - Simplifica fraccions grans fins a la irreductible
    fraccio_enter    - Fracció d'un nombre enter
    fraccio_de_fraccio - Fracció de fracció d'un enter

  Exemples:
    python matecursa.py fraccions
    python matecursa.py fraccions --mode combinades --pages 3
    python matecursa.py fraccions --mode mix --pages 5 --file fraccions.pdf
  """
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  pdf.set_auto_page_break(False)

  for pagina in range(pages):
    pdf.add_page()

    # ── Capçalera ──
    pdf.set_font('helvetica', '', 13)
    pdf.set_xy(5, 10)
    pdf.cell(0, 0, 'Nom: ............................................................... Data: .......................')

    pdf.set_line_width(0.4)
    pdf.line(5, 18, 205, 18)

    y = 22

    # ── Contingut segons mode ──
    if mode == 'combinades':
      _seccio_operacions_combinades(pdf, y, n_ex=14)

    elif mode == 'simplificacio':
      _seccio_simplificacio(pdf, y, n_ex=9)

    elif mode == 'fraccio_enter':
      _seccio_fraccio_enter(pdf, y, n_ex=6)

    elif mode == 'fraccio_de_fraccio':
      _seccio_fraccio_de_fraccio(pdf, y, n_ex=6)

    else:  # mix — cada secció en una pàgina pròpia
      _seccio_operacions_combinades(pdf, y, n_ex=14)

      pdf.add_page()
      pdf.set_font('helvetica', '', 13)
      pdf.set_xy(5, 10)
      pdf.cell(0, 0, 'Nom: ............................................................... Data: .......................')
      pdf.set_line_width(0.4)
      pdf.line(5, 18, 205, 18)
      y2 = 22
      y2 = _seccio_simplificacio(pdf, y2, n_ex=9)
      y2 += 6
      pdf.set_line_width(0.2)
      pdf.line(5, y2, 205, y2)
      y2 += 6
      y2 = _seccio_fraccio_enter(pdf, y2, n_ex=6)
      y2 += 6
      pdf.set_line_width(0.2)
      pdf.line(5, y2, 205, y2)
      y2 += 6
      _seccio_fraccio_de_fraccio(pdf, y2, n_ex=6)

    # ── Peu de pàgina ──
    pdf.set_line_width(0.4)
    pdf.line(5, 288, 205, 288)
    pdf.set_font('helvetica', '', 8)
    pdf.set_xy(5, 289)
    pdf.cell(0, 0, f'P\u00e0gina {pagina + 1} de {pages}', align='C')

  pdf.output(file, 'F')
  print(f"Generat: {file}  ({pages} p\u00e0gines, mode: {mode})")


#
# problemes
#

operacions = {

  ## sumes
  "sumes_2": [
    "Tinc {} cosins per part de pare i {} per part de mare. Quants cosins tinc?",
    "En dos incendis diferents es van cremar {} i {} hectàreas respecticament. Quantes s'han cremat en total?"
  ],
  "sumes_3": [
    "Ahir vaig fer {}km, avui n'he fet {}km, demà en faré {}km. Quants kilometres hauré fet en total?",
    "Al Zoo hi ha {} espècies de mamífers, {} espècies d'aus i {} espècies de ràptils. Quantes espècies hi ha?",
  ],

  ## restes
  "restes_primer_gros": [
    "Tenia {} caramels, però n'he regalat {}. Quants me'n queden?",
    "Li he donat {} sardines al gat, però només se'n ha menjat {}. Quantes en queden?",
    "Un guepart pot còrrer a {}km/h, però una zebra va {}km/h més lenta que el guepart. A quina velocitat por còrrer la zebra?",
    "De un total de {} hectàreas, se'n han creamat {}. Quantes no s'han cremat?",
    "Tenia {} ampolles d'aigua a casa. Han vingut els meus amics i n'he donat una a cadascú i només m'en quedan {} Quants amics han vingut?",
  ],

  ## multiplicacions
  "multiplicacions": [
    "Vull comprar {} tasses i cada una val {}. Quants diners necessito per comprar-les?",
    "Per fer un berenar vull comprar {} croisants per cada persona. Si venen {} amics, quants croisants haig de comprar?",
    "A cada paquet de mocadors n'hi ha {}. Si tinc {} paquets, quants mocadors tinc?",
    "Si faig {} km cada hora i m'hi he estat {} hores. Quants kilometres he fet en total?",
    "La meva tortuga pon {} vegades a l'any. Cada vegada que ho fa en neixen {} tortugues. Al final de l'any, quantes tortugues hauran nascut?",
    "Si hi ha {} bolígrafs en cada paquet. Si tenim {} paquets, quants bolígrafs tenim?",
    "Si cadascú es menja {} pomes per esmorçar, quantes pomes necessitem si a casa som {}",
  ],
  "multiplicacions_un_sol_numero": [
    "Avui anirem a fer una excursió amb raquetes de neu amb {} companys. Quantes raquetes necessitem? (dues per persona)",
    "Quantes persones serem si venen {} parelles",
  ],

  ## divisions
  "divisions_gros_primer": [
    "Tinc {} euros, si cada llibre val {} euros, quants llibres puc comprar?",
  ],
  "divisions_petit_primer": [
    "Vull preparar truites per sopar. Per cada una necesito {} ous, si en tinc {} quantes en podré preparar?"
  ]
}

def problemes_get_pregunta(sumes_min, sumes_max, mul_min, mul_max):
  group = random.choice(list(operacions.keys()))

  pregunta = random.choice(operacions[group])

  if group=="sumes_2":
    return pregunta.format(randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max))
  elif group=="sumes_3":
    return pregunta.format(randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max))
  elif group=="restes_primer_gros":
    resta_gros = randrange(sumes_min+int(sumes_max/4), int(sumes_max/2))
    resta_petit = randrange(sumes_min, resta_gros)
    return pregunta.format(resta_gros, resta_petit)
  elif group=="restes_un_sol_numero":
    return pregunta.format(randrange(sumes_min, sumes_max))
  elif group=="multiplicacions":
    return pregunta.format(randrange(mul_min, mul_max), randrange(mul_min, mul_max))
  elif group=="multiplicacions_un_sol_numero":
    return pregunta.format(randrange(mul_min, mul_max))
  elif group=="divisions_gros_primer":
    factor_1 = randrange(mul_min, mul_max)
    factor_2 = randrange(mul_min, mul_max)
    resultat = factor_1*factor_2
    return pregunta.format(resultat, factor_1)
  elif group=="divisions_petit_primer":
    factor_1 = randrange(mul_min, mul_max)
    factor_2 = randrange(mul_min, mul_max)
    resultat = factor_1*factor_2
    return pregunta.format(factor_1, resultat)
  else:
    return ""


@click.command()
@click.option('--file', default='problemes.pdf', help='output file')
@click.option('--pagines', default=4, help='numero de pàgines')
@click.option('--sumes-min', default=5, help='sumes min int')
@click.option('--sumes-max', default=150, help='sumes max int')
@click.option('--mul-min', default=2, help='multiplicacions min int')
@click.option('--mul-max', default=10, help='multiplicacions max int')
def problemes(file, pagines, sumes_min, sumes_max, mul_min, mul_max):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(1, int(pagines+1)):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 12.0)
    for linea in range(0,5):
      pdf.set_xy(10.0, 35.5+ (linea*45))
      pdf.multi_cell(w=0,h=10, txt=str(linea+1)+'. '+problemes_get_pregunta(sumes_min, sumes_max, mul_min, mul_max).encode('latin-1', 'replace').decode('latin-1'))
  pdf.output(file,'F')

#
# operacions combinades
#

PATRONS_FACIL = [
  "(a + b) * c - d",
  "a + (b - c) * d",
  "(a - b) + (c * d)",
  "(a + b) - (c + d)",
]

PATRONS_MITJA = [
  "(a * b) - (c - d)",
  "(a + b) - (c * d)",
  "a - (b * c) + d",
  "(a - b) * (c + d)",
]

PATRONS_DIFICIL = [
  "(a + b) * (c - d)",
  "(a - b) + (c * d)",
  "(a + b) - (c * d)",
  "(a - b) - (c + d)",
]

def fmt(n):
  return f"({n})" if n < 0 else str(n)

def genera_operacio(mode):
  if mode == "mix":
    nivell = random.choice(["facil", "mitja", "dificil"])
  else:
    nivell = mode

  if nivell == "facil":
    patro = random.choice(PATRONS_FACIL)
    nums = {k: randrange(1, 10) for k in ["a","b","c","d"]}

  elif nivell == "mitja":
    patro = random.choice(PATRONS_MITJA)
    nums = {k: random.choice([randrange(1,10), -randrange(1,10)]) for k in ["a","b","c","d"]}

  else:  # dificil
    patro = random.choice(PATRONS_DIFICIL)
    nums = {k: random.choice([randrange(1,10), -randrange(1,10)]) for k in ["a","b","c","d"]}

  expr = patro
  for k, v in nums.items():
    expr = expr.replace(k, fmt(v))

  return expr + " ="

@click.command()
@click.option('--file', default='operacions_combinades.pdf')
@click.option('--pages', default=20)
@click.option(
    '--mode',
    type=click.Choice(['facil', 'mitja', 'dificil', 'mix']),
    default='mix',
    help='Nivell de dificultat: facil, mitja, dificil o mix'
)
def operacions_combinades(file, pages, mode):

  pdf = FPDF(orientation='P', unit='mm', format='A4')

  for pagina in range(pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15)
    pdf.set_xy(5,18)
    pdf.cell(0,0,'Nom: ........................................ Data: ........................')

    pdf.set_font('helvetica','',20)

    anterior_operacio = ""

    for columna in range(2):
      for linea in range(14):
        pdf.set_xy(10 + columna*100, 32.5 + linea*17)

        operacio = ""
        while operacio == anterior_operacio:
          operacio = genera_operacio(mode)

        pdf.cell(0,0,operacio)
        anterior_operacio = operacio

  pdf.output(file,'F')


#
# main
#

matecursa.add_command(sumes)
matecursa.add_command(sumes_horitzontal)

matecursa.add_command(restes)
matecursa.add_command(restes_vertical)

matecursa.add_command(multiplicacions)
matecursa.add_command(multiplicacions_vertical)
matecursa.add_command(taules_multiplicar)

matecursa.add_command(divisions)

matecursa.add_command(problemes)

matecursa.add_command(enters_sumes_restes)
matecursa.add_command(operacions_combinades)

matecursa.add_command(fraccions)

if __name__ == '__main__':
  matecursa()
  