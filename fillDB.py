from db import *


def fill(db):
    # sprawdzanie i dodawanie po kolei znaków
    name = "A.1"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz przejścia"
        qr = "QR_A1"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.2"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz wyprzedzania"
        qr = "QR_A2"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.3"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz wyprzedzania (dotyczy zestawów)"
        qr = "QR_A3"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.4"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz mijania i wyprzedzania"
        qr = "QR_A4"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.5"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz postoju (na kotwicy lub na cumach przy brzegu)"
        qr = "QR_A5"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.5.1"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz postoju na szerokości określonej na znaku w metrach (od znaku)"
        qr = "QR_A5_1"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.6"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz kotwiczenia, wleczenia kotwicy, łańcucha lub liny"
        qr = "QR_A6"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.7"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz cumowania do brzegu"
        qr = "QR_A7"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.8"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz zawracania"
        qr = "QR_A8"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.9"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz wytwarzania fali"
        qr = "QR_A9"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.10"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz przejścia poza skrajnią określoną tablicami (pod mostem, przez jaz)"
        qr = "QR_A10"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.11"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz przejścia – przygotować się do wejścia lub przejścia"
        qr = "QR_A11"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.12"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz ruchu statków o napędzie mechanicznym"
        qr = "QR_A12"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.13"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz ruchu statków używanych wyłącznie do uprawiania sportu lub rekreacji"
        qr = "QR_A13"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.14"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz uprawiania narciarstwa wodnego oraz holowania statków powietrznych za statkiem"
        qr = "QR_A14"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.15"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz ruchu statków żaglowych"
        qr = "QR_A15"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.16"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz ruchu statków, które nie są statkami o napędzie mechanicznym i żaglowym"
        qr = "QR_A16"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.17"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz pływania na desce z żaglem"
        qr = "QR_A17"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.18"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Koniec strefy, w której małe statki używane wyłącznie do uprawiania sportu lub rekreacji mogły rozwijać duże prędkości"
        qr = "QR_A18"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "A.19"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz wodowania i wciągania statków na brzeg"
        qr = "QR_A19"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "A.20"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zakaz ruchów skuterów wodnych"
        qr = "QR_A20"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.1"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz ruchu w kierunku wskazanym przez znak"
        qr = "QR_B18"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.2a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz skierowania statku na tę stronę szlaku żeglownego, która leży z lewej strony burty"
        qr = "QR_B2a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.2b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz skierowania statku na tę stronę szlaku żeglownego, która leży z prawej strony burty"
        qr = "QR_B2b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.3a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz trzymania się tej strony szlaku żeglownego, która leży z lewej burty"
        qr = "QR_B3a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.3b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz trzymania się tej strony szlaku żeglownego, która leży z prawej burty"
        qr = "QR_B3b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.4a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz przejścia na tę stronę szlaku żeglownego, która leży z lewej strony burty"
        qr = "QR_B4a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.4b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz przejścia na tę stronę szlaku żeglownego, która leży z prawej strony burty"
        qr = "QR_B4b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.5"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz zatrzymania statku w warunkach określonych przepisami"
        qr = "QR_B5"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.6"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz nieprzekraczania podanej na znaku prędkości w km/h"
        qr = "QR_B6"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.7"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz nadania sygnału dźwiękowego"
        qr = "QR_B7"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.8"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz zachowania szczególnej ostrożności"
        qr = "QR_B8"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.9a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz zachowania szczególnej ostrożności. Wejście na główną drogę dozwolone, gdy nie zmusi to statku na tej drodze do zmiany kursu lub prędkości"
        qr = "QR_B9a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.9b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz zachowania szczególnej ostrożności przy przecinaniu głównej drogi wodnej, które może mieć miejsce gdy nie zmusza to statków do zmiany kursu lub prędkości"
        qr = "QR_B9b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.10"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz zmiany kursu lub prędkości przez statki idące główną drogą wodną w sytuacjach, gdy z portu lub z bocznej drogi wodnej wychodzą statki"
        qr = "QR_B10"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "B.11a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz prowadzenia nasłuchu radiotelefonicznego"
        qr = "QR_B11a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "B.11b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Nakaz prowadzenia nasłuchu radiotelefonicznego na wskazanym kanale"
        qr = "QR_B11b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()

    name = "C.1"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Ograniczona głębokość"
        qr = "QR_C1"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "C.2"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Ograniczona wysokość prześwitu nad zwierciadłem wody"
        qr = "QR_C2"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "C.3"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Ograniczona szerokość szlaku lub kanału żeglownego"
        qr = "QR_C3"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "C.4"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Inne ograniczenia ruchu żeglugowego – należy się z nimi zapoznać."
        qr = "QR_C4"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "C.5"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Granica szlaku żeglownego oddalona od prawego (lewego) brzegu w metrach, podanych liczbą na znaku. Statki powinny przechodzić w odległości większej."
        qr = "QR_C5"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "D.1a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zalecenie przejścia w obydwu kierunkach"
        qr = "QR_D1a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "D.1b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zalecenie przejścia w jednym kierunku (przejście z przeciwnego kierunku zabronione)"
        qr = "QR_D1b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "D.2"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zalecenie trzymania się we wskazanym obszarze"
        qr = "QR_D2"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "D.3"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zalecenie przejścia w kierunku określonym strzałką lub w nocy w kierunku światła izofazowego"
        qr = "QR_D3"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.1"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie przejścia (znak ogólny)"
        qr = "QR_E1"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "E.2"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Wskazanie linii napowietrznej nad drogą wodną (liczba w prawym dolnym rogu oznacza wysokość linii napowietrznej nad poziomem najwyższej wody żeglownej)"
        qr = "QR_E2"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.3"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Jaz w bliskiej odległości"
        qr = "QR_E3"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "E.4a"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Prom na uwięzi"
        qr = "QR_E4a"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.4b"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Prom przemieszczający się swobodnie"
        qr = "QR_E4b"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    
    name = "E.5"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na postój (na kotwicy lub na cumach przy brzegu)"
        qr = "QR_E5"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.6"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na postój na kotwicy i wleczenie kotwicy, łańcucha lub liny"
        qr = "QR_E6"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.7"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na cumowanie do brzegu"
        qr = "QR_E7"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.8"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Wskazanie miejsca do zawracania"
        qr = "QR_E8"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.11"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Koniec obowiązywania zakazu lub nakazu albo ograniczenia – obowiązuje tylko w jednym kierunku ruchu żeglugowego"
        qr = "QR_E11"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.13"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Miejsce poboru wody pitnej"
        qr = "QR_E13"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.14"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Miejsce, w którym można korzystać z telefonu"
        qr = "QR_E14"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.15"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch żeglugowy statków o napędzie mechanicznym"
        qr = "QR_E15"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.16"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch żeglugowy statków używanych wyłącznie do uprawiania sportu lub rekreacji"
        qr = "QR_E16"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.17"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na uprawianie narciarstwa wodnego oraz holowanie statków powietrznych za statkiem"
        qr = "QR_E17"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.18"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch statków żaglowych"
        qr = "QR_E18"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.19"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch statków o napędzie wiosłowym"
        qr = "QR_E19"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.20"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na pływanie na desce z żaglem"
        qr = "QR_E20"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.21"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch małych statków sportowych i turystycznych z dużą prędkością"
        qr = "QR_E21"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.22"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na wodowanie i wciąganie statków na brzeg"
        qr = "QR_E22"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
        
    name = "E.23"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Wskazanie kanału radiotelefonicznego, na którym można uzyskać informacje nawigacyjne"
        qr = "QR_E23"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
            
    name = "E.24"
    existing_sign = Sign.query.filter_by(SignName=name).first()
    if not existing_sign:
        description = "Zezwolenie na ruch skuterów wodnych"
        qr = "QR_E24"
        new_sign = Sign(SignName=name, Description=description, QRCode=qr)
        db.session.add(new_sign)
        db.session.commit()
    

    # sprawdzanie i dodawanie po kolei osiągnięć
    name = "Nowicjusz"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Znajdź 1 znak"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()
    
    name = "Poszukiwacz"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Znajdź 5 znaków"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()
    
    name = "Odkrywca"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Znajdź 10 znaków"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()
    
    name = "Badacz"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Znajdź 20 znaków"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Ekspert"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Znajdź 50 znaków"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Początkujący quizmaster"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Rozwiąż 1 quiz"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Zaawansowany quizmaster"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Rozwiąż 5 quizów"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Mistrz quizów"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Rozwiąż 10 quizów"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Geniusz quizów"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Rozwiąż 20 quizów"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

    name = "Arcymistrz quizów"
    existing_achievement = Achievement.query.filter_by(AchievementName=name).first()
    if not existing_achievement:
        description = "Rozwiąż 50 quizów"
        new_achievement = Achievement(AchievementName=name, Description=description)
        db.session.add(new_achievement)
        db.session.commit()

# sprawdzanie i dodawanie po kolei pytań