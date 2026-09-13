from reportlab.pdfgen import canvas

def create_pdf(saida, resultados):
   pdf_resultados = canvas.Canvas(saida)
   y = 750

   pdf_resultados.drawString(100, 800, "Relatório de senhas vazadas")

   for i in resultados:
      texto = (f"Usuario: {i['usuario']} - Vazamentos encontrados: {i['vezes']}")
      pdf_resultados.drawString(100, y, texto)
      y -= 30

   pdf_resultados.save()
   print("PDF gerado com sucesso!")