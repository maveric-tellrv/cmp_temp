# compare the tempest test based on the tempest test run

import re
import json


list_tempest=[]
neutron_tests = ['test_qos','test_agent','neutron.tests','routers','ports','ipv6','subnet']
cinder_test = ['snapshot']
manila_test = ['shares']


with open('tempest_api') as f:
        lines = f.readlines()

#function accepts liens as list of tests.
def strip_values(lines):
        list_tempest = []
        for l in lines:
                try:
                        li = re.search(r'^.*?\[',l).group().strip('[')
                        list_tempest.append(li)
                except AttributeError:
                        li = None
        return(list_tempest)
# print list_tempest


# Code to list plugin test from tempest file
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
                test_name_list.append(value)
        for test_name in value:
                sub_test.append(test_name)
        sub_test = strip_values(sub_test)
    return sub_test

# pprint(data['test_cases'][ ]['name'])

list_tempest = plugin_test(strip_values(lines),'agent')
list_result = read_json_test('neutron/neutron_agents/neutron_agents-validation_report.json')
print len(list_tempest),len(list_result)
