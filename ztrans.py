import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

n, z = sp.symbols('n z')
x_n = (0.5**n)

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
Z = sp.simplify(X_z)
print(f"Z-transform X(z): {Z}")

"""def plot_zeros_poles(zeros,poles):
    
    zeros = np.array([complex(zero) for zero in zeros], dtype=np.complex128)
    poles = np.array([complex(pole) for pole in poles], dtype=np.complex128)

    
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)

    
    plt.scatter(zeros.real, zeros.imag, s=100, c='b', marker='o', label='Zeros')
    
    
    plt.scatter(poles.real, poles.imag, s=100, c='r', marker='x', label='Poles')
    
    
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
    plt.gca().add_artist(unit_circle)

    plt.title('Zeros and Poles in the Z-Plane')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

numerator, denominator = Z.args[0][0].as_numer_denom()
print('Numerator: ',numerator,' Denominator: ', denominator)

poles = sp.solve(denominator, z)
print("Poles of the system:", poles)

zeros = sp.solve(numerator, z)
print("Zeros of the system:", zeros)

plot_zeros_poles(zeros,poles)"""    