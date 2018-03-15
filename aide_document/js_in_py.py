import js2py
from js2py.internals import seval
from js2py import require

seval.eval_js_vm('console.log( "Hello World!" )')
js2py.translate_file('example.js', 'example.py')
import example

# js2py.translate_file('translation.js', 'translation.py')
