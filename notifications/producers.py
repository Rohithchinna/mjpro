# chat_producer.py

import pika

def send_message(chat_room, message):
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for the chat room
    channel.queue_declare(queue=chat_room, durable=True)

    # Send the message to the chat room queue
    channel.basic_publish(
        exchange='',
        routing_key=chat_room,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        ))
    print(f" [x] Sent '{message}' to chat room '{chat_room}'")

    # Close the connection
    connection.close()

# Example usage
if __name__ == "__main__":
    chat_room = 'general'  # Chat room name
    message = 'Hello, everyone!'  # Message to send
    send_message(chat_room, message) 