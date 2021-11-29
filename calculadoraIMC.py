import PySimpleGUI as sg

sg.theme('LightGrey5')
layout = [
    [sg.Text('Calculadora de IMC', font=('bold', 16))],
    [sg.Text('Insira sua altura em centímetros ', font=13), sg.Input('0', key='altura', size=(5,1)), sg.Text ('cm')],
    [sg.Text('                Insira seu peso            ', font=13), sg.Input('0', key='peso', size=(5,1)), sg.Text('kg')],
    [sg.Button('Calcular IMC'), sg.Button('Sair')],
    [sg.Text('Se gostou do programa e quiser incentivar o desenvolvedor, faça uma doação.')],
    [sg.Text('Pix: lopes.laerte@gmail.com')],
    [sg.Text('Desenvolvido por: Laerte Lopes')]

]

janela = sg.Window("Calculadora IMC - Milerte v1.0", layout=layout, element_justification='center')


while True:  # criando eventos
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Sair':
        break
    if eventos == 'Calcular IMC':
        try:
            altura = float(valores['altura'])
            peso = float(valores['peso'])
        except ValueError:
                sg.popup("Os campos não podem ficar vazios nem conter letras")
    try:
        imc = peso / (altura/100)**2
        if imc < 18.5:
            sg.popup('O seu IMC é de {:.2f}, o que revela magreza'.format(imc))
        elif imc >= 18.5 and imc < 24.9:
            sg.popup('O seu IMC é de {:.2f}, o que revela um peso normal'.format(imc))
        elif imc >= 24.9 and imc < 29.9:
            sg.popup('O seu IMC é de {:.2f}, o que revela sobrepeso'.format(imc))
        elif imc >= 29.9 and imc < 39.9:
            sg.popup('O seu IMC é de {:.2f}, o que revela obesidade'.format(imc))
        else:
            sg.popup('O seu IMC é de {:.2f}, o que revela o obesidade grave'.format(imc))
    except ZeroDivisionError:
        sg.popup("Preencha os valores dos campos Altura e Peso")

# MENOR QUE 18,5	MAGREZA	0
# ENTRE 18,5 E 24,9	NORMAL	0
# ENTRE 25,0 E 29,9	SOBREPESO	I
# ENTRE 30,0 E 39,9	OBESIDADE	II
# MAIOR QUE 40,0	OBESIDADE GRAVE	III