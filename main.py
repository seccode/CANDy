from collections import Counter
import zstandard as zstd

def compress(s,comp):
    mc=[m[0] for m in Counter(s).most_common()]
    c={
        mc[0]:chr(0),
        mc[1]:chr(1),
        mc[2]:chr(2),
        mc[3]:chr(3)
    }
    m=[c[_s] for _s in s]
    return comp.compress("".join(m).encode())

if __name__=="__main__":
    s=open("dna").read().replace("\n","")

    comp=zstd.ZstdCompressor(level=22)
    _b=comp.compress(s.encode())

    b=compress(s,comp)
    print((len(_b)-len(b))/len(_b))
