# Processo Seletivo – Intensivo Maker | IoT
## Relatório do Candidato

**Nome Completo:** Iza Francine Carvalho Vieira

---

## Arquitetura do Sistema Embarcado

Implementei uma arquitetura de controle de eletricidade baseada em **leitura de botões físicos e acionamento de LEDs**, otimizada para resposta rápida e baixo consumo de energia. A estrutura segue o fluxo:

- **Entrada:** 3 botões de pressão conectados aos pinos GPIO da Raspberry Pi Pico (pull-up interno).
- **Lógica de Controle:**
  - Leitura digital dos botões com **debounce por tempo** (200 ms) para evitar leituras falsas.
  - Estado atual da cor armazenado implicitamente (apenas um LED aceso por vez).
- **Saída:** 3 LEDs (vermelho, verde, azul) com resistores de 220 Ω, acionados conforme a seleção.

O diagrama de estados é simples:

- **Estado inicial:** todos os LEDs apagados.
- **Botão vermelho pressionado** → acende LED vermelho, apaga os demais.
- **Botão verde pressionado** → acende LED verde, apaga os demais.
- **Botão azul pressionado** → acende LED azul, apaga os demais.

A simulação é executada automaticamente via **GitHub Actions** com o **Wokwi CLI**.

---

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas para o desenvolvimento deste desafio foram:

- `machine` (MicroPython) – controle dos pinos GPIO e interfaces de baixo nível.
- `time` (MicroPython) – implementação do debounce e temporizações.
- (Opcional) `Wokwi CLI` e `GitHub Actions` – para execução automatizada da simulação.

Nenhuma biblioteca externa além da biblioteca padrão do MicroPython foi necessária, garantindo leveza e compatibilidade com microcontroladores de baixo custo.

---

## Técnica de Otimização do Sistema

Apliquei uma técnica para garantir **robustez e eficiência** no sistema embarcado:

2. **Pull-up interno da Raspberry Pi Pico**  
   Configuração `Pin.IN, Pin.PULL_UP` para dispensar resistores externos nos botões, reduzindo a contagem de componentes e simplificando o circuito.

O objetivo principal alcançado com essas abordagens foi garantir **estabilidade na leitura** e **confiabilidade na atuação dos LEDs**, mesmo em simulações com variações de tempo (típicas do Wokwi). 

---

## Resultados Obtidos

O sistema foi simulado com sucesso no ambiente **Wokwi** (Raspberry Pi Pico + MicroPython). Após os commits no repositório, o pipeline do **GitHub Actions** executou o `wokwi-cli` e validou:

- Inicialização correta do hardware virtual.
- Leitura consistente dos botões (sem bouncing).
- Acendimento exclusivo do LED correspondente ao botão pressionado.
- Ausência de travamentos ou loops infinitos.

O projeto completo foi integrado à esteira de CI/CD e está pronto para **deploy em hardware real** com mínimas alterações (apenas ajuste de pinos físicos).

---

O processo reforçou a importância de **testes automatizados em simulação** antes da implantação em hardware físico. Utilizei o Wokwi CLI para validar o comportamento do sistema de forma reprodutível, o que é essencial em projetos colaborativos.

Além disso, graças aos meus estudos anteriores em **sistemas embarcados e CI/CD**, consegui estruturar um código simples, mas profissional, com:
- Debounce eficiente.
- Uso correto de pull-ups internos.
- Pipeline de integração contínua com secrets (proteção da API key do Wokwi).

Essa experiência me mostrou como pequenos detalhes (como o tratamento de bouncing) são cruciais para a confiabilidade de um produto eletrônico. Fiquei satisfeita em ver o LED acender corretamente cada vez que o botão virtual era pressionado na simulação – foi como “ver a mágica acontecer” no mundo embarcado.
