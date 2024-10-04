import subprocess

# Pfad zum Python-Skript
script = "ageCalculator.py"

# Liste der Testfälle
dates = ["25.12.1995", "31.02.2020", "29.02.2000", "01.01.2024", "15.08.1990"]

# Schleife über die Datumsangaben
for date in dates:
    print(f"Test mit Eingabe: {date}")
    
    # Aufruf des Skripts mit dem Datum als Argument
    result = subprocess.run(["python", script, date], capture_output=True, text=True)
    
    # Ausgabe des Ergebnisses
    print(result.stdout)
    print(result.stderr)  # Fehlerausgabe hinzufügen
    print("------------------------------------------")
