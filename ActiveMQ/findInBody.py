##############################################
### Owner: Vladimir Zemtsov
### Mail: vl.zemtsov@gmail.com
### Desc: Find message-id in the body that contains string
##############################################
import stomp
import time

###
host = "127.0.0.1"
port = 61613
user = "ActiveMQ user"
password = "ActiveMQ password"
queue = "test.queue"
substr = "test_str"
###

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        if substr in message:
            print(headers['message-id'])

def readQueue(queue):
    conn = stomp.Connection(host_and_ports = [(host, port)])
    conn.set_listener('print', MyListener(conn))
    conn.start()
    conn.connect(login=user, passcode=password)
    conn.subscribe(destination='/queue/'+queue, id=0, ack='auto')
    time.sleep(60)
    conn.unsubscribe(0)
    conn.disconnect()

def main():
    readQueue(substr)

if __name__ == '__main__':
    main()
    