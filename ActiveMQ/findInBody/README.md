# This script find message-id's who have SUBSTR in body

- Set correct configs. (Queue queue.test must be empty)
- Run script
- Copy all message from queue which we want to find SUBSTR to queue.test (use JMX (jconsole)). U have only 60 sec, or change time.sleep in def readQueue
- Drink ;)