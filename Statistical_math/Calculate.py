import bisect
def reverse(ls:list):
    return ls.reverse()

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
    def deviation(self, ls:list):
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
        init = list(r)
        for i in range(len(r) - (len(r) // 2) - 1):
            del init[i]
        if len(r) % 2 == 0:
            return (init[0] + init[1]) / 2
        else:
            return init[0]

    def dispersion(self, ls:list):
        meanloop = 0
        meanloopadd = 0
        outputint = 0
        for l in ls:
            meanloop += int(l)
            meanloopadd += 1
        mean = meanloop / meanloopadd
        output = []
        for j in ls:
            output.append(int(j) - mean)
        for k in output:
            outputint += (k ** 2)
        return outputint / len(ls)


if __name__ == '__main__':
    cal = Calculate()
    print(reverse([1, 2, 3, 4, 5, 6]))
    print(cal.median([3, 4, 2, 4, 5, 7, 3, 6]))

