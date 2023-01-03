import numpy
import math
from time import sleep
print('='*50)
print('BEM-VINDO AO PACOTE DE 15 PROGRAMAS EM UM!')
print('Por favor, selecionado qual programa deseja usar: ')
print('(1) Olá mundo!')
print('(2) Digitar um valor inteiro')
print('(3) Somar valores')
print('(4) Calcular média de notas')
print('(5) Conversor de metros para centímetros')
print('(6) Calcular área do círculo')
print('(7) Dobro da área do quadrado')
print('(8) Calculador salário simples')
print('(9) Conversor temperatura Farenheit para Celsius')
print('(10) Mexendo com números')
print('(11) Calculador peso ideal simples')
print('(12) Calculador peso ideal completo')
print('(13) Calculador de peso de peixes')
print('(14) Calculador salário completo')
print('(15) Calculador de uso de tinta')
opcao = int(input('Digite uma opção válida: '))

match opcao:
      case 1:
            print('Olá mundo!')
            print('=' * 50)
      case 2:
            var = int(input('Digite um valor inteiro: '))
            print('O número informado foi {0}'.format(var))
            print('=' * 50)
      case 3:
            n1 = int(input('Informe um número: '))
            n2 = int(input('Informe um número: '))
            s = n1 + n2
            print('A soma de {0} com {1} é {2}'.format(n1, n2, s))
            print('=' * 50)
      case 4:
            no1 = float(input("Digite a nota do 1° Aluno: "))
            no2 = float(input("Digite a nota do 2° Aluno: "))
            no3 = float(input("Digite a nota do 3° Aluno: "))
            no4 = float(input('Digite a nota do 4° Aluno: '))
            m = (no1 + no2 + no3 + no4) / 4
            print(f'A media dos alunos foi {m:.2f}')
      case 5:
            medM = float(input('Digite a medida em metros: '))
            medC = medM * 100
            print(f'A medida em centímetros vale: {medC:.2f} cm')
      case 6:
            r = float(input('Digite o raio do círculo: '))
            arc = numpy.pi * r ** 2
            print(f'A área desse círculo é: {arc:.2f} m²')
      case 7:
            arq = float(input('Insira a área do quadrado: '))
            arq2 = arq * 2
            print(f'O dobro da área do quadrado vale {arq2:.2f} m²')
      case 8:
            qntdH = int(input('Quantas horas você trabalha por dia? '))
            recbH = int(input('Quanto você recebe por hora? '))
            qntdHtotal = qntdH * 30
            sal = qntdHtotal * recbH
            print(f'Seu salário esse mês foi de R$ {sal}')
      case 9:
            gf = float(input('Insira a temperatura em graus Fahrenheit: '))
            gc = (gf - 32) / 1.8
            print(f'A temperatura em graus celsius é de {gc:.2f}°C')
      case 10:
            n1 = int(input('Forneça um número inteiro: '))
            n2 = int(input('Forneça um número inteiro: '))
            n3 = float(input('Forneça um número real: '))
            a = (2 * n1) * (n2 / 2)
            b = (3 * n1) + n3
            c = n3 ** 3
            print(f'O produto do dobro do primeiro com a metade do segundo vale {a:.2f}')
            print(f'A soma do triplo do primeiro com o terceiro vale {b:.2f}')
            print(f'O terceiro elevado ao cubo vale {c:.2f}')
      case 11:
            al = float(input("Digite sua altura: "))
            ps = (72.7 * al) - 58
            print(f"Seu peso ideal é {ps:.2f}")
      case 12:
            alt = float(input("Digite sua altura: "))
            sex = str(input("Você é homem ou mulher? Digite a resposta: "))
            sexf = sex.strip().upper()
            if sexf == "HOMEM" or sexf == "MULHER":
                  if sexf == "HOMEM":
                        psh = (72.7 * alt) - 58
                        print(f"Seu peso ideal é {psh:.2f}")
                  else:
                        psm = (62.1 * alt) - 44.7
                        print(f'Seu peso ideal é {psm:.2f}')
            else:
                  print("Entrada inválida! Por favor digite 'Homem' ou 'Mulher'")
      case 13:
            psmax = 50
            ps = float(input("Insira o peso total dos peixes pescados: "))
            if ps > 50:
                  print("Houve um excesso! Calculando multa pelo excesso...")
                  sleep(2)
                  psexc = ps - psmax
                  multa = psexc * 4.0
                  print(f"Concluído! A multa a ser paga é de R${multa:.2f} referente ao excesso de {psexc:.2f} KG!")
            else:
                  print("Não houve excesso! Não precisa pagar multa.")
      case 14:
            salh = float(input("Insira quanto você ganha por hora trabalhada: "))
            htd = float(input("Insira quantas horas você trabalha por dia (exceto sábado): "))
            dts = int(input("Insira quantos dias você trabalha por semana (exceto sábado): "))
            sab = str(input("Você trabalha aos sábados? Digite sua resposta: "))
            sabf = sab.strip().upper()
            if sabf == "SIM":
                  htsab = float(input("Insira quantas horas você trabalha no sábado: "))
                  dfm = int(input("Insira quantos dias você faltou durante o mês: "))
                  salb = salh * ((htd * dts + htsab) * 4)
                  print("Calculando descontos....")
                  sleep(2)
                  ddiasf = dfm * htd * salh
                  dir = salb * 0.11
                  dinss = salb * 0.08
                  dsind = salb * 0.05
                  sall = salb - (dir + dinss + dsind + ddiasf)
                  print("Sucesso!")
                  print(f"Seu salário bruto este mês foi de R$ {salb:.2f}")
                  print(f"E seu salário líquido é R$ {sall:.2f}! Os seus descontos foram:")
                  print(f"Desconto por dias faltados = R$ {ddiasf:.2f}")
                  print(f'Desconto referente ao imposto de renda (11%) = R$ {dir:.2f}')
                  print(f'Desconto referente ao INSS (8%) = R$ {dinss:.2f}')
                  print(f'Desconto referente ao sindicato (5%) = R$ {dsind:.2f}')
                  print(f'O total de descontos foi de R$ {ddiasf + dir + dinss + dsind:.2f}')
                  print('Programa concluído!')
            elif sabf == "NÃO":
                  dfm = int(input("Insira quantos dias você faltou durante o mês: "))
                  salb = salh * (htd * dts * 4)
                  print("Calculando descontos....")
                  sleep(2)
                  ddiasf = dfm * htd * salh
                  dir = salb * 0.11
                  dinss = salb * 0.08
                  dsind = salb * 0.05
                  sall = salb - (dir + dinss + dsind + ddiasf)
                  print("Sucesso!")
                  print(f"Seu salário bruto este mês foi de R$ {salb:.2f}")
                  print(f"E seu salário líquido é R$ {sall:.2f}! Os seus descontos foram:")
                  print(f"Desconto por dias faltados = R$ {ddiasf:.2f}")
                  print(f'Desconto referente ao imposto de renda (11%) = R$ {dir:.2f}')
                  print(f'Desconto referente ao INSS (8%) = R$ {dinss:.2f}')
                  print(f'Desconto referente ao sindicato (5%) = R$ {dsind:.2f}')
                  print(f'O total de descontos foi de R$ {ddiasf + dir + dinss + dsind:.2f}')
                  print('Programa concluído!')
            else:
                  print("Entrada inválida! Tente novamente")
      case 15:
            tmPar = float(input('Insira o tamanho da parede a ser pintada em m²: '))
            qtdTin = tmPar / 6
            qtdLata = math.ceil(qtdTin / 18)
            qtdGalao = math.ceil(qtdTin / 3.6)
            pLata = qtdLata * 80.0
            pGalao = qtdGalao * 25.0
            excTinGalao = (3.6 * qtdGalao) - qtdTin
            excTinLata = (18 * qtdLata) - qtdTin
            print(f'Para pintar essa parede de {tmPar:.2f} m² serão necessários {qtdTin:.2f} litros de '
                  f'tinta!')
            print(f'Se você comprar apenas latas de 18 litros, vai comprar ao todo {qtdLata} latas e '
                  f'vai custar'
                  f' R$ {pLata:.2f}')
            print(f'Se você comprar apenas galões de 3.6 litros, vai comprar ao todo {qtdGalao} galões '
                  f'e vai custar'
                  f' R$ {pGalao:.2f}')
            if excTinLata > excTinGalao:
                  qtdTinLata = (qtdLata - 1) * 18
                  falTinta = qtdTin - qtdTinLata
                  qtdGalao = math.ceil(falTinta / 3.6)
                  pGalao = qtdGalao * 25.0
                  pLata = (qtdLata - 1) * 80.0
                  print(f'Se você comprar {qtdLata - 1} latas de 18 litros e {qtdGalao} galões de 3.6 '
                        f'litros'
                        f' vai pagar R$ {pGalao + pLata}')
            else:
                  qtdTinGalao = (qtdGalao - 1) * 3.6
                  falTinta = qtdTin - qtdTinGalao
                  qtdLata = math.ceil(falTinta / 18)
                  pGalao = (qtdGalao - 1) * 25.0
                  pLata = qtdLata * 80.0
                  print(f'Se você comprar {qtdGalao - 1} galões de 3.6 litros e {qtdLata} latas de 18 '
                        f'litros'
                        f' vai pagar R$ {pGalao + pLata}')
      case _:
            print('Opção inválida! Tente novamente')