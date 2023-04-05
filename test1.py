from mo import moo_fun
name = 'Current module'
def bar():
    print('Current module funnction bar:')
    print('variable name: ',name)
def call_moo_fun(fun):
    fun()
if __name__ == '__main__':
    bar()
    print()
    moo_fun()
    print()
    call_moo_fun(moo_fun)

