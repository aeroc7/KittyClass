const http = require('http');
const zmq = require("zeromq")

async function forwardData(data) {
    const sock = new zmq.Request

    sock.connect("tcp://localhost:7373");
    
    console.log("Sending data to NN");
    console.log(data.length)
    
    // Remove base64 header, so we just have the raw data
    data = data.split(',')[1];
    
    await sock.send(data);
    const [result] = await sock.receive();
    console.log(result + '\n');
}

function onRequest(req, res) {
    let data = '';
    req.on('data', chunk => {
        data += chunk;
    });

    req.on('end', () => {
        console.log("Recieved data");
        forwardData(data)
    });
}

http.createServer(onRequest).listen(5000);
console.log("Server is running");