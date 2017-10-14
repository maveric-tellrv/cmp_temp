# compare the tempest test based on the tempest test run

import re
import json


list_tempest=[]
neutron_tests = ['test_qos','test_agent','neutron.tests','routers','ports','ipv6','subnet']
cinder_test = ['snapshot']
manila_test = ['shares']


with open('tempest_network') as f:
        lines = f.readlines()

#function accepts liens as list of tests.
def strip_values(lines):
        list_tempest = []
        for l in lines:
                try:
                        l = l.strip("\n")
                        if l[-1] == "]":
                            li = re.search(r'^.*?\[',l).group().strip('[')
                        # li = re.search(r'^.*?\[', l).group()[:-1]
                            list_tempest.append(li)
                        else:
                            list_tempest.append(l)

                except AttributeError:
                        li = None
        return(list_tempest)



# Code to list plugin test from tempest file
#returns list and lenght of list

def plugin_test(list_tempest,test_plugin):
        testlist = []
        for i in list_tempest:
                if test_plugin in i:
                        testlist.append(i)
                        # print i
        # print len(testlist)
        return (testlist,len(testlist))

# for i in neutron_tests:
#         print ("Plugin type->",i)
#         a,b = plugin_test(list_tempest,i)
#         print ("No of test found->",b)


def read_json_test(path):
    sub_test=[]
    test_name_list =[]
    with open(path) as data_file:
        data = json.load(data_file)
        for key, value in data.items():
            pass
        for test_name in value:
                if 'setUpClass' in test_name:
                    result = re.sub(r'setUpClass \(', '', test_name)[:-1]
                    sub_test.append(result)
                else:
                    sub_test.append(test_name)
        sub_test = strip_values(sub_test)
    return sub_test


(list_tempest,len_of_list) = plugin_test(strip_values(lines),'network')
# (list_tempest,len_of_list) = plugin_test(strip_values(list_tempest),'agent')
list_result = read_json_test('neutron/neutron_lbaasv2/neutron_lbaasv2-validation_report.json')
print len(list_tempest),len(list_result)
print list_tempest
print list_result

#
temp = set(list_tempest) -set(list_result)
# for i in temp:
#     print i
print ("######### list_result")
for i in list_result:
    print i
print ("######")
for i in list_tempest:
    print i
print len(temp)