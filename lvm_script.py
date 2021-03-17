import os
while True:
                         os.system("clear")
                         os.system("tput setaf 10")
                         print( """
\n                    
Press 1 : Create PV(Physical Volume)
press 2 : Create VG(Volume Group)
press 3 : Create LV(logical volume) from VG(volume group)
press 4 : Extend the size of VG(volume group)                                   
press 5 : Exit
press 6 : Get Menu
  
                          """)
                         os.system("tput setaf 7")
                         chh=input("enter your choice.... :")

                         if int(chh) == 1:
                             nos=int(input("How many PV you want: "))
                             print("\n")
                             os.system("fdisk -l")
                             for i in range(0,nos):
                                 pv=input("Enter disk name for Physical Volume :")
                                 os.system("pvcreate {}".format(pv))
                                 os.system("pvdisplay {}".format(pv))

                         elif int(chh) == 2:
                             nvg = input("Enter the the name of Volume group :")
                             t=int(input("How many physical volume would u like to add in this V.G ?: "))       
                             for p in range(0,t):
                                 pvv=input("Enter the name of physical volume to add :")
                                 os.system("vgcreate {} {}".format(nvg,pvv))
                                 os.system("vgdisplay {}".format(nvg))
                                 
                         elif int(chh) == 3:
                             size = input("enter the size of logical volume :")
                             lv = input("enter the name of the lv you to create :")
                             vn = input("enter the name of  volume group   :")
                             os.system("lvcreate --size {} --name {} {}".format(size,lv,vn)) 
                             os.system("lvdisplay {}/{}".format(vn,lv))
                             print("lv created successfully....")
                             print("\n formating partition")
                             os.system("mkfs.ext4  /dev/{}/{}".format(vn,lv))
                             print("partition created successfully")
                             print("\n mount this partition")
                             fn = input("enter the name of the folder you would like to mount into : ")
                             os.system("mount /dev{}/{}  /{}".format(vn,lv,fn))
                         
                         elif int(chh) == 4:
                             lvv = input("enter the name of LV you want to extend : ")
                             ex = input("enter the size of logical volume you want to extend : ")
                             os.system("lvextend --size +{} {}".format(ex,lvv))
                             input("\n enter to format the extended partition ")
                             os.system("resize2fs {}".format(lvv))

                         elif int(chh) == 5:
                             exit()
                         elif int(chh) == 6:
                             break 

                         else:
                             print("Check the menu again")
                             continue
