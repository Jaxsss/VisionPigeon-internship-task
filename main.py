import json
import time

# open and load json file
f = open("filename.json")
data = json.load(f)

# count unique users
list_unique_users = []
for i in data:
    list_unique_users.append(i)

print("Number of unique users:", len(set(list_unique_users)))


# count unique requests
list_unique_requests = []
for i in data:
    setname = i
    number = 0
    for i in data[setname]:
        if number == 1:
            list_unique_requests.append(i)
        number += 1

print("Number of unique requests:", len(set(list_unique_requests)))

# time.sleep is put there so you have a while to check the number of unique users and requests
time.sleep(3)

# average time between item_id requests
# i extracted time from the JSON file, but I couldnt make it work because the loop iterates and the previous time variable isn't storable to be later used outside of an if statement
# if statement is there because every first iteration, it returns "variant"
for i in data:
    setname = i
    number = 0

    for i in data[setname]:
        result = data[setname].items()
        number = 0

        for key, value in result:
            number +=1
            if number == 2:
                string_value = str(value[0])
                stripped = string_value.strip("[]'")
                date = stripped[:10]
                time = stripped[11:]
                time = time[:8]

#max number of requests per a single item_id where similarInJsonList was returned
for i in data:
    setname = i
    number = 0

    for i in data[setname]:
        result = data[setname].items()

        for key, value in result:
            number += 1
            if number == 2:
                string_value = str(value[0])
                request_number = string_value.count('similarInJsonList')

                if request_number == 1:
                    print(key, "- did", request_number, "request.")

                if request_number >= 2:
                    print(key, "- did", request_number, "requests.")

                if request_number == 0:
                    print(key, "- didn't make any request.")
        break

# close json file
f.close()

# close terminal after executing the script
input("Press ENTER to exit.")
