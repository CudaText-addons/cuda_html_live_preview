try:
    from flask import Flask, request, send_file
    from jinja2 import Template, Environment, BaseLoader, FileSystemLoader
except:
    print("""
************************************************
*    HTML Live Preview could not connect to    *
*    server. Check that you have Python 3      * 
*    with Flask installed, and server is       *
*    running via 'Start server' command.)      *
*    Press enter to close this window          *
************************************************
""")
    input()
import os
import sys
'''
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
'''
#os.chdir('C:\\ProgramFiles\\CudaText3\\py\\cuda_html_live_preview')

text=''
nump=0

app=Flask(__name__) 
app.config['DEBUG'] = False

script='''
<script type='text/javascript'>
function load(url,callback)
{
  var xhr=new XMLHttpRequest();
  xhr.onreadystatechange=function()
  {
    if (xhr.readyState==4)
    {
      callback(xhr.response);
    }
  }
  xhr.open('GET',url,true);
  xhr.send('');
}
var old='0'
function load(url,callback)
{
  var xhr=new XMLHttpRequest();
  xhr.onreadystatechange=function()
  {
    if (xhr.readyState==4)
    {
      callback(xhr.response);
    }
  }
  xhr.open('GET',url,true);
  xhr.send('');
}
function init(rs)
{
  old=rs;
}
load('/num',init)
function check(response)
  {
    if (response!=old)
    {
      console.log(response);
      old=response;
      document.location=document.location;
    }
    else
    {
      console.log('keep calm')
    }
  }
function monitor(){
  load('/num',check)
}
setInterval(monitor,1000);
</script>
'''

fullpath=''

@app.route('/setpath/<path:path>')
def pathpage(path):
    global fullpath
    fullpath=path
    os.chdir(path)
    return ''

@app.route('/view')
def view():
    global text 
    try:
        global fullpath
        os.chdir(fullpath)
        return script+Environment(loader=FileSystemLoader(fullpath)).from_string(text).render()+'<br>'
    except:    
        Environment(loader=FileSystemLoader(fullpath)).from_string(text).render()
        return script+'Error in template'
    
@app.route('/set/<new_text>')
def set(new_text):
    global text
    global nump 
    nump+=1
    text=new_text.replace('%01','/')
    return ''
    
@app.route('/num')
def num():
    global num
    return str(nump)

@app.route('/<path:path>')
def catch_all(path):
    try:
        global fullpath
        #print(fullpath)
        os.chdir(fullpath)
        abspath=os.path.abspath(path)
        #print(abspath)
        if os.path.exists(abspath):
            return send_file(abspath)
        return 'You want path: %s' % abspath
    except:
        return 'error'
    
app.run(port=int(sys.argv[1]))
