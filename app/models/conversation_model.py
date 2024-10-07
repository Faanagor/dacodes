from typing import List
from pydantic import BaseModel


class ConversationResponse(BaseModel):
    conversation_ids: List[str]
    total: int
    page: int
    per_page: int
