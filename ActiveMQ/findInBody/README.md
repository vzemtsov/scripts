# This script find message-id's who have SUBSTR in body

- Set correct configs. 
- Run script
- Copy all message from queue which we want to find SUBSTR to queue.test (use JMX (jconsole)). U have only 60 sec, or change time.sleep in def readQueue
- Drink ;)

# Этот скрипт находит message-id сообщений, в которых находится опдстрока

- Установите правильные конфики (Очередь queue.test)
- Запустите скрипт
- Скопируйте все сообщений из очереди, в котороq нужно найти подстроку в теле в queue.test (используйте для этого JMX (jconsole)). Нужно это сделать за 60 секунд, либо до запуска скрипта.
- Смотрите релультат

Warning: Этот скрипт прочитает все сообщения из очереди, т.е. они пропадут из ActiveMQ. По этому для работы создать отдельную очередь для этого скрипта куда копировать все сообщения
