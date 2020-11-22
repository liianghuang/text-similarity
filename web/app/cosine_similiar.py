import string
import math
class Similiarity:
    def __init__(self):
        # word count dictionary
        self.count_A = dict()
        self.count_B = dict()
        self.exclude = set(string.punctuation)

    def build_count(self, text1, text2):
        text1 = ''.join(ch for ch in text1 if ch not in self.exclude).split()
        text2 = ''.join(ch for ch in text2 if ch not in self.exclude).split()
        for c in text1:
            if c in self.count_A:
                self.count_A[c] += 1
            else:
                self.count_A[c] = 1
        for c in text2:
            if c in self.count_B:
                self.count_B[c] += 1
            else:
                self.count_B[c] = 1

    def cosine(self):
        key_set = set(self.count_A.keys()).union(self.count_B.keys())
        sum_square_a = 0
        sum_square_b = 0
        dot_prod = 0
        for k in key_set:
            sum_square_a += self.count_A[k]**2 if k in self.count_A else 0
            sum_square_b += self.count_B[k]**2 if k in self.count_B else 0
            if k in self.count_A and k in self.count_B:
                dot_prod += self.count_A[k]*self.count_B[k]
        return dot_prod/(math.sqrt(sum_square_a)*math.sqrt(sum_square_b))

if __name__ == "__main__":
    s = Similiarity()
    text = []

    f = open('sample.txt')
    lines = f.readlines()
    #print(lines)

    s.build_count(lines[0], lines[1])
    print("cosine similiarity of text1 and text2 is: "+ str(s.cosine()))
    s2 = Similiarity()
    s2.build_count(lines[0], lines[2])
    print("cosine similiarity of text1 and text3 is: "+ str(s2.cosine()))
    f.close()
