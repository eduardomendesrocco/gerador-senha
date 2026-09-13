### Versão 2.0 com caracteres limitados pelo usuário e categorias não limitadas.
import secrets

todos_caracteres = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "&", "*", "-", "_", "=", "+", ",", ".", ";", ":", "?"
]

def password_generator():
    senha = ""
    quantidade_caracteres = int(input("Digite a quantidade desejada de caracteres na senha ( maior que 6 ) -> "))

    if quantidade_caracteres >= 6:
        for i in range(quantidade_caracteres):
            senha += secrets.choice(todos_caracteres)

        print(f"Senha gerada com sucesso! -> | {senha} |")

    else:
        password_generator()

if __name__ == "__main__":
    password_generator()