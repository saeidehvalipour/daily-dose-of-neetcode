class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # هر سطر با 1 شروع می‌شود
            row = [1] * (i + 1)

            # پر کردن وسط سطر
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle
        