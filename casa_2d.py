import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Inicialização do Pygame e OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Casa 2D com Ciclo Dia/Noite')

# Variáveis globais
is_day = True
# Gerar mais estrelas para uma noite mais realista
stars = [(random.uniform(-1, 1), random.uniform(0, 1)) for _ in range(100)]

def draw_rectangle(x1, y1, x2, y2):
    """Desenha um retângulo usando coordenadas dos vértices"""
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    """Desenha um triângulo usando coordenadas dos vértices"""
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def draw_circle(x, y, radius, segments=30):
    """Desenha um círculo usando um polígono com o número especificado de segmentos"""
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(segments + 1):
        angle = 2.0 * math.pi * i / segments
        glVertex2f(x + math.cos(angle) * radius, y + math.sin(angle) * radius)
    glEnd()

def draw_cloud(x, y):
    """Desenha uma nuvem usando círculos sobrepostos"""
    glColor3f(1.0, 1.0, 1.0)  # Branco para as nuvens
    # Nuvem principal
    draw_circle(x, y, 0.1)
    # Círculos adicionais para dar volume à nuvem
    draw_circle(x + 0.1, y, 0.08)
    draw_circle(x - 0.1, y, 0.08)
    draw_circle(x + 0.05, y + 0.05, 0.07)
    draw_circle(x - 0.05, y + 0.05, 0.07)

def draw_background():
    """Desenha o fundo (céu e chão) com ciclo dia/noite"""
    if is_day:
        # Céu diurno (gradiente de azul claro para azul mais escuro)
        glBegin(GL_QUADS)
        glColor3f(0.529, 0.808, 0.922)  # Azul claro no topo
        glVertex2f(-1.0, 1.0)
        glVertex2f(1.0, 1.0)
        glColor3f(0.678, 0.847, 0.902)  # Azul um pouco mais escuro embaixo
        glVertex2f(1.0, 0.0)
        glVertex2f(-1.0, 0.0)
        glEnd()

        # Chão (gradiente de verde escuro para verde mais claro)
        glBegin(GL_QUADS)
        glColor3f(0.196, 0.804, 0.196)  # Verde claro em cima
        glVertex2f(-1.0, 0.0)
        glVertex2f(1.0, 0.0)
        glColor3f(0.0, 0.502, 0.0)  # Verde escuro embaixo
        glVertex2f(1.0, -1.0)
        glVertex2f(-1.0, -1.0)
        glEnd()

        # Sol
        glColor3f(1.0, 1.0, 0.0)  # Amarelo
        draw_circle(0.7, 0.7, 0.1)

        # Nuvens
        draw_cloud(-0.3, 0.7)
        draw_cloud(0.3, 0.8)
        draw_cloud(-0.6, 0.6)
    else:
        # Céu noturno (gradiente de azul escuro para preto)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.1)  # Azul escuro no topo
        glVertex2f(-1.0, 1.0)
        glVertex2f(1.0, 1.0)
        glColor3f(0.0, 0.0, 0.0)  # Preto embaixo
        glVertex2f(1.0, 0.0)
        glVertex2f(-1.0, 0.0)
        glEnd()

        # Chão noturno (gradiente de verde muito escuro para verde escuro)
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.2, 0.0)  # Verde muito escuro em cima
        glVertex2f(-1.0, 0.0)
        glVertex2f(1.0, 0.0)
        glColor3f(0.0, 0.1, 0.0)  # Verde ainda mais escuro embaixo
        glVertex2f(1.0, -1.0)
        glVertex2f(-1.0, -1.0)
        glEnd()

        # Lua
        glColor3f(0.9, 0.9, 0.9)  # Cinza claro
        draw_circle(-0.7, 0.7, 0.08)

        # Estrelas (mais numerosas e com diferentes tamanhos)
        glColor3f(1.0, 1.0, 1.0)  # Branco
        for star in stars:
            # Varia o tamanho das estrelas
            size = random.uniform(1.0, 3.0)
            glPointSize(size)
            glBegin(GL_POINTS)
            glVertex2f(star[0], star[1])
            glEnd()

