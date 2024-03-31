class DiceNumber:
    def __init__(self, current_x, current_y, left, right, up, down, front, back):
        self.current_x = current_x
        self.current_y = current_y
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.front = front
        self.back = back

    def move(self, direction: int):
        if direction == 1:
            if self.current_y + 1 >= M:
                return False
            else:
                self.current_y += 1
            temp = self.up
            self.up = self.left
            self.left = self.down
            self.down = self.right
            self.right = temp
        elif direction == 2:
            if self.current_y - 1 < 0:
                return False
            else:
                self.current_y -= 1
            temp = self.up
            self.up = self.right
            self.right = self.down
            self.down = self.left
            self.left = temp
        elif direction == 3:
            if self.current_x - 1 < 0:
                return False
            else:
                self.current_x -= 1
            temp = self.up
            self.up = self.front
            self.front = self.down
            self.down = self.back
            self.back = temp
        elif direction == 4:
            if self.current_x + 1 >= N:
                return False
            else:
                self.current_x += 1
            temp = self.front
            self.front = self.up
            self.up = self.back
            self.back = self.down
            self.down = temp

        return True

    def swap(self, _board):
        board_value = _board[self.current_x][self.current_y]
        if board_value != 0:
            self.down = board_value
            _board[self.current_x][self.current_y] = 0
        else:
            _board[self.current_x][self.current_y] = self.down
        return _board

    def print_up_number(self):
        print(self.up)


N, M, x, y, K = map(int, input().split())
dice = DiceNumber(x, y, 0, 0, 0, 0, 0, 0)
board = [list(map(int, input().split())) for _ in range(N)]
command_list = list(map(int, input().split()))
for command in command_list:
    result = dice.move(command)
    if result:
        board = dice.swap(board)
        dice.print_up_number()
