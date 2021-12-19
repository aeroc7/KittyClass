const http = require('http');
const zmq = require("zeromq")
require('dotenv').config()

async function forwardData(data) {
    const sock = new zmq.Request

    sock.connect("tcp://10.0.0.161:7373");
    // Remove base64 header, so we just have the raw data
    data = data.split(',')[1];

    await sock.send(data);
    return await sock.receive();
}

async function onRequest(req, res) {
    const buffers = [];

    for await (const chunk of req) {
        buffers.push(chunk);
    }

    const data = Buffer.concat(buffers).toString();

    result = forwardData(data);
    result
        .then(result_data => {
            res.writeHead(200, {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'text/plain'
            });
            res.write(result_data.toString());
            res.end();
        });
}

http.createServer(onRequest).listen(5000, '10.0.0.161');
console.log("Server is running");