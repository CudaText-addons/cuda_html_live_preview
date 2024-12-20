Plugin for CudaText.
Allows to use live preview of HTML and Markdown files in the browser, during editing,
without need to reload browser page.
Requires Python 3, Flask framework and Markdown2 library.
Tested on Windows 10 and Linux (Ubuntu 19).

How to use
----------

- Install Python 3 from official site.
  With adding it to PATH variable.
  Plugin will try to run "python3" or "python" ("python.exe" on Windows), so one
  of them must be runnable.

- On Windows: if you have file python.exe in the CudaText folder, delete it,
  so plugin will not find it on running "python.exe".

- Install "Flask" in Python.

  On Windows, run in console:
    pip install flask
    pip install markdown2

  On non-Windows, run in terminal:
    pip3 install flask
    pip3 install markdown2

- In CudaText, specify path to browser: "Plugins / HTML Live Preview / Config".
  For example: "chrome", "firefox", "opera" or full path to executable file, without quotes.
  Restart CudaText.

- In CudaText, call "Plugins / HTML Live Preview / Start server".
  This should show console/terminal with running Flask server.
  Only if console/terminal window appeared, and it shows normal-looking Flask messages,
  plugin will work!
  Browser should open at http://127.0.0.1:5000/view

After that, just edit some HTML file.
Server will detect your changes (not immediately: after editing, make small pause)
and browser should show the preview.

These lexer names are handled: any with "HTML" word, "Jinja2" and "Markdown".

Note: after the opening of HTML file, browser will not show the preview,
you need to edit the file a little.
Note: on clicking any link in the browser, live preview stops, until you return to the 
http://127.0.0.1:5000/view


Browsers
--------

Supported:
- Google Chrome
- Firefox
- Opera
- Microsoft Edge 42

Not supported:
- Internet Explorer


About
-----
Authors:
  Medvosa, https://github.com/medvosa
  Alexey Torgashin (CudaText)
License: MIT
