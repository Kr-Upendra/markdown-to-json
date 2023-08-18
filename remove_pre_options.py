def remove_items(dict):
    filtered_data_dict = {key: value for key, value in dict.items() if "option" not in key}
    return filtered_data_dict