# This file is generated by /Users/cirl/scipy-build/numpy-1.2.1/setupegg.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

lapack_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3']}
blas_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3', '-I/System/Library/Frameworks/vecLib.framework/Headers']}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print name + ":"
        if not info_dict:
            print "  NOT AVAILABLE"
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print "    %s = %s" % (k,v)
        print
    