#exemple: kenedy lake is transformed form two NNP to one GRP
patterns=["bay","beach","cave","creek","desert","earth","forest","hill","island",
"lake","mountain","ocean","peak","plain","pond","river","riverbed","sea","stream","swamp","valley","waterfall","woods","street","road"]

def pattern_matcher(tags):
    res={}
    prev=""

    for t in tags:
        if t[0] in patterns:
            grp=prev+" "+t[0]
            res[grp]="GRP"
            if prev != "":
                del res[prev]
        else:
            res[t[0]]=t[1]
            prev=t[0]
    return res
