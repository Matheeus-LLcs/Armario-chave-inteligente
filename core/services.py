
from datetime import date, datetime
from typing import Tuple
from uuid import UUID

from .models import Espaco, Usuario
from supabase import Client


class ValidadorReservaService:

    @classmethod
    def validar_direito_retirada(
        cls,
        espaco: Espaco,
        usuario: Usuario,
        dt_referencia: date = None,
        hr_referencia: datetime.time = None
    ) -> Tuple[bool, str]:

        try:
            supabase: Client = cls.supabase

            p_uuid_armario = espaco.chave_armario_id

            # Consulta a hierarquia de reservas no Supabase
            resultado = (
                supabase
                .table("hierarquia_reservas")
                .select("*")
                .in_(
                    "tipo",
                    ["Remanejamento", "Pontual", "Fixa"]
                )
                .execute()
            )

            return True, "Consulta realizada com sucesso."

        except Exception as e:
            return False, f"Erro ao validar retirada: {str(e)}"
