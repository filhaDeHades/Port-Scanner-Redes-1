# Port-Scanner-Redes-1
Trabalho de implementação em grupo para a matéria de Redes de Computadores 1.
Professor: Diego Passos

# Membros do Grupo
- Alan Gomes
- Bruna de Assunção
- Matheus Pimentel
- Tamires da Hora

# Como rodar o programa
A primeira entrada é o Host a ser verificado. A segunda entrada é o range de portas a serem verificadas no seguinte formato: a b.
Isto é, vamos fazer a verificação do host nas portas do intervalo [a,b]. 

Exemplo: host (localhost) nas portas [70-80]:
Digite o host a ser analisado: localhost
Digite o range das portas a serem analisadas: 70 80

Saida => Porta : status. 
Exemplo => 80 : disponível.

# Informações extras
Os status possíveis das saídas são: disponível, filtrada, fechada. As saídas são ordenadas pelo seu status.

Exemplo:
80 : disponível
78 : filtrada
90 : fechada
