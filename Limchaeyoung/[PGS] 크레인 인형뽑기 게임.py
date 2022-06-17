# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    cnt = 0
    data = []
    print(board)
    for x in moves:
        for y in range(len(board)):
            if board[y][x-1] != 0:
                data.append(board[y][x-1])
                board[y][x-1] = 0
                if len(data) >= 2:
                    if data[-2] == data[-1]:
                        data.pop()
                        data.pop()
                        cnt += 2
                break
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))