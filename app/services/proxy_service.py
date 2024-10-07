import httpx


async def proxy_request(category_id: str):
    url = f"https://cualquierapi.com/categories/{category_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": "Error fetching data from the external API"
            }, response.status_code
