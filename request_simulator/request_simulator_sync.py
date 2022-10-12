import time
from readchar import readchar
import random

def handle_request(counter):
    """
    TODO:
    - Doplňte funkci tak, aby vždy vypsala na standardní výstup:
      > Request #{counter} start ({wait_interval}s)
      počkala náhodně wait_interval (1-5) sekund, čím budeme simulovat například
      nějaký pomalý dotaz do databáze a potom vypsala:
      > "Request #{counter} end"
    """
    pass

def main():
    counter = 0
    while True:
        if readchar() == " ":
            counter += 1
            handle_request(counter)
        time.sleep(0.01)

if __name__ == '__main__':
    main()
