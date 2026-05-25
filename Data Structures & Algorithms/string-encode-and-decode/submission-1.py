class Solution:

    def encode(self, strs: List[str]) -> str:
        return f'{",".join(str(len(s)) for s in strs)}|{"".join(strs)}'

    def decode(self, s: str) -> List[str]:
        if s == "|":
            return []

        sizes, strings = s.split("|", maxsplit=1)

        i = 0
        decoded = []
        for size in sizes.split(","):
            size = int(size)
            decoded.append(strings[i:i + size])
            i += size
        return decoded