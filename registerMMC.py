# Python script for showing and modifying some parameters about your eMMC :
# Registers to be shown : 
#    csd : The Card-Specific Data register provides information on how to access the contents stored in e•MMC
#          
#    cid : The Card Identification register is 128 bits wide. 
#	       It contains the Device identification information used during the Device identification phase
#    extcsd : This register defines the Deviceproperties and selected modes. It is 512 bytes long
# Change the Sector block size
# author : YHA 

import os

print("##### Afficher les registers de l'eMMC ######")

# Variables
path = "/sys/kernel/debug/mmc0/ios"
device = "/dev/mmcblk0"

# Lire les ios
f_path = open(path,"r")
t_path = f_path.read()

print("Ton eMMC : \n", t_path)

# Affichage CSD
print("Le register CSD : \n", )
os.system('mmc csd read /sys/class/mmc_host/mmc0/mmc0\:0001/')

# Affichage CID
print("Le register CID : \n", )
os.system('mmc cid read /sys/class/mmc_host/mmc0/mmc0\:0001/')

# Affichage extended CSD :
answer = input("Voulez-vous afficher le register CSD extended ? o/n :\n")
if answer=='o':
	print("Le register Extended CSD :\n")
	os.system('mmc extcsd read /dev/mmcblk0')
# Changement de la taille des Block secteurs 
sec_block = input("Voulez-vous changer la taille du secteur de votre eMMC ? o/n : \n")
if sec_block=='o':
	print("La taille actuelle des Block de votre MMC :")
	os.system('blockdev --getbsz /dev/mmcblk0')
	sec_taille = input("\n\t *Choisir une taille (512, 1024, 2048, 4096, 8192 octets ...) :")
	os.system('blockdev --setbsz $sec_taille /dev/mmcnlk0') # test this command before using the code !!!!!!!!

# Fin
print("\nDone!")
