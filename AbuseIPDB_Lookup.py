import requests

apikey = <<NEED TO FIX WITH CONFIGPARSER>>

url = 'https://www.abuseipdb.com/check/'
ip = '154.121.5.240'

category = {
        3: 'Fraud_Orders',
        4: 'DDoS_Attack',
        9: 'Open_Proxy',
        10: 'Web_Spam',
        11: 'Email_Spam',
        14: 'Port_Scan',
        18: 'Brute_Force',
        19: 'Bad_Web_Bot',
        20: 'Exploited_Host',
        21: 'Web_App_Attack',
        22: 'SSH',
        23: 'IoT_Targeted'}

r = requests.get('{}{}/json?key={}&days=365'.format(url, ip, apikey))
j = r.json()

if not j == []:
    print "IP found in Abuse IP DB"
    for cat in j['category']:
        print category[cat]
    print j