def draw_house():
    """Desenha a casa com parede lateral, porta, janelas e telhado"""
    # Parede frontal (azul escuro)
    glColor3f(0.0, 0.0, 0.5)
    draw_rectangle(-0.5, -0.5, 0.5, 0.3)

    # Parede lateral (azul mais escuro para dar profundidade)
    glColor3f(0.0, 0.0, 0.4)  # Azul um pouco mais escuro
    glBegin(GL_QUADS)
    glVertex2f(0.5, -0.5)   # Base direita da parede frontal
    glVertex2f(0.8, -0.4)   # Base da parede lateral
    glVertex2f(0.8, 0.3)    # Topo da parede lateral
    glVertex2f(0.5, 0.3)    # Topo direita da parede frontal
    glEnd()

    # Telhado (telhas em tons de vermelho)
    # Telhado frontal (triângulo principal)
    glBegin(GL_TRIANGLES)
    # Gradiente de vermelho para o telhado
    glColor3f(0.6, 0.1, 0.1)  # Vermelho escuro no topo
    glVertex2f(0.0, 0.6)     # Ponto do topo (centralizado)
    glColor3f(0.8, 0.2, 0.2)  # Vermelho mais claro na base
    glVertex2f(-0.5, 0.3)    # Ponto esquerdo da base
    glVertex2f(0.5, 0.3)     # Ponto direito da base
    glEnd()
    
    # Telhado lateral (trapézio)
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.2, 0.2)  # Vermelho mais claro
    glVertex2f(0.5, 0.3)     # Ponto onde encontra a parede frontal
    glVertex2f(0.8, 0.3)     # Ponto onde encontra a parede lateral
    glColor3f(0.7, 0.15, 0.15)  # Vermelho um pouco mais escuro
    glVertex2f(0.65, 0.6)    # Ponto alto da lateral (ajustado para alinhar com o topo central)
    glVertex2f(0.0, 0.6)     # Ponto do topo do telhado frontal
    glEnd()

    # Linhas do telhado para simular telhas
    glColor3f(0.5, 0.1, 0.1)  # Vermelho mais escuro para as linhas
    glLineWidth(1.0)
    # Linhas horizontais no telhado frontal
    for i in range(5):
        y = 0.3 + (i * 0.06)
        x1 = -0.5 + (i * 0.1)
        x2 = 0.5 - (i * 0.1)
        glBegin(GL_LINES)
        glVertex2f(x1, y)
        glVertex2f(x2, y)
        glEnd()

    # Chaminé
    glColor3f(0.3, 0.3, 0.3)  # Cinza para a chaminé
    draw_rectangle(0.2, 0.5, 0.3, 0.7)
    # Topo da chaminé
    glColor3f(0.4, 0.4, 0.4)
    draw_rectangle(0.15, 0.7, 0.35, 0.72)

    # Porta (roxa)
    glColor3f(0.5, 0.0, 0.5)
    draw_rectangle(-0.15, -0.5, 0.15, 0.0)

    # Maçaneta da porta
    glColor3f(0.0, 1.0, 1.0)  # Ciano
    draw_circle(0.1, -0.25, 0.02)

    # Janelas (verde claro)
    glColor3f(0.0, 0.8, 0.8)
    # Janela esquerda (frontal)
    draw_rectangle(-0.4, -0.2, -0.2, 0.0)
    # Cruz da janela frontal
    glColor3f(0.0, 0.4, 0.4)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(-0.3, -0.2)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.4, -0.1)
    glVertex2f(-0.2, -0.1)
    glEnd()

    # Janela direita (frontal)
    glColor3f(0.0, 0.8, 0.8)
    draw_rectangle(0.2, -0.2, 0.4, 0.0)
    # Cruz da janela direita
    glColor3f(0.0, 0.4, 0.4)
    glBegin(GL_LINES)
    glVertex2f(0.3, -0.2)
    glVertex2f(0.3, 0.0)
    glVertex2f(0.2, -0.1)
    glVertex2f(0.4, -0.1)
    glEnd()

def main():
    """Função principal do programa que gerencia o loop de renderização e eventos"""
    global is_day
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    is_day = True
                elif event.key == pygame.K_n:
                    is_day = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_background()
        draw_house()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main() 