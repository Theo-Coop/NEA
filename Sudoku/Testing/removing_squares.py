import board_generation_testing

full_board = board_generation_testing.generatedBoard()


def solve(self):
    if board.whole_board_valid():


        find = board.find_empty()

        if find == False:
            # Solver has finished
            enable_utilities()
            enable_slider()
            return True
        else:
            row, col = find[0], find[1]

        for i in range(1, 10):
            if board.num_valid(i, row, col):
                board.board[row][col] = i

                window.update()
                if solving_speed != 0:
                    time.sleep(self.solving_speed)
                solver_update_num(i, row, col, "green")


                if solve():
                    return True
                else:
                    board.board[row][col] = 0

                    window.update()
                    solver_update_num("-", row, col, "red")
    else:
        messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")
                    

    return False