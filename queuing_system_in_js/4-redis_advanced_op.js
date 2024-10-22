/**
 * 
 */
const redis = require('redis');

const client = redis.createClient();

client.on('connect', function (){
    console.error(`Redis client not connected to the server: #{err}`);
});

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Boogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
        console.error(`Error retrieving data: ${err}`);
    } else {
        console.log(obj);
    }
});

client.quit();