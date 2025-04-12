texto = input("Ingrese un texto: ").lower()
vocales = "aeiou"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
print(f"El texto contiene {contador} vocales.")