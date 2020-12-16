class Solution:
    def spiral_order(self, matrix) -> list:
        # boundaries for spiral traversal
        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        # 0 -> right, 1 -> down, 2 -> left, 3 -> up
        direction = 0

        spiral = []
        while top_row <= bottom_row and left_col <= right_col:
            if direction == 0:
                # add all vals on top row
                for i in range(left_col, right_col + 1):
                    spiral.append(matrix[top_row][i])
                top_row += 1

            elif direction == 1:
                # add all vals on right col
                for i in range(top_row, bottom_row + 1):
                    spiral.append(matrix[i][right_col])
                right_col -= 1

            elif direction == 2:
                # add all vals on bottom row
                for i in range(right_col, left_col - 1, -1):
                    spiral.append(matrix[bottom_row][i])
                bottom_row -= 1

            elif direction == 3:
                # add all vals on left col
                for i in range(bottom_row, top_row - 1, -1):
                    spiral.append(matrix[i][left_col])
                left_col += 1

            direction = (direction + 1) % 4

        return spiral
