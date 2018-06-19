
import numpy as np

class Numtransform():
    """Num Transform a string of DNA to {0,1}"""
    def __init__(self, dna_si):
        super(Numtransform, self).__init__()
        self.dna_si = dna_si
        self.dna_si_len =  len( self.dna_si)
        self.dna_si_nts = ''.join( list( set( self.dna_si ))  )
        self.dna_si_nt_len = len( self.dna_si_nts )
        
    def _NT_per_nt( self, dna_si , nt ):
        self.res = list()
        for i in self.dna_si:
            if i.find( nt ) == -1 :
                self.res.append( 0 )
            else :
                self.res.append( 1 )
        return(self.res) 

    def array2d( self ):
        """Returns a a 2d numpy array 
        """
        self.res_np = np.zeros(  self.dna_si_len * self.dna_si_nt_len ).reshape( self.dna_si_nt_len , self.dna_si_len )
        for e,i in enumerate( self.dna_si_nts ):
            self.res_np[e] = self._NT_per_nt( self.dna_si, i )
        return( np.array(self.res_np))
