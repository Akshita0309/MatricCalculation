import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements for {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(" Incorrect number of elements. Try again.")
            return input_matrix(name)
        matrix.append(row)

    return np.array(matrix)

def display_matrix(title, matrix):
    print(f"\n {title}:")
    print(matrix)

def main():
    while True:
        print("\n===== MATRIX OPERATIONS TOOL =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                if A.shape == B.shape:
                    display_matrix("Result (A + B)", A + B)
                else:
                    print(" Matrices must have same dimensions.")

            elif choice == "2":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                if A.shape == B.shape:
                    display_matrix("Result (A - B)", A - B)
                else:
                    print(" Matrices must have same dimensions.")

            elif choice == "3":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                if A.shape[1] == B.shape[0]:
                    display_matrix("Result (A × B)", np.dot(A, B))
                else:
                    print(" Columns of A must equal rows of B.")

            elif choice == "4":
                A = input_matrix("Matrix")
                display_matrix("Transpose", A.T)

            elif choice == "5":
                A = input_matrix("Matrix")
                if A.shape[0] == A.shape[1]:
                    print("\n Determinant:", np.linalg.det(A))
                else:
                    print(" Determinant only for square matrices.")

            elif choice == "6":
                print("👋 Exiting Matrix Operations Tool.")
                break

            else:
                print(" Invalid choice. Try again.")

        except Exception as e:
            print("⚠ Error:", e)

if __name__ == "__main__":
    main()

