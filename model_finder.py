import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import quote

SOURCES = [
    "https://www.google.com/search?tbm=isch&q=3d+model+",
    "https://www.bing.com/images/search?q=3d+model+",
    "https://yandex.com/images/search?text=3d+model+",
]


async def find_3d_models(query):
    results = []
    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession(headers=headers) as session:
        for source in SOURCES:
            try:
                url = source + quote(query)

                async with session.get(url, timeout=15) as response:
                    html = await response.text()

                soup = BeautifulSoup(html, "html.parser")

                for a in soup.find_all("a", href=True):
                    href = a["href"]

                    if any(
                        ext in href.lower()
                        for ext in [".max", ".fbx", ".obj", ".blend", ".3ds"]
                    ):
                        results.append(
                            {
                                "title": a.get_text(" ", strip=True) or "3D Model",
                                "url": href,
                                "source": source.split("/")[2],
                            }
                        )

            except Exception:
                continue

    return results