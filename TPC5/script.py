import csv
import re

def carregar_produtos():
    produtos = {}
    with open('stock.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            produto_id = int(row['Id'])
            produto_nome = row['Produto'].strip()
            produto_preco = row['Preço'].strip()
            produtos[produto_id] = {'produto': produto_nome, 'preco': produto_preco}
    return produtos

# Função para listar os produtos disponíveis
def listar_produtos(produtos):
    for id, info in produtos.items():
        print(f"{id}: {info['produto']} ({info['preco']})")


def processar_moeda(saldo_atual, moedas):
    saldo_euros = 0
    saldo_centavos = 0
    moedas_validas = {'5c': 0.05, '10c': 0.10, '20c': 0.20, '50c': 0.50, '1e': 1, '2e': 2}
    for moeda in moedas:
        moeda_lower = moeda.lower()
        if moeda_lower in moedas_validas:
            valor = moedas_validas[moeda_lower]
            if moeda_lower.endswith('e'):
                saldo_euros += valor
            elif moeda_lower.endswith('c'):
                saldo_centavos += valor
        else:
            print(f"Moeda inválida: {moeda}")
    saldo_atual += saldo_euros * 100 + saldo_centavos
    return saldo_atual
        


def selecionar_produto(produtos, saldo_atual, id_produto):
    if id_produto in produtos:
        preco_produto_str = produtos[id_produto]['preco']
        
        # Verificar se o preço é em euros ou em centavos
        if 'e' in preco_produto_str:
            # Extrair valores separadamente para euros e centavos
            match = re.match(r'(\d+)e (\d+)c', preco_produto_str)
            
            if match:
                preco_euros = int(match.group(1))
                preco_centavos = int(match.group(2))
                preco_total = preco_euros * 100 + preco_centavos
                
                print(f"Preço do produto: {preco_euros}e {preco_centavos}c")
                
                if saldo_atual >= preco_total:
                    saldo_atual -= preco_total
                    print(f"Compra bem-sucedida! Saldo restante: {saldo_atual // 100}e {saldo_atual % 100}c")
                    return saldo_atual
                else:
                    print("Erro: Saldo insuficiente.")
                    return saldo_atual
            else:
                print("Erro: Formato de preço inválido.")
                return saldo_atual
        else:
            preco_centavos = int(re.findall(r'\d+', preco_produto_str)[0])
            
            print(f"Preço do produto: {preco_centavos}c")
            
            if saldo_atual >= preco_centavos:
                saldo_atual -= preco_centavos
                print(f"Compra bem-sucedida! Saldo restante: {saldo_atual // 100}e {saldo_atual % 100}c")
                return saldo_atual
            else:
                print("Erro: Saldo insuficiente.")
                return saldo_atual
    else:
        print("Produto não encontrado.")
        return saldo_atual

# Função principal
def main():
    produtos = carregar_produtos()
    saldo_atual = 0

    while True:
        
        comando = input(">> ").upper()

        if comando.startswith("LISTAR"):
            listar_produtos(produtos)
            print("\n====================================================")
            print("Comandos Disponíveis:")
            print("  - MOEDA <moedas>: Inserir moedas (ex: MOEDA 1e 50c)")
            print("  - SELECIONAR <ID>: Selecionar um produto para comprar")
            print("  - SAIR: Encerrar a compra e receber troco")

        elif comando.startswith("MOEDA"):
            listar_produtos(produtos)
            moedas = comando.split()[1:]
            if len(moedas) == 1:
                saldo_atual = processar_moeda(saldo_atual, [moedas[0]])
            else:
                saldo_atual = processar_moeda(saldo_atual, moedas)
            print("\n====================================================")
            print(f"Saldo = {saldo_atual // 100}e {saldo_atual % 100}c")
            print("\n====================================================")
            print("  - LISTAR: Listar produtos disponíveis")
            print("  - SELECIONAR <ID>: Selecionar um produto para comprar")
            print("  - SAIR: Encerrar a compra e receber troco")

        elif comando.startswith("SELECIONAR"):
            listar_produtos(produtos)
            id_produto = int(comando.split()[1])
            saldo_atual = selecionar_produto(produtos, saldo_atual, id_produto)

            print("\n====================================================")
            print("  - LISTAR: Listar produtos disponíveis")
            print("  - SELECIONAR <ID>: Selecionar um produto para comprar")
            print("  - SAIR: Encerrar a compra e receber troco")

        elif comando == "SAIR":
            print(f"Troco: {saldo_atual // 100}e {saldo_atual % 100}c")
            break

        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()
