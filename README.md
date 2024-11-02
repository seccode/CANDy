# CANDy
DNA compression method

![CANDy](candy.webp)

# Method
Replace each DNA char with chars closer together in ascii space. For a string "abd", the distance of the string is (ord(b)-ord(a)) + (ord(d)-ord(b)), so by choosing replacement chars that minimize the distance, we improve compression.

# Results
Zstd (level 22) compresses this DNA sequence sample 95%, and we improve this by 2%
