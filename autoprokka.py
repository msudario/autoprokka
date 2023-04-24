#!/usr/bin/env python3
# coding: utf-8

import os
import subprocess
import argparse


parser = argparse.ArgumentParser(
    description='running autoPROKKA')

parser.add_argument('-g', '--genus', metavar='', type=str, required=True,
                    help='the genus of the species i.e: Dickeya')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='path to the files i.e: home/usr/Desktop/myfiles')

args = parser.parse_args()

folder_input = os.path.expanduser(f'{args.input}') 
genus = f'{args.genus}'
extensoes = ['.fna', '.faa', '.fasta']

def run_prokka(folder_input): 
    os.chdir(folder_input)

    caminho_nova_pasta = os.path.join(folder_input, 'results_autoprokka')

    for arquivos in os.listdir(folder_input):
        for extensao in extensoes:
            if arquivos.endswith(extensao): 
                with open(os.path.join(folder_input, arquivos), "r") as file:
                    first_line = file.readline().split()

                    if len(first_line) > 2:        
                        if first_line[3] != 'strain':
                                if first_line[4] is not 'chromosome' or first_line[4] is not 'contig' or first_line[4] is not 'complete' or first_line[4] is not 'contig1':
                                    strain = first_line[3].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '') + first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                    locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                    command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                    f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']

                                    subprocess.call(command_line)
    
                                else:
                                    strain = first_line[3].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                    locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                    command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                    f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']
                
                                    subprocess.call(command_line)

                        elif first_line[3] == 'strain':
                                if first_line[5] is not 'chromosome' or first_line[5] is not 'contig' or first_line[5] is not 'complete' or first_line[5] is not 'contig1':
                                    strain = first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '') + first_line[5].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                    locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                    command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                    f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']

                                    subprocess.call(command_line)

                                else: 
                                    strain = first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '') + first_line[5].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                    locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                    command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                    f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']
                                       
                                    subprocess.call(command_line)
                        
                    else:

                        while True:
                            print(f'the file {arquivos} has no information about its locus tag, please type the locus tag you would like prokka to annotate') 
                            locus_tag = input('Type your locus tag:')
                            ask = input(f' Your locus_tag name is {locus_tag} Are you sure? (y/n): ')
                            if ask == 'y'.lower():
                                strain = arquivos.replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{strain}'), '--genus',
                                f'{genus}', '--prefix', f'{locus_tag}', '--locustag', f'{locus_tag}', f'{arquivos}']
                                subprocess.call(command_line)
                                break
                            elif ask == 'n'.lower():
                                 continue
                            else: print('Please enter a valid answer (y/n)')
                            

def criar_pasta(folder_input) :
    os.chdir(folder_input)

    if 'results_autoprokka' not in os.listdir():
        os.mkdir('results_autoprokka')  

def processar_arquivos(folder_input):
    criar_pasta(folder_input)
    run_prokka(folder_input)

    
if __name__ == '__main__':
    processar_arquivos(folder_input)



