
class LCG:
    """
    Classe para gerar números pseudo-aleatórios usando o Linear Congruencial Generator.

    Esta classe mantém um estado interno que é atualizado a cada chamada
    do método .next(), gerando um fluxo contínuo de números.
    """
    def __init__(self, seed, multiplier, increment, modulus):
        """
        Inicializa o gerador LCG com os seus parâmetros.
        
        Args:
            seed (int): O valor inicial da seed.
            multiplier (int): O multiplicador (a).
            increment (int): O incremento (c).
            modulus (int): O módulo (m).
        """
        self.seed = seed
        self.state = seed
        self.a = multiplier
        self.c = increment
        self.m = modulus

    def next(self):
        """ Calcula e retorna o próximo número da sequência. """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state