import zstandard as zstd

def compress(s,comp):
    c={
        "A":"2",
        "C":"3",
        "G":"1",
        "T":"4"
    }
    m=[c[_s] for _s in s]
    return comp.compress("".join(m).encode())

if __name__=="__main__":
    s=open("dna").read()

    comp=zstd.ZstdCompressor(level=22)
    _b=comp.compress(s.encode())

    b=compress(s,comp)
    print((len(_b)-len(b))/len(_b))
