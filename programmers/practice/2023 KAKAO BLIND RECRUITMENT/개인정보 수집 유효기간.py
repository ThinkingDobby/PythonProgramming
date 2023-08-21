from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    today = datetime.strptime(today, "%Y.%m.%d")
    memo = dict()

    for i in terms:
        a, b = i.split()
        memo[a] = int(b)

    ans = []
    for i in range(len(privacies)):
        f, s = privacies[i].split()
        date = datetime.strptime(f, "%Y.%m.%d")
        if today >= date + relativedelta(months=memo[s]):
            ans.append(i + 1)

    return ans


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
ans = solution(today, terms, privacies)
print(ans)