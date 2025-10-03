def tower_of_hanoi(n,a,b,c):
    if n==1:
        print(f"Move disk 1 from {a} to {c}")
        return
    #Move n-1 disks from source to helper
    tower_of_hanoi(n-1,a,c,b)
    #Move the nth disk from source to destination
    print(f" Move disk {n} from {a} to {c} ")
    tower_of_hanoi(n-1,b,a,c)
#Number of disks
num_disks=2
#num_disks=int(input("enter number:"))    
tower_of_hanoi(num_disks,'A','B','C')

