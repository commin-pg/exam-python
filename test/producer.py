import logging
import pika
from scrapy.utils.serialize import ScrapyJSONEncoder

encode = ScrapyJSONEncoder()

def main():
    parameters = pika.ConnectionParameters(host='127.0.0.1')

    with pika.BlockingConnection(parameters=parameters) as connection:

        channel = connection.channel()

        # Declare the queue
        # channel.queue_declare(queue="local", durable=True, exclusive=False, auto_delete=False)

        # Turn on delivery confirmations
        channel.confirm_delivery()

        channel.basic_publish(exchange='', routing_key='local',
                              body=encode.encode({'AAA':'Test message.222'})+'\n',
                              # properties=pika.BasicProperties(content_type='text/plain',
                              #                                 delivery_mode=1),
                              mandatory=True
                              )



if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)-15s %(levelname)s [%(name)s.%(funcName)s] %(message)s',
                       level=logging.DEBUG)
    logging.captureWarnings(True)

    main()
