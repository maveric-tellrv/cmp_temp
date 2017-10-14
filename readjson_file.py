import json

from pprint import pprint

def read_json_test(path):
    sub_test=[]
    value1=[]
    with open(path) as data_file:
        data = json.load(data_file)

        for key, value in data.items():
            pass
        for keys in value:
            sub_test.append(keys)
        print sub_test
        # for key,test_name in data.items():
        #     # print test_name
        #     sub_test.append(test_name)
        #
        # print len(sub_test),sub_test
# pprint(data['test_cases'][ ]['name'])

read_json_test('neutron/neutron_lbaasv2/neutron_lbaasv2-validation_report.json')