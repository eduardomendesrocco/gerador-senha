### Existem métodos bem mais simples e fáceis de se fazer um algoritmo que gera senhas aleatórias.
### Algoritmo apenas para teste pessoal e de uso livre.
### Versão 1.0 porque tem uma quantidade limitada de cada categoria de caractere.
import secrets

biblioteca = {
    "letras_maiusculas": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "letras_minusculas": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "numeros": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "especiais": ["!", "@", "#", "$", "%", "&", "*", "-", "_", "=", "+", ",", ".", ";", ":", "?"]
}

def secrets_shuffle(array):
    for i in range(len(array)-1, 0, -1):
        j = secrets.randbelow(i + 1)
        array[i], array[j] = array[j], array[i]

# Parte da criação e randomização da senha

def password_generator():
    senha = ""
    for i in range(6):
        senha += secrets.choice(biblioteca["letras_minusculas"])

    for i in range(4):
        senha += secrets.choice(biblioteca["letras_maiusculas"])

    for i in range(4):
        senha += secrets.choice(biblioteca["numeros"])

    for i in range(2):
        senha += secrets.choice(biblioteca["especiais"])

    # Tranformamos em lista para poder embaralhar (shuffle) e transformar em string novamente depois.
    array_senha = list(senha)
    secrets_shuffle(array_senha)
    senha = "".join(array_senha)

    print(f"Senha gerada com sucesso! -> | {senha} |")

if __name__ == "__main__":
    password_generator()
