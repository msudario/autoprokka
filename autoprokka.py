import os
import glob
import subprocess
import argparse


parser = argparse.ArgumentParser(
    description='running autoPROKKA')
parser.add_argument('-f', '--format', metavar='', type=str, required=True,
                    help='Valid PROKKA format i.e: fasta, fna')
parser.add_argument('-o', '--outdir', metavar='', type=str, required=True,
                    help='outdir i.e home/usr/Desktop')
parser.add_argument('-g', '--genus', metavar='', type=str, required=True,
                    help='the genus of the species i.e: Dickeya')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='path to the files i.e: home/usr/Desktop/myfiles')
parser.add_argument('-s', '--species', metavar='', type=str, required=False,
                    help='species i.e: dadantii')


args = parser.parse_args()

folder_input = f'{args.input}'

for i in glob.glob(os.path.join(folder_input, f'*.{args.format}')):
    if args.format in ['fna', 'faa', 'fasta']:
        nome_do_arquivo = []
        os.chdir(f'{args.input}')
        nome_do_arquivo = i.split('/')
        nome_final = nome_do_arquivo[-1].split(f'{args.format}')
        nome_vf = nome_final[0].replace('.', '')

        if args.species:

            command_line = ['prokka', '--outdir', f'{args.outdir}/results_prokka_{nome_vf}', '--genus', f'{args.genus}',
                            '--species', f'{args.species}', '--prefix', f'{nome_vf}', '--locustag', f'{args.genus[0]}{sp_name[0]}{nome_vf}', f'{args.input}/{nome_vf}.{args.format}']
        else:
            with open(i, "r") as file:
                sp_name = []
                first_line = file.readline().split()
                if len(first_line) > 2:
                    sp_name = first_line[2]
                else:
                    sp_name = first_line[0]
            command_line = ['prokka', '--outdir', f'{args.outdir}/results_prokka_{nome_vf}', '--genus',
                            f'{args.genus}', '--prefix', f'{nome_vf}', '--locustag', f'{args.genus[0]}{sp_name[0]}{nome_vf}', f'{args.input}/{nome_vf}.{args.format}']

        subprocess.call(command_line)
    else:
        print('Please enter a valid format (faa, fasta, fna)')
