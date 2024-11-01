from collections import Counter
from tqdm import tqdm
import zstandard as zstd

def compress(s,comp):
    c={
        "A":"3",
        "C":"2",
        "G":"4",
        "T":"1"
    }
    m=[c[_s] for _s in s]
    return comp.compress("".join(m).encode())

if __name__=="__main__":
    s=open("dna").read()

    comp=zstd.ZstdCompressor(level=22)
    _b=comp.compress(s.encode())
    print((len(s)-len(_b))/len(s))

    b=compress(s,comp)
    print((len(s)-len(b))/len(s))
