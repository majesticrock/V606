import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()
    
    if err_vars == None:
        err_vars = f.free_symbols
        
    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'
        
    return latex(sympy.sqrt(s), symbol_names=latex_names)

va, v2, v1 = sympy.var('va v1 v2')

f = va / (v2 - v1)

print(f)
print(error(f))
print()

#E_x + q**2*r
#\sqrt{\sigma_{E_{x}}^{2} + 4 \sigma_{q}^{2} q^{2} r^{2} + \sigma_{r}^{2} q^{4}}

