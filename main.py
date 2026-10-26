
# Calculaturation #
# Version 1.0 #

#\\ Variables //#

from rich import print
from rich.panel import Panel
from rich.console import Console
import math
import time
import os

console = Console()

#\\ Variables //#


# --//--\/--//-- #

#\\ Functions //#


def Clean():
    os.system("cls" if os.name == "nt" else "clear")


def Pythagorean_Cal():
    a = float(console.input("[bold green] Primeiro cateto: [/bold green]"))
    b = float(console.input("[bold green] Segundo cateto: [/bold green]"))

    result = math.hypot(a, b)

    print(f"[bold cyan]Result: {result}[/bold cyan]")


def Sum():
    num1 = float(console.input("[bold green] Primeiro número: [/bold green]"))
    num2 = float(console.input("[bold green] Segundo número: [/bold green]"))

    result = num1 + num2
    print(f"[bold cyan]Result: {result}[/bold cyan]")


def Subtract():
    num1 = float(console.input("[bold green] Primeiro número: [/bold green]"))
    num2 = float(console.input("[bold green] Segundo número: [/bold green]"))

    result = num1 - num2
    print(f"[bold cyan]Result: {result}[/bold cyan]")


def Divide():
    num1 = float(console.input("[bold green] Primeiro número: [/bold green]"))
    num2 = float(console.input("[bold green] Segundo número: [/bold green]"))

    if num2 == 0:
        print("[bold red]Não é possível dividir por zero.[/bold red]")
        return

    result = num1 / num2
    print(f"[bold cyan]Result: {result}[/bold cyan]")


def Multiply():
    num1 = float(console.input("[bold green] Primeiro número: [/bold green]"))
    num2 = float(console.input("[bold green] Segundo número: [/bold green]"))

    result = num1 * num2
    print(f"[bold cyan]Result: {result}[/bold cyan]")


#\\ Main //#

def Main():
    Clean()

    print(Panel.fit("[bold cyan]Calculaturation[/bold cyan]"))
    print("[bold cyan]Welcome to Calculaturation[/bold cyan]")
    print("[bold cyan]By Davi Lucas[/bold cyan]")
    print("[bold cyan]Version 1.0[/bold cyan]")
    print()

    console.input("[bold cyan]Press Enter to boot[/bold cyan]")
    time.sleep(1)

    while True:
        Clean()

        print(Panel.fit("[bold cyan]Calculaturation[/bold cyan]"))
        print("[bold cyan]Pythagorean, Sum, Subtract, Divide, Multiply, Exit[/bold cyan]")
        print()

        name = console.input("[bold green]Name: [/bold green]").strip().lower()

        try:
            if name == "pythagorean":
                Pythagorean_Cal()

            elif name == "sum":
                Sum()

            elif name == "subtract":
                Subtract()

            elif name == "divide":
                Divide()

            elif name == "multiply":
                Multiply()

            elif name == "exit":
                print("[bold cyan]Closing Calculaturation...[/bold cyan]")
                break

            else:
                print("[bold red]Operação não encontrada.[/bold red]")

        except ValueError:
            print("[bold red]Digite números válidos.[/bold red]")

        console.input("\n[bold cyan]Press Enter to continue[/bold cyan]")


if __name__ == "__main__":
    Main()
