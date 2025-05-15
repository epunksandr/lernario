# lernario

### Datenbank erstellen
Die lernario.db Datei wurde aus dem GitHub Repository entfernt, da sie für Merge-Konflikte gesorgt hat. Deshalb sollte
die lernario.db nachdem Erstellen auf die .gitignore-Liste kommen. Um die Datenbank zu erstellen, müssen folgende Schritte
getan werden:  
```commandline
sqlite3 lernario.db < schema.sql
sqlite3 lernario.db < dummy_daten.sql
```
