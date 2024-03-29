from basic_test_server import BasicTestServer
from practice.server_test.basic_wav_receiving_protocol import BasicWAVReceivingProtocol


class FileTransferTestServer(BasicTestServer):
    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: ", addr)

        # 프로토콜 이용하는 통신 객체 생성
        pt = BasicWAVReceivingProtocol(self.clntSock, BasicTestServer.bufSize)
        # 데이터 수신
        header = pt.getHeader()
        # 데이터 저장
        pt.save(header)

        self.clntSock.sendall("Transfer Finished".encode())

        self.stopServer()


if __name__ == "__main__":
    for i in range(10):
        basicTestServer = FileTransferTestServer()
        basicTestServer.runServer()
