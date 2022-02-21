# import pika 
# class Publisher: 
#     def __init__(self): 
#         self.__url = '101.101.218.148' 
#         self.__port = 5672 
#         self.__vhost = 'mq_test' 
#         self.__cred = pika.PlainCredentials('admin', 'khm0813') 
#         self.__queue = 't_msg_q'; 
#         return

#     def main(self): 
#         conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred)) 
#         chan = conn.channel() 
#         chan.basic_publish( exchange = '', routing_key = self.__queue, body = 'Hello RabbitMQ' ) 
#         conn.close() 
#         return 

# publisher = Publisher() 
# publisher.main()


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('101.101.218.148',5672,'mq_test',pika.PlainCredentials('admin', 'khm0813')))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()