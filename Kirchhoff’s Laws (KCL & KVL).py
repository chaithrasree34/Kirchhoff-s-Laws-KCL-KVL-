# Kirchhoff-s-Laws-KCL-KVL-
# Kirchhoff's Laws Calculator

print("Kirchhoff's Laws")
print("1. KCL - Kirchhoff's Current Law")
print("2. KVL - Kirchhoff's Voltage Law")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    # KCL: Sum of currents entering = Sum of currents leaving

    n = int(input("Enter number of incoming currents: "))
    incoming = 0

    for i in range(n):
        current = float(input(f"Enter incoming current {i + 1} (A): "))
        incoming += current

    n = int(input("Enter number of outgoing currents: "))
    outgoing = 0

    for i in range(n):
        current = float(input(f"Enter outgoing current {i + 1} (A): "))
        outgoing += current

    print("\nTotal incoming current =", incoming, "A")
    print("Total outgoing current =", outgoing, "A")

    if abs(incoming - outgoing) < 0.001:
        print("KCL is satisfied.")
    else:
        print("KCL is NOT satisfied.")

elif choice == 2:
    # KVL: Sum of voltage rises = Sum of voltage drops

    n = int(input("Enter number of voltage sources/rises: "))
    voltage_rise = 0

    for i in range(n):
        voltage = float(input(f"Enter voltage rise {i + 1} (V): "))
        voltage_rise += voltage

    n = int(input("Enter number of voltage drops: "))
    voltage_drop = 0

    for i in range(n):
        voltage = float(input(f"Enter voltage drop {i + 1} (V): "))
        voltage_drop += voltage

    print("\nTotal voltage rise =", voltage_rise, "V")
    print("Total voltage drop =", voltage_drop, "V")

    if abs(voltage_rise - voltage_drop) < 0.001:
        print("KVL is satisfied.")
    else:
        print("KVL is NOT satisfied.")

else:
    print("Invalid choice.")
