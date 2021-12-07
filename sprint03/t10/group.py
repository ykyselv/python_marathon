import itertools
import json

def group(to_group, keys):
    r_dict = dict()
    my_l = []    
    for i in range(len(keys)):
        gr = itertools.groupby(to_group,key = lambda x:x[keys[i]])
        for k, g in gr:
            for el in list(g):
                my_l.append(el)
                if not r_dict.get(el[keys[i]]):
                    r_dict[el[keys[i]]] = []
                r_dict[el[keys[i]]].append(el)
                del el[keys[i]]
    return r_dict

# if __name__ == '__main__':
#     test_case_data = [
#         {
#         'name': 'Alex',
#         'gender': 'male',
#         'species': 'human',
#         'job': 'bicycle repair man'
#         },
#         {
#         'name': 'Monika',
#         'gender': 'female',
#         'species': 'human',
#         'job': 'stockbroker'
#         },
#         {
#         'name': 'Bob',
#         'gender': 'male',
#         'species': 'human',
#         'job': 'quantity surveyor'
#         },
#         {
#         'name': 'Veronika',
#         'gender': 'female',
#         'species': 'human',
#         'job': 'church warden'
#         },
#         {
#         'name': 'George',
#         'gender': 'male',
#         'species': 'human',
#         'job': 'bicycle repair man'
#         },
#         ]
#     test_case_data_group_fields_1 = ['species','gender','job']

#     res_1 = group(test_case_data, test_case_data_group_fields_1)
#     print(json.dumps(res_1, indent=2))
#     print()