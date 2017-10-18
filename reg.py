# compare the tempest test based on the tempest test run

import re
import json

# list the test folder for each plugin in the test run.
list_tempest=[]

'''	define the directory structure of the neutron cinder and manila test run.
	neutron_tests = ['test_qos','test_agent','neutron.tests','routers','ports','ipv6','subnet']
	cinder_test = ['snapshot']
	manila_test = ['shares']
'''


# Function to extract the resulti.json file from folder
'''def return_test_json(dir_name):
	retunn dict_test_json '''


# Read the tempest file data [ ostestr -l | grep tempest.api > tempest_api ]
''' def tempest_api():
	tempest_api should use ostestr -l | grep tempest> tempest_api
	returns tempest_api'''

with open('tempest_api') as f:
        lines = f.readlines()



#function accepts liens as list of tests.
def strip_values(lines):
        list_tempest = []
        for l in lines:
                try:
                        l = l.strip("\n")
                        if l[-1] == "]":
			    li = re.sub(r'\[.*\]','',l)
                        #  li = re.search(r'^.*?\[',l).group().strip('[')
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



# Function to read the data from the result json file and return the subtest list.
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




# Write a function to retrun the tempest regex and plugin test result read
#tempest_regex_plugin is let say filter the test related to volume then #tempest_regex_plugin
# test_run_plugin = neutron test run json file

''' def get_tempest_result(tempest_regex_plugin,test_run_plugin):
	(list_tempest,len_of_list) = plugin_test(strip_values(lines),'test_volume')
	(list_tempest,len_of_list) = plugin_test(strip_values(list_tempest),'agent')
	list_result = read_json_test('neutron/neutron_lbaasv2/neutron_lbaasv2-validation_report.json')
	print len(list_tempest),len(list_result)
	return (list_tempest,list_result) '''


def get_tempest_list_result_list(tempest_regex,result_path):

	(list_tempest,len_of_list) = plugin_test(strip_values(lines),tempest_regex)
	# (list_tempest,len_of_list) = plugin_test(strip_values(list_tempest),'agent')
	list_result = read_json_test(result_path)
	print ("\n Total tempest test found {0} \n Total result test found {1}".format(len(list_tempest),len(list_result)))
	return (list_tempest,list_result)


#Function to compare the subtest with the python set function  
'''
def comp_result(list_tempest,list_result):
	for tests in return_test_json(neutron):
		list_result = read_json_test('result_file.json')
		temp = set(list_tempest) -set(list_result)
		print ("######### list_result")
		for i in list_result:
    			print i
		print ("######")
		for i in list_tempest:
    			print i
		print len(temp)
		return temp '''

def comp_result():

	''' Function to compare the list of test in tempest and result file '''
	
	list_tempest,list_result = get_tempest_list_result_list("test_extra_dhcp_options","neutron/neutron_dhcp_extra/neutron_dhcp_extra-validation_report.json")

	temp_missing_test = set(list_tempest) - set(list_result)
	temp_outdated_test = set(list_result) - set(list_tempest)
	if temp_missing_test:
		print ("######### missing_test")
		for i in temp_missing_test:
			print i
	if temp_outdated_test:
		print ("###### outdated test")
		for i in temp_outdated_test:
			print i
	print ("Total missing test {0}".format(len(temp_missing_test)))
	print ("Total outdated test {0}".format(len(temp_outdated_test)))

        

comp_result()
