"""
Iterate over sections in a config file - https://stackoverflow.com/questions/22068050/iterate-over-sections-in-a-config-file
"""

# NOTE: Print section
for each_section in conf.sections():
    for (each_key, each_val) in conf.items(each_section):
        print(each_key)
        print(each_val)


# NOTE: Print whole config
print({section: dict(config[section]) for section in config.sections()})