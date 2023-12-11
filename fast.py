import pandas as pd
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Archivo excel del que se va a sacr el archivo .fasta
archivo_excel = 'Tabla.xlsx'
# Se lee el archivo Excel
df = pd.read_excel(archivo_excel)

# Nombre de la columna que contiene las secuencias de ADN
columna = 'GenBank assembly accession'

# Se crean objetos SeqRecord para cada secuencia y se guardan en una lista
obj = []
for index, row in df.iterrows():
    sequence = str(row[columna])
    if pd.notna(sequence):
        record = SeqRecord(Seq(sequence), id=str(index), description="")
        obj.append(record)

# Archivo .fasta resultante
archivo_fasta = 'salida.fasta'

# Se guardan los registros en un archivo .fasta
with open(archivo_fasta, "w") as fasta_file:
    for secuencia in obj:
        if pd.notna(secuencia.seq):
            fasta_file.write(str(secuencia.seq) + "\n")

print(f"Archivo .fasta creado con exito.")