class Solution:
    def encode(self, strs: list[str]) -> str:
        encode = ""
        for s in strs:
            # print(f"{len(s)}#{s}")
            encode += f"{len(s)}#{s}"
        return encode

    def decode(self, s: str) -> list[str]:
        decoded = []
        len_i = ""
        i = 0

        while i < len(s):
            while s[i] != "#":
                print(f"{s[i]}")
                len_i += s[i]
                i += 1

            length = int(len_i)
            i += 1
            decoded_string = s[i: i + length]
            
            len_i = ""

            i += length

            decoded.append(decoded_string)

        return decoded
