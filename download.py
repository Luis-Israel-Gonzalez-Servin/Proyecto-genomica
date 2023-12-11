import os
import requests
import zipfile

GENOMES_FOLDER = 'secuencias'


if not os.path.exists(GENOMES_FOLDER):
    os.makedirs(GENOMES_FOLDER)

with open('salida.fasta') as f:
    accessions = f.readlines()

    accessions = [x.strip() for x in accessions]

    for accession in accessions:

        url = f'https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/{accession}/download?include_annotation_type=GENOME_FASTA'
        r = requests.get(url)

        with open(f'{GENOMES_FOLDER}/{accession}.zip', 'wb') as fasta:
            fasta.write(r.content)
        print(f'Secuencia {accession} descargada con éxito.')
        print(f'Extrayendo el zip')

        with zipfile.ZipFile(f'{GENOMES_FOLDER}/{accession}.zip', 'r') as zip_ref:
            zip_ref.extractall(GENOMES_FOLDER)

        print(f'Secuencia {accession} extraída con éxito.')
        print(f'Eliminando el zip')
        os.remove(f'{GENOMES_FOLDER}/{accession}.zip')
