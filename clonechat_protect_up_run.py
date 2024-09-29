from rich.console import Console
from rich.panel import Panel
from protect_content import clonechat_protect_up

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]Clonechat Protect Upload[/bold cyan]",
        border_style="bold"
    ))
    clonechat_protect_up.main()

if __name__ == '__main__':
    main()