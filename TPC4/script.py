import re
import sys

def analisador_lexico(instrucao_sql):
    # padrões de expressões regulares 
    padrao_select = re.compile(r'(?i:\bSELECT\b)')
    padrao_from = re.compile(r'(?i:\bFROM\b)')
    padrao_where = re.compile(r'(?i:\bWHERE\b)')
    padrao_identificador = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
    padrao_numero = re.compile(r'\b\d+\b')
    padrao_operadores = re.compile(r'[=<>]')
    padrao_virgula = re.compile(r',')

    # Dicionário para armazenar contagem de tokens
    contagem_tokens = {}

    while instrucao_sql:
        # Ignora espaços em branco
        instrucao_sql = instrucao_sql.lstrip()

        if match := padrao_select.match(instrucao_sql):
            token = ('SELECT', match.group())
        elif match := padrao_from.match(instrucao_sql):
            token = ('FROM', match.group())
        elif match := padrao_where.match(instrucao_sql):
            token = ('WHERE', match.group())
        elif match := padrao_identificador.match(instrucao_sql):
            token = ('IDENTIFICADOR', match.group())
        elif match := padrao_numero.match(instrucao_sql):
            token = ('NUMERO', match.group())
        elif match := padrao_operadores.match(instrucao_sql):
            token = ('OPERADOR', match.group())
        elif match := padrao_virgula.match(instrucao_sql):
            token = ('VIRGULA', match.group())
        else:
            posicao = len(instrucao_sql) - len(instrucao_sql.lstrip())
            print(f"Erro: Caractere não reconhecido - {instrucao_sql[0]} na posição {posicao}")
            break

        # Atualiza a instrução SQL
        instrucao_sql = instrucao_sql[len(match.group()):]

        # Atualiza a contagem de tokens
        contagem_tokens[token] = contagem_tokens.get(token, 0) + 1

    return contagem_tokens

# Função para ler o conteúdo do arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

# Verifica se os args foram dados como suposto
if len(sys.argv) != 2:
    print("O comando correto é: python3 script.py nome_do_arquivo")
    sys.exit(1)

nome_arquivo = sys.argv[1]

# Lê o conteúdo do arquivo
instrucao_sql = ler_arquivo(nome_arquivo)
contagem_tokens = analisador_lexico(instrucao_sql)

# Imprime a contagem de tokens de cada tipo
print("\nContagem de tokens:")
for token, count in contagem_tokens.items():
    print(f"{token}: {count}")
