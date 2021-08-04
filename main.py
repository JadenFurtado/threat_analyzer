# payload to be taken in from get or post request as required
# function checks the query to determine if dangerous or not

def check_query():
    # as this is just a simple proof of concept, 
    # we are taking the input manually
    payload = input("please enter a payload")
    # open the sample payloads to compare against the user's input
    log = open('XSS payload.txt')
    logfile = log.read().splitlines()
    # flag if match-case is found
    found = False
    for line in logfile:
        if str(payload) in line:
            found = True
            # exit the loop
            break
    log.close()
    return found