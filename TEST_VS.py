tecnici = ["Franco", "Gianni", "Luca", "Piero"]
abilità_tecnici = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 1, 1]
]
abilità = ["bracci mec", "motore", "vetri"]

macchine_da_riparare = ["n1", "n2", "n3", "n4"]
abilità_richieste_per_riparazione = [
    [1, 1, 1],
    [0, 1, 1]
    [0, 1, 0],
    [0, 1, 1]]

# Creiamo una matrice vuota
matrice_abilità = []

# Aggiungiamo l'intestazione delle colonne (abilità) come prima riga
matrice_abilità.append([""] + abilità)

# Aggiungiamo le righe dei tecnici con le relative abilità
for i, tecnico in enumerate(tecnici):
    riga = [tecnico] + abilità_tecnici[i]
    matrice_abilità.append(riga)

# Per stampare la matrice
for riga in matrice_abilità:
    print(riga)

#credo la matrice con le macchine e le abilità richeste
matrice_abilitàPerMacchine = []


