CREATE TABLE faecher (
    fach_id INTEGER PRIMARY KEY,
    fach TEXT
);

CREATE TABLE lehrer (
    lehrer_id INTEGER PRIMARY KEY,
    vorname TEXT,
    nachname TEXT,
    email TEXT UNIQUE,
    passwort TEXT
);

CREATE TABLE klassen (
    klasse_id INTEGER PRIMARY KEY,
    klassenname TEXT,
    einschulungsjahr INTEGER
);

CREATE TABLE schueler (
    schueler_id INTEGER PRIMARY KEY,
    klasse_id INTEGER,
    vorname TEXT,
    nachname TEXT,
    FOREIGN KEY (klasse_id) REFERENCES klassen(klasse_id) ON DELETE CASCADE
);

CREATE TABLE unterrichte (
    unterricht_id INTEGER PRIMARY KEY,
    lehrer_id INTEGER,
    fach_id INTEGER,
    klasse_id INTEGER,
    FOREIGN KEY (lehrer_id) REFERENCES lehrer(lehrer_id) ON DELETE CASCADE,
    FOREIGN KEY (fach_id) REFERENCES faecher(fach_id) ON DELETE CASCADE,
    FOREIGN KEY (klasse_id) REFERENCES klassen(klasse_id) ON DELETE CASCADE
);

CREATE TABLE abwesenheiten (
    abwesenheit_id INTEGER PRIMARY KEY,
    schueler_id INTEGER,
    datum DATE,
    FOREIGN KEY (schueler_id) REFERENCES schueler(schueler_id) ON DELETE CASCADE
);

CREATE TABLE noten (
    note_id INTEGER PRIMARY KEY,
    schueler_id INTEGER,
    unterricht_id INTEGER,
    note REAL,
    FOREIGN KEY (schueler_id) REFERENCES schueler(schueler_id) ON DELETE CASCADE,
    FOREIGN KEY (unterricht_id) REFERENCES unterrichte(unterricht_id) ON DELETE CASCADE
);

CREATE TABLE termine (
    termin_id INTEGER PRIMARY KEY,
    termin_name TEXT NOT NULL,
    datum DATE NOT NULL,
    klasse_id INTEGER,
    beschreibung TEXT,
    FOREIGN KEY (klasse_id) REFERENCES klassen(klasse_id) ON DELETE CASCADE
);