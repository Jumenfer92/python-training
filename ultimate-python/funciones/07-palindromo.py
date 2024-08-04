#PALINDROMO
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto):
    textoreves = ""
    for char in texto:
        textoreves = char + textoreves
    return textoreves

def es_palindraomo(texto):
    texto = no_space(texto)
    textoreves = reverse(texto)
    return texto.lower() == textoreves.lower() 

es_palindraomo("amo la paloma")