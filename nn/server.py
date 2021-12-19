import zmq
import base64
import io

from PIL import Image
from zmq.sugar.constants import POLLIN
from run import nn_run_image

SOCKET_LOC = "tcp://10.0.0.161:7373"


class SocketHdlr():
    def __init__(self, loc):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(loc)

        print("Starting server")
        self.receive()

    def receive(self):
        try:
            while True:
                # Poll infinitely at 1 second increments. Hack to allow for
                # keyboard interrupts in the terminal
                if self.socket.poll(timeout=1000, flags=POLLIN) != 0:
                    message = self.socket.recv()
                    img_info = self.run_image(message)
                    # Return neural network predictions
                    self.socket.send(img_info)
        except KeyboardInterrupt:
            print("Ending server")
            exit(0)

    def run_image(self, message):
        img = self.bytes_to_img(message)
        # Forward to neural network
        return nn_run_image(img)

    def bytes_to_img(self, message):
        # Decode from base64
        message = base64.b64decode(message)
        # Open in RGB mode, neural network only supports 3 channels
        return Image.open(io.BytesIO(message)).convert('RGB')


if __name__ == "__main__":
    hdlr = SocketHdlr(SOCKET_LOC)
