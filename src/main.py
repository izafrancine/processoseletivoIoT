import machine
import time

led_r = machine.Pin(15, machine.Pin.OUT)
led_g = machine.Pin(14, machine.Pin.OUT)
led_b = machine.Pin(13, machine.Pin.OUT)


button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)


cores = [
    (0, 0, 0), # 0: Apagado
    (1, 0, 0), # 1: Vermelho
    (0, 1, 0), # 2: Verde
    (0, 0, 1), # 3: Azul
    (1, 1, 0), # 4: Amarelo
    (0, 1, 1), # 5: Ciano
    (1, 0, 1), # 6: Magenta
    (1, 1, 1), # 7: Branco
]

indice_cor = 0

def aplicar_cor(indice):
    """Aplica os valores digitais aos pinos do LED RGB."""
    r, g, b = cores[indice]
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)


aplicar_cor(indice_cor)
estado_anterior_botao = 1

print("Controle de Eletricidade/Cores iniciado!")
print("Pressione o botão para mudar a cor do LED RGB.")


while True:
    estado_atual_botao = button.value()

   
    if estado_anterior_botao == 1 and estado_atual_botao == 0:
       
        indice_cor = (indice_cor + 1) % len(cores)
        aplicar_cor(indice_cor)
        print(f"Eletricidade alterada! Índice de cor atual: {indice_cor}")
        
       
        time.sleep(0.2)

    estado_anterior_botao = estado_atual_botao
    time.sleep(0.05) 