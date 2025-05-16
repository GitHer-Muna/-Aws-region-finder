import httpx

async def validate_country(country: str) -> bool:
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            resp = await client.get(f"https://restcountries.com/v3.1/name/{country}")
            return resp.status_code == 200
        except httpx.RequestError as e:
            print(f"x Failed to fetch country: {country} — {e}")
            # print(f"Request failed: {e}")
            return False
