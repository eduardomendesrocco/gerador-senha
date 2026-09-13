# Gerador de Senhas

Script simples em Python para gerar senhas aleatórias e seguras, usando o módulo `secrets` da biblioteca padrão.

## Como funciona

O usuário escolhe a quantidade de caracteres da senha (mínimo 6). Cada caractere é sorteado aleatoriamente de uma lista com letras maiúsculas, minúsculas, números e caracteres especiais, usando `secrets.choice()`.

## Requisitos

- Python 3
- Nenhuma instalação extra necessária (`secrets` já vem na biblioteca padrão)

## Como usar

```bash
python gerador_senha_01.py
|           OU           | 
python gerador_senha_02.py
```

O programa vai pedir a quantidade de caracteres desejada:

```
Digite a quantidade desejada de caracteres na senha ( maior que 6 ) -> 12
Senha gerada com sucesso! -> | xY7!qR2@wL9# |
```

Se o número digitado for menor que 6, o programa pede novamente.

## Aviso

Projeto feito apenas para fins de estudo/teste pessoal.