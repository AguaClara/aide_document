__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'input', u'trans', u'translate'])
@Js
def PyJsHoisted_trans_(input, this, arguments, var=var):
    var = Scope({u'this':this, u'input':input, u'arguments':arguments}, var)
    var.registers([u'input'])
    return var.get(u'translate')(var.get(u'input')).get(u'text')
PyJsHoisted_trans_.func_name = u'trans'
var.put(u'trans', PyJsHoisted_trans_)
var.put(u'translate', var.get(u'require')(Js(u'google-translate-api')))
pass
pass
pass


# Add lib to the module scope
example = var.to_python()