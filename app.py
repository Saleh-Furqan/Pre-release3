# ======== storing all services and their costs in lists ============= #
servicesList = [['basicClean', 10.5], ['extWindows', "extra 10%"],
                ['twoFloors', "extra 10%"], ['threeFloors', "extra 15%"],
                ['insideClean', "extra 25%"], ['polWindows', "extra 5%"],
                ['solarPanel', 20]]
servicesNames = []
servicesCosts = []
for i in range(len(servicesList)):
    servicesNames.append(servicesList[i][0])
    servicesCosts.append(servicesList[i][1])
# ==================================================================== #

# =================== variables for task 3 (tallies for services) ============== #
twofloors = [0, 'twoFloors']
threefloors = [0, 'threeFloors']
insideclean = [0, 'insideClean']
polwindows = [0, 'polWindows']
solarpanel = [0, 'solarPanel']
# ============================================================================== #

# Task 2, bullet point 1: "display the services and the cost of each one"
print("==================================================")
print("==================================================")
print(
    "Welcome to my Window Cleaning Service!\nPlease have a look at all the services we provide\nto order, say yes to add a new user!"
)
print("==================================================")
print("==================================================")

for i in range(len(servicesList)):
    print("Service:", servicesNames[i], "\t\t\t cost:", servicesCosts[i])

print("==================================================")
print("==================================================")
# ==================================================================== #

index = 0
users = []


# ====== Function for validating yes/no questions ======= #
def validateYesNo(statement):
    x = input(statement)
    while x != "yes" and x != "no":
        print("Invalid response")
        x = input(statement)
    return x


# ======================================================= #

user = validateYesNo("new user? (yes/no)  ")
while user == "yes":

    userInfo = []
    index += 1

    # ======================== Task 2, bullet point 2: "input and store a customer's details..." ================= #
    # -----Name input validation
    name = input("Enter name: ")
    while len(name) < 5 or len(name) > 20:
        print(
            "Invalid name format. Please enter something between 5-20 characters."
        )
        name = input("Enter name: ")

    # ------Address input validation
    address = input("Enter Address: ")
    while len(address) < 5 or len(address) > 20:
        print(
            "Invalid address format. Please enter something between 5-20 characters."
        )
        address = input("Enter Address: ")

    # Task 1, bullet point 2: "use the array index of this position as a unique number of the itemised bill"
    userInfo.append(index)

    # Task 1, bullet point 1: "store customer name and address in a single dimensional array at the next position"
    userNameAddress = [name, address]
    userInfo.append(userNameAddress)

    # ============================================================================================================ #

    # ------Task 1, bullut point 3:
    servicesRequired = []
    serviceIndex = 0
    newService = validateYesNo("Add service? (yes/no)  ")
    while newService == "yes":
        print("= = = = = = = = = = = = = = = = = = = = = = = = = ")
        service = input(
            "Here ar our services: \n\n 'basicClean', 'extWindows', 'twoFloors', 'threeFloors', 'insideClean', 'polWindows', 'solarPanel' \n\n What service does user require?  "
        )

        while service not in servicesNames:
            print(
                "\n=============================================\nInvalid service. Enter a valid service please\n=============================================\n"
            )
            service = input(
                "Here ar our services: \n\n 'basicClean', 'extWindows', 'twoFloors', 'threeFloors', 'insideClean', 'polWindows', 'solarPanel' \n\n What services does user require?  "
            )
        else:
            servicesRequired.append([service])
            serviceIndex += 1

        print("==================================================")
        newService = validateYesNo("Add another service? (yes/no)  ")

    print("\n---List of services (in lists of their own)", name,
          "requires: \n", servicesRequired)
    userInfo.append(servicesRequired)
    # =========================================================================================================== #

    # Task 2, bullet point
    totalCost = 0
    for i in range(len(servicesRequired)):
        if servicesRequired[i] == ["basicClean"]:
            totalCost += 10
        elif servicesRequired[i] == ["extWindows"]:
            totalCost += 5
        elif servicesRequired[i] == ["solarPanel"]:
            totalCost += 20

    for i in range(len(servicesRequired)):
        if servicesRequired[i] == ["twoFloors"]:
            totalCost *= 1.1
            twofloors[0] += 1
        elif servicesRequired[i] == ["threeFloors"]:
            totalCost *= 1.15
            threefloors[0] += 1
        elif servicesRequired[i] == ["insideClean"]:
            totalCost *= 1.25
            insideclean[0] += 1
        elif servicesRequired[i] == ["polWindows"]:
            totalCost *= 1.05
            polwindows[0] += 1

    userInfo.append(totalCost)
    print("\n---List with all of the user details: \n", userInfo, "\n")
    users.append(userInfo)
    user = input("New user? (yes/no)  ")

print("\n==================Users and their Info=====================")
for i in range(len(users)):
    print(users[i])
print("===========================================================\n")

# ======================================== Task 3 ===================================== #
popService = [twofloors, threefloors, insideclean, polwindows]
popService.sort(key=lambda x: x[0])
mostPopularService = popService[3]
leastPopularService = popService[0]
print("===================== popular services =================")
if index > 0:
    print(mostPopularService[1],
          "Is the most popular service.\nIt was requested",
          mostPopularService[0] / index, "times all orders")
    print(leastPopularService[1],
          "Is the least popular service.\nIt was requested",
          leastPopularService[0] / index, "times all orders")
    print("========================================================")
else:
    print("========================================================")
    print("\nIndex is zero as no users added in database\n")

# ===================================================================================== #
