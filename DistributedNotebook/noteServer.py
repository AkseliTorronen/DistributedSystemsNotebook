from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import xml.etree.ElementTree as ET
from datetime import datetime

def searchForEntry(topic):
    tree = ET.parse('db.xml')
    root = tree.getroot()
    entry = root.find(f".//topic[@name='{topic}']")

    if entry is None:
        return "Topic didn't match any entries!"
    else:
        return ET.tostring(entry)

def addEntry(topic, note, text,):
    tree = ET.parse('db.xml')
    root = tree.getroot()
    entry = root.find(f".//topic[@name='{topic}']")
    stampOfTime = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    if entry is None:
        newEntry = ET.fromstring(f'\n<topic name="{topic}">\n<note name="{note}">\n<text>\n{text}\n</text>\n<timestamp>\n{stampOfTime}\n</timestamp>\n</note>\n</topic>\n')
        root.append(newEntry)
    else:
        newEntry = ET.fromstring(f'\n<note name="{note}">\n<text>\n{text}\n</text>\n<timestamp>\n{stampOfTime}\n</timestamp>\n</note>\n')
        entry.append(newEntry)
    tree.write("db.xml") #saving changes to the xml file

server = SimpleXMLRPCServer(('localhost', 1234), logRequests=True, allow_none=True)
server.register_function(searchForEntry)
server.register_function(addEntry)
print("[SERVER RUNNING]")
server.serve_forever()