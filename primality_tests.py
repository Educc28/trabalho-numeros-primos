import random

def fermat_primality_test(n, k=40):
    """
    Executa o teste de primalidade de Fermat.

    Args:
        n (int): O número a ser testado.
        k (int): O número de rodadas para testar. Aumentar k aumenta a precisão.
    
    Returns:
        bool: True se n é provavelmente primo, False se n é composto.
    """
    # Casos base
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Executa o teste k vezes com bases 'a' diferentes
    for _ in range(k):
        a = random.randrange(2, n - 2)

        # Verifica se a^(n-1) % n == 1
        if pow(a, n - 1, n) != 1:
            return False # n é definitivamente composto

    # Se passou em todos os testes, é provavelmente primo
    return True

def miller_rabin(n, k=40):
    """
    Executa o teste de primalidade de Miller-Rabin.
    
    Args:
        n (int): O número a ser testado.
        k (int): O número de rodadas para o teste. Aumentar k aumenta a precisão.
        
    Returns:
        bool: True se n é provavelmente primo, False se n é composto.
    """
    # Casos base
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Executa o teste k vezes
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
            
    return True