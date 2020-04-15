class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = list(S); t = list(T)

        words = []
        for i in range(len(s)):
            if s[i] != "#":
                words.append(s[i])
            else:
                if words != []:
                    words.pop(-1)

        wordt = []
        for i in range(len(t)):
            if t[i] != "#":
                wordt.append(t[i])
            else:
                if wordt != []:
                    wordt.pop(-1)

        if "".join(words) == "".join(wordt):
            return True
        else:
            return False
