import json
SERVICE_NAME = "service_name1"
SERVICE_TEMPLATE = "sample.json"
PARAMTERS_FILE = "parameters.json"
OUTPUT_FILE = "test.json"

def file_read(filename) ->dict:
    try:
        with open (filename, "r") as f:
            override_params = f.read()
        return json.loads(override_params)
    except FileNotFoundError as e:
        print(f"File not found as: {e}")
    except (TypeError, ValueError) as ex:
        print(f"json serialization error: {ex}")


def override_parameters(service_name: str, override_parameters_read: dict) -> dict:
    for i in override_parameters_read:
        if service_name in i:
            params_dict = i.get(SERVICE_NAME)
    return params_dict

def params_process(override_data: dict) -> list:
    params = file_read(PARAMTERS_FILE)
    for i in params:
        for k,v in override_data.items():
            if k in i.values():
                try:
                     i["ParameterValue"] = v
                except IndexError as e:
                    print(f"ParameterValue doesnot exist {e}")
                print(f"successfully updated ParameterValue with {v}")            
    return params

def params_update(params: list)->None:
    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(params, json_file, indent=4)


if __name__ == "__main__":
    override_parameters_read = file_read(SERVICE_TEMPLATE)
    data = override_parameters(SERVICE_NAME, override_parameters_read)
    updated_params = params_process(data)
    params_update(updated_params)
    






