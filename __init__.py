import os
from cudatext import *
import urllib
import re
from urllib import parse, request
from urllib.parse import urljoin

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_html_live_preview.ini')

def show(text):
    #abs_url = "C:\\ProgramFiles\\CudaText3\\py\\cuda_html_live_preview"
    req_text=text
    #req_text = req_text.replace('src=\'','src=\''+abs_url+os.sep)
    req_text=urllib.parse.quote(req_text)
    # "src"
    print('http://127.0.0.1:5000/set/'+req_text)  
    urllib.request.urlopen('http://127.0.0.1:5000/set/'+req_text)

class Command:

    def __init__(self):
        pass

    def config(self):
        pass
                
    def on_change_slow(self, ed_self):
        
        show(str(ed_self.get_text_all()).replace('\n','').replace('/','__UIUIU**__'))
        '''path=ed.get_filename()
        if os.sep in path:
                path=path[:-1]
        print(path)
        urllib.request.urlopen('http://127.0.0.1:5000/setpath/'+path.replace(os.sep,'##sep##'))
        print(type(str(ed_self.get_text_all())))'''
        pass