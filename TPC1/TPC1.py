from collections import defaultdict

class AnalisadorCSV:
    def __init__(self, file_path: str):
        with open(file_path, encoding='utf-8') as f:
            linhas = f.readlines()

        dataset = [linha.replace('\n', '').split(',') for linha in linhas]
        # Remover cabeçalho
        header = dataset.pop(0)

        # Variáveis para as estatísticas
        modalidades = set()
        aptos = 0
        inaptos = 0
        idades = []

        # 0    1      2         3          4           5     6      7        8        9    10      11      12
        #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
        for line in dataset:
            modalidades.add(line[8])

            # Verificando se o atleta é apto ou inapto
            if line[12] == 'true':
                aptos += 1
            else:
                inaptos += 1

            # Recolha das idades para a distribuição etária
            idade = int(line[5])
            idades.append(idade)

        # Calcula as percentagens de aptos e inaptos
        total_atletas = len(dataset)
        percent_aptos = (aptos / total_atletas) * 100
        percent_inaptos = (inaptos / total_atletas) * 100

        # Ordena as modalidades por ordem alfabetica
        modalidades_ordenadas = sorted(modalidades)

        # Criação da distribuição de atletas por escalão etário
        escaloes = defaultdict(int)

        for idade in idades:
            escalao = (idade // 5) * 5
            escaloes[escalao] += 1

        # Ordena as chaves do dicionário para imprimir por ordem
        escaloes_ordenados = sorted(escaloes.items())

        self.modalidades_ordenadas = modalidades_ordenadas
        self.percent_aptos = percent_aptos
        self.percent_inaptos = percent_inaptos
        self.escaloes_etarios = escaloes_ordenados

# Exemplo de uso
analise = AnalisadorCSV('emd.csv')
print("Modalidades:", analise.modalidades_ordenadas)
print("Percentagem de Aptos:", analise.percent_aptos)
print("Percentagem de Inaptos:", analise.percent_inaptos)

# Chama a função para imprimir a distribuição por escalão etário
print("Distribuição por escalão etário:")
for escalao, quantidade in analise.escaloes_etarios:
    print(f"{escalao}-{escalao+4}: {quantidade} atletas")
