# Casa 2D com Ciclo Dia/Noite
**Computação Gráfica e Processamento de Imagens**

**Aluno:** Eduardo Esplinio  
**Matrícula:** 06003445

## Assuntos
- Formas geométricas em 2D
- Primitivas OpenGL
- Interação com teclado
- Simulação de ambiente (dia/noite)

## Descrição
Este projeto implementa uma casa 2D usando OpenGL em Python, com simulação de ciclo dia/noite. O projeto demonstra o uso de primitivas básicas do OpenGL para criar uma cena interativa.

## Estrutura do Projeto
```
.
├── README.md
├── requirements.txt
└── casa_2d.py
```

## Requisitos
- Python 3.x
- PyOpenGL
- Pygame

## Instalação
1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar
```bash
python casa_2d.py
```

### Controles
- Tecla 'D': Ativa o modo dia
- Tecla 'N': Ativa o modo noite
- Fechar a janela: Encerra o programa

## Detalhes da Implementação

### Elementos da Casa
- Parede frontal e lateral
- Porta com maçaneta
- Duas janelas com cruzes
- Telhado com telhas
- Chaminé

### Ambiente
- Céu com gradiente de cores
- Chão com gradiente de verde
- Nuvens durante o dia
- Sol durante o dia
- Lua e estrelas durante a noite

### Funcionalidades
- Alternância entre dia e noite
- Gradientes de cores no céu e chão
- Estrelas com tamanhos variados
- Nuvens com volume
- Telhado com detalhes de telhas 