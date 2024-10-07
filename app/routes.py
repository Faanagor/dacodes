from fastapi import APIRouter

from app.services.proxy_service import proxy_request
from app.services.conversation_service import get_conversations
from app.models.conversation_model import ConversationResponse

router = APIRouter()


# Ruta para manejar el proxy
@router.get("/categories/{category_id}")
async def proxy(category_id: str):
    return await proxy_request(category_id)


# Ruta para obtener conversaciones
@router.get("/api/conversations", response_model=ConversationResponse)
async def conversations(company: str, tags: str):
    return await get_conversations(company, tags)
