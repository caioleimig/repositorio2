import os
os.system('cls')

def notas(nota1, nota2):
   media = nota1 / 2 + nota2 / 2
   return media
def situação(media):
   if media > 6:
      print('Aluno aprovado.')
   elif media >= 4 and media <= 6:
      print('Aluno sob verificação.')
   else: print('Aluno reprovado.')
   return situação

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = notas(nota1, nota2)
situação(media)