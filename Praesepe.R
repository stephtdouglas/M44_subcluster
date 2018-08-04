## Kernel density estimation for M44 (Praesepe) with Gaia data 
## Earl Patrick Bellinger 
## earlbellinger@gmail.com 
## August 4, 2018 

#setwd("D:/Praesepe")

library(FITSio)
library(ks)
library(magicaxis)

P <- readFITS(file = 'Praesepe_cut.fits')
DF <- data.frame(P$col)
names(DF) <- P$colNames
ra <- DF$gaia_dr2_source.ra 
dec <- DF$gaia_dr2_source.dec 

xlim <- c(134, 126)
ylim <- c(16, 23)
mar <- c(3.2, 3, 1, 1)
mgp <- c(2, 0.25, 0)
family <- 'Palatino Linotype'
xlab <- 'Right Ascension'
ylab <- 'Declination'
width <- 6.97522/2
height <- 3
axis.lwd <- 1.66
tcl <- -0.346

# perform the KDE 
dens <- kde(data.frame(ra, dec)) 

## SCATTERPLOT
lims <- ra>xlim[2] & ra<xlim[1] & dec>ylim[1] & dec<ylim[2]
cairo_pdf('M44_ra_dec.pdf', width=width, height=height) 
par(mar=mar, mgp=mgp, family=family)
plot(NA, 
    xlim=xlim, ylim=ylim,
    axes=F, xaxs='i', yaxs='i',
    xlab=xlab, ylab=ylab)
points(ra[lims], dec[lims], 
    pch=20, cex=0.33, 
    col=adjustcolor(1, alpha.f=1))
box(lwd=axis.lwd)
magaxis(1:4, labels=F, lwd.ticks=axis.lwd, tcl=0)
magaxis(1:2, labels=T, lwd.ticks=axis.lwd, tcl=tcl, las=1, 
    majorn=3, family=par()$family)
dev.off()

## CONTOUR (LINES)
cairo_pdf('M44_kde_lines.pdf', width=width, height=height) 
par(mar=mar, mgp=mgp, family=family)
plot(dens, 
    cont=c(1:100)[c(T,F,F,F)], 
    drawlabels=F,
    xlim=xlim, ylim=ylim,
    axes=F, xaxs='i', yaxs='i',
    xlab=xlab, ylab=ylab)
box(lwd=axis.lwd)
magaxis(1:4, labels=F, lwd.ticks=axis.lwd, tcl=0)
magaxis(1:2, labels=T, lwd.ticks=axis.lwd, tcl=tcl, las=1, 
    majorn=3, family=par()$family)
dev.off()

## FILLED CONTOUR (COLORS)
cont <- seq(1, 100, length.out=10)
cairo_pdf('M44_kde.pdf', width=width, height=height) 
par(mar=mar, mgp=mgp, family=family)
plot(dens, display="filled.contour", # make the density plot 
    cont=cont, 
    xlim=xlim, ylim=ylim,
    axes=F, xaxs='i', yaxs='i',
    xlab=xlab, ylab=ylab)
box(lwd=axis.lwd)
magaxis(1:4, labels=F, lwd.ticks=axis.lwd, tcl=0)
magaxis(1:2, labels=T, lwd.ticks=axis.lwd, tcl=tcl, las=1, 
    majorn=3, family=par()$family)
dev.off()
