#IP_Hosts screen: 443.https.tls.certificate.parsed.subject.common_name
#                 443.https.tls.certificate.parsed.fingerprint_sha256
#
#
#1ae0e2f635ebb687fe7a414ad94c0bdaaea4aa7cc14fcc0501e51c28a41164a1
#
#Certificates screen: parsed.subject_key_info.fingerprint_sha256
#                     parsed.fingerprint_sha256



import censys.ipv4
import censys.certificates
import re
UID = <<FIX WITH CONFIGPARSER>>
SECRET = <<FIX WITH CONFIGPARSER>>
c = censys.certificates.CensysCertificates(UID, SECRET)
i = censys.ipv4.CensysIPv4(UID, SECRET)

fields_cert = ["parsed.names", "parsed.subject.common_name", "parsed.issuer.common_name", "parsed.fingerprint_sha256", "parsed.issuer.email_address", "parsed.subject_dn"]
fields_ip = ['ip', 'protocols', '443.https.tls.certificate.parsed.subject.common_name', '443.https.tls.certificate.parsed.issuer.email_address', 'autonomous_system.name', 'tags', '443.https.tls.certificate.parsed.subject_dn', '443.https.tls.certificate.parsed.issuer.organization']

for cert in c.search("malwarebytes", fields=fields_cert):
    if re.search("Let's Encrypt", str(cert['parsed.issuer.common_name'])):
        print cert
        for ip in i.search(cert['parsed.fingerprint_sha256'], fields=fields_ip):
            print
            print(ip)

{u'parsed.fingerprint_sha256': u'441d44ae7446836d99e7b125541ac29db8c7690464463412fbaae7cb174d6f5b', u'parsed.names': [u'malwarebytes-anti-malware.ru', u'www.malwarebytes-anti-malware.ru'], u'parsed.issuer.common_name': [u"Let's Encrypt Authority X3"], u'parsed.subject.common_name': [u'malwarebytes-anti-malware.ru']}

for cert in c.search("malwarebytes", fields=fields_cert):
    print("Certificates with 'malwarebytes' and issued by 'Let's Encrypt'")
    if re.search("Let's Encrypt", str(cert['parsed.issuer.common_name'])):
        print("Parsed Names: {}".format(cert['parsed.names']))
        print("  Subject DN: {}".format(ip['parsed.subject_dn']))
        print("  Subject CN: {}".format(cert['parsed.subject.common_name']))
    if cert.has_key('parsed.issuer.email_address') and not cert['parsed.issuer.email_address'] in emails:
        #print(cert['parsed.issuer.email_address'])
        for e in cert['parsed.issuer.email_address']:
            #print(e)
            emails.append(e)
            for ip in i.search("\"{}\"".format(cert['parsed.issuer.email_address'][0]), fields=fields_ip):
                if not ip in IPs:
                    if not re.search('akamai', str(ip['tags']), re.IGNORECASE):
                        if "malwarebytes" in str(ip):
                            print("IP: {}".format(ip['ip']))
                            print("  Cert Email: {}".format(cert['parsed.issuer.email_address']))
                            print("  Subject DN: {}".format(ip['443.https.tls.certificate.parsed.subject_dn']))
                            print("  Organization: {}".format(ip['443.https.tls.certificate.parsed.issuer.organization']))
                            print("  Subject CN: {}".format(ip['443.https.tls.certificate.parsed.subject.common_name']))
                            #print(ip['ip'], ip['autonomous_system.name'], ip['tags'])
                            IPs.append(ip['ip'])
