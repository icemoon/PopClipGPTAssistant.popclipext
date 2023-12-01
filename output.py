import os
from common import Resource
import subprocess
from subprocess import Popen, PIPE, call

class Printer:
    content = ""
    type = ""
        #proofreader
        #summary
        #developer

    def __init__(
        self,
        *,
        content: str = None,
        work: str = None):
        self.content = content.replace("\"", "'")
        self.type = work

    def __get_icon_path(self):
        icon_name = Resource.GetIconName(self.type)

        disk_prefix = subprocess.Popen('osascript -e \'path to desktop as text\'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode()
        disk_prefix = disk_prefix.split(':')[0]
        icon_path = disk_prefix + os.getcwd().replace('/', ':') + icon_name
        return icon_path

    def run(self):
        try:
            icon_path = self.__get_icon_path()
            title = Resource.GetPrintTitle(self.type)
            script = f'''
            try
                display dialog "{self.content}" with icon alias "{icon_path}" with title "{title}" buttons {{"Copy", "OK"}} default button 2
                set button to the button returned of the result
                return button
            on error errMsg
                display alert errMsg
            end try
            '''
            p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, text=True)
            stdout, stderr = p.communicate(script)
            if stdout.strip() == "Copy":
                call(('osascript', '-e', f'set the clipboard to "{self.content}"'))
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    p = Printer(content='"Hello, World!", test "out print"', work="proofreader")
    p.run()