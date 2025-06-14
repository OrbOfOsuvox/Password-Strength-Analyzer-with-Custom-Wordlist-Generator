from app.ui_cli import run_generate_mode, run_analyze_mode

def main():
    print("Password Strength & Wordlist Tool")
    print("----------------------------------")
    print("1. Analyze password strength")
    print("2. Generate password wordlist")
    
    choice = input("Select option (1 or 2): ").strip()
    
    if choice == '1':
        run_analyze_mode()
    elif choice == '2':
        run_generate_mode()
    else:
        print("Invalid selection. Please choose 1 or 2.")

if __name__ == '__main__':
    main()
