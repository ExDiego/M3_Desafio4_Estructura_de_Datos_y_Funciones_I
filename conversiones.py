import sys

if len(sys.argv) < 4:
    print("error!!, por favor ingresar valores")
else:
    Factor={
        "sol": float(sys.argv[1]),
        "peso_argentino": float(sys.argv[2]),
        "dollar": float(sys.argv[3])
    }

    clp= float(sys.argv[4])

    print(f'''
            TABLA DE CONVERSION

            Los {clp:.0f} pesos equivale a :

            {(Factor["sol"]*clp):.1f}  Soles Peruanos.
            {(Factor["peso_argentino"]*clp):.1f}  Peso Argentino.
            {(Factor["dollar"]*clp):.1f}  Dolares Americanos.
            ''')