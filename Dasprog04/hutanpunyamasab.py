r, c, n = map(int, input().split())
gold = [list(map(int, input().split())) for _ in range(r)]
moves = input()

pos_i, pos_j = 0, 0
jum_gold = gold[pos_i][pos_j]
gerakansalah = False

def is_valid(row, col):
    return 0 <= row <= r and 0 <= col <= c
for _ in range(n+1):
    for move in moves:
        if move == 'L':
            if is_valid(pos_i, pos_j - 1):
                pos_j -= 1
                jum_gold += gold[pos_i][pos_j] - 2
            else:
                gerakansalah = True
                break
        elif move == 'R':
            if is_valid(pos_i, pos_j + 1):
                pos_j += 1
                jum_gold += gold[pos_i][pos_j] + 3
            else:
                gerakansalah = True
                break
        elif move == 'U':
            if is_valid(pos_i - 1, pos_j):
                pos_i -= 1
                jum_gold += gold[pos_i][pos_j] + 3
            else:
                gerakansalah = True
                break
        elif move == 'D':
            if is_valid(pos_i + 1, pos_j):
                pos_i += 1
                jum_gold += gold[pos_i][pos_j] - 2
            else:
                gerakansalah = True
                break
        else:
            gerakansalah = True
            break

print(jum_gold)

if gerakansalah:
    print("Gerakanmu salah bung!")