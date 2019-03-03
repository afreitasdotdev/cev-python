# Python 3.6

import os
import pymysql
import sys

### Variables

# Get group number
speakerGroup = sys.argv[1]

# Get SQL IP
getIP="docker inspect mysql | \
    grep '\"IPAddress\"\:\ \"172' | \
    awk '{print $2}' | \
    sort -u | \
    tr -d ',' | \
    sed -s 's/\"//g' >/dev/null"

# DB Connection
conexao = pymysql.connect(\
    db='snep', \
    user='snep', \
    passwd='sneppass', \
    host=os.system(getIP))

cursor = conexao.cursor()

query = "SELECT name \
    FROM peers A \
    INNER JOIN core_peer_groups B \
    ON A.id = B.peer_id \
    where B.group_id=%s"

cursor.execute(query, (speakerGroup,))

resultado = cursor.fetchall()

print(resultado)

for ramais in resultado:
    print("Teste cabuloso {}".format(ramais))

    callFile = open("/root/conf.call","w+")
    callFile.write("Channel: SIP/{}\n".format(ramais))
    callFile.write("Application: ConfBridge\n")
    callFile.write("Data: 6661,,speaker_user\n")
    callFile.close()



#for linha in resultado :
#    speakers=''.join(linha)
#    print('channel originate SIP/{} extension *717{}'.format(speakers, speakerGroup))
#    print(speakers)

conexao.close()


