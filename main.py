from frontend.menu import mostrar_menu
from utils.limpiar import clear_screen 


def main():
    clear_screen()
    print("=== SISTEMA DE PRODUCTOS ===")
    mostrar_menu()

if __name__ == "__main__":
    main()