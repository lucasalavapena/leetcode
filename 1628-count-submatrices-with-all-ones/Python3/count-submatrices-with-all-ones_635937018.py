class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Given a matrix of 0's and 1's, this program determines the
        number of submatrices that consist of all 1's.

        :param mat: matrix of 0's and 1's
        :type mat: list[list[int]]
        :return: number of submatrices of all 1's
        :rtype: int
        """
        rows = len( mat )
        cols = len( mat[0] )

        """
        For each row, determine the number of submatrices of all 1's
        that terminate at each location and begin on the same row.
        """
        for r in range( rows ):
            for c in range( 1, cols ):
                if mat[r][c]:
                    mat[r][c] = mat[r][c - 1] + 1

        """
        Process the above matrix one row at a time. Moving down each
        column, determine the number of submatrices of all 1's that
        start on that row looking left.  Repeat for each row and return
        the total number of submatrices.

        For each 1 within a row, count the submatrices that contain
        the 1 and start on the same row either at the 1 or to the
        left of the 1. Proceed down the column that contains the 1
        until reaching a 0 or the bottom row of the matrix. While
        proceeding down a column, the width of the submatrices stays
        the same or gets thinner.
        """
        submatrices = 0
        for r in range( rows ):
            for c in range( cols ):
                if mat[r][c]:
                    row = r
                    submatrix_width = mat[r][c]
                    while row < rows and mat[row][c]:
                        submatrix_width = min( submatrix_width, mat[row][c] )
                        submatrices += submatrix_width
                        row += 1
        return submatrices

            
        