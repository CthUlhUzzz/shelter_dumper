# shelter_dumper
Decrypt and encrypt Fallout Shelter save files

Decryption: cat Vault1.sav | shelter_dumper.py -d > Vault1.sav.decrypted
Encryption: cat Vault1.sav.decrypted | shelter_dumper.py > Vault1.sav
