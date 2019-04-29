# script pour afficher les registres d'un eMMC :
# les registers qui sont affichés : 
#    csd  
#    cid 
#    extcsd 

import os

print("##### Afficher les registers de l'eMMC ######")

# variables
path = "/sys/kernel/debug/mmc0/ios"
device = "/dev/mmcblk0"

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
answer = input("Voulez-vous afficher le register CSD extended ? o/n :")
if answer=='o':
	print("Le register Extended CSD :\n")
	os.system('mmc extcsd read /dev/mmcblk0')
print("Done!")
