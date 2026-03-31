"Unit tests for lab9"

import unittest
from ncclient import manager
from netaddr import IPAddress
import ipaddress
import netmiko


FETCH_INFO = """
             <filter>
             <config-format-text-block>
             <text-filter-spec> %s </text-filter-spec>
             </config-format-text-block>
             </filter>
             """

class Tests(unittest.TestCase):
     def test_router3(self):
         connection = manager.connect(
                      host='198.51.100.30',
                      port=22,
                      username='admin',
                      password='admin',
                      hostkey_verify=False,
                      device_params={'name': 'iosxr'},
                      allow_agent=False,
                      look_for_keys=False)

         FETCH_LO_INFO = FETCH_INFO % ('int loopback99')
         output = connection.get_config('running', FETCH_LO_INFO)
         split1 = str(output).split()
         loIP = split1[9]
         loPrefix = str(ipaddress.ip_network(split1[9] + '/' +
                    split1[10], strict=False).prefixlen)
         inputToCompare = '10.1.3.1/24'

         self.assertEqual(loIP + '/' + loPrefix, inputToCompare)

     def test_router2(self):
         dictItem = {
         "device_type": "cisco_ios",
         "host": "R2",
         "ip": '198.51.100.20',
         "username": "admin",
         "password": "admin",
         "secret": "admin"
          }
         connect = netmiko.ConnectHandler(**dictItem)
         connect.enable()

         output = connect.send_command('ping 10.1.5.1 source 10.1.2.1')
         stringOutput = str(output)
         result = False
         if 'Success rate' in stringOutput and '10.1.2.1' in stringOutput:
             result = True
         self.assertTrue(result)


     def test_router1(self):
         connection = manager.connect(
                      host='198.51.100.10',
                      port=22,
                      username='admin',
                      password='admin',
                      hostkey_verify=False,
                      device_params={'name': 'iosxr'},
                      allow_agent=False,
                      look_for_keys=False)
         FETCH_AREA_INFO = FETCH_INFO % ('| include area')
         output = connection.get_config('running', FETCH_AREA_INFO)
         split1 = str(output).split()
         area1 = split1[8] + " " + split1[9]
         area2 = split1[13] + " " + split1[14]
         self.assertEqual(area1, area2)


if __name__ == '__main__':
    unittest.main()
