Captura de Tela e Verificação de Mudanças no Ambiente - PyAutoGUI
Este projeto estendido utiliza a biblioteca PyAutoGUI para não apenas capturar automaticamente a tela, mas também realizar verificações adicionais no ambiente do sistema.

Novas Funcionalidades
Fechamento de Abas e Janelas:
Além de capturar a tela, o script agora fecha todas as abas e janelas abertas no sistema, garantindo uma área de trabalho limpa.

Retorno à Tela Inicial do Windows:
Após as capturas e o fechamento de abas, o script navega de volta à tela inicial do Windows, proporcionando uma base consistente para as futuras análises.

Verificação de Mudanças:
O script realiza uma comparação entre a captura inicial e a captura subsequente, identificando mudanças no ambiente, como adição de aplicativos ou pastas.

Como Usar
Instale as Dependências:
Certifique-se de ter o PyAutoGUI instalado. Você pode instalá-lo usando o seguinte comando:

Copy code
pip install pyautogui
Configure as Opções:
Edite o script para definir o caminho da imagem a ser procurada, o intervalo de tempo entre as capturas, e outras configurações necessárias.

Execute o Script:
Execute o script Python, observando o fechamento de abas, o retorno à tela inicial e a detecção de mudanças no ambiente.

Notas Importantes
Este script é projetado para proporcionar uma visão abrangente das alterações no ambiente do sistema após a execução.

Certifique-se de usar esta ferramenta de maneira ética e em conformidade com as leis e regulamentações locais.