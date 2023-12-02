import json

def logged_in(username, password):
    with open('.database.json', 'rb') as f:
        d = json.load(f)
        nodes = d["nodes"]
        node = {"username": username, "password": password}

        '''for node in nodes:
            if node['username'] == username:
                if node['password'] == password:
                    return True
                else:
                    return False
                
            else:
                return False'''
        if node in nodes:
            return True
        else:
            return False
            
def node_exists(nw_node, json_data):
    if nw_node in json_data['nodes']:
        return True
    
    else:
        return False


def register(username, password):
    new_node = {
        "username": username,
        "password": password
    }

    with open('.database.json', 'rb') as f:
        json_data = json.load(f)

    if node_exists(new_node, json_data):
        return False
    
    else:
        json_data["nodes"].append(new_node)

        with open('.database.json', 'wb') as f:
            json.dump(json_data, f, indent=4)
        
        return True


    





print(logged_in("uday", "bringmethanos"))
