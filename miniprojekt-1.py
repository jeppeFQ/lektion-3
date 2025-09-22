# FREMMØDESYSTEM - Version 2
from datetime import datetime

class Elev:
    """En elev med fremmødehistorik"""
    def __init__(self, navn, klasse, email=""):
        self.navn = navn
        self.klasse = klasse
        self.email = email
        self.registreringer = []
        self.kontaktperson = None  # Tilføjes senere
    
    def tilføj_registrering(self, dato, status, kommentar=""):
        reg = Registrering(dato, status, kommentar)
        self.registreringer.append(reg)
    
    def get_fraværsdage(self):
        return len([r for r in self.registreringer 
                   if r.status in ["Fraværende", "Syg"]])
    
    def get_seneste_status(self):
        if self.registreringer:
            return self.registreringer[-1].status
        return "Ingen registrering"
    
    def __str__(self):
        return f"{self.navn} ({self.klasse})"

class Klasse:
    """En skoleklasse med elever"""
    def __init__(self, klassenavn, klasselærer=""):
        self.klassenavn = klassenavn
        self.klasselærer = klasselærer
        self.elever = []
    
    def tilføj_elev(self, elev):
        self.elever.append(elev)
    
    def find_elev(self, navn):
        for elev in self.elever:
            if elev.navn.lower() == navn.lower():
                return elev
        return None
    
    def get_fremmøde_oversigt(self, dato):
        """Returnerer fremmøde for en specifik dato"""
        oversigt = {
            "Tilstede": 0,
            "Fraværende": 0,
            "Syg": 0
        }
        
        for elev in self.elever:
            for reg in elev.registreringer:
                if reg.dato == dato:
                    if reg.status in oversigt:
                        oversigt[reg.status] += 1
        
        return oversigt
    
    def get_fraværsliste(self):
        """Finder elever med meget fravær"""
        problemliste = []
        for elev in self.elever:
            if elev.get_fraværsdage() > 5:  # Grænse for bekymrende fravær
                problemliste.append(elev)
        return problemliste
    
    def __str__(self):
        return f"Klasse {self.klassenavn} ({len(self.elever)} elever)"




klasse_7a = Klasse("7A", "Jens Hansen")

emma = Elev("Emma Nielsen", "7A", "emma@email.dk")
lucas = Elev("Lucas Andersen", "7A", "lucas@email.dk")
sofie = Elev("Sofie Larsen", "7A")

klasse_7a.tilføj_elev(emma)
klasse_7a.tilføj_elev(lucas)
klasse_7a.tilføj_elev(sofie)

print(f"✓ Tilføjet {len(klasse_7a.elever)} elever til {klasse_7a.klassenavn}")


idag = "2024-11-15"
print(f"\n3. Registrerer fremmøde for {idag}...")
    
emma.tilføj_registrering(idag, "Tilstede")
lucas.tilføj_registrering(idag, "Syg", "Feber")
sofie.tilføj_registrering(idag, "Tilstede")

print(f"\n4. Oversigt for {idag}:")
oversigt = klasse_7a.get_fremmøde_oversigt(idag)
for status, antal in oversigt.items():
    print(f"   {status}: {antal} elever")

lucas.tilføj_registrering("2024-11-14", "Fraværende", "Ikke meldt ind")
lucas.tilføj_registrering("2024-11-13", "Syg")
lucas.tilføj_registrering("2024-11-12", "Fraværende")
emma.tilføj_registrering("2024-11-14", "Tilstede")
sofie.tilføj_registrering("2024-11-14", "Tilstede")

print("\nTjekker for elever med for meget fravær...")
problem_elever = klasse_7a.get_fraværsliste()
    
if problem_elever:
    print("⚠️  Elever med bekymrende fravær:")
    for elev in problem_elever:
        print(f"   - {elev.navn}: {elev.get_fraværsdage()} fraværsdage")
else:
    print("✓ Ingen elever med bekymrende fravær"

for elev in klasse_7a.elever:
    print(f"   {elev.navn}:")
    print(f"      - Seneste status: {elev.get_seneste_status()}")
    print(f"      - Total fraværsdage: {elev.get_fraværsdage()}")
    print(f"      - Email: {elev.email or 'Ikke angivet'}")


#=====================================================================================


# EKSEMPEL: Borgerhenvendelsessystem
class Svar:
    def __init__(self, tekst, afsender, dato):
        self.tekst = tekst
        self.afsender = afsender
        self.dato = dato

class Henvendelse:
    def __init__(self, emne, beskrivelse, borger):
        self.emne = emne
        self.beskrivelse = beskrivelse
        self.borger = borger  # Link til Borger objekt
        self.status = "Ny"
        self.svar = []
        self.sagsbehandler = None
    
    def tilføj_svar(self, tekst, afsender):
        svar = Svar(tekst, afsender, "i dag")
        self.svar.append(svar)
        self.status = "Besvaret"

class Borger:
    def __init__(self, navn, email, telefon=""):
        self.navn = navn
        self.email = email
        self.telefon = telefon
        self.henvendelser = []
    
    def opret_henvendelse(self, emne, beskrivelse):
        h = Henvendelse(emne, beskrivelse, self)
        self.henvendelser.append(h)
        return h

class Afdeling:
    def __init__(self, navn):
        self.navn = navn
        self.henvendelser = []
        self.medarbejdere = []

#================================================================================================

