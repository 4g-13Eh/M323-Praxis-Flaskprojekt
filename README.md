# Praxisprojekt M323

## Projektbeschreibung
Das ist eine kleine Flask-Applikation, welche fürs Moduls 323 entwickelt wurde. Die Anwendung demonstriert verschiedene funktionale Programmierkonzepte durch eine Sammlung von Endpoints. Bis auf die C-Lernziele haben alle Lernziele einen eigenen Endpoint.

## Lernziele
### Grundlagen
- **A1G**: Erklärung der Eigenschaften von Funktionen, wie z. B. pure Funktionen und deren Unterschiede zu anderen Programmierstrukturen wie Prozedur.
- **B1G**: Erklärung grundlegender Algorithmen.
- **B2G**: Behandlung von Funktionen als Objekte, die in Variablen gespeichert und weitergegeben werden können.
- **B3G**: Schreiben einfacher Lambda-Ausdrücke für einzelne Operationen, z. B. Quadrieren einer Zahl.
- **B4G**: Einzeln anwenden von Map, Filter und Reduce auf Listen.
- **C1G**: Aufzählen von Refactoring-Techniken, die einen Code lesbarer und verständlicher machen.

### Fortgeschritten
- **A1F**: Erläuterung des Konzepts von immutable values und deren Bedeutung in der funktionalen Programmierung.
- **B1F**: Fähigkeit, Algorithmen in funktionale Bestandteile zu zerlegen.
- **B2F**: Verwendung von Funktionen als Argumente für andere Funktionen zur Erstellung höherwertiger Funktionen.
- **B3F**: Schreiben von Lambda-Ausdrücken, die mehrere Argumente verarbeiten können.
- **B4F**: Kombinierte Verwendung von Map, Filter und Reduce für komplexe Datenverarbeitung.
- **C1F** Anwenden von Refactoring-Techniken, um Code lesbarer und verständlicher zu gestalten.

### Erweitert
- **A1E**: Aufzeigen, wie Probleme in den Konzepten objektorientierte Programmierung (OO), prozedurale Programmierung und funktionale Programmierung gelöst werden. Vergleich der Lösungen.
- **B1E**: Implementierung von Funktionen in zusammenhängende Algorithmen.
- **B2E**: Verwendung von Funktionen als Objekte und Argumente für komplexe Aufgaben, einschließlich Anwendung von Closures.
- **B3E**: Verwendung von Lambda-Ausdrücken zur Steuerung des Programmflusses, z. B. Sortieren von Listen basierend auf benutzerdefinierten Kriterien.
- **B4E**: Anwendung von Map, Filter und Reduce für komplexe Datenverarbeitungsaufgaben wie Aggregation von Daten oder Transformation von Datenstrukturen.
- **C1E**: Einschätzen der Auswirkungen des Refactorings auf das Verhalten des Codes und Sicherstellen, dass keine unerwünschten Nebeneffekte auftreten.

## Installation / Ausführung
1. Repository klonen
```
git clone git@github.com:HUE-Dedf1sh/M323-Praxis-Flaskprojekt.git
```
2. In das Verzeichnis wechseln
```
cd M323-Praxis-Flaskprojekt
```
3. Requirements installieren
```
pip install -r requirements.txt
```
4. Applikation starten mit
```python main.py```
oder
```flask --app main.py run``` 


## Tests
Die Endpoints wurde mit Postman getestet. Sie können die Tests mit dem untenstehenden Button importieren. Falls der Button  oder die Tests nicht funktionieren, können Sie die Tests auch manuell importieren. Die Tests befinden sich im Verzeichnis ```tests```. Die Applikation muss gestartet sein, damit die Tests funktionieren.

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/26136977-092e08fa-a279-483f-9f86-d14f178ed2d8?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D26136977-092e08fa-a279-483f-9f86-d14f178ed2d8%26entityType%3Dcollection%26workspaceId%3D378bc62c-a63d-448e-8372-032400ac36c1)