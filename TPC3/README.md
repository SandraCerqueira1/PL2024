# TPC3: Somador on/off
## 25/02/2024

## Autor

- A100681
- Sandra Fabiana Pires Cerqueira

## Resumo
### Objetivos
**Somador on/off em Python**

O objetivo deste trabalho prático foi criar um programa em Python que funcione como um somador on/off. 
A ideia era somar todas as sequências de dígitos encontradas num texto, ligando ou desligando esse comportamento com as palavras "On" e "Off", independentemente de estarem em maiúsculas ou minúsculas. Sempre que o  caracter "=" for encontrado, o resultado da soma até o momento é exibido no terminal.


### Resultado

O `comador.py` foi desenvolvido para atender aos requisitos do somador on/off.
No entanto, há uma limitação relacionada à detecção de "On" e "Off" quando essas palavras estão contidas na mesma palavra (por exemplo, "strogonOFF"). 
A tentativa de resolver esta limitação não foi bem-sucedida até o momento.
O código funciona devidamente mas para casos em que on e off nao pertençam à mesma palavra.

Para testar o código utilizei o seguinte comando:
```bash
python3 somador.py testar.txt
```
Tendo obtido o seguinte resultado para o texto `"24 23 = olaola ON 23 20 -10 = off 14 on 20 = strogon = 10 ="` contido no ficheiro `testar.txt`
```bash
A soma até ao "=" número 1 é igual a 0
A soma até ao "=" número 2 é igual a 33
A soma até ao "=" número 3 é igual a 53
A soma até ao "=" número 4 é igual a 53
A soma até ao "=" número 5 é igual a 63
```
