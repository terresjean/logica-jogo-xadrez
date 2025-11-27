# logica_xadrez.py

class Peca:
    def __init__(self, cor):
        self.cor = cor

    def movimentos_validos(self, pos, tabuleiro):
        return []

class Rei(Peca):
    def movimentos_validos(self, pos, tabuleiro):
        movimentos = []
        direcoes = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        x, y = pos
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[ny][nx]
                if destino is None or destino.cor != self.cor:
                    movimentos.append((nx, ny))
        return movimentos

class Torre(Peca):
    def movimentos_validos(self, pos, tabuleiro):
        movimentos = []
        direcoes = [(1,0),(-1,0),(0,1),(0,-1)]
        x, y = pos
        for dx, dy in direcoes:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    break
                destino = tabuleiro[ny][nx]
                if destino is None:
                    movimentos.append((nx, ny))
                else:
                    if destino.cor != self.cor:
                        movimentos.append((nx, ny))
                    break
        return movimentos

class Tabuleiro:
    def __init__(self):
        self.tab = [[None for _ in range(8)] for _ in range(8)]
        self.iniciar()

    def iniciar(self):
        # Exemplo: colocar apenas dois Reis e duas Torres
        self.tab[0][4] = Rei("preto")
        self.tab[7][4] = Rei("branco")
        self.tab[0][0] = Torre("preto")
        self.tab[7][0] = Torre("branco")

    def mover(self, origem, destino):
        ox, oy = origem
        dx, dy = destino
        p = self.tab[oy][ox]
        if p is None:
            return False
        if destino in p.movimentos_validos(origem, self.tab):
            self.tab[dy][dx] = p
            self.tab[oy][ox] = None
            return True
        return False

    def mostrar(self):
        for linha in self.tab:
            print(['.' if p is None else type(p).__name__[0] for p in linha])
        print()

if __name__ == "__main__":
    t = Tabuleiro()
    t.mostrar()
    print("Movendo torre branca de (0,7) para (0,5)")
    t.mover((0,7), (0,5))
    t.mostrar()
