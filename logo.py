# You've to install pyfiglet colorama to install this just write in bash shell "pip install pyfiglet colorama"  
import pyfiglet
from colorama import init, Fore, Style
import shutil

init(autoreset=True)

def print_centered_cipherx_404(text="CipherX_404", font="slant", fg=Fore.CYAN, bright=True):
    banner = pyfiglet.figlet_format(text, font=font)
    style = Style.BRIGHT if bright else Style.NORMAL
    
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    
    centered_lines = []
    for line in banner.splitlines():
        centered_line = line.center(terminal_width)
        centered_lines.append(centered_line)
        
    colored_banner = style + fg + "\n".join(centered_lines) + Style.RESET_ALL
    print(colored_banner)

if __name__ == "__main__":
    print_centered_cipherx_404()
