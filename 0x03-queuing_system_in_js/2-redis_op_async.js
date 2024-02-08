import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();

client
    .on('error', (error) => console.log('Redis client not connected to the server:', error))
    .on("connect", () => console.log("Redis client connected to the server"));


    const get = promisify(client.get).bind(client) 

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
    try {
        const value = await get(schoolName) 
        console.log(value)
    }catch(error) {
        console.error('Error:', error)
    }  
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');