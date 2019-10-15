#exemple: kenedy lake is transformed form two NNP to one GRP
patterns=["bay","beach","cave","creek","desert","earth","forest","hill","island",
"lake","mountain","ocean","peak","plain","pond","river","riverbed","sea","stream","swamp","valley","waterfall","woods","street","road"]

def pattern_matcher(tags):
    temp={}
    res=[]
    prev=""
    for t in tags:
        if t[0] in patterns:
            grp=prev+" "+t[0]
            temp[grp]="GRP"
            if prev != "":
                del temp[prev]
        else:
            temp[t[0]]=t[1]
            prev=t[0]
    for key,value in temp.items():
        res.append((key,value))

    return res
