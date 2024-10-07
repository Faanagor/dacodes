from fastapi import HTTPException


async def get_conversations(company: str, tags: str):
    # Simulando la recuperación de datos de conversaciones basadas en filtros

    if company == "microsoft":
        conversation_ids = ["conv-123", "conv-456", "conv-789"]
        tags_list = tags.split(",")

        # Simular lógica de filtrado (aquí puedes agregar tu lógica real)
        if "competition" in tags_list:
            # Filtros aplicados
            return {
                "conversation_ids": conversation_ids,
                "total": len(conversation_ids),
                "page": 1,
                "per_page": 50,
            }

    raise HTTPException(
        status_code=404, detail="No conversations found for the given filters."
    )
