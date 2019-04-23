```python
import configparser
import os

class Config:
    """
    Methods:
        - generate()
        - add_value()
        - get_section()
        - add_value()
    """
    
    @staticmethod
    def _get_config():
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config

    @staticmethod
    def generate():
        """
        Generate config.ini file
        """

        work_dir = os.getcwd()
        config = configparser.ConfigParser()
        config["Paths"] = { "home_dir" : work_dir,
                            "test_reports_dir" : r"{wd}\test".format(wd = work_dir)}

        config["Processing_files"] = {}
        with open("config.ini", "w") as configfile:
                config.write(configfile)

    @staticmethod
    def add_value(section, option, value):
        """
        Add value into config.ini file
        """

        config = Config._get_config()
        config.set(section, option, value)
        with open("config.ini", "w") as configfile:
            config.write(configfile)

    @staticmethod
    def get_section(section):
        """
        Get a section in dict
        """
        
        config = Config._get_config()
        return dict(config.items(section))
    
    @staticmethod
    def get_value(key, value):
        """
        Method for getting value from config.ini file
        """

        config = Config._get_config()
        return config.get(key, value)


"""
Iterate over sections in a config file - https://stackoverflow.com/questions/22068050/iterate-over-sections-in-a-config-file
"""

# NOTE: Print section
# TODO: Write debug method
for each_section in conf.sections():
    for (each_key, each_val) in conf.items(each_section):
        print(each_key)
        print(each_val)


# NOTE: Print whole config
# TODO: Write debug method
print({section: dict(config[section]) for section in config.sections()})
```