import math, queue
from collections import Counter

# === Problem 3 ===

# Provided test cases
test_cases = [
    ('book', 'back'),
    ('kookaburra', 'kookybird'),
    ('elephant', 'relevant'),
    ('AAAGAATTCA', 'AAATCA')
]

alignments = [
    ('b--ook', 'bac--k'),
    ('kook-ab-urr-a', 'kooky-bi-r-d-'),
    ('relev--ant', '-ele-phant'),
    ('AAAGAATTCA', 'AAA---T-CA')
]

# Naive recursive edit distance (inefficient)
def MED(S, T):
    if not S: return len(T)
    if not T: return len(S)
    if S[0] == T[0]:
        return MED(S[1:], T[1:])
    return 1 + min(MED(S[1:], T), MED(S, T[1:]))

# Memoized edit distance (top-down DP)
def fast_MED(S, T, MED=None):
    if MED is None:
        MED = {}
    key = (S, T)

    if key in MED:
        return MED[key]
    if not S:
        MED[key] = len(T)
    elif not T:
        MED[key] = len(S)
    elif S[0] == T[0]:
        MED[key] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        MED[key] = 1 + min(insert, delete)

    return MED[key]

# Alignment reconstruction using the memo table from fast_MED
def fast_align_MED(S, T):
    memo = {}
    fast_MED(S, T, memo)

    i, j = len(S), len(T)
    s_aligned, t_aligned = [], []

    while i > 0 or j > 0:
        s_prefix, t_prefix = S[:i], T[:j]
        cost = memo.get((s_prefix, t_prefix), math.inf)

        match = i > 0 and j > 0 and S[i - 1] == T[j - 1]
        insert = j > 0 and memo.get((s_prefix, T[:j - 1]), math.inf) + 1 == cost
        delete = i > 0 and memo.get((S[:i - 1], t_prefix), math.inf) + 1 == cost

        if match:
            s_aligned.insert(0, S[i - 1])
            t_aligned.insert(0, T[j - 1])
            i -= 1
            j -= 1
        elif insert:
            s_aligned.insert(0, '-')
            t_aligned.insert(0, T[j - 1])
            j -= 1
        elif delete:
            s_aligned.insert(0, S[i - 1])
            t_aligned.insert(0, '-')
            i -= 1
        else:
            # fallback to match/mismatch
            s_aligned.insert(0, S[i - 1] if i > 0 else '-')
            t_aligned.insert(0, T[j - 1] if j > 0 else '-')
            i = max(i - 1, 0)
            j = max(j - 1, 0)

    return ''.join(s_aligned), ''.join(t_aligned)
