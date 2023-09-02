class Solution:
    def simplifyPath(self, path: str) -> str:
        path, canonical = path.split("/"), []
        for p in path:
            if p == ".." and canonical:
                canonical.pop()
            elif p and p != "." and p != "..":
                canonical.append(p)

        return "/" + "/".join(canonical)
