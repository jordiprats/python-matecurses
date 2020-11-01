from random import randrange
from fpdf import FPDF


import click

@click.command()
@click.option('--file', default='sumes.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=2, help='max int')
@click.option('--max', default=5, help='max int')
def sumes(file, pages, min, max):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    for pagina in range(0, pages):
        pdf.add_page()
        pdf.set_font('helvetica', '', 15.0)
        pdf.set_xy(5.0, 18)
        pdf.cell(w=0,h=0, txt='Nom: ................................................................................ Data: .....................................', ln=0 )
        pdf.set_xy(5.0, 276)
        pdf.set_font('helvetica', '', 25.0)
        pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
        pdf.set_font('helvetica', '', 20.0)
        anterior_operacio = ''
        operacio = ''
        for linea in range(0,14):
            for columna in range(0, 4):
                pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
                while anterior_operacio == operacio:
                    print('range: '+str(min)+'-'+str(max))
                    primer_numero = randrange(min, max)
                    segon_numero = randrange(min, max)
                    operacio = str(primer_numero)+' + '+str(segon_numero)+' ='
                pdf.cell(w=0,h=0, txt=operacio, ln=0 )
                anterior_operacio = operacio
        if pagina%4 == 0:
            max += 1
    pdf.output(file,'F')


if __name__ == '__main__':
    sumes()
    