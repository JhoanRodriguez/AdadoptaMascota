def to_camel(string: str) -> str:
    return "".join(word.capitalize() for word in string.split("_"))


class Config:
    orm_mode = True
    getter_dict = True
    use_enum_values = True
    alias_generator = to_camel
