import PySimpleGUI as sg

class TelaPython:
    def __init__ (self):
        sg.theme('Black')
        layout = [
        [sg.Text('Informe as notas de prova, pim e ava.')],
        [sg.Text('Prova',size = (23,0)), sg.Input(size = (5,0),key='prova')],
        [sg.Text('Pim',size = (23,0)), sg.Input(size = (5,0),key='pim')],
        [sg.Text('Ava',size = (23,0)), sg.Input(size = (5,0),key='ava')],
        [sg.Button('Calcular a Media',size = (30,0))],
        [sg.Output(size=(32,10))]
       ]

        self.janela = sg.Window("Calculo de Media").layout(layout)
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            prova = self.values['prova']
            pim = self.values['pim']
            ava = self.values['ava']
            while True:
                    if (prova.isdigit() and pim.isdigit() and ava.isdigit()):
                        prova = float(self.values['prova'])
                        pim = float(self.values['pim'])
                        ava = float(self.values['ava'])
                    else:
                        [sg.popup(f'ERRO! Digite um número inteiro.')]
                        break
                    if (prova > 10) or (pim > 10) or (ava > 10):
                            [sg.popup(f'ERRO! Digite uma nota entre 0 e 10')]
                            break
                    else: 
                        media = prova*7 + pim*2 + ava
                        notaFinal= media/10
                        print(f'Média final: {notaFinal}')
                        break



tela = TelaPython()
tela.Iniciar()
