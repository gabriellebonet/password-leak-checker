from pdf_generate import create_pdf
from check_credential import get_credential
import argparse

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("file_input", help="Insira o nome do documento com as credenciais")
   parser.add_argument("--saida", default="relatorio_senhas.pdf", help="Nome do pdf gerado com o relatório de vazamentos")
   args = parser.parse_args()

   arquivo = args.file_input
   if not arquivo.endswith(".csv"):
      arquivo += ".csv"

   saida = args.saida
   if not saida.endswith(".pdf"):
         saida += ".pdf"

   resultados = []

   get_credential(arquivo, resultados)
   create_pdf(saida, resultados)

if __name__ == '__main__':
   main()