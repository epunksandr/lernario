-- Fächer
INSERT INTO faecher (fach_id, fach) VALUES
(1, 'Mathematik'),
(2, 'Deutsch'),
(3, 'Englisch'),
(4, 'Biologie'),
(5, 'Geschichte');

-- Klassen
INSERT INTO klassen (klasse_id, klassenname) VALUES
(1, '5A'),
(2, '5B');

-- Lehrer
--passwort bei allen drei Lehrern: passwort
INSERT INTO lehrer (lehrer_id, vorname, nachname, email, passwort) VALUES
(1, 'test', 'test', 'test@schule.de', '5630fa4e304e9dc0c18b47376dc77ef0a342895f44868ae20e85fcc6834df8d2186faad0bd985aaa171d58807b8e09e4743e5bb9d4d47dc6dc2b8c52e9b31cd4'),
(2, 'Thomas', 'Schmidt', 'thomas.schmidt@schule.de', '5630fa4e304e9dc0c18b47376dc77ef0a342895f44868ae20e85fcc6834df8d2186faad0bd985aaa171d58807b8e09e4743e5bb9d4d47dc6dc2b8c52e9b31cd4'),
(3, 'Laura', 'Fischer', 'laura.fischer@schule.de', '5630fa4e304e9dc0c18b47376dc77ef0a342895f44868ae20e85fcc6834df8d2186faad0bd985aaa171d58807b8e09e4743e5bb9d4d47dc6dc2b8c52e9b31cd4');

-- Schüler
INSERT INTO schueler (schueler_id, klasse_id, vorname, nachname) VALUES
(1, 1, 'Max', 'Mustermann'),
(2, 1, 'Julia', 'Schneider'),
(3, 2, 'Lukas', 'Weber'),
(4, 2, 'Lea', 'Koch');

-- Unterrichte
INSERT INTO unterrichte (unterricht_id, lehrer_id, fach_id, klasse_id) VALUES
(1, 1, 1, 1), -- Anna Müller unterrichtet Mathe in 5A
(2, 2, 2, 1), -- Thomas Schmidt unterrichtet Deutsch in 5A
(3, 3, 3, 2), -- Laura Fischer unterrichtet Englisch in 5B
(4, 1, 4, 2); -- Anna Müller unterrichtet Biologie in 5B

-- Abwesenheiten
INSERT INTO abwesenheiten (abwesenheit_id, schueler_id, datum) VALUES
(1, 1, '2025-01-15'),
(2, 2, '2025-02-10'),
(3, 4, '2025-03-22');

-- Noten
INSERT INTO noten (note_id, schueler_id, unterricht_id, note) VALUES
(1, 1, 1, 2.3),
(2, 1, 2, 3.0),
(3, 2, 1, 1.7),
(4, 3, 3, 2.0),
(5, 4, 4, 2.5);

-- Termine
INSERT INTO termine (termin_id, termin_name, datum, klasse_id, beschreibung) VALUES
(1, 'Elternabend', '2025-06-10', 1, 'Besprechung der Halbjahresnoten'),
(2, 'Wandertag', '2025-05-30', 2, 'Ausflug zum Zoo'),
(3, 'Zeugnisausgabe', '2025-07-15', NULL, 'Alle Klassen');