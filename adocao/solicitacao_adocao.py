from enum import Enum

from adocao.adocao import IDADE_MINIMA_ADOTANTE, pode_adotar


class Status(Enum):
    PENDENTE = "PENDENTE"
    APROVADA = "APROVADA"
    RECUSADA = "RECUSADA"


class SolicitacaoAdocao:
    def __init__(self, pet, nome_adotante: str, idade_adotante: int):
        if not pode_adotar(idade_adotante):
            raise ValueError(
                f"Adotante precisa ter pelo menos {IDADE_MINIMA_ADOTANTE} anos."
            )
        self.pet = pet
        self.nome_adotante = nome_adotante
        self.status = Status.PENDENTE

    def aprovar(self):
        self._validar_pendente()
        self.status = Status.APROVADA

    def recusar(self):
        self._validar_pendente()
        self.status = Status.RECUSADA

    def _validar_pendente(self):
        if self.status != Status.PENDENTE:
            raise RuntimeError(f"Solicitação já foi {self.status.value}.")
