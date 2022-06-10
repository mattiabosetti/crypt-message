from cryptography.fernet import Fernet

msg = input("Inserisci il messaggio da criptare: ")

chiave = Fernet.generate_key()

mes_crypt = Fernet(chiave).encrypt(bytes(msg, "UTF_8"))

with open("messaggio_criptato.txt", "wb") as f:
    f.write(mes_crypt)
    f.close
with open("chiave.key", "wb") as f:
    f.write(chiave)
    f.close