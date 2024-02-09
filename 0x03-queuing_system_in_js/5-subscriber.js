import { createClient } from 'redis';


const client = createClient();

client
    .on('error', (error) => console.log('Redis client not connected to the server:', error))
    .on("connect", () => console.log("Redis client connected to the server"));

client.subscribe("holberton school channel")

client.on('message', (channel, message) => {
    if (message === "KILL SERVER") {
        client.unsubscribe()
        client.quit()
    }
    console.log(message)
})

