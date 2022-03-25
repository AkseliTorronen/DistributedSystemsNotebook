import xmlrpc.client, sys
proxy = xmlrpc.client.ServerProxy('http://localhost:1234', allow_none=True)

while True:
    print("\nWhat would you like to do?")
    print("1) Search for an entry by topic")
    print("2) Add an entry")
    print("0) exit")
    choice = input("Choose an option: ")
    
    try:
        choice = int(choice)

        if choice == 0:
            sys.exit()

        elif choice == 1:
            topic = input("\nGive a topic to search: ")
            try:
                print(str(proxy.searchForEntry(topic)))
            except xmlrpc.client.Fault as err:
                print("A fault occurred")
                print("Fault code: %d" % err.faultCode)
                print("Fault string: %s" % err.faultString)

        elif choice == 2:
            topic = input("\nGive a topic for your note: ")
            title = input("Give a name for your note: ")
            text = input("Write down your note: ")
            #Can't create an empty note
            while len(topic)==0 or len(title)==0 or len(text)==0:
                print("\nTopic, title and note are required for the creation of a new note, please enter them all.")
                if len(topic)==0:
                    topic = input("\nGive a topic for your note: ")
                if len(title)==0:
                    title = input("Give a name for your note: ")
                if len(text)==0:
                    text = input("Write down your note: ")

            try:
                proxy.addEntry(topic, title, text)
            except xmlrpc.client.Fault as err:
                print("A fault occurred")
                print("Fault code: %d" % err.faultCode)
                print("Fault string: %s" % err.faultString)

        else:
            print("Unknown command.")
    
    except ValueError:
        print("\nPlease insert a number (0-2)")
