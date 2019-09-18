class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = address.split('.')
        dfip = "[.]".join(addr)
        return dfip
        