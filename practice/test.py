#S refers to soluble, T refers to Transmembrane

#각각에 대하여 viterbi algorithm을 통해 aa sequence의 state의 p값이
#가장 큰 것을 구하자

states=("S","T")
observation=("D","E","L","I","F","F","L","I","F")
starts_probability={"S":0.788136664480353, "T":0.211863335519647}
transition_probability={
    "S":{"S":0.9872140687721683,"T":0.012785931227831702},
    "T":{"T":0.9526608562484516,"S":0.04733914375154832}}
emission_probability={"S":{"D":0.05813960526076878,"E":0.06335074414579084,"F":0.046500789841608006,"I":0.058635904202199454,"L":0.08893737554698801},
                      "T":{"D":0.009107386101385808,"E":0.009535174323700593,"F":0.10723975278343784,"I":0.1287529973319524,"L":0.15801146022132412}}
def print_dptable(V):
    s="   "+" ".join(("%7d"%i) for i in range(len(V)))+"\n"
    for y in V[0]:
        s+="%.5s: "%y
        s+=" ".join("%7s"%("%f"%v[y]) for v in V)
        s+="\n"
    print(s)
def viterbi(obs,states,start_p,trans_p,emit_p):
    V=[{}]
    path={}

    for st in states:
        V[0][st]=start_p[st]*emit_p[st][obs[0]]
        path[st]=[st]
        print("V",V)
    # V=[{'S': 0.04582195456442669, 'T': 0.0019295211973048712}]
    # path={'S': ['S'], 'T': ['T']}
    for t in range(1,len(obs)):
        V.append({})
        a=[]
        for y in states:
            for y0 in states:
                (prob,state)=(V[t-1][y0]*trans_p[y0][y]*emit_p[y][obs[t]],y0)
                a.append([prob,state])
            print(a)
            print("max",max(a)[0])
            V[t][y]=max(a)[0]
            print(V)
            a=[]


def example():
    return viterbi(observation, states, starts_probability,transition_probability,emission_probability)
print(example())

