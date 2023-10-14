import json
SERVICE_NAME = "service_name1"
SERVICE_TEMPLATE = "sample.json"
PARAMTERS_FILE = "parameters.json"

def file_read(filename) ->dict:
    try:
        with open (filename, "r") as f:
            override_params = f.read()
        return json.loads(override_params)
    except FileNotFoundError as e:
        print(f"File not found as: {e}")
    except (TypeError, ValueError) as ex:
        print(f"json serialization error: {e}")


#parameters = file_read("parameters.json")


def override_parameters(service_name: str, override_parameters_read: dict) -> dict:
    for i in override_parameters_read:
        if service_name in i:
            params_dict = i.get(SERVICE_NAME)
    return params_dict

def params_process(override_data):
    params = file_read(PARAMTERS_FILE)
    for i in params:
        for k,_ in override_data.items():
            if k in i.values():
                print(i)
    print(override_data)


if __name__ == "__main__":
    override_parameters_read = file_read(SERVICE_TEMPLATE)
    data = override_parameters(SERVICE_NAME, override_parameters_read)
    params_process(data)
    






