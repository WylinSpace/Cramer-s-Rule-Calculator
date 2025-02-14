class RealCramer:
    def __init__(self, A, B, C, D, E, F):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F

    @staticmethod
    def interface():
        print("Enter the coefficients according to the equations:")
        print("Ax + By = C")
        print("Dx + Ey = F")

        A = float(input("Enter A: "))
        B = float(input("Enter B: "))
        C = float(input("Enter C: "))
        D = float(input("Enter D: "))
        E = float(input("Enter E: "))
        F = float(input("Enter F: "))

        detA = (A * E) - (B * D)
        
        if detA == 0:
            print("The system has no unique solution (either no solution or infinite solutions).")
            return

        detB = (C * E) - (B * F)
        detC = (A * F) - (C * D)

        X = detB / detA
        Y = detC / detA

        print(f"The solution is:\nX = {X}\nY = {Y}")

