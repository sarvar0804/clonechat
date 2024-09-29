from rich.console import Console
from rich.panel import Panel
from protect_content import clonechat_protect_down

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]Clonechat Protect Download[/bold cyan]",
        border_style="bold"
    ))
    clonechat_protect_down.main()

if __name__ == "__main__":
    main()
