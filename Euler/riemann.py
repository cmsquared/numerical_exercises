import math
import numpy
import pylab

def riemann():

    # grid info
    xmin = 0.0
    xmax = 1.0

    nzones = 2
    ng = 0
    
    dx = (xmax - xmin)/float(nzones)

    xl = (numpy.arange(2*ng+nzones) - ng)*dx
    xr = (numpy.arange(2*ng+nzones)+1 - ng)*dx

    xc = 0.5*(xl + xr)


    #------------------------------------------------------------------------
    # plot a domain without ghostcells
    pylab.plot([xmin,xmax], [0,0], color="k", lw=2)

    # domain left edge
    pylab.plot([xl[ng], xl[ng]], [0, 0.5], color="k", lw=2)

    n = ng
    while (n < ng+nzones):

        # draw right edge
        pylab.plot([xr[n], xr[n]], [0, 0.5], color="k", lw=2)        

        # draw center marker
        pylab.plot([xc[n], xc[n]], [-0.05, 0], color="k")                
        n += 1

    # domain left edge
    pylab.plot([xr[ng+nzones-1], xr[ng+nzones-1]], [0, 0.5], color="k", lw=2)

       

    # label a few
    pylab.text(xc[ng+nzones/2-1], -0.1, r"$i$", 
               horizontalalignment='center', verticalalignment='top')

    pylab.text(xc[ng+nzones/2], -0.1, r"$i+1$", 
               horizontalalignment='center', verticalalignment='top')

    pylab.text(xl[ng+nzones/2], -0.1, r"$i+1/2$", 
               horizontalalignment='center', verticalalignment='top')


    # L
    pylab.scatter(xl[ng+nzones/2]-0.05*dx, 0.25, marker="x")

    pylab.text(xl[ng+nzones/2]-0.075*dx, 0.25, r"$U_{i+1/2,L}^{n+1/2}$", 
               horizontalalignment='right', verticalalignment='center')

    pylab.text(xc[ng+nzones/2-1], 0.25, r"$U_i$",
               horizontalalignment='center', verticalalignment='center', fontsize="16")


    # R
    pylab.scatter(xl[ng+nzones/2]+0.05*dx, 0.25, marker="x")

    pylab.text(xl[ng+nzones/2]+0.075*dx, 0.25, r"$U_{i+1/2,R}^{n+1/2}$", 
               horizontalalignment='left', verticalalignment='center')

    pylab.text(xc[ng+nzones/2], 0.25, r"$U_{i+1}$",
               horizontalalignment='center', verticalalignment='center', fontsize="16")


    # flux
    pylab.arrow(xl[ng+nzones/2]-0.25*dx, 0.6, 0.5*dx, 0, 
                shape='full', head_width=0.075, head_length=0.05, 
                lw=1, width=0.03,
                edgecolor="none", facecolor="red",
                length_includes_head=True, zorder=100)
    
    pylab.text(xl[ng+nzones/2], 0.68, r"$F(U_{i+1/2}^{n+1/2})$", color="red",
               horizontalalignment="center")


    pylab.xlim(xl[0]-0.5*dx,xr[2*ng+nzones-1]+0.5*dx)
    pylab.ylim(-0.25, 0.75)
    pylab.axis("off")

    pylab.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

    f = pylab.gcf()
    f.set_size_inches(8.0,2.5)


    pylab.savefig("riemann_comp.eps")


if __name__== "__main__":
    riemann()
