class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        d =[]
        dd = ""
        for v,i in enumerate(word):
            if i != ch:
                d.insert(0,i)
            else:
                dd = word[v+1:]
                break
        d.insert(0,ch)
        s = "".join(d)
        print(s)
        return s + dd

        