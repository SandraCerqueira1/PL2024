import sys
import re

def somador_on_off_arquivo(nome_arquivo):
    somar = False
    soma = 0
    contador_de_iguais = 1  
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            for palavra in palavras:
                if re.search(r'(?i:on)', palavra):
                    somar = True
                elif re.search(r'(?i:off)', palavra):
                    somar = False
                elif somar and re.match(r'^[-+]?\d+$', palavra):
                    soma += int(palavra)

                elif '=' in palavra:
                    print(f'A soma até ao "=" número {contador_de_iguais} é igual a {soma}')
                    contador_de_iguais += 1  

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <nome_do_arquivo>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    somador_on_off_arquivo(nome_arquivo)

if __name__ == "__main__":
    main()
