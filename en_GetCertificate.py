import OpenSSL
import ssl
import socket

while(1):
    server = raw_input('Name? ')
    ctx = OpenSSL.SSL.Context(ssl.PROTOCOL_TLSv1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x509 = None
    try:
        s.connect((server, 443))
        cnx = OpenSSL.SSL.Connection(ctx, s)
        cnx.set_tlsext_host_name(server)
        cnx.set_connect_state()
        cnx.do_handshake()

        x509 = cnx.get_peer_certificate()
        #print x509
        s.close()
    except Exception as e:
        print e
    common_name = x509.get_subject().commonName.decode()
    print common_name
