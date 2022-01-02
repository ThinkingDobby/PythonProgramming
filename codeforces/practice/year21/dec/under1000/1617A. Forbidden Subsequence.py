for t in range(int(input())):
    S = input()
    T = input()

    S = "".join(sorted(S))
    if T == "abc":
        if "a" in S and "b" in S and "c" in S:
            cnt = S.count("b")
            S = S.replace("b", "")
            S = S[:S.rindex("c") + 1] + "b" * cnt + S[S.rindex("c") + 1:]
    print(S)
