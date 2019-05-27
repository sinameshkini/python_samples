from urllib.request import urlretrieve
urlretrieve("http://sajab.sazabgolestan.com/server.php?action=station&imei=9359374362&station_index=3","my picture.txt")


def find_data(file,name,next_name,space):
    data = file[file.find(name)+len(name)+space:file.find(next_name)-space]
    return data


f = open("my picture.txt","r")
s = str(f.read())
#print(s)
status = int(find_data(s,'status','name',3))
print(status)
