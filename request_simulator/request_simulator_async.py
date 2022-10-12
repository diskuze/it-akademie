import asyncio
from readchar import readchar
import random

"""
Návod: Základem asynchronního řešení je, že existuje producer requestů a několik consumerů,
mezi kterými se přepíná. A pokud jeden consumer zrovna řeší nějakou I/O operaci, předá
řízení event loop a ta přepne do jiného consumera nebo producera.

TODO:
- Vytvořte si novou asynchronní frontu asyncio.Queue(), do které budou producenti zapisovat, consumeři číst
- Vytvořte producenta, který do fronty bude zapisovat "requesty". V našem případě číslo requestu
- Vytvořte si několik consumerů (ve webovém slovníků se jim často říká workers), které budou requesty z fronty číst
  a asynchronně zpracovávat. Consumer bude simulovat I/O operaci (například dotaz do datbáze) pomocí asyncio.sleep().
- "Ukliďte" - Task.cancel(), Queue.join(), ...

Zkuste si program spustit. Správně by vám měl nyní dovolit zmáčknout mezerník několikrát za sebou a odpovědi jednotlivých
requestů byste měli získat v různém pořadí.
"""

async def main():
    request_counter = 0

    # producer
    while(readchar() == " "):
        request_counter += 1


if __name__ == "__main__":
    asyncio.run(main())
