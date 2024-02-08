import { createClient, print } from 'redis';

const client = createClient();

client
    .on('error', (error) => console.log('Redis client not connected to the server:', error))
    .on("connect", () => console.log("Redis client connected to the server"));


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, data) => {
        if (error) {
            console.error(error)
            return;
        }
        console.log(data)
    })
       
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');