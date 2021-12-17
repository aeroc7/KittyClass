#include <zmq.h>

#include <iostream>

int main() {
    void *context = zmq_ctx_new();
    std::cout << context;
    return EXIT_SUCCESS;
}
