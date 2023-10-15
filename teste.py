def exibe_nomes(**nomes):
    for nome in nomes.values():
        print(nome)

#passando valores como argumentos nomeados, ou seja, chave=valor, avulsos, sem precisar de um dicionário
exibe_nomes(nome1='João', nome2='Maria', nome3='José')

#construindo um dicionário
pessoa = {'nome':'João'}

#tentando passar o dicionário inteiro
#vai dar erro, pois, assim, o dicionário é um argumento posicional, e a função espera argumentos nomeados
exibe_nomes(pessoa)

#para passar um dicionário os dados do dicionário, como argumentos nomeados, usamos o operador **, desempacotando o dicionário
exibe_nomes(**pessoa)

from django.urls import reverse
signup_url = reverse('signup')
