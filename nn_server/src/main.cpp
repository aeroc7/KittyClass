#include <assert.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <zmq.h>

#include <iomanip>
#include <iostream>

using base64 = cppcodec::base64_rfc4648;

static void detailed_fail(int stat) {
    if (stat == EINVAL) {
        std::cout << "EINVAL\n";
    } else if (stat == EPROTONOSUPPORT) {
        std::cout << "EPROTONOSUPPORT\n";
    } else if (stat == ENOCOMPATPROTO) {
        std::cout << "ENOCOMPATPROTO\n";
    } else if (stat == EADDRINUSE) {
        std::cout << "EADDRINUSE\n";
    } else if (stat == EADDRNOTAVAIL) {
        std::cout << "EADDRNOTAVAIL\n";
    } else if (stat == ENODEV) {
        std::cout << "ENODEV\n";
    } else if (stat == ETERM) {
        std::cout << "ETERM\n";
    } else if (stat == ENOTSOCK) {
        std::cout << "ENOTSOCK\n";
    } else if (stat == EMTHREAD) {
        std::cout << "EMTHREAD\n";
    } else {
        std::cout << stat << '\n';
    }
}

int main(void) {
    //  Socket to talk to clients
    void *context = zmq_ctx_new();
    void *responder = zmq_socket(context, ZMQ_REP);
    int rc = zmq_bind(responder, "tcp://127.0.0.1:7373");
    if (rc != 0) {
        detailed_fail(errno);
        abort();
    }

    while (1) {
        char buffer[10];
        char *buf = new char[200];
        zmq_recv(responder, buf, 200, 0);

        for (int i = 0; i < 25; ++i) {
            std::cout << buf[i];
        }

        std::cout << '\n';
        sleep(1);  //  Do some 'work'
        zmq_send(responder, "World", 5, 0);
    }
    return 0;
}