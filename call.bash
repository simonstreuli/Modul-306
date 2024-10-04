#!/bin/bash

# Pfad zum Python-Skript
script="alter_berechnen.py"

# Liste der Testfälle
dates=("25.12.1995" "31.02.2020" "29.02.2000" "01.01.2024" "15.08.1990")

# Schleife über die Datumsangaben
for date in "${dates[@]}"; do
    echo "Test mit Eingabe: $date"
    python3 $script "$date"
    echo "------------------------------------------"
done
