# n(i) is number of rows, m(j) is number of columns
# Project by Vedran Kocijan

def copy_mat(matrix):
    new_mat = []
    for i in range(0, len(matrix)):
        new_mat.append(["."])
        new_mat[i].pop()
    for row, num1 in enumerate(matrix):
        for col, num2 in enumerate(matrix[row]):
            new_mat[row].append(num2)
    return new_mat


def determinant_mat(matrix, sum=0):
    i = 2
    if len(matrix[0]) == 2 and len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    for num_row in range(0, len(matrix[0])):
        sub_mat = copy_mat(matrix)
        sub_mat.pop(0)
        for num_row2 in range(0, len(sub_mat)):
            sub_mat[num_row2].pop(num_row)
        sum = sum + (-1) ** (i) * matrix[0][num_row] * determinant_mat(sub_mat)
        i += 1
    return sum


def display_mat(mat):
    for column in mat:
        print(column)


def input_matrix(char_mat):
    input_string = "..."
    columns = []
    print("Insert matrix {} by following rules:".format(char_mat))
    print("1.Space between numbers"
          "\n2.To end your matrix add space and character e to your last number")
    while input_string[-1] != "e":
        row = []
        input_string = input()
        for num in input_string.split(" "):
            if num == "e":
                pass
            else:
                row.append(int(num))
        columns.append(row)
    return columns

def name_mat(choice, mat_list):
    for mat_num in mat_list:
        if choice == mat_num[0]:
            return mat_num[1]


def main():
    mat_list = []
    n = int(input("Enter number of matrixes: "))
    for mat_num in range(1, n + 1):
        print("______________________________")
        char_mat = input(f"Assign character to matrix num.{mat_num}: ")
        tup = (char_mat, input_matrix(char_mat))
        mat_list.append(tup)
    choice = int(input("Select what do you want:"
                       "\n0. Display matrix"
                       "\n1.Find determinant of matrix"))
    print("\n____________________________")
    if choice == 0:
        choice = input("Which one? Enter matrix assignment: ")
        print(display_mat(name_mat(choice, mat_list)))
    if choice == 1:
        choice = input("Which one? Enter matrix assignment: ")
        print(determinant_mat(name_mat(choice,mat_list)))
    return 0


if __name__ == '__main__':
    main()
