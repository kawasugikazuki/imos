H, W, N = [int(i) for i in input().split()]

snow_area = [[0]*(W + 1) for _ in range(H + 1)]

for i in range(N):
  A, B, C, D = [int(i) for i in input().split()]
  snow_area[A-1][B-1] += 1
  snow_area[C][D] += 1
  snow_area[A-1][D] -= 1
  snow_area[C][B-1] -= 1


# 横方向
for i in range(H + 1):
    for j in range(1, W + 1):
        snow_area[i][j] += snow_area[i][j - 1]

# 縦方向
for j in range(W + 1):
    for i in range(1, H + 1):
        snow_area[i][j] += snow_area[i - 1][j]

for i in range(H):
    for j in range(W):
        print(snow_area[i][j], end=' ')
    print("")