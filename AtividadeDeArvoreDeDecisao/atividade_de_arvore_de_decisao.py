from decimal import Decimal
from extenso import dExtenso

extenso = dExtenso()
consultores = list()

while True:
    while True:
        consultor = dict()
        consultor['nome'] = input('Nome do Consultor: ')
        consultor['cargo'] = input('Cargo (Advogado/Estagiário): ')
        consultor['email'] = input('E-mail: ')
        consultores.append(consultor)
        continua = input('Deseja adicionar outro Consultor (s/n)?: ' or 'n')
        if continua == 'N' or continua == 'n':
            break

    forma_de_pagamento = input('Qual é a forma de pagamento (1 - Por mês / 2 - Por projeto): ')

    if forma_de_pagamento == '1':
        n_salarios = input('Qual é o número de salários mínimos?: ')
        v_salario = Decimal(input('Qual é o valor do salário mínimo [R$ 998,00]?: ') or 998.00)
        total = int(n_salarios) * v_salario
        clausula_forma ='''
            O valor da prestação dos serviços advocatícios é equivalente ao montante de
            {n_salarios} ({n_salarios_extenso}) salários mínimos, que devem ser pagos com 
            periodicidade mensal. O valor atual do salário mínimo é de R$ {v_salario:.2f}
            ({v_salario_extenso} reais). Deste modo, o valor mensal a ser pago é de
            R$ {total:.2f} ({total_extenso} reais).'''.format(n_salarios=n_salarios,
                                                              n_salarios_extenso=extenso.getExtenso(n_salarios),
                                                              v_salario=v_salario,
                                                              v_salario_extenso=extenso.getExtenso(str(v_salario)),
                                                              total=total,
                                                              total_extenso=extenso.getExtenso(str(total)))

    else:
        n_horas = input('Qual o número de horas trabalhadas?: ')
        v_hora = Decimal(input('Qual é o valor da hora trabalhada?: '))
        total = int(n_horas) * v_hora
        clausula_forma ='''
            O valor da prestação dos serviços advocatícios é equivalente
            a {n_horas} ({n_horas_extenso}) horas trabalhadas de um advogado, o qual deve ser
            pago ao final do projeto. O valor atual da hora trabalhada é de R$ {v_hora:.2f},
            {v_hora_extenso} reais). Deste modo, o valor total a ser pago é de 
            R$ {total:.2f} ({total_extenso} reais).'''.format(n_horas=n_horas,
                                                              n_horas_extenso=extenso.getExtenso(n_horas),
                                                              v_hora=v_hora,
                                                              v_hora_extenso=extenso.getExtenso(str(v_hora)),
                                                              total=total,
                                                              total_extenso=extenso.getExtenso(str(total)))

# ===== IMPRESSÃO ======================================================================================================

    output = ''

    if len(consultores) == 1:
        output += '\n' + 'IV – Consultor' + '\n\n'
    else:
        output += '\n' + 'IV – Equipe de Consultores' + '\n\n'

    for i, consultor in enumerate(consultores):
            output += '{nome} ({cargo}): e-mail: {email}'.format(nome=consultor['nome'], cargo=consultor['cargo'], email=consultor['email']) + '\n\n'

    output += 'V – Investimento e Condições de Pagamento\n'
    output += clausula_forma
    output += '\n'

    print(output)

# ===== IMPRESSÃO PARA ARQUIVO =========================================================================================

    correto = input('O texto acima está correto (s/n)?: ' or 's')
    if correto == 's':
        nome_arquivo = input('Qual o nome do arquivo para salvar o texto?: ')
        with open(nome_arquivo, 'w') as f:
            print(output, file=f)
        print('\nSalvo com sucesso! \n')
        print('Viu como a automação facilita sua vida? Até a próxima...\n')

        break
    else:
        print('\n Vamos fazer tudo de novo...\n')
