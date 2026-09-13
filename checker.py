import csv
import hashlib
import requests
import time
from pdf_generate import create_pdf
import argparse

def get_credential(db, resultados):
   with open(db, encoding='utf-8') as arquivo:
      for credencial in csv.DictReader(arquivo):
         hash_sha1 = hashlib.sha1(credencial['senha'].encode("utf-8")).hexdigest()
         pref_hash = hash_sha1[:5].upper()
         sufi_hash = hash_sha1[5:].upper()
         check_hash(pref_hash, sufi_hash, credencial, resultados)

def check_hash(pref_hash, sufi_hash, credencial, resultados):
   try:
      vazamentos = None

      response = requests.get(f"https://api.pwnedpasswords.com/range/{pref_hash}", headers={"User-Agent": "password-checker/1.0"}, timeout=15)
      text_response = response.text.splitlines()

      for i in text_response:
         partes = i.split(':')
         if (sufi_hash.upper() == partes[0]):
            vazamentos = partes[1]
            resultados.append({"usuario": credencial['usuario'], "vezes": vazamentos})

            print(f"Senha encontrada como vazada {vazamentos} vezes!! {credencial['usuario']}")
            break

      if vazamentos is None:
         print("Zero vazamentos!")
      print(f"==== Busca para {credencial['usuario']} feita! ====")

      time.sleep(1.3)
   except requests.exceptions.RequestException as e:
      print(f"Erro na consulta do usuário {credencial['usuario']}: {e}")

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