# Validation for: Existence of Isolating Subsets in the Near-Balanced Regime
# (objection B2 of "Reviewer Objections and Next Steps (K-Crossed Probit Paper)")
#
# Part A: greedy 2-cell block construction under iid-uniform sampling,
#         near-balanced kappa_1 = kappa_2 = kappa_3. Checks the construction
#         succeeds (hits its target S = delta * min(R1, R2/2, R3/2)) w.h.p.
# Part B: latent covariance of the constructed subset is exactly
#         block-equicorrelated (within-block off-diag = sigma_1^2, cross = 0).
# Part C: rank identity rank([D_k | D_k']) = R_k + R_k' - #components of the
#         bipartite co-occurrence graph; diagonal design (i,i,k) drops to R_1.

import numpy as np
from collections import defaultdict

rng = np.random.default_rng(7)


def greedy_isolating(cells, R2, R3, delta=0.5):
    """Greedy construction of disjoint 2-cell partial-permutation blocks."""
    R1 = 1 + max(c[0] for c in cells)
    S_target = int(delta * min(R1, R2 // 2, R3 // 2))
    byi = defaultdict(list)
    for (i, j, k) in cells:
        byi[i].append((j, k))
    usedj, usedk = set(), set()
    blocks = {}
    for i in sorted(byi, key=lambda i: -len(byi[i])):
        if len(blocks) >= S_target:
            break
        seen, found = [], None
        for (j, k) in byi[i]:
            if j in usedj or k in usedk:
                continue
            for (j2, k2) in seen:
                if j2 != j and k2 != k:
                    found = ((i, j, k), (i, j2, k2))
                    break
            if found:
                break
            seen.append((j, k))
        if found:
            (i1, j1, k1), (i2, j2, k2) = found
            usedj |= {j1, j2}
            usedk |= {k1, k2}
            blocks[i] = [found[0], found[1]]
    return blocks, S_target


# ---------------- Part A: success w.h.p., near-balanced ----------------
print("Part A: greedy success under iid uniform sampling, kappa=(.45,.45,.45)")
kap = 0.45
for R in (40, 80, 160):
    N = int(R ** (1 / kap))
    succ = 0
    reps = 20
    for _ in range(reps):
        cells = list(zip(rng.integers(0, R, N), rng.integers(0, R, N),
                         rng.integers(0, R, N)))
        blocks, S_target = greedy_isolating(cells, R, R, delta=0.5)
        succ += (len(blocks) == S_target)
    print(f"  R={R:4d} N={N:7d} target S={S_target:4d}  success {succ}/{reps}")

# ---------------- Part B: block-equicorrelated covariance ----------------
print("\nPart B: latent covariance of constructed subset")
R, kapB = 60, 0.45
N = int(R ** (1 / kapB))
cells = list(zip(rng.integers(0, R, N), rng.integers(0, R, N),
                 rng.integers(0, R, N)))
blocks, S_target = greedy_isolating(cells, R, R, delta=0.5)
chosen = [c for b in blocks.values() for c in b]
s1, s2, s3, sE = 0.7, 0.4, 0.3, 1.0
n = len(chosen)
C = np.zeros((n, n))
for a in range(n):
    for b in range(n):
        ia, ja, ka = chosen[a]
        ib, jb, kb = chosen[b]
        C[a, b] = (s1 * (ia == ib) + s2 * (ja == jb) + s3 * (ka == kb)
                   + sE * (a == b))
# expected: within-block off-diagonal exactly s1, across blocks exactly 0
ok_within, ok_cross = True, True
for a in range(n):
    for b in range(n):
        if a == b:
            continue
        same_block = (chosen[a][0] == chosen[b][0])
        if same_block and not np.isclose(C[a, b], s1):
            ok_within = False
        if not same_block and not np.isclose(C[a, b], 0.0):
            ok_cross = False
print(f"  n={n} cells; within-block offdiag == sigma1^2: {ok_within}; "
      f"cross-block == 0: {ok_cross}")

# ---------------- Part C: rank = R1 + R2 - #components ----------------
print("\nPart C: rank([D1|D2]) = R1 + R2 - #components (co-occurrence graph)")


def rank_and_components(pairs, R1, R2):
    Nn = len(pairs)
    D = np.zeros((Nn, R1 + R2))
    for l, (i, j) in enumerate(pairs):
        D[l, i] = 1
        D[l, R1 + j] = 1
    rank = np.linalg.matrix_rank(D)
    parent = list(range(R1 + R2))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (i, j) in pairs:
        a, b = find(i), find(R1 + j)
        if a != b:
            parent[a] = b
    comps = len({find(v) for v in
                 ({i for i, _ in pairs} | {R1 + j for _, j in pairs})})
    return rank, comps


R1 = R2 = 25
# (i) random rich design
pairs = list(zip(rng.integers(0, R1, 300), rng.integers(0, R2, 300)))
r, c = rank_and_components(pairs, R1, R2)
print(f"  random design : rank={r}, R1+R2-comps={R1 + R2 - c}  "
      f"match={r == R1 + R2 - c}")
# (ii) diagonal (married) design (i,i)
pairs = [(i, i) for i in range(R1) for _ in range(4)]
r, c = rank_and_components(pairs, R1, R2)
print(f"  diagonal      : rank={r} (= R1? {r == R1}), "
      f"R1+R2-comps={R1 + R2 - c}  match={r == R1 + R2 - c}")
