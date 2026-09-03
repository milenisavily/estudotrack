from colorama import init, Fore, Style
init()

# ------- Relatório de Disciplinas do Aluno -------

#Cabeçalho
def gerar_cabecalho(titulo):
    """Gera um cabeçalho para o relatório."""

    print("\n" + Fore.CYAN + "-"*45 + Style.RESET_ALL)
    print(Fore.GREEN + f"{titulo}".center(45) + Style.RESET_ALL)
    print(Fore.CYAN + "-"*45 + Style.RESET_ALL)

#Número de Disciplinas
def qtd_disciplinas():
    """Valida quantas disciplinas o aluno deseja registrar, garantindo que seja um número entre 1 e 5."""
    
    while True:
        try:
            
            qtd = int(input("\nQuantas disciplinas deseja registrar? "))
            if 0 < qtd <= 5:
                return qtd
            else:
                print("O número de disciplinas permitido é de 1 a 5. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

#Nome das Disciplinas
def nome_disciplinas(qtd):
    """Armazena os nomes das disciplinas em uma lista."""
    
    disciplinas = []
    
    for i in range(qtd):
        disciplina = input(f"Disciplina {i+1}: ")
        disciplinas.append(disciplina)
    return disciplinas

#Horas Estudadas por Dia
def horas_diaria(disciplinas, qtd):
    """Armazena as horas diárias de estudo de cada disciplina em uma lista."""
    
    tempo = []
    
    for i in range(qtd):
        while True:
            try:
                
                horas = int(input(f"Horas estudadas em {disciplinas[i]}: "))
                if 0 <= horas <= 24:
                    tempo.append(horas)
                    break
                elif horas > 24:
                    print("O número de horas não pode exceder 24. Tente novamente.")
                elif horas < 0:
                    print("O número de horas não pode ser negativo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
    return tempo

#Meta de Horas Diárias
def meta_horas(disciplinas, qtd):
    """Armazena a meta de horas diárias para cada disciplina em uma lista."""
    
    meta = []
    
    for i in range(qtd):
        while True:
            try:
                horas = int(input(f"Meta de horas diárias para {disciplinas[i]}: "))
                
                if 0 <= horas <= 24:
                    meta.append(horas)
                    break
                elif horas > 24:
                    print("A meta de horas diárias não pode exceder 24. Tente novamente.")
                elif horas < 0:
                    print("A meta de horas diárias não pode ser negativa. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
    return meta

#Notas Atuais
def nota_atual(disciplinas, qtd):
    """Armazena as notas atuais de cada disciplina em uma lista"""
    notas = []
    
    for i in range(qtd):
        while True:
            try:
                nota = float(input(f"Nota atual de {disciplinas[i]}: "))
                    
                if 0.00 <= nota <= 10.00:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve ser entre 0.00 e 10.00. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite uma nota válida.")
    return notas

#Calculo da Média de Horas Estudadas
def total_horas(tempo):
    """Calcula a média das horas estudadas em 24 horas (total diário)."""
    
    return sum(tempo)

#Media de Notas
def media_notas(notas):
    """Calcula a média das notas das disciplinas."""
    
    media_notas = sum(notas) / len(notas)
    return media_notas

#% Cumprimento da Meta de Horas
def percentual_cumprimento(tempo, meta):
    """Calcula o percentual de cumprimento da meta de horas para cada disciplina."""   
    
    percentual = []
    
    for i in range(len(tempo)):
        if meta[i] > 0:
            percentual.append(tempo[i] / meta[i] * 100)
        else:
            percentual.append(0)
    return percentual

#Estimativa de Horas Estudadas na Semana
def estimativa_semanal(tempo):
    """Estima o total de horas estudadas na semana com base nas horas diárias informadas."""
    
    estimativa = sum(tempo) * 7
    return estimativa

#Relatório Final
def EstudoTrack():
    """Exibe um relatório final com todas as informações coletadas e calculadas.""" 
    
    print("\nIniciando o EstudoTrack do(a) aluno(a)...")
    aluno = input("\nDigite seu nome: ")

    qtd = qtd_disciplinas()
    disciplinas = nome_disciplinas(qtd)
    horas = horas_diaria(disciplinas, qtd)
    meta = meta_horas(disciplinas, qtd)
    notas = nota_atual(disciplinas, qtd)

    gerar_cabecalho("RELATÓRIO DE DESEMPENHO")
    print(f"Aluno: {aluno}")

    media = media_notas(notas)
    percentual = percentual_cumprimento(horas, meta)

    for i in range(qtd):

        print(f"\nDisciplina: {disciplinas[i]}")
        print(f"  Horas estudadas por dia: {horas[i]}hrs")
        print(f"  Meta de horas diárias: {meta[i]}h")
        print(f"  Percentual de cumprimento da meta: {percentual[i]:.2f}%")
        print(f"  Nota atual: {notas[i]:.2f}")

    gerar_cabecalho("MONITORAMENTO DOS HORÁRIOS DE ESTUDOS")
    estimativa = estimativa_semanal(horas)
    hrs_estudadas = total_horas(horas)
    
    print(f"  Média de horas estudadas por dia: {hrs_estudadas}h")
    print(f"  Estimativa de horas estudadas na semana: {estimativa}h")

    gerar_cabecalho("RECOMENDAÇÕES")

    if media < 6.0:
        print("  - Sua média de notas está abaixo de 6.0. Considere dedicar mais tempo aos estudos.")
    
    for i in range(qtd):
        if percentual[i] < 70:
            print(f"  - Para {disciplinas[i]}, tente aumentar seu tempo de estudo.")
        elif 70 <= percentual[i] < 100:
            print(f"  - Para {disciplinas[i]}, você está no caminho certo, continue assim.")
    if all(p > 70 for p in percentual):
        print("  - Parabéns! Você está cumprindo bem suas metas de tempo.")

EstudoTrack()
