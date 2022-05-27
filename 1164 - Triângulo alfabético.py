##Triângulo alfabético

##Como dito por um importante personagem de um igualmente memorável filme: "palavras são, na minha nada humilde opinião, nossa inesgotável fonte de magia [...]". Evidentemente, para formar palavras é necessário que exista um alfabeto como, por exemplo, nosso alfabeto latino.
##
##O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres diferentes, se desconsiderarmos as acentuações e as diferenças entre letras maiúsculas e minúsculas.
##
##Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. Em um dos desenhos, Harry escreve na primeira linha e primeira coluna de uma folha quadriculada o primeiro caractere do alfabeto. Na segunda linha escreve duas vezes o segundo caractere, ocupando as duas primeiras colunas. Na terceira linha escreve três vezes o terceiro caractere, ocupando as três primeiras colunas e assim por diante. Harry percebeu que dessa forma consegue formar um triângulo alfabético, semelhante ao visto na Figura 1, onde a primeira linha contém apenas um 'A' e a sétima contém sete 'G'.

n = int(input())


letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for triang in range(n):
    print(letras[triang]*(triang+1))
    
