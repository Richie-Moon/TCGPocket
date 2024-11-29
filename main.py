from tcgdexsdk import TCGdex
import asyncio

tcgdex = TCGdex("en") # You can also use `Language.EN` TCGdex(Language.EN)

async def test():
    res = await tcgdex.set.get("P-A")
    print(res)


asyncio.run(test())