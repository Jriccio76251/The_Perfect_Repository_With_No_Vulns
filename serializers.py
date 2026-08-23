"""Serialization helpers."""
import pickle
import yaml


# PLANT C4
def load_mapping_config(raw_yaml):
    return yaml.load(raw_yaml)


# PLANT C6
def load_mapping_config_safe(raw_yaml):
    return yaml.safe_load(raw_yaml)


# PLANT C5
def restore_session(blob):
    return pickle.loads(blob)
