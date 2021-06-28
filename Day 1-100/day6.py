'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

from collections.abc import MutableMapping


def flatten(nested_dict,seperator='.',name=None):
    flatten_dict = {}
    if not nested_dict:
        return flatten_dict

    if isinstance(nested_dict,MutableMapping):
        for key, value in nested_dict.items():
            if name is not None:
                flatten_dict.update(
                    flatten(
                        nested_dict=value,
                        seperator=seperator,
                        name=f'{name}{seperator}{key}',
                    ),
                )
            else:
                flatten_dict.update(
                    flatten(
                        nested_dict=value,
                        seperator=seperator,
                        name=key,
                    ),
                )
    else:
        flatten_dict[name] = nested_dict
    return flatten_dict


if __name__ == '__main__':
    print('--Dictionary--')
    a = {
            "key": 3,
            "foo": {
                    "a": 5,
                    "bar": {
                            "baz": 8
                            }
                    }
            }
    print(flatten(nested_dict=a))

