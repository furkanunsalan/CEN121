def solution():
    A = {"play", "read", "smile", "write code"}
    B = {"smile","write code","run"}
    C = set(["laugh","write code","go","read"])
    
    ab_intersection = A.intersection(B)
    print(f"A intersection B: {ab_intersection}")
    print(f"A intersection C: {A.intersection(C)}")
    print(f"A, B, C intersection: {ab_intersection.intersection(C)}")

solution()