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
        for i,v in enumerate(word):
            if v != ch:
                d.insert(0,v)
            else:
                dd = word[i+1:]
                break
        d.insert(0,ch)
        s = "".join(d)
        print(s)
        return s + dd

        