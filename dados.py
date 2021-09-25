import random
from rich.console import Console

def Simulador_de_dados():
    console = Console()
    console.print("-*-"*12)
    console.print("[bold green]BEM VINDO AO SIMUDALOR DE DADOS RPG[/]")
    console.print("-*-"*12)
    usuario = console.input("[bold yellow]Deseja jogar dados? [/]")
    console.print("-*-"*12)
    while (
        usuario == "S"
        or usuario == "s"
        or usuario == "N"
        or usuario == "s"
        or usuario != "S"
        or usuario != "s"
        or usuario != "N"
        or usuario != "n"
    ):
        if (
            usuario == "S"
            or usuario == "s"
        ):
            if (
                usuario == "S"
                or usuario == "s"
            ):
                try:
                    quantidade_de_dados = int(console.input("[bold yellow]Digite a quantidade de [bold red]Dados[/]: [/]"))
                    quantidade_de_lados = int(console.input("[bold yellow]Digite a quantidade de [bold red]Lados[/]: [/]"))
                    console.print("-*-"*12)
                    console.print(f"[bold yellow]foi escolhido:[/][bold magenta] {quantidade_de_dados}d{quantidade_de_lados}[/]")
                    valor_maximo = quantidade_de_dados * quantidade_de_lados
                except (ValueError, TypeError):
                    console.print("[bold red]Ocorreu algum erro no tipo de dados que você digitou, tente novamente[/]")
                    console.print("-*-"*12)
                    usuario = console.input("[bold yellow]Deseja jogar dados? [/]")
                else:
                    console.print(f"[bold yellow]O valor minimo é:[/][bold red] {quantidade_de_dados}[/]")
                    console.print(f"[bold yellow]O valor maximo é:[/][bold green] {valor_maximo}[/]")
                    resultado = random.randint(quantidade_de_dados, valor_maximo)
                    console.print("-*-"*12)
                    console.print(f"[bold yellow]O resultado final foi:[/] [bold green]{resultado}[/]")
                    console.print("-*-"*12)
                    usuario = console.input("[bold yellow]Deseja jogar mais dados? [/]")
                    
            elif (
                usuario == "N"
                or usuario == "n"
            ):
                break
            else:
                console.print("-*-"*12)
                console.print("[bold red]Digite [blue]'S'[/] ou [blue]'s'[/] para jogar dados e [blue]'N'[/] ou [blue]'n'[/] para sair[/]")
                console.print("-*-"*12)
                usuario = console.input("[bold yellow]Deseja jogar dados? [/]")
                
        elif (
            usuario == "N"
            or usuario == "n"
        ):
            console.print("[bold yellow]Muito obrigado, Volte Sempre![/]")
            break
        else:
            console.print("[bold red]Digite [blue]'S'[/] ou [blue]'s'[/] para jogar dados e [blue]'N'[/] ou [blue]'n'[/] para sair[/]")
            console.print("-*-"*12)
            usuario = console.input("[bold yellow]Deseja jogar dados? [/]")

Simulador_de_dados()
