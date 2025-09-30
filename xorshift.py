class Xorshift64:
    """
    Classe para gerar números pseudo-aleatórios usando o algoritmo Xorshift64.
    
    Esta implementação requer uma seed inicial diferente de zero.
    """
    def __init__(self, seed):
        """
        Inicializa o gerador Xorshift64.
        
        Args:
            seed (int): O valor inicial da seed. Não pode ser zero.
        """
        self.seed = seed if seed != 0 else 1
        self.state = self.seed
    
    def next(self):
        """
        Calcula e retorna o próximo número da sequência usando a variante xorshift64.
        """
        x = self.state
        x ^= x << 13
        x &= 0xFFFFFFFFFFFFFFFF # Garante 64 bits
        x ^= x >> 7
        x ^= x << 17
        x &= 0xFFFFFFFFFFFFFFFF # Garante 64 bits
        
        self.state = x
        return self.state