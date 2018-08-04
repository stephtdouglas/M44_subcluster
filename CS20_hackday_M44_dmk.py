from __future__ import print_function

import pdb

import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits

from sklearn.cluster import SpectralClustering
from sklearn.cluster import KMeans
from sklearn import mixture

import gal_xyz

table_M44 = fits.open( 'Praesepe_cut.fits' )[1].data

radec_M44 = np.array( [ table_M44['gaia_dr2_source.ra'], table_M44['gaia_dr2_source.dec'] ] ).T
radecplx_M44 = np.array( [ table_M44['gaia_dr2_source.ra'], table_M44['gaia_dr2_source.dec'], table_M44['gaia_dr2_source.parallax'] ] ).T

pmplx_M44 = np.array( [ table_M44['gaia_dr2_source.pmra'], table_M44['gaia_dr2_source.pmdec'], table_M44['gaia_dr2_source.parallax'] ] ).T

xyz_M44   = gal_xyz.gal_xyz( radec_M44[:,0], radec_M44[:,1], radecplx_M44[:,2], radec = True, plx = True )

gmm_clust  = mixture.GaussianMixture( n_components = 2, covariance_type = 'full' )
gmm_clust.fit( pmplx_M44 )

pred_M44   = gmm_clust.predict( pmplx_M44 )

plt.clf()
plt.plot( radec_M44[:,0][pred_M44 == 0], radec_M44[:,1][pred_M44 == 0], '.', ms = 2 )
plt.plot( radec_M44[:,0][pred_M44 == 1], radec_M44[:,1][pred_M44 == 1], '.', ms = 2 )
plt.gca().invert_xaxis()
plt.show()

print( gmm_clust.means_ )
print( gmm_clust.covariances_ )

plt.clf()
# X/Y
plt.subplot( 3, 2, 1 )
plt.plot( xyz_M44[0][pred_M44==0], xyz_M44[1][pred_M44==0], 'k.', ms = 2 )
plt.plot( xyz_M44[0][pred_M44==1], xyz_M44[1][pred_M44==1], 'r.', ms = 2 )
# X/Z
plt.subplot( 3, 2, 2 )
plt.plot( xyz_M44[0][pred_M44==0], xyz_M44[2][pred_M44==0], 'k.', ms = 2 )
plt.plot( xyz_M44[0][pred_M44==1], xyz_M44[2][pred_M44==1], 'r.', ms = 2 )
# YZ
plt.subplot( 3, 2, 3 )
plt.plot( xyz_M44[2][pred_M44==0], xyz_M44[1][pred_M44==0], 'k.', ms = 2 )
plt.plot( xyz_M44[2][pred_M44==1], xyz_M44[1][pred_M44==1], 'r.', ms = 2 )
# ra/dec
plt.subplot( 3, 2, 4 )
plt.plot( radec_M44[:,0][pred_M44 == 0], radec_M44[:,1][pred_M44 == 0], 'k.', ms = 2 )
plt.plot( radec_M44[:,0][pred_M44 == 1], radec_M44[:,1][pred_M44 == 1], 'r.', ms = 2 )
# pm
plt.subplot( 3, 2, 5 )
plt.plot( pmplx_M44[:,0][pred_M44==0], pmplx_M44[:,1][pred_M44==0], 'k.', ms = 2 )
plt.plot( pmplx_M44[:,0][pred_M44==1], pmplx_M44[:,1][pred_M44==1], 'r.', ms = 2 )
# dist
plt.subplot( 3, 2, 6 )
plt.plot( radec_M44[:,0][pred_M44==0], pmplx_M44[:,2][pred_M44==0], 'k.', ms = 2 )
plt.plot( radec_M44[:,0][pred_M44==1], pmplx_M44[:,2][pred_M44==1], 'r.', ms = 2 )
plt.show()
         

#[ -37, -13 ]
#[ -34.5, -12 ]