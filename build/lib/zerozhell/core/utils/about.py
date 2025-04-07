import platform

def about():
    s_color = "\033[92m" if platform.system() != "Windows" else ""
    e_color = "\033[0m" if platform.system() != "Windows" else ""
    about = f"""{s_color}
    
            ZeroZhell Framework
            Author : Calvin Ronksley
            Contact : hexzhen3x7@blackzspace.de XOR blackzspace.de@outlook.de
            Codename : Infinity
            Github-Repo : https://github.com/faultybytehunterz/zerozhell
            Organisation : https://github.com/faultybytehunterz
            IRC: https://irc.blackzspace.de/+6679
            
    {e_color}"""
    print(about)