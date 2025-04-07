from colorama import Fore, Back, Style


color_map = {
    'r': Fore.RED,
    'g': Fore.GREEN,
    'b': Fore.BLUE,
    'y': Fore.YELLOW,
    'm': Fore.MAGENTA,
    'c': Fore.CYAN,
    'w': Fore.WHITE,
    'k': Fore.BLACK,
    'n': Fore.BLACK, 
    
    'R': Fore.LIGHTRED_EX,
    'G': Fore.LIGHTGREEN_EX,
    'B': Fore.LIGHTBLUE_EX,
    'Y': Fore.LIGHTYELLOW_EX,
    'M': Fore.LIGHTMAGENTA_EX,
    'C': Fore.LIGHTCYAN_EX,
    'W': Fore.LIGHTWHITE_EX,
    'K': Fore.LIGHTBLACK_EX,  
    
    'br': Back.RED,
    'bg': Back.GREEN,
    'bb': Back.BLUE,
    'by': Back.YELLOW,
    'bm': Back.MAGENTA,
    'bc': Back.CYAN,
    'bw': Back.WHITE,
    'bk': Back.BLACK,
    'bn': Back.BLACK,  
    
    'bR': Back.LIGHTRED_EX,
    'bG': Back.LIGHTGREEN_EX,
    'bB': Back.LIGHTBLUE_EX,
    'bY': Back.LIGHTYELLOW_EX,
    'bM': Back.LIGHTMAGENTA_EX,
    'bC': Back.LIGHTCYAN_EX,
    'bW': Back.LIGHTWHITE_EX,
    'bK': Back.LIGHTBLACK_EX,
}

def p(text):
    """ Funktion für Farben und Neon-Farben """
    for key, value in color_map.items():
        text = text.replace(key, value)
    print(text + Style.RESET_ALL)  

def p_help():
    """ Gibt alle Farb-Kürzel mit Farbkombinationen aus """
    for key, (color_code, description) in color_map.items():
        print(f"{key}: {description}")
        print(f"  Beispiel: {color_code}{key}This is an example{Style.RESET_ALL}")
        print()
        
p("BC HELLO")
