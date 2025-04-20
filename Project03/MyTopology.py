from mininet.topo import Topo  
class MyTopo( Topo ):  

    def __init__( self ):
        Host = []
        Switch = []

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        for i in range(1, 14):
            Switch.append(self.addSwitch( 's' + str(i) ))
        
        for i in range(1, 12):
            Host.append(self.addHost( 'h' + str(i) ))

        # Add links
        for i in range(0, 11):
            self.addLink( Host[i], Switch[i] )        

        self.addLink( Switch[0], Switch[1] )
        self.addLink( Switch[0], Switch[2] )
        self.addLink( Switch[0], Switch[3] )
        self.addLink( Switch[0], Switch[4] )
        
        self.addLink( Switch[1], Switch[3] )
        
        self.addLink( Switch[2], Switch[4] )
        
        self.addLink( Switch[3], Switch[5] )
        self.addLink( Switch[3], Switch[11] )

        self.addLink( Switch[4], Switch[5] )
        self.addLink( Switch[4], Switch[12] )

        
        self.addLink( Switch[6], Switch[7] )
        self.addLink( Switch[6], Switch[8] )
        self.addLink( Switch[6], Switch[9] )
        self.addLink( Switch[6], Switch[10] )
        
        self.addLink( Switch[7], Switch[5] )
        self.addLink( Switch[7], Switch[9] )
        self.addLink( Switch[7], Switch[12] )
        
        self.addLink( Switch[8], Switch[5] )
        self.addLink( Switch[8], Switch[10] )
        self.addLink( Switch[8], Switch[11] )
        
            
topos = { 'mytopo': ( lambda: MyTopo() ) }
