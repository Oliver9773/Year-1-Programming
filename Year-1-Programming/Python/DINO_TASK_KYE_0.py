Dino_Raw = input("Enter Y if you hear dino raw")
if Dino_Raw == "Y":
    Dino_Big = input("Enter Y if dino is big")
    if Dino_Big == "Y":
        Dino_Horns = input("Enter Y if Dino has horns")
        if Dino_Horns == "Y":
            print("SAFE - Triceratops")
        else:
            Dino_Spikes = input("Enter Y if Dino has spike or spikes")
            if Dino_Spikes == "Y":
                Dino_Spike = input("Enter Y if Dino has only one spike")
                if Dino_Spike == "Y":
                    print("Hide - Spinosaurus")
                else:
                    print("Safe - Stegosaurus")
            else:
                Dino_Stand = input("Enter Y if Dino stands on two feet")
                if Dino_Stand == "Y":
                    print("Hide - T-REX")
                else:
                    Answer_Check = input("Enter Y if Dino stands on 4 legs")
                    if Answer_Check == "Y":
                        print("Safe - Brachiosaurus")
                    else:
                        print("The Dino is not found type a capital Y when answering the inquiry as true")
    else:
        print("HIDE - Velociraptor")
else:
    print ("SAFE - No Dino")