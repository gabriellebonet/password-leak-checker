# Password Leak Checker (Have I Been Pwned)

Script simples em Python que verifica se as senhas de uma lista de usuários já apareceram em vazamentos reais de dados, usando a API Pwned Passwords do [Have I Been Pwned](https://haveibeenpwned.com/). Gera um relatório em PDF com os usuários em risco. Feito como projeto de estudo sobre APIs, hashing e privacidade.

## Como funciona

O script lê um CSV com usuários e senhas, gera o hash SHA-1 de cada senha e consulta a API do HIBP usando **k-anonimidade** — a senha nunca sai da sua máquina:

- Só os **5 primeiros caracteres** do hash são enviados à API.
- A API devolve uma lista de hashes com aquele prefixo e quantas vezes cada um vazou.
- A comparação do restante do hash acontece **localmente**, e o número de vazamentos é registrado.
- Usuários com senha encontrada são listados no PDF gerado.
- A cada consulta o script aguarda 1,3s para respeitar o rate limit da API.

## Como usar

Precisa do Python 3 e das dependências `requests` e `reportlab`. Recomendo usar um ambiente virtual para não conflitar com os pacotes do seu sistema:

```bash
git clone https://github.com/gabriellebonet/password-leak-checker.git
cd password-leak-checker

# cria e ativa o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# instala as dependências dentro do ambiente
pip install requests reportlab
```

Rode o script passando o CSV com as credenciais:

```bash
python checker.py usuarios_exemplo.csv
```

Opções disponíveis (veja todas com `python checker.py -h`):

| Argumento | O que faz |
|---|---|
| `file_input` | Arquivo CSV com as credenciais |
| `--saida` | Nome do PDF gerado (padrão: `relatorio_senhas.pdf`) |

Exemplo completo:

```bash
python checker.py usuarios_exemplo.csv --saida relatorio.pdf
```

Formato esperado do CSV:

```csv
usuario,senha
joao.silva,senha123
maria.souza,UmSegredo!2026
```

## Testando

Com o script rodando:

- **Senha vazada:** use uma senha fraca conhecida (ex: `123456`) → o terminal mostra quantas vezes ela apareceu em vazamentos e o usuário entra no PDF.
- **Senha segura:** use uma senha longa e aleatória → aparece "Zero vazamentos!" e o usuário não vai pro PDF.
- **Sem internet / API fora do ar:** o script avisa o erro daquele usuário e continua com os demais.

No final da execução, abra o PDF gerado na pasta do projeto.

## Sobre

Projeto feito para estudos, para entender na prática como consumir APIs REST, trabalhar com hashes SHA-1 e como a técnica de k-anonimidade permite consultar bases de vazamentos sem expor as senhas dos usuários.

## Licença

MIT
