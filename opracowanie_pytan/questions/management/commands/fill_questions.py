# -*- coding: UTF-8 -*-
'''
Created on May 11, 2016

@author: root
'''
from django.core.management.base import BaseCommand, CommandError
from opracowanie_pytan.questions.models import Kierunek, Pytanie


class Command(BaseCommand):
    help = 'Adds specializations and their questions'

    def handle(self, *args, **options):
        everything = [
            {"PYTANIA Z PRZEDMIOTÓW PODSTAWOWYCH I KIERUNKOWYCH": [
                "Omówić podstawowe elementy programowania obiektowego dostępne w języku PHP.",
                "Naszkicować sposób implementacji klasy PHP ukrywającej szczegóły połączenia z bazą danych PostgreSQL. Proszę krótko omówić zastosowane rozwiązania i ich zalety.",
                "Na czym polega metoda 'dziel i zwyciężaj'?",
                "Scharakteryzuj algorytmy sortowania – idee ich działania i złożoności obliczeniowe.",
                "Co to jest złożoność obliczeniowa algorytmu? Podaj przykładowe złożoności obliczeniowe.",
                "Proszę omówić podstawowe elementy typowego procesora stosowanego w komputerach PC.",
                "Krótko scharakteryzować różnice między architekturą typu RISC i CISC 2.",
                "Omówić hierarchię pamięci stosowaną we współczesnych komputerach. Podać podstawowe cechy pamięci podręcznych.",
                "Proszę wyjaśnić różnice między mapowaniem asocjacyjnym, bezpośrednim i zbiorowo-asocjacyjnym pamięci podręcznej.",
                "Podać definicję systemu operacyjnego oraz różne sposoby klasyfikacji systemów operacyjnych (z przykładami).",
                "Omówić zasadę działania mechanizmu stronicowania i wymiany we współczesnym systemie operacyjnym typu UNIX.",
                "Konfiguracja routera dla małej sieci z dostępem do Internetu, np. Wi-FI (NETIA).",
                "Technologie sieci światłowodowych: źródła i detektory światła, modulatory, kable.",
                "Omów różnice pomiędzy programowaniem imperatywnym i obiektowym.",
                "Omów następujące własności obiektów -> konstruktor, destruktor, zmienne i metody prywatne i publiczne, przeciążenie metod i konstruktorów.",
                "Cechy grafiki wektorowej i rastrowej – porównanie.",
                "Przedstawić metodę śledzenia promieni (ray-tracing) oraz podać jej właściwości.",
                "Proszę omówić zasadę działania sieci neuronowej. Proszę podać przykłady różnych typów sieci neuronowych, ich charakterystykę i przykładowe zastosowania.",
                "Omówić zasadę działania optymalizacji metodą algorytmu genetycznego. Proszę naszkicować sposób implementacji takiego algorytmu.",
                "Wymienić i omówić podstawowe własności relacyjnej bazy danych.",
                "Wymienić podstawowe grupy i instrukcje języka SQL i omówić jedną z nich na przykładzie.",
                "Zarządzanie wymaganiami na system aplikacyjny.",
                "Cykl wytwarzania systemu z podejściem przyrostowym.",
                "Przedstaw prawa de Morgana i zilustruj je na podstawie układu bramek logicznych.",
                "Omów działania procesora i koprocesora. Podstawowe rejestry i zasady działania na nich w obydwu przypadkach.",
                "Wymień podstawowe elementy kodeksu etycznego.",
                "Omów problem odpowiedzialności informatyka za moralne i społeczne konsekwencje jego działalności."
                ]},
            {"GRAFIKA KOMPUTEROWA I MULTIMEDIA": [
                "W wyniku jakich procesów powstaje obraz cyfrowy?",
                "Omów, na czym polega zasada 'złotego podziału' w fotografii.",
                "Na czym polega zjawisko aberracji chromatycznej?",
                "W jaki sposób powstaje flara na zdjęciu?",
                "Wymień i krótko opisz etapy powstawania filmu fabularnego?",
                "Wymień i scharakteryzuj plany w filmie?",
                "Na czym polega montaż liniowy i nieliniowy podczas produkcji filmu?",
                "Co to jest postprodukcja?",
                "Co jest podstawą budowy obrazu bitmapowego, technicznie określanego jako obraz rastrowy?",
                "Czym jest kanał alfa w programie Adobe Photoshop?",
                "Która z wymienionych form kompresji jest określana jako bezstratna?: a. jpg z maksymalną jakością; b. tif z zaznaczonym oknem LZW; c. psd d.gif",
                "W jakich trybach koloru nie mogą być stosowane filtry: a. CMYK; b. RGB; c. bitmap (bitmapa) i indexed color (kolor indeksowany); d. duotone (duoton)",
                "Opisz różnicę pomiędzy przetwarzaniem punktowym a kontekstowym, podaj wady i zalety obu przetwarzań oraz ich zastosowanie.",
                "Na czym polega erozja, dylatacja, otwarcie i zamknięcie przy przetwarzaniu morfologicznym?",
                "Wymień i opisz algorytmy do detekcji krawędzi.",
                "Jak działa i w jakim celu stosuje się filtry medianowe?",
                "Co to są 'mipmapy', jak się je tworzy i w jakim celu się je stosuje?",
                "Opisz rodzaje oświetlenia stosowanego w modelowaniu scen 3D.",
                "Co to jest teksturowanie? Omów sposoby nakładania tekstur na różne obiekty.",
                "Wymień i scharakteryzuj rodzaje rzutowania stosowanego w grafice komputerowej.",
                "Jakie rodzaje oświetlenia występują w programie POV-Ray? Omów je.",
                "Jakie operacje CSG (ang. Constructive Solid Geometry) są dostępne w programie POV-Ray i na czym polegają?",
                "W jaki sposób realizuje się animację w programie POV-Ray?",
                "Jakie możliwości ustawień materiału posiada POV-Ray? Omów je."
                ]},
            {"SIECI KOMPUTEROWE I SYSTEMY ROZPROSZONE": [
                "Na czym polega impas w programowaniu współbieżnym i jak można go unikać?",
                "Proszę krótko opisać zasadę działania semafora typu Mutex.",
                "Proszę krótko opisać „Problem ucztujących filozofów”.",
                "Co to są operacje atomowe procesora? Kiedy konieczne jest ich wykorzystanie?",
                "Proste szyfry. Szyfrowanie metodą podstawiania.",
                "Szyfrowanie metodą przestawiania. Zasada Kerckhoffsa.",
                "Szyfrowanie z kluczem. Szyfrowanie symetryczne. Szyfrowanie asymetryczne.",
                "Matematyczne podstawy kryptografii. Największy wspólny dzielnik.",
                "Typowe reguły protokołu trasowania (podzielony horyzont, zatruwanie, zatrucie wstecz aktualizacje wymuszone, zliczanie do nieskończoności). Jak one są realizowane w protokołach RIP i OSPF?",
                "Jakie warunki musi spełniać sieć, aby routery BGP (Border Gateway Protocol) się komunikowały? Omów podstawowe cechy protokołu BGP.",
                "Metryka w protokołach trasowania (RIP, EIGRP, OSPF).",
                "Protokół drzewa rozpinającego w warstwie 2 sieci. Co nowego wprowadza rozwiązanie VLAN?",
                "Wymień dwa systemy plików, na których możliwa jest instalacja systemu FreeBSD.",
                "Czy jądro FreeBSD to mikrojądro?",
                "Co to jest DTrace?",
                "Omów proces uruchamiania systemu FreeBSD.",
                "Co to znaczy przetwarzać dane osobowe?",
                "Jakie akty prawne chronią dane osobowe?",
                "Jakie są zagrożenia fizyczne dla systemów informatycznych?",
                "Proszę opisać proces szacowania ryzyka.",
                "Co to jest Usługa Katalogowa (AD)?",
                "Co to jest DNS i jak działa?",
                "Proszę opisać grupy występujące w AD.",
                "Proszę opisać systemy RAID.",
                ]},
            {"BEZPIECZEŃSTWO I OCHRONA INFORMACJI": [
                "Na czym polega impas w programowaniu współbieżnym i jak można go unikać?",
                "Proszę krótko opisać zasadę działania semafora typu Mutex.",
                "Proszę krótko opisać 'Problem ucztujących filozofów'.",
                "Co to są operacje atomowe procesora? Kiedy konieczne jest ich wykorzystanie?",
                "Proste szyfry. Szyfrowanie metodą podstawiania.",
                "Szyfrowanie metodą przestawiania. Zasada Kerckhoffsa.",
                "Szyfrowanie z kluczem. Szyfrowanie symetryczne. Szyfrowanie asymetryczne.",
                "Matematyczne podstawy kryptografii. Największy wspólny dzielnik.",
                "Typowe reguły protokołu trasowania (podzielony horyzont, zatruwanie, zatrucie wstecz, aktualizacje wymuszone, zliczanie do nieskończoności). Jak one są realizowane w protokołach RIP i OSPF?",
                "Jakie warunki musi spełniać sieć, aby routery BGP (Border Gateway Protocol) się komunikowały? Omów podstawowe cechy protokołu BGP.",
                "Metryka w protokołach trasowania (RIP, EIGRP, OSPF).",
                "Protokół drzewa rozpinającego w warstwie 2 sieci. Co nowego wprowadza rozwiązanie VLAN?",
                "Co to znaczy przetwarzać dane osobowe?",
                "Jakie akty prawne chronią dane osobowe?",
                "Jakie są zagrożenia fizyczne dla systemów informatycznych?",
                "Proszę opisać proces szacowania ryzyka?",
                "Co to jest Usługa Katalogowa (AD)?",
                "Co to jest DNS i jak działa?",
                "Proszę opisać grupy występujące w AD.",
                "Proszę opisać systemy RAID.",
                "Omów algorytmy determinizacji automatów skończonych i ich znaczenie.",
                "Języki regularne a automaty skończone.",
                "Omów fazy pracy komilatora.",
                "Co to jest i jakie zadania realizuje Parser.",
                ]},
            {"ZARZĄDZANIE INFORMACJĄ I BAZY DANYCH": [
                "Proste szyfry. Szyfrowanie metodą podstawiania.",
                "Szyfrowanie metodą przestawiania. Zasada Kerckhoffsa.",
                "Szyfrowanie z kluczem. Szyfrowanie symetryczne. Szyfrowanie asymetryczne.",
                "Matematyczne podstawy kryptografii. Największy wspólny dzielnik.",
                "Wyjaśnij, co to jest procedura składowana (ang. stored procedure), i wskaż zakres jej stosowania.",
                "Wyjaśnij, co to jest Wyzwalacz (ang. trigger), i wskaż zakres jego stosowania.",
                "Wyjaśnij, co to jest model relacyjny (ang. relational model) bazy danych.",
                "Wyjaśnij, co to są transakcje w SQL i do czego służą. Wymień znane transakcje.",
                "Wyjaśnić pojęcia z teorii nierelacyjnych baz danych (CAP – Consistency, Availability, Partition Tolerance, BASE – Basically Available, Soft-state, Eventually consistent). Porównać definicją z relacyjnych baz danych (ACID – Atomicity, Consistency, Isolation, Durability).",
                "Klasyfikacja baz nierelacyjnych według kryterium dwie cechy z trzech CAP na jeden system bazodanowy.",
                "Struktura bazy nierelacyjnej Mongodb (format JSON).",
                "Polecenia wyszukiwania i agregacji w bazie nierelacyjnej Mongodb (find, aggregate).",
                "Co to znaczy przetwarzać dane osobowe?",
                "Jakie akty prawne chronią dane osobowe?",
                "Jakie są zagrożenia fizyczne dla systemów informatycznych?",
                "Proszę opisać proces szacowania ryzyka.",
                "Co to jest Usługa Katalogowa (AD)?",
                "Co to jest DNS i jak działa?",
                "Proszę opisać grupy występujące w AD.",
                "Proszę opisać systemy RAID.",
                "Omów algorytmy determinizacji automatów skończonych i ich znaczenie.",
                "Języki regularne a automaty skończone.",
                "Omów fazy pracy komilatora.",
                "Co to jest i jakie zadania realizuje Parser?",
                ]},
            {"APLIKACJE INTERNETOWE I MOBILNE": [
                "Wyjaśnij, co to jest język xml (ang. Extensible Markup Language), i wskaż zakres jego zastosowania.",
                "Wyjaśnij, co to są kaskadowe arkusze stylów (ang. Cascading Style Sheets, CSS), i wskaż zakres ich używania.",
                "Wyjaśnij, co to jest język XSL (ang. Extensible Stylesheet Language), i wskaż zakres jego używania.",
                "Wyjaśnij, co to jest język HTML (ang. HyperText Markup Language), i wskaż zakres jego używania.",
                "Na czym polega impas w programowaniu współbieżnym i jak można go unikać?",
                "Proszę krótko opisać zasadę działania semafora typu Mutex.",
                "Proszę krótko opisać „Problem ucztujących filozofów”.",
                "Co to są operacje atomowe procesora? Kiedy konieczne jest ich wykorzystanie?",
                "Opis struktury pliku z klasą w języku Java (nazwa pliku, nazwa klasy, funkcja main).",
                "Podaj kilka przykładów mechanizmów programowania wątków w Javie, np. klasa Executor.",
                "Wymień i krótko opisz biblioteki graficzne Javy.",
                "Narzędzia kompilacji i konsolidacji w Javie (ant, maven).",
                "Opisz różnicę pomiędzy przetwarzaniem punktowym a kontekstowym, podaj wady i zalety obu przetwarzań oraz ich zastosowanie.",
                "Na czym polega erozja, dylatacja, otwarcie i zamknięcie przy przetwarzaniu morfologicznym?",
                "Wymień i opisz algorytmy do detekcji krawędzi.",
                "Jak działa i w jakim celu stosuje się filtry medianowe?",
                "Wymień popularne mobilne systemy operacyjne i omów ich podstawowe cechy, historię rozwoju.",
                "Jakie funkcje telefonu mogą być oprogramowane w systemie Android, a jakie w systemie Apple IOS?",
                "Omówić opracowane w systemie Android cykle klasy Activity i klasy Service (osobno i z porównaniem).",
                "Wątki w systemie Android (czy wszystkie mają takie same możliwości jak np. wątki w Linuxie?).",
                "Możliwości systemów zarządzania treścią w programowaniu internetowym.",
                "Idea technologii AJAX w tworzeniu aplikacji i internetowych.",
                "Wzorzec projektowy MVC w tworzeniu aplikacji indenowych.",
                "Kontrolki serwerowe Web Server a HTML Server w technologii ASP.NET.",
                ]},
            {"INŻYNIERIA OPROGRAMOWANIA": [
                "Scharakteryzuj systematykę wzorców projektowych w inżynierii oprogramowania.",
                "Scharakteryzuj grupę behawioralnych wzorców projektowych na wybranych przykładach.",
                "Scharakteryzuj grupę kreacyjnych wzorców projektowych na wybranych przykładach.",
                "Scharakteryzuj grupę strukturalnych wzorców projektowych na wybranych przykładach.",
                "Podaj definicję refaktoryzacji oraz omów kilka przekształceń refaktoryzacyjnych.",
                "Scharakteryzuj i porównaj metody przesyłania danych za pomocą HTTP – POST i GET.",
                "Opisz sposoby generowania dynamicznych stron internetowych z wykorzystaniem systemu szablonów, np. Django.",
                "Podaj i scharakteryzuj składowe wzorca projektowego MVC.",
                "Podaj i omów najważniejsze składowe projektu i aplikacji tworzonych z wykorzystaniem szkieletu aplikacyjnego Django.",
                "Wyjaśnij, co to jest język XML (ang. Extensible Markup Language), i wskaż zakres jego zastosowania.",
                "Wyjaśnij, co to są kaskadowe arkusze stylów (ang. Cascading Style Sheets, CSS), i wskaż zakres ich używania.",
                "Wyjaśnij, co to jest język XSL (ang. Extensible Stylesheet Language), i wskaż zakres jego używania.",
                "Wyjaśnij, co to jest język HTML (ang. HyperText Markup Language), i wskaż zakres jego używania.",
                "Wyjaśnij różnicę pomiędzy analizą systemu a projektowaniem systemu.",
                "Scharakteryzuj rolę i zadania analityka systemowego.",
                "Scharakteryzuj wymagania funkcjonalne i niefunkcjonalne.",
                "Opisz, na czym polega obsługa cyklu życia produktu.",
                "Czym różni się testowanie od debugowania? Proszę podać krótkie definicje.",
                "Scharakteryzuj cele i narzędzia testowania jednostkowego.",
                "Czym różnią się metody testowania „czarnej skrzynki” i „białej skrzynki”?",
                "Scharakteryzuj różne poziomy testowania oprogramowania.",
                "Opisz i porównaj metody przetwarzania danych XML – SAX i DOM.",
                "Opisz wady i zalety programowania wielowątkowego i wieloprocesowego w Pythonie.",
                "Scharakteryzuj wyrażenia i podaj zakres zastosowań wyrażeń regularnych.",
                ]},
        ]

        for spec in everything:
            kierunek = Kierunek.objects.create(name=spec.keys()[0])
            for question in spec[spec.keys()[0]]:
                Pytanie.objects.create(name=question,
                                       spec=kierunek,
                                       reserved=None)