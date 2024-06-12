##ΠΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ – ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΤΡΙΤΗ 11 ΙΟΥΝΙΟΥ 2024
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Γ
##Σε έναν διαγωνισμό μαθηματικών συμμετέχουν μαθητές από όλη τη χώρα.
##Κάθε διαγωνιζόμενος βαθμολογείται σε δέκα (10) θέματα. Η βαθμολογία
##κάθε θέματος είναι από 1 έως και 20 μονάδες. Η τελική βαθμολογία κάθε
##διαγωνιζόμενου προκύπτει από τον μέσο όρο των βαθμολογιών των δέκα
##(10) θεμάτων. Στην επόμενη φάση του διαγωνισμού προκρίνονται οι
##διαγωνιζόμενοι που έχουν τελική βαθμολογία μεγαλύτερη από 15 και σε
##όλα τα θέματα έχουν βαθμό μεγαλύτερο ή ίσο του 12. Να αναπτύξετε
##πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο:
##Γ1. Για κάθε διαγωνιζόμενο:
##α) Να διαβάζει το ονοματεπώνυμό του (μον.1).
##β) Να διαβάζει τη βαθμολογία για καθένα εκ των δέκα (10) θεμάτων με
##έλεγχο ορθότητας τιμών (μον.4).
##γ) Η εισαγωγή των δεδομένων να τερματίζει, όταν δοθεί ως ονοματεπώνυμο
##διαγωνιζόμενου η λέξη "ΤΕΛΟΣ" (μον.2).
##Θεωρήστε ότι υπάρχουν τουλάχιστον δύο (2) διαγωνιζόμενοι.
##Μονάδες 7
##Γ2. Να υπολογίζει και να εμφανίζει την τελική βαθμολογία κάθε
##διαγωνιζόμενου.
##Μονάδες 4
##Γ3. Να εμφανίζει κατάλληλο μήνυμα, εάν ο διαγωνιζόμενος προκρίνεται
##στην επόμενη φάση.
##Μονάδες 5
##Γ4. Να βρίσκει και να εμφανίζει τη μεγαλύτερη τελική βαθμολογία.
##Μονάδες 4
##Γ5. Να υπολογίζει και να εμφανίζει το ποσοστό των διαγωνιζόμενων που
##προκρίθηκαν στην επόμενη φάση.
##Μονάδες 5
##
THEMATA = 10
MONADES = 20
PROKRISI = 15.0
ORIO = 12

onomatepwnymo = ""
max_teliki_vathmologia = 0
synolo_diag = 0
synolo_prokr = 0

##while onomatepwnymo != "ΤΕΛΟΣ":
##    onomatepwnymo = input("Ονοματεπώνυμο διαγωνιζόμενου: ")
##    if onomatepwnymo == "ΤΕΛΟΣ":
##        print("Τερματισμός εισαγωγής δεδομένων")
##    else:
##        synolo_diag += 1
##        synolo_vathmologias = 0
##        panw_apo_orio = True
##        for thema in range(1, THEMATA+1):
##            vathmologia = ""
##            while not vathmologia.isdigit() \
##              or int(vathmologia) not in range(1, MONADES+1):
##                vathmologia = input("Βαθμολογία στο θέμα {}: ".format(thema))
##            vathmologia = int(vathmologia)
##            if vathmologia < ORIO:
##                panw_apo_orio = False
##            synolo_vathmologias += vathmologia
##        teliki_vathmologia = synolo_vathmologias/THEMATA
##        print(teliki_vathmologia) ##
##        if panw_apo_orio == True and teliki_vathmologia > PROKRISI:
##            print("Ο διαγωνιζόμενος προκρίνεται στην επόμενη φάση")
##            synolo_prokr += 1
##        if max_teliki_vathmologia < teliki_vathmologia:
##            max_teliki_vathmologia = teliki_vathmologia
##print("Μεγαλύτερη τελική βαθμολογία: {}".format(max_teliki_vathmologia))
##print("Ποσοστό των διαγωνιζόμενων που προκρίθηκαν στην επόμενη φάση: {:.1%}".format(synolo_prokr / synolo_diag))

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    INPUTFILENAME="vathmologies.txt"
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        while onomatepwnymo != "ΤΕΛΟΣ":
            onomatepwnymo = inputfile.readline().strip('\n').strip('\ufeff')
            print("Ονοματεπώνυμο διαγωνιζόμενου: {}".format(onomatepwnymo))
            if onomatepwnymo == "ΤΕΛΟΣ":
                print("Τερματισμός εισαγωγής δεδομένων")
            else:
                synolo_diag += 1
                synolo_vathmologias = 0
                panw_apo_orio = True
                for thema in range(1, THEMATA+1):
                    vathmologia = ""
                    while not vathmologia.isdigit() \
                      or int(vathmologia) not in range(1, MONADES+1):
                        vathmologia = inputfile.readline().strip('\n').strip('\ufeff')
                        print("Βαθμολογία στο θέμα {}: {}".format(thema, vathmologia))
                    vathmologia = int(vathmologia)
                    if vathmologia < ORIO:
                        panw_apo_orio = False
                    synolo_vathmologias += vathmologia
                teliki_vathmologia = float(synolo_vathmologias)/float(THEMATA)
                print("Τελική βαθμολογία: {}".format(teliki_vathmologia))
                if panw_apo_orio == True and teliki_vathmologia > PROKRISI:
                    print("Ο διαγωνιζόμενος προκρίνεται στην επόμενη φάση")
                    synolo_prokr += 1
                if max_teliki_vathmologia < teliki_vathmologia:
                    max_teliki_vathmologia = teliki_vathmologia
    print("Μεγαλύτερη τελική βαθμολογία: {}".format(max_teliki_vathmologia))
    print("Ποσοστό των διαγωνιζόμενων που προκρίθηκαν στην επόμενη φάση: {:.1%}".format(synolo_prokr / synolo_diag))
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)
