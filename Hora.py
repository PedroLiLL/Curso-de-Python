import time
from traceback import print_tb

def main():
    
    h24 = time.strftime("%H:%M:%S")
    print("Hora Actual (formato 24 horas):",h24)
    h12 = time.strftime("%I:%M:%S")
    print("Hora Actual (formato 12 horas):",h12)
    

if __name__ == '__main__':
    main()