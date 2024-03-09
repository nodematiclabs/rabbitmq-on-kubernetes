import pika

credentials = pika.PlainCredentials('', '')
connection = pika.BlockingConnection(pika.ConnectionParameters('hello-world', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=lambda ch, method, properties, body: print(ch, method, properties, body))
channel.start_consuming()