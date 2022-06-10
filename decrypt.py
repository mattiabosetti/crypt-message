from cryptography.fernet import Fernet

msg = input("Inserisci il messaggio da decriptare: ")
chiave = input("Inserisci la chiave di crittografia: ")


mes_crypt = Fernet(chiave).decrypt(bytes(msg, "UTF_8"))

with open("messaggio_decriptato.txt", "wb") as f:
    f.write(mes_crypt)
    f.close