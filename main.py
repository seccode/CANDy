import zstandard as zstd

def compress(s,comp):
    c={
        "A":chr(0),
        "C":chr(1),
        "G":chr(2),
        "T":chr(3)
    }
    m=[c[_s] for _s in s]
    return comp.compress("".join(m).encode())

if __name__=="__main__":
    s=open("dna").read()

    comp=zstd.ZstdCompressor(level=22)
    _b=comp.compress(s.encode())

    b=compress(s,comp)
    print((len(_b)-len(b))/len(_b))
