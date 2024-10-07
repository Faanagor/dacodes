from fastapi.testclient import TestClient
from app.main import app

# Inicializar el cliente de prueba
client = TestClient(app)


# def test_proxy():
#     # Simular la prueba del endpoint de proxy
#     response = client.get("/categories/MLA97994")
#     assert response.status_code == 200
#     assert "data" in response.json()  # Cambia según lo que devuelva tu API
#     # proxy


def test_get_conversations():
    # Simular la prueba del endpoint de conversaciones
    response = client.get(
        "/api/conversations?company=microsoft&tags=competition,orientation"
    )
    assert response.status_code == 200
    assert "conversation_ids" in response.json()
