import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();

client
    .on('error', (error) => console.log('Redis client not connected to the server:', error))
    .on("connect", () => console.log("Redis client connected to the server"));

const HolbertonSchools = {
    "Portland": "50",
    "Seattle": "80",
    "New York": "20",
    "Bogota": "20",
    "Cali": "40",
    "Paris": "2",
}

const getAll = promisify(client.hgetall).bind(client) 

Object.entries(HolbertonSchools).forEach(([key, value]) => {
    client.hset('HolbertonSchools', key, value, print)
})

async function getAllHolbertonSchools() {
    try {
        const value = await getAll("HolbertonSchools")
        console.log(value)
    } catch(error) {
        console.error('Error: ', error)
    }    
}

getAllHolbertonSchools()



