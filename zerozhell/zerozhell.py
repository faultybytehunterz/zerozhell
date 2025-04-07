#!/usr/bin/python3
# check dependencies before start
from .core.utils import check_dependencies
check_dependencies()

import cmd
import os
import sys
import time
import subprocess
from .mods import *
from .mods import module_list, all_modules
from .core.utils import logo, about, update


completions = module_list()


class MainCommandLine(cmd.Cmd):
    # check for update
    # update(where="main_menu")

    intro = logo()

    prompt = 'zerozhell > '
    doc_header = 'Commands'
    undoc_header = 'Undocumented Commands'
    
    
    
    
    

    def do_use(self, line):
        """Select module for modules"""
        if line in module_list():

            module = globals()[line]
            if hasattr(module, 'Main'):
                module = module.Main()
                module.prompt = f"zerozhell > {line} > "
                module.cmdloop()
            else:
                print(f"*** Module `{module}` not has `Main` class!")

        else:
            print(f"*** Module {line} not found!")



    def do_show(self, line):
        """Show available modules"""
        all_modules()




    




    def complete_use(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in completions if s.startswith(mline)]
    
    
    

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: 
            func[0](arg)
        else:
            os.system(line)
            
            
            

    def do_about(self, line):
        """About Us"""
        about()
        
        
        

    def do_update(self, line):
        """Check for update"""
        update(where="update_command")
        
        

            
    def do_exit(self, line):
        """Exit"""
        sys.exit(0)
        return True
    
    def do_help(self, line):
        """Show help"""
        if line:
            try:
                cmd, arg, line = self.parseline(line)
                func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
                if func: 
                    func[0](arg)
                else:
                    os.system(line)
            except Exception as e:
                print(f"*** {e}")
        else:
            super().do_help(line)
            
            
    def help_print(self):
        """Print help"""
        print("Print help")
        print("Example: print <message>")


def loop():
    try:
        MainCommandLine().cmdloop()
    except KeyboardInterrupt:
        print("\nBye!")

if __name__ == '__main__':
    loop()