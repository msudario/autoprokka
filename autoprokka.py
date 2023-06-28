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
                    passes = ['chromosome', 'contig', 'complete', 'contig1', 'chromosome,', 'contig,', 'complete,', 'contig1,', 'contig_1', 'contig_1,']      
                    if first_line[3].lower() != 'strain' or first_line[4].lower() != 'strain':
                                strain = os.path.splitext(arquivos)[0]
                                command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{strain}'), '--genus',
                                f'{genus}', '--prefix', f'{strain}', '--locustag', f'{strain}', f'{arquivos}']

                                subprocess.call(command_line)


                    elif first_line[3] == 'strain':
                            if first_line[5].lower() not in passes:
                                strain = first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '') + first_line[5].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']

                                subprocess.call(command_line)

                            else: 
                                strain = first_line[4].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']
                                       
                                subprocess.call(command_line)
                        
                    elif first_line[4] == 'strain':
                            if first_line[6].lower() not in passes:
                                strain = first_line[5].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '') + first_line[6].replace(">","").replace("(", "").replace(")", "").replace(";","").replace(",","").replace("/","").replace("|","").replace("\\","").replace("[","").replace("]","").replace('.','').replace('-', '').replace('fasta', '').replace('fna', '').replace('faa', '')
                                locus_tag = first_line[1][0] + first_line[2][0] + first_line[2][1]
                                command_line = ['prokka', '--outdir', os.path.join(caminho_nova_pasta, f'{locus_tag}_{strain}'), '--genus',
                                f'{genus}', '--prefix', f'{locus_tag}_{strain}', '--locustag', f'{locus_tag}_{strain}', f'{arquivos}']

                                subprocess.call(command_line)                    
                            

def criar_pasta(folder_input) :
    os.chdir(folder_input)

    if 'results_autoprokka' not in os.listdir():
        os.mkdir('results_autoprokka')  

def processar_arquivos(folder_input):
    criar_pasta(folder_input)
    run_prokka(folder_input)

    
if __name__ == '__main__':
    processar_arquivos(folder_input)
