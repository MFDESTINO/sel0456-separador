#!/usr/bin/env/python3

def read_file(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    return lines

def replace_commas(lines):
    return [l.replace(',',';') for l in lines]
    
def write_file(fname, lines):
    with open(fname, 'w') as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    lines = read_file("arquivo_dados.txt")
    replaced_lines = replace_commas(lines)
    write_file("arquivo_dados_trocado.txt", replaced_lines)
