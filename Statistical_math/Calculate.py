import bisect
class Calculate:
    def __init__(self):
        pass
    def mean(self, ls:list):
        meanloop = 0
        meanloopadd = 0
        for l in ls:
            meanloop += int(l)
            meanloopadd += 1
        return meanloop / meanloopadd
    def dispersion(self, ls:list):
        meanloop = 0
        meanloopadd = 0
        for l in ls:
            meanloop += int(l)
            meanloopadd += 1
        mean = meanloop / meanloopadd
        output = []
        for j in ls:
            output.append(int(j) - mean)
        return output

    def median(self, a:list):
        r = sorted(a)
        s_index = 0
        e_index = len(r)
        init = r
        if len(r) % 2 == 0:
            for i in range(len(r) - 2):
                init.pop(s_index + i)
                init.pop(e_index - i)
        return init






if __name__ == '__main__':
    cal = Calculate()
    print(cal.median([3, 4, 2, 4, 5, 7, 3, 6]))

