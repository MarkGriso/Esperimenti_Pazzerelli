import pandas as pd
import numpy as np

tecnici = ["Franco", "Gianni", "Luca", "Piero"]
abilità = ["bracci mec", "motore", "vetri"]
abilità_tecnici = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 1, 1]
]

macchine_da_riparare = ["n1", "n2", "n3", "n4"]
abilità_richieste_per_riparazione = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 1, 0],
    [0, 1, 1]
]

# Creazione della matrice con tecnici come righe e abilità_tecnici come colonne
df_tecnici_abilità = pd.DataFrame(abilità_tecnici, index=tecnici, columns=abilità)

# Creazione della matrice con macchine_da_riparare come colonne e abilità come colonne
df_riparazioni_abilità = pd.DataFrame(abilità_richieste_per_riparazione, columns=abilità, index=macchine_da_riparare)

print("Matrice con tecnici come righe e abilità come colonne:")
print(df_tecnici_abilità)
print("\nMatrice con macchine_da_riparare come colonne e abilità come colonne:")
print(df_riparazioni_abilità)



def ottimizza_abilità(abilità_tecnici, abilità_richieste):
    # Converti le liste in DataFrame Pandas
    df_tecnici = pd.DataFrame(abilità_tecnici)
    df_richieste = pd.DataFrame(abilità_richieste)
    
    # Calcola la discrepanza tra le abilità richieste e le abilità attuali dei tecnici
    discrepanza = df_richieste - df_tecnici
    
    # Per ogni tecnico, calcola il numero di abilità che devono essere aggiunte
    abilità_da_aggiungere = discrepanza.clip(lower=0).sum(axis=1)
    
    # Ordina i tecnici in base al numero di abilità da aggiungere e ottimizza le abilità
    tecnici_ottimizzati = df_tecnici.copy()
    for tecnico, abilità_da_aggiungere in abilità_da_aggiungere.iteritems():
        if abilità_da_aggiungere > 0:
            # Se ci sono abilità da aggiungere, prendi le prime abilità richieste
            abilità_mancanti = discrepanza.loc[tecnico].nlargest(abilità_da_aggiungere).index
            tecnici_ottimizzati.loc[tecnico, abilità_mancanti] = 1
    
    # Restituisci le abilità ottimizzate
    return tecnici_ottimizzati.values.tolist()

def assegna_tecnici(abilità_tecnici, df_richieste, tecnici, macchine):
    # Ottimizza le abilità dei tecnici
    abilità_ottimizzate = ottimizza_abilità(abilità_tecnici, df_richieste.values.tolist())
    
    # Converti le abilità ottimizzate in un DataFrame Pandas
    df_tecnici = pd.DataFrame(abilità_ottimizzate, columns=df_richieste.columns)
    
    # Calcola il numero di abilità soddisfatte per ogni tecnico
    abilità_soddisfatte = df_tecnici.dot(df_richieste.T)
    
    # Associa ogni macchina al tecnico con il massimo numero di abilità soddisfatte
    assegnazioni = {}
    for macchina, richieste in zip(macchine, df_richieste.values):
        tecnico = abilità_soddisfatte[tecnici].idxmax(axis=1)[macchina]
        assegnazioni[macchina] = tecnico
    
    return assegnazioni


def ottimizza_e_assegna_tecnici(tecnici, abilità, abilità_tecnici, macchine, abilità_richieste):
    # Ottimizza le abilità dei tecnici
    abilità_ottimizzate = ottimizza_abilità(abilità_tecnici, abilità_richieste)
    
    # Converti le abilità ottimizzate in un DataFrame Pandas
    df_tecnici = pd.DataFrame(abilità_ottimizzate, columns=abilità)

    df_richieste = pd.DataFrame(abilità_richieste)
    print("df_richieste_outpu \n", df_richieste)
    
    # Calcola il numero di abilità soddisfatte per ogni tecnico
    abilità_soddisfatte = df_tecnici.dot(df_richieste.T)
    
    # Associa ogni macchina al tecnico con il massimo numero di abilità soddisfatte
    assegnazioni = {}
    for macchina, richieste in zip(macchine, df_richieste.values):
        tecnico = abilità_soddisfatte[tecnici].idxmax(axis=1)[macchina]
        assegnazioni[macchina] = tecnico
    
    # Crea una lista di tuple di tecnici e macchine assegnate
    tecnici_macchine_assegnate = [(tecnico, macchina) for macchina, tecnico in assegnazioni.items()]
    
    return tecnici_macchine_assegnate

# Esempio di utilizzo della funzione
risultato = ottimizza_e_assegna_tecnici(tecnici, abilità, abilità_tecnici, macchine_da_riparare, abilità_richieste_per_riparazione)
print("Assegnazioni univoche di tecnico e macchina da riparare ottimale:")
print(risultato)