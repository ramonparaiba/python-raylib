# 📚 Estudos de Raylib em Python

Repositório dedicado aos meus estudos e experimentos com a biblioteca **Raylib** utilizando **Python**. Aqui você encontrará projetos, exemplos, anotações e recursos relacionados ao desenvolvimento de jogos e aplicações multimídia com essa poderosa biblioteca.

![Raylib Logo](https://github.com/raysan5/raylib/blob/master/logo/raylib_180x180.png)  
*(Se quiser, adicione uma imagem ou banner personalizado)*

## 🚀 Sobre o Raylib

[Raylib](https://www.raylib.com/) é uma biblioteca simples e fácil de usar para desenvolvimento de jogos e aplicações gráficas, com bindings para Python através do [raylib-python](https://github.com/overdev/raylib-py). Ela é perfeita para prototipagem rápida e aprendizado de conceitos de programação de jogos.

## 📂 Estrutura do Repositório
/estudos-raylib-python/
│
├── /exemplos-basicos/ - Códigos introdutórios e conceitos fundamentais ✅
├── /projetos/ - Projetos completos ou em desenvolvimento 🔄
├── /anotacoes/ - Notas, tutoriais e referências úteis 🔄
├── /recursos/ - Assets, imagens, fonts usadas nos projetos 🔄
└── /desafios/ - Pequenos desafios ou exercícios 🔄


## 🛠️ Como Usar

1. **Pré-requisitos**:
   - Python 3.x instalado
   - Biblioteca raylib para Python:
     ```bash
     pip install raylib
     ```

2. **Clonar o repositório**:
   ```bash
   git clone https://github.com/ramonparaiba/python-raylib

## ✨ Exemplo Básico
Aqui está um trecho de código simples para começar:

``from pyray import *
init_window(800, 450, "Tela em branco")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Primeira tela Raylib", 190, 200, 20, VIOLET)
    end_drawing()
close_window() ``

## 📚 Recursos de Aprendizado
* Documentação Oficial do Raylib
- raylib-python no GitHub
- Exemplos Oficiais (em C, mas úteis)
- Livro "Learn Raylib" (em inglês)

## 🤝 Como Contribuir
#### Sinta-se à vontade para:
- Reportar issues
- Sugerir melhorias
- Enviar pull requests com exemplos adicionais

## 📄 Licença
Este projeto está sob a licença GPL-3.0 license - veja o arquivo LICENSE para detalhes.

