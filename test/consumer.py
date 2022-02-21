import logging
import pika
from scrapy.utils.serialize import ScrapyJSONDecoder

decoder = ScrapyJSONDecoder()


def on_message(channel, method_frame, properties, body):
    print(method_frame.delivery_tag)
    print(body)
    try:
        print(decoder.decode(str(body, 'UTF-8')))
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    except TypeError as e:
        pass
    print()


def main():
    parameters = pika.ConnectionParameters(host='127.0.0.1')

    with pika.BlockingConnection(parameters=parameters) as connection:

        channel = connection.channel()

        channel.basic_consume('local', on_message)
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()





if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)-15s %(levelname)s [%(name)s.%(funcName)s] %(message)s',
                        level=logging.DEBUG)
    logging.captureWarnings(True)

    main()