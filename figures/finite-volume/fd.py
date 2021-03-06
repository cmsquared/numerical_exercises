import math
import numpy
import pylab
import grid_plot_util as gpu

# plot a simple finite-difference grid

#-----------------------------------------------------------------------------

nzones = 8

# data that lives on the grid
#a = numpy.array([0.3, 1.0, 0.9, 0.8, 0.25, 0.15, 0.5, 0.55])
a = numpy.array([0.3, 1.0, 0.9, 0.8, 0.25, 0.1, 0.5, 0.55])

gr = gpu.grid(nzones, fd=1)


pylab.clf()

gpu.drawGrid(gr)

gpu.labelCenter(gr, nzones/2,   r"$i$")
gpu.labelCenter(gr, nzones/2-1, r"$i-1$")
gpu.labelCenter(gr, nzones/2+1, r"$i+1$")
gpu.labelCenter(gr, nzones/2-2, r"$i-2$")
gpu.labelCenter(gr, nzones/2+2, r"$i+2$")


# draw the data
i = 0
while i < nzones:
    gpu.drawFDData(gr, i, a[i], color="r")    
    i += 1
    

gpu.labelFD(gr, nzones/2, a[nzones/2], r"$f_i$", color="r")

# label dx
pylab.plot([gr.xc[gr.ng+nzones/2-1], gr.xc[gr.ng+nzones/2-1]], [-0.35,-0.25], color="k")
pylab.plot([gr.xc[gr.ng+nzones/2], gr.xc[gr.ng+nzones/2]], [-0.35,-0.25], color="k")
pylab.plot([gr.xc[gr.ng+nzones/2-1], gr.xc[gr.ng+nzones/2]], [-0.3,-0.3], color="k")
pylab.text(0.5*(gr.xc[gr.ng+nzones/2-1] + gr.xc[gr.ng+nzones/2]), -0.45, r"$\Delta x$", 
           horizontalalignment="center")



pylab.axis([gr.xmin-gr.dx,gr.xmax+gr.dx, -0.5, 1.2])
pylab.axis("off")

pylab.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

f = pylab.gcf()
f.set_size_inches(10.0,3.0)

pylab.savefig("fd_grid.png")
pylab.savefig("fd_grid.eps")

