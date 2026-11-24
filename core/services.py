
from datetime import date, datetime
from typing import Tuple

from .models import Espaco, Usuario


class ValidadorReservaService:

    @classmethod
    def validar_direito_retirada(
        cls,
        espaco: Espaco,
        usuario: Usuario,
        dt_referencia: date = None,
        hr_referencia: datetime.time = None
    ) -> Tuple[bool, str]:
        """
        Valida se o usuário possui direito à retirada
        do espaço na data e horário de referência.

        Returns:
            Tuple[bool, str]: (resultado da validação, mensagem)
        """

        pass
