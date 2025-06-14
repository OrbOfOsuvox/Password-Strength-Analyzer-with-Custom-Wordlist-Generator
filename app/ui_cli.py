import os
import subprocess
from app.generator import generate_wordlist

def run_generate_mode():
    print("\n[Wordlist Generator Mode]")
    inputs = []
    inputs.append(input("Full Name: "))
    inputs.append(input("Birthdate (e.g. 1995 or 14June): "))
    inputs.append(input("Pet Name: "))
    inputs.append(input("Favourite Book: "))
    inputs.append(input("Bike/Car Name: "))

    wordlist = generate_wordlist(inputs)

    # Ensure output directory
    output_dir = "wordlists"
    os.makedirs(output_dir, exist_ok=True)

    # Get filename
    filename = input("Enter output file name (without .txt, default: 'generated'): ").strip() or "generated"
    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(output_dir, filename)

    # Check for existing file
    if os.path.exists(filepath):
        overwrite = input(f"⚠️ File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("✖️ Operation cancelled.")
            return

    # Write wordlist
    with open(filepath, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')

    abs_path = os.path.abspath(filepath)
    print(f"\n✅ Wordlist saved to: {abs_path}")

    # Open file on Windows
    try:
        os.startfile(abs_path)
    except AttributeError:
        # Fallback for non-Windows
        subprocess.call(['open', abs_path])

def run_analyze_mode():
    print("\n[Password Strength Analyzer Mode]")
    password = input("Enter password to analyze: ")

    result = analyze_password(password)

    print("\n[Password Analysis Result]")
    print(f"Password: {result['password']}")
    print(f"Strength Score (0=Weak, 4=Strong): {result['score']}")
    print(f"Estimated Crack Time: {result['crack_time']}")
    if result['feedback']['warning']:
        print("⚠️ Warning:", result['feedback']['warning'])
    if result['feedback']['suggestions']:
        print("💡 Suggestions:", ", ".join(result['feedback']['suggestions']))
