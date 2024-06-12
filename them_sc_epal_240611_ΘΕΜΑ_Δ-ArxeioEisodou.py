##ΠΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ – ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΤΡΙΤΗ 11 ΙΟΥΝΙΟΥ 2024
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Δ
##Δίνεται το αρχείο "branch.txt", το οποίο περιέχει ονόματα
##υποκαταστημάτων μίας εταιρείας. Το αρχείο έχει ενδεικτικά την παρακάτω
##δομή:
##Micro_Vironas
##Mega_Kifisia
##.
##.
##.
##Σε κάθε γραμμή του αρχείου "branch.txt" βρίσκεται το όνομα του
##υποκαταστήματος.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο:
##Δ1. Να διαβάζει το αρχείο "branch.txt" γραμμή προς γραμμή και να
##καταχωρίζει τα ονόματα των υποκαταστημάτων σε μία λίστα με όνομα ΟΝ.
##Θεωρήστε ότι στο αρχείο υπάρχουν τουλάχιστον δύο (2) υποκαταστήματα.
##Μονάδες 4
##Δ2. Για κάθε υποκατάστημα:
##α) Να διαβάζει την ημερήσια είσπραξη για κάθε μία από τις τριάντα (30)
##ημέρες του μήνα Ιουνίου (μον.3).
##β) Να υπολογίζει το σύνολο των εισπράξεων του μήνα Ιουνίου και να το
##καταχωρίζει σε λίστα με όνομα S_POSO (μον.4).
##Μονάδες 7
##Δ3. α) Να υπολογίζει και να εμφανίζει τον μέσο όρο των εισπράξεων όλων
##των υποκαταστημάτων για τον μήνα Ιούνιο.
##β) Να υπολογίζει και να εμφανίζει το πλήθος των υποκαταστημάτων που
##έχουν εισπράξεις μεγαλύτερες ή ίσες του μέσου όρου.
##Μονάδες 6
##Δ4. Να ταξινομεί τη λίστα S_POSO με χρήση του αλγορίθμου ταξινόμησης
##της ευθείας ανταλλαγής (φυσαλίδα – bubble sort) σε φθίνουσα σειρά,
##αναδιατάσσοντας συγχρόνως τη λίστα ΟΝ, έτσι ώστε να διατηρείται η
##αντιστοιχία ονομάτων υποκαταστημάτων – εισπράξεων. Σε περίπτωση
##ισότητας εισπράξεων να γίνεται ταξινόμηση με αλφαβητική σειρά ως προς
##τα ονόματα της λίστας ΟΝ.
##Μονάδες 8
##
ON = []
S_POSO = []
ARXEIO_EISODOY = "branch.txt"
IMERES = 30

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    with open(ARXEIO_EISODOY, 'r', encoding="utf-8") as inputfile:
        ON = inputfile.readlines()
    for i in range(len(ON)):
        ON[i] = ON[i].strip('\n').strip('\ufeff')
        print(ON[i])
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    INPUTFILENAME="eispraxeis.txt"
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        eispr_olwn = 0.0
        for branch in range(len(ON)):
            print("Υποκατάστημα: {}".format(ON[branch]))
            synolo_eispr = 0.0
            for day in range(1, IMERES+1):
                eispraxi = ""
                while not eispraxi.replace('.', '').isdigit():
                    eispraxi = inputfile.readline().strip('\n').strip('\ufeff')
                    print("Ημερήσια είσπραξη της {}/6: €{}".format(day, eispraxi))
                eispraxi = float(eispraxi)
                synolo_eispr += eispraxi
            print("Σύνολο εισπράξεων του μήνα Ιουνίου: €{:.2f}".format(synolo_eispr))
            S_POSO.append(synolo_eispr)
            eispr_olwn += synolo_eispr
        mesos_oros_olwn = float(eispr_olwn)/float(len(ON))
        print("Μέσος όρος εισπράξεων όλων των υποκαταστημάτων τον μήνα Ιούνιο: €{:.2f}".format(mesos_oros_olwn))
        ypok_megal_mesou_orou = 0
        print("Υποκαταστήματα που έχουν εισπράξεις μεγαλύτερες ή ίσες του μέσου όρου")
        print("---------------------------------------------------------------------")
        for i in range(len(S_POSO)):
            if S_POSO[i] >= mesos_oros_olwn:
                ypok_megal_mesou_orou += 1
                print("{:20}\t€{:8.2f}".format(ON[i], S_POSO[i]))
        print("Πλήθος υποκαταστημάτων που έχουν εισπράξεις μεγαλύτερες ή ίσες του μέσου όρου: {}".format(ypok_megal_mesou_orou))
        N = len(S_POSO)
        for i in range(N-1): # range(0, N–1, 1)
            for j in range(N-1 , i , -1): # μέχρι και i–1
                if S_POSO[j] > S_POSO[j-1]:
                    S_POSO[j], S_POSO[j-1] = S_POSO[j-1], S_POSO[j]
                    ON[j], ON[j-1] = ON[j-1], ON[j]
                elif S_POSO[j] == S_POSO[j-1]:
                    if ON[j] < ON[j-1]:
                        ON[j], ON[j-1] = ON[j-1], ON[j]
        print("{:17}\t{:16}".format("Υποκατάστημα", "Eισπράξεις"))
        print("-"*len("{:17}\t{:16}".format("Υποκατάστημα", "Eισπράξεις")))
        for i in range(len(S_POSO)):
            print("{:20}\t€{:8.2f}".format(ON[i], S_POSO[i]))
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)
