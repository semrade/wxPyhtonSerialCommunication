import json
#json_object = {"key1": "val1", "key2": [{"key3":"val3", "key4":"val4"}, 123, "abc"]}

json_object = {
    "PHYSICAL_VALUES": {
        "CMD CURRENT" : [
        {
            "Elements" :  3,
            "I_Phase 1" : "0",
            "I_Phase 2" : "0",
            "I_Phase 3" : "0"
        },
        {
            "Elements" : 1,
            "I_BUS" : 0
        }
        ],
        "CMD VOLTAGE" : [
        {
            "Elements" :  3,
            "V_Phase 1" : "0",
            "V_Phase 2" : "0",
            "V_Phase 3" : "0"
        },
        {
            "Elements" :  1,
            "V_BUS" : "0"
        }
        ]
    }
}

def parse_json_response(content):

    if len (content.Keyeys()) > 1 :
        for key, value in content.iteritems():
            print (key)
            print (value)
            
            if type(value) is dict:
                parse_json_response(value)
    else:
        print(value)



def iterate_multidimensional(my_dict):
    for Key,Value in my_dict.items():
        if(isinstance(Value,dict)):
            print(Key+":")
            iterate_multidimensional(Value)
            continue
        elif(isinstance(Value,list)):
            for i in range(0,len(Value)): 
                if (isinstance(Value[i],dict)):
                    iterate_multidimensional(Value[i])
            
        print(str(Value))

if __name__ == '__main__':
    """
    content = json.loads(str(json_object))
    print(content.Keyeys())
    print(content.iteritems())
    #parse_json_response(content)
    """
    iterate_multidimensional(json_object)