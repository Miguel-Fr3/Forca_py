
def gera_traco(word):
    qtd = len(word)
    resp = ""
    contador = 0
    while contador < qtd:
        resp = resp + "_ "
        contador = contador + 1
    return resp

def busca(char, palavra, segredo):
    i = 0
    resp = ""
    while i < len(palavra):
        if char == palavra[i]:
            resp = resp + char + " "
        else:
            resp = resp + segredo[i + i] + " "
        i = i + 1
    return resp

erros = 0
word = "versa"
segredo = gera_traco(word)

while erros < 6 and "_" in segredo:
    print(segredo)
    print("Erros: ",erros)
    letra = input("Digite uma letra: ")

    if letra in word:
        segredo = busca(letra, word, segredo)
    else:
        erros = erros + 1

if erros < 6:
    print("Parabéns, você acertou a palavra", word)
else:
    print("Mais sorte da próxima vez: ", word)





    