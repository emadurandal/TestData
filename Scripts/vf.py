import numpy as np
from vectorfields import CustomUVW
ufunc = lambda x,y,z: x * 1
vfunc = lambda x,y,z: y * 2
wfunc = lambda x,y,z: z * 3

vf = CustomUVW(ufunc, vfunc, wfunc, (4, 4, 4), (4, 4, 4))
vf.save_vf('vf_simple.vf')
