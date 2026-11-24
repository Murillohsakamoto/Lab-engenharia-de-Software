IDADE_MINIMA_ADOTANTE = 18


def pode_adotar(idade_adotante: int) -> bool:
    return idade_adotante >= IDADE_MINIMA_ADOTANTE


def filtrar_por_especie(pets, especie: str):
    return [p for p in pets if p.especie.lower() == especie.lower()]


def buscar_por_nome(pets, termo: str):
    termo = termo.strip().lower()
    return [p for p in pets if termo in p.nome.lower()]
