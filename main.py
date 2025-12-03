# main.py
import numpy as np
import matplotlib.pyplot as plt
from f_function import f, y_exact

def _num_steps(a, b, h):
    # Σταθερό σε στρογγυλοποιήσεις: εξασφαλίζει ότι t_N == b και δεν “χάνεται” το τελευταίο σημείο.
    return int(round((b - a) / h + 1e-12))

# -----------------------------
# Forward Euler (FD)
# -----------------------------
def forward_euler(f, a, b, y0, h):
    N = _num_steps(a, b, h)
    t = np.linspace(a, b, N + 1)
    y = np.zeros(N + 1, dtype=float)
    y[0] = y0
    for n in range(N):
        y[n + 1] = y[n] + h * f(t[n], y[n])
    return t, y

# -----------------------------
# Central Difference (CD) — 2-βηματική με εκκίνηση FE
# -----------------------------
def central_difference(f, a, b, y0, h):
    """
    y_{n+1} = y_{n-1} + 2h f(t_n, y_n),  n = 1,...,N-1
    Εκκίνηση: y_1 = y_0 + h f(t_0, y_0)
    """
    N = _num_steps(a, b, h)
    t = np.linspace(a, b, N + 1)
    y = np.zeros(N + 1, dtype=float)
    y[0] = y0
    if N >= 1:
        y[1] = y[0] + h * f(t[0], y[0])  # Forward Euler bootstrap
    for n in range(1, N):                # n=1,...,N-1 => παράγει και το y[N]
        y[n + 1] = y[n - 1] + 2.0 * h * f(t[n], y[n])
    return t, y

# -----------------------------
# Improved Euler (Heun)
# -----------------------------
def improved_euler(f, a, b, y0, h):
    N = _num_steps(a, b, h)
    t = np.linspace(a, b, N + 1)
    y = np.zeros(N + 1, dtype=float)
    y[0] = y0
    for n in range(N):
        k1 = f(t[n], y[n])
        k2 = f(t[n] + h, y[n] + h * k1)
        y[n + 1] = y[n] + 0.5 * h * (k1 + k2)
    return t, y

def run_once(a, b, y0, h, title_prefix=""):
    # Υπολογισμοί
    t_fe, y_fe = forward_euler(f, a, b, y0, h)
    t_cd, y_cd = central_difference(f, a, b, y0, h)
    t_ie, y_ie = improved_euler(f, a, b, y0, h)

    # Έλεγχος πλεγμάτων (θα ταυτίζονται αν όλα είναι σωστά)
    assert np.allclose(t_fe, t_cd) and np.allclose(t_fe, t_ie)
    t = t_fe

    # Ακριβής λύση & σφάλματα
    y_ex = y_exact(t)
    err_fe = np.max(np.abs(y_ex - y_fe))
    err_cd = np.max(np.abs(y_ex - y_cd))
    err_ie = np.max(np.abs(y_ex - y_ie))

    # Πίνακας στην οθόνη
    print(f"\n=== {title_prefix} h = {h:.3f} ===")
    print("i   t_i        y_FD         y_CD         y_IE         y_exact     |err_FD|    |err_CD|    |err_IE|")
    for i in range(len(t)):
        print(f"{i:<3d}{t[i]:>8.4f}  {y_fe[i]:>12.8f}  {y_cd[i]:>12.8f}  {y_ie[i]:>12.8f}  {y_ex[i]:>12.8f}  "
              f"{abs(y_ex[i]-y_fe[i]):>10.3e}  {abs(y_ex[i]-y_cd[i]):>10.3e}  {abs(y_ex[i]-y_ie[i]):>10.3e}")

    print(f"\nMax error FE: {err_fe:.6e}")
    print(f"Max error CD: {err_cd:.6e}")
    print(f"Max error IE: {err_ie:.6e}")

    # Γράφημα (κρατάω exact+IE+CD για καθαρότητα. Αν θέλεις και FE, ξε-σχολίασε την γραμμή)
    plt.figure()
    # plt.plot(t, y_fe, 'o-', label='Forward Euler')
    plt.plot(t, y_cd, 'o-', label='Central Difference')
    plt.plot(t, y_ie, 's-', label='Improved Euler (Heun)')
    plt.plot(t, y_ex, '--', label='Exact')
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title(f"{title_prefix} Προσεγγίσεις vs Ακριβής (h={h})")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return {"h": h, "err_fe": err_fe, "err_cd": err_cd, "err_ie": err_ie}

if __name__ == "__main__":
    print("Δώσε δεδομένα αρχικού προβλήματος y'(t)=f(t,y), y(a)=y0")
    a = float(input("a: "))
    b = float(input("b: "))
    y0 = float(input("y0: "))
    mode = input("Θες να τρέξω για h=0.2 και h=0.1; [y/n]: ").strip().lower()

    results = []
    if mode == 'y':
        for h in (0.2, 0.1):
            results.append(run_once(a, b, y0, h, title_prefix="Αποτέλεσμα"))
        # Σύνοψη σφαλμάτων
        print("\nΣΥΝΟΨΗ ΣΦΑΛΜΑΤΩΝ (max |y(t_i)-y_i|):")
        print("h       err_FE        err_CD        err_IE")
        for r in results:
            print(f"{r['h']:<6.3f}  {r['err_fe']:<12.6e} {r['err_cd']:<12.6e} {r['err_ie']:<12.6e}")
    else:
        h = float(input("Δώσε βήμα h: "))
        run_once(a, b, y0, h, title_prefix="Αποτέλεσμα")