import binascii
class Pointer() :
    def __init__(self) :
        self.b_List = []

def drawCluster(f, clusterNo) :
    global CLUSTER_SIZE

    position = CLUSTER_SIZE * clusterNo
    p = Pointer()
    hexdump(p, CLUSTER_SIZE, position)

def hexdump(p, n, a) :
    i, j = 0, 0
    pos = ''
    hexS = ''
    hexSP = ''
    ascS = ''
    
    while(n > 0) :
        if n >= 16 :
            i = 16
        else :
            i = n

        f.seek(a)
        p = Pointer()
        
        pos = '{:08x} :'.format(a)

        for j in range(0, i) :
            p.b_List.append(f.read(1))
            hexS += ' ' + p.b_List[j].hex()
            
        for j in range(i, 16) :
            hexSP += '  '


        for j in range (0, 16) :
            s = p.b_List[j].decode()
            if s == '\n' :
                s = '\\n'
            ascS += s
            
        string = pos+hexS+hexSP+' | '+ascS
        print(string)

        del(p.b_List)
        
        n -= i
        a += i

if __name__ == "__main__" :
    f = open('forecasts1.csv', 'rb')
    position = 0
    CLUSTER_SIZE = 16
    clusterNo = 0
    for clusterNo in range (clusterNo, clusterNo+10) :
        drawCluster(f, clusterNo)
